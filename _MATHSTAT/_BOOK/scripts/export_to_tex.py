#!/usr/bin/env python3
"""Regenerate main.tex from _TOPICS, following structure.txt.

Omits markdown Topics and References sections. Citations live in Bibliography.
"""

from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path

BOOK_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK_DIR / "scripts"))

from generate_topics import (  # noqa: E402
    FOLDER_ALIASES,
    STRUCTURE_TXT,
    TOPICS_DIR,
    extract_title,
    slugify_text,
)

MATHSTAT = BOOK_DIR.parent
TEX = MATHSTAT / "main.tex"
INDEX_RMD = BOOK_DIR / "index.Rmd"
BIBLIOGRAPHY = TOPICS_DIR / "Bibliography" / "Bibliography.md"

HEADING_CMD = {0: "section", 1: "subsection", 2: "subsubsection"}

# Per-page PDF margins for Derivation of Normal Distribution (see topic comments).
# <!-- pdf-page-width: default -->  article defaults
# <!-- pdf-page-width: wide -->     narrower margins for two-column justifications
DERIVATION_FOLDER = "Derivation-of-Normal-Distribution"
DERIVATION_GEOMETRY = "margin=0.75in"
PAGE_WIDTH_RE = re.compile(
    r"<!--\s*pdf-page-width:\s*(default|wide)\s*-->",
    re.IGNORECASE,
)


def load_structure_nodes() -> list[tuple[int, str]]:
    nodes: list[tuple[int, str]] = []
    for raw in STRUCTURE_TXT.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = (len(raw) - len(raw.lstrip(" "))) // 2
        nodes.append((indent, raw.strip()))
    return nodes


def folder_for_section(name: str) -> Path:
    alias = FOLDER_ALIASES.get(name)
    if alias:
        return TOPICS_DIR / alias
    return TOPICS_DIR / name.replace(" ", "-")


def find_page(folder: Path, name: str) -> Path | None:
    if not folder.is_dir():
        return None
    key = slugify_text(name)
    hub = folder / f"{folder.name}.md"

    def is_topic_md(path: Path) -> bool:
        # Keep *.draft.md / *.skip.md in git; never include them in the PDF export.
        return (
            path.is_file()
            and path.suffix.lower() == ".md"
            and not path.name.endswith(".draft.md")
            and not path.name.endswith(".skip.md")
        )

    # Prefer an exact stem match (Frequency-Domain.md for "Frequency Domain").
    for path in folder.iterdir():
        if is_topic_md(path) and slugify_text(path.stem) == key:
            return path
    for path in folder.iterdir():
        if is_topic_md(path) and slugify_text(extract_title(path)) == key:
            return path
    if hub.is_file() and not hub.name.endswith(".draft.md") and not hub.name.endswith(".skip.md"):
        if slugify_text(extract_title(hub)) == key:
            return hub
    return None


def preface_from_index() -> str:
    text = INDEX_RMD.read_text(encoding="utf-8")
    match = re.search(r"^# Introduction\s*\n+(.*)$", text, re.DOTALL | re.MULTILINE)
    body = match.group(1).strip() if match else ""
    return body


def strip_h1_and_book_nav(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    kept: list[str] = []
    skipping = False
    for line in lines:
        if re.match(r"^#{1,2}\s+(Topics|References)\s*$", line, re.I):
            skipping = True
            continue
        if skipping and re.match(r"^#{1,2}\s+\S", line):
            skipping = False
        if skipping:
            continue
        kept.append(line)
    return "\n".join(kept).strip()


_DISPLAY_ENV_RE = re.compile(
    r"\\begin\{(?:align|gather|multline|eqnarray|flalign)\*?\}"
)


def compact_display_math(chunk: str) -> str:
    """Keep writer line-breaks in markdown; emit one-line $$...$$ for PDF.

    Newlines inside ordinary display math are only for editing convenience;
    LaTeX already treats them as spaces, but compacting avoids blank-line
    accidents and matches Springer/Dover density in the generated .tex.
    amsmath display environments keep their structure for unwrap_display_envs.
    """
    if not (chunk.startswith("$$") and chunk.endswith("$$")):
        return chunk
    inner = chunk[2:-2]
    if _DISPLAY_ENV_RE.search(inner):
        return chunk
    inner = re.sub(r"[ \t]*\n[ \t]*", " ", inner)
    inner = re.sub(r" {2,}", " ", inner).strip()
    return f"$$\n{inner}\n$$"


def protect_math(text: str) -> tuple[str, list[str]]:
    chunks: list[str] = []

    def stash(match: re.Match[str]) -> str:
        chunks.append(compact_display_math(match.group(0)))
        return f"@@MATH{len(chunks) - 1}@@"

    text = re.sub(r"\$\$[\s\S]*?\$\$", stash, text)
    text = re.sub(r"\\\([\s\S]*?\\\)", stash, text)
    text = re.sub(r"\$[^$]+\$", stash, text)
    return text, chunks


def restore_math(text: str, chunks: list[str]) -> str:
    for i, chunk in enumerate(chunks):
        text = text.replace(f"@@MATH{i}@@", chunk)
    return text


# amsmath display environments must not sit inside $$...$$ in LaTeX
_DISPLAY_ENVS = (
    "align*",
    "align",
    "gather*",
    "gather",
    "multline*",
    "multline",
    "eqnarray*",
    "eqnarray",
    "flalign*",
    "flalign",
)


def unwrap_display_envs(text: str) -> str:
    """Strip $$ wrappers around amsmath display environments for PDF export."""
    for env in _DISPLAY_ENVS:
        text = re.sub(
            rf"\$\$\s*(\\begin\{{{re.escape(env)}\}}[\s\S]*?\\end\{{{re.escape(env)}\}})\s*\$\$",
            r"\1",
            text,
        )
    return text


def protect_urls(text: str) -> tuple[str, list[str]]:
    chunks: list[str] = []

    def stash(match: re.Match[str]) -> str:
        url = match.group(0).rstrip(".,;:)]")
        trailing = match.group(0)[len(url) :]
        chunks.append(url)
        return f"@@URL{len(chunks) - 1}@@{trailing}"

    text = re.sub(r"https?://[^\s<>]+", stash, text)
    return text, chunks


def restore_urls(text: str, chunks: list[str]) -> str:
    for i, url in enumerate(chunks):
        text = text.replace(f"@@URL{i}@@", rf"\url{{{url}}}")
    return text


def escape_tex(text: str) -> str:
    """Escape LaTeX specials in prose. Call while math and URLs are stashed."""
    return (
        text.replace("&", r"\&")
        .replace("%", r"\%")
        .replace("#", r"\#")
        .replace("_", r"\_")
        .replace("~", r"\textasciitilde{}")
        .replace("^", r"\textasciicircum{}")
    )


def page_width_directive(text: str) -> str | None:
    match = PAGE_WIDTH_RE.search(text)
    return match.group(1).lower() if match else None


HTML_COMMENT_RE = re.compile(r"<!--[\s\S]*?-->")


def strip_html_comments(text: str) -> str:
    """Drop HTML comments so commented markdown never reaches the PDF."""
    return HTML_COMMENT_RE.sub("", text)


def convert_html_breaks(text: str) -> str:
    """Turn <br>, <br/>, <br /> into a PDF paragraph break with light spacing."""
    return re.sub(r"<br\s*/?\s*>", r"\\par\\medskip\n", text, flags=re.I)


_ITALIC_H4_WORDS = frozenset(
    {
        "example",
        "remark",
        "proof",
        "counterexample",
        "note",
        "notation",
        "claim",
    }
)


def _styled_h4_head(title: str) -> str:
    """Build a LaTeX run-in head from a #### title line (emphasis or keyword)."""
    title = title.strip()
    bold = re.match(r"^\*\*([^*]+)\*\*(.*)$", title)
    if bold:
        label, rest = bold.group(1).strip(), bold.group(2).strip()
        head = f"\\textbf{{{label}}}"
        return f"{head} {rest}".rstrip() if rest else head

    italic = re.match(r"^\*([^*]+)\*(.*)$", title)
    if italic:
        label, rest = italic.group(1).strip(), italic.group(2).strip()
        head = f"\\emph{{{label}}}"
        return f"{head} {rest}".rstrip() if rest else head

    # Keyword fallback when markers are omitted: Example → italic, Theorem → bold.
    first = re.split(r"[\s.:]+", title, maxsplit=1)[0].lower()
    if first in _ITALIC_H4_WORDS:
        return f"\\emph{{{title}}}"
    return f"\\textbf{{{title}}}"


def _is_list_line(line: str) -> bool:
    return bool(re.match(r"^[ \t]*(?:[-*]|\d+\.)[ \t]+", line))


def preserve_block_newlines(body: str) -> str:
    """Keep markdown line structure inside a block in the PDF.

    - Single newlines between prose → PDF line breaks (\\\\)
    - One blank line → normal paragraph break
    - Extra blank lines → \\vspace so vertical gaps are visible
    - List items and display math keep ordinary newlines
    """
    chunks: list[str] = []

    def stash(match: re.Match[str]) -> str:
        chunks.append(match.group(0))
        return f"@@BMDMATH{len(chunks) - 1}@@"

    text = re.sub(r"\$\$[\s\S]*?\$\$", stash, body)
    text = re.sub(r"\\\([\s\S]*?\\\)", stash, text)
    text = re.sub(r"(?<!\$)\$(?!\$)(?:\\\$|[^$\n])+\$", stash, text)

    lines = text.split("\n")
    out: list[str] = []
    for i, line in enumerate(lines):
        out.append(line.rstrip())
        if i >= len(lines) - 1:
            break
        nxt = lines[i + 1]
        if not line.strip() or not nxt.strip():
            continue
        if _is_list_line(line) or _is_list_line(nxt):
            continue
        # Display math already breaks the line; avoid \\ before/after it.
        if "@@BMDMATH" in line or "@@BMDMATH" in nxt:
            continue
        # Soft break between adjacent non-empty prose lines.
        out[-1] = out[-1] + r"\\"

    text = "\n".join(out)

    def blank_run(match: re.Match[str]) -> str:
        # One blank line (two newlines) = normal paragraph.
        # Each extra blank line adds one baselineskip of visible space.
        extra = match.group(0).count("\n") - 2
        if extra <= 0:
            return "\n\n"
        return f"\n\n\\vspace{{{extra}\\baselineskip}}\n\n"

    text = re.sub(r"\n{2,}", blank_run, text)

    for i, chunk in enumerate(chunks):
        text = text.replace(f"@@BMDMATH{i}@@", chunk)
    return text


def _format_mdblock(head: str | None, body: str) -> str:
    raw = textwrap.dedent(body)
    body = preserve_block_newlines(raw.strip())
    if head and body:
        # The newline after a #### heading is Markdown structure, not authored
        # body spacing. Keep textbook labels run-in: "Example 1. Let ...".
        # Newlines within `body` are still preserved by preserve_block_newlines.
        inner = f"{head} {body}"
    elif head:
        inner = head
    else:
        inner = body
    return f"\\begin{{mdblock}}\n{inner}\n\\end{{mdblock}}\n"


def convert_styled_h4_blocks(text: str) -> str:
    """Turn foldable #### headings into flush-left example/theorem blocks.

    Markdown (folds in the IDE):
      #### *Example 1.*
      body...

      #### **Theorem 1.15** (Intersection of classes of sets)
      body...

    Also accepts plain ``#### Example 1`` / ``#### Theorem 1`` via keyword style.
    Body runs until the next ATX heading (#–######) or end of text.
    Single newlines in the body become PDF line breaks.
    """
    lines = text.splitlines(keepends=True)
    if not lines:
        return text

    heading_re = re.compile(r"^(#{1,6})[ \t]+(.*)$")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        match = heading_re.match(line.rstrip("\n"))
        if not match or len(match.group(1)) != 4:
            out.append(line)
            i += 1
            continue

        head = _styled_h4_head(match.group(2))
        i += 1
        body_lines: list[str] = []
        while i < len(lines):
            next_match = heading_re.match(lines[i].rstrip("\n"))
            if next_match:
                break
            body_lines.append(lines[i])
            i += 1

        body = "".join(body_lines)
        out.append(_format_mdblock(head, body))

    return "".join(out)


def convert_blocks(text: str) -> str:
    """Turn markdown blocks into flush-left Springer-style mdblock environments.

    Supported forms:
      #### *Example 1.* / #### **Theorem 1**   (preferred; IDE-foldable)

      ::: {.mdblock}
      ...
      :::

      <block>...</block>   (legacy)
    """
    text = convert_styled_h4_blocks(text)

    def one_block(match: re.Match[str]) -> str:
        return _format_mdblock(None, match.group(1))

    # Pandoc fenced divs: ::: {.mdblock} ... :::  or  ::: mdblock ... :::
    text = re.sub(
        r"^:::\s*(?:\{\.mdblock\}|mdblock)\s*\n([\s\S]*?)^:::\s*$",
        one_block,
        text,
        flags=re.MULTILINE | re.I,
    )
    # Legacy HTML-ish tag
    text = re.sub(
        r"<block>\s*([\s\S]*?)\s*</block>",
        one_block,
        text,
        flags=re.I,
    )
    return text


MDBLOCK_BEGIN = "% BEGIN generated mdblock"
MDBLOCK_END = "% END generated mdblock"

MDBLOCK_ENV = r"""
% BEGIN generated mdblock
% Flush-left first line; later paragraphs keep normal indent.
% Soft line-breaks inside the block come from markdown newlines.
\newenvironment{mdblock}{%
  \par\addvspace{1.5\baselineskip}%
  \noindent\ignorespaces
}{%
  \par\addvspace{1.5\baselineskip}%
}
% END generated mdblock
""".strip()


def ensure_mdblock_env(preamble: str) -> str:
    """Insert or replace the generated environment without parsing TeX braces."""
    begin = preamble.find(MDBLOCK_BEGIN)
    end = preamble.find(MDBLOCK_END, begin + 1)
    if begin >= 0 and end >= 0:
        end += len(MDBLOCK_END)
        return preamble[:begin] + MDBLOCK_ENV + preamble[end:]

    # Migrate the older unmarked definition. It was always immediately before
    # \title; replacing that whole region also removes debris from old regex
    # replacements that could leave unmatched `}%` lines on every export.
    env = preamble.find(r"\newenvironment{mdblock}")
    title = preamble.find(r"\title{", env + 1)
    if env >= 0 and title >= 0:
        comment = preamble.rfind("\n% Flush-left", 0, env)
        start = comment + 1 if comment >= 0 else env
        return (
            preamble[:start].rstrip()
            + "\n\n"
            + MDBLOCK_ENV
            + "\n\n"
            + preamble[title:].lstrip()
        )

    marker = r"\newtheorem{definition}{Definition}"
    if marker in preamble:
        return preamble.replace(marker, MDBLOCK_ENV + "\n\n" + marker, 1)
    return preamble.rstrip() + "\n\n" + MDBLOCK_ENV + "\n"


def md_to_tex(text: str) -> str:
    text = PAGE_WIDTH_RE.sub("", text)
    text = strip_html_comments(text)
    text = strip_h1_and_book_nav(text)
    if not text:
        return ""
    if not text.endswith("\n"):
        text += "\n"

    text = convert_html_breaks(text)
    text = convert_blocks(text)
    text, math = protect_math(text)
    text, urls = protect_urls(text)
    text = escape_tex(text)

    def definition_block(match: re.Match[str]) -> str:
        name = match.group(1).strip()
        body = match.group(2).strip()
        return (
            "\\begin{mdframed}\n"
            f"\\begin{{definition}}[{name}]\n"
            f"{body}\n"
            "\\end{definition}\n"
            "\\end{mdframed}"
        )

    text = re.sub(
        r"<i>\s*\*\*definition(?:\s*\[[^\]]+\])?\*\*\s*\(\*([^*]+)\*\)\s*(.*?)</i>",
        definition_block,
        text,
        flags=re.DOTALL | re.I,
    )

    def table_block(match: re.Match[str]) -> str:
        rows = []
        for line in match.group(0).strip().splitlines():
            line = line.strip()
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                continue
            rows.append(cells)
        if not rows:
            return ""
        ncol = max(len(row) for row in rows)
        colspec = " | ".join(
            [r">{\raggedright\arraybackslash}X"] * ncol
        )
        lines = [
            r"\begin{tabularx}{1\textwidth} {|" + f" {colspec} " + "|}",
            r"\hline",
        ]
        for i, row in enumerate(rows):
            row = row + [""] * (ncol - len(row))
            lines.append(" & ".join(row) + r" \\")
            lines.append(r"\hline")
        lines.append(r"\end{tabularx}")
        return "\n".join(lines)

    text = re.sub(
        r"(?:^\|.+\|[ \t]*\n)+",
        table_block,
        text,
        flags=re.MULTILINE,
    )

    text = re.sub(
        r"^(\*\*(.+?):\*\*)\s*",
        lambda m: f"\\paragraph{{{m.group(2)}}} ",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\\emph{\1}", text)

    # escape_tex already turned # into \#. Promote markdown headings.
    text = re.sub(r"^\\#\\# (.+)$", r"\\subsection{\1}", text, flags=re.MULTILINE)
    text = re.sub(r"^\\#\\#\\# (.+)$", r"\\subsubsection{\1}", text, flags=re.MULTILINE)

    def convert_lists(block: str) -> str:
        def one_list(match: re.Match[str], ordered: bool) -> str:
            items = []
            for line in match.group(0).strip().splitlines():
                item = re.sub(r"^\s*(?:\d+\.|-)\s*", "", line).strip()
                if item:
                    items.append(item)
            env = "enumerate" if ordered else "itemize"
            inner = "\n".join(f"    \\item {item}" for item in items)
            return f"\\begin{{{env}}}\n{inner}\n\\end{{{env}}}\n"

        block = re.sub(
            r"(?:^[ \t]*\d+\.\s+.+\n?)+",
            lambda m: one_list(m, True),
            block,
            flags=re.MULTILINE,
        )
        block = re.sub(
            r"(?:^[ \t]*- .+\n?)+",
            lambda m: one_list(m, False),
            block,
            flags=re.MULTILINE,
        )
        return block

    text = convert_lists(text)
    text = restore_urls(text, urls)
    text = restore_math(text, math)
    text = unwrap_display_envs(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def existing_preamble() -> str:
    tex = TEX.read_text(encoding="utf-8")
    match = re.search(
        r"^(.*\\tableofcontents\s*)",
        tex,
        re.DOTALL,
    )
    if not match:
        raise RuntimeError("Could not find preamble/tableofcontents in main.tex")
    return ensure_mdblock_env(match.group(1).rstrip())


def node_has_children(nodes: list[tuple[int, str]], index: int) -> bool:
    level, _ = nodes[index]
    return index + 1 < len(nodes) and nodes[index + 1][0] > level


def export() -> None:
    nodes = load_structure_nodes()
    if not nodes:
        raise RuntimeError(f"No structure entries in {STRUCTURE_TXT}")

    parts = [existing_preamble(), "", "%----------------------------------------------------------------------------"]
    preface = preface_from_index()
    parts.append("\\newpage")
    parts.append("\\section{Preface}")
    if preface:
        parts.append(md_to_tex("# Introduction\n\n" + preface) or preface)
    parts.append("")

    current_folder: Path | None = None
    # PDF geometry state: "default" (article) or "wide" (narrower margins)
    current_width = "default"

    def set_page_width(desired: str) -> None:
        nonlocal current_width
        if desired == current_width:
            return
        if desired == "wide":
            parts.append(f"\\newgeometry{{{DERIVATION_GEOMETRY}}}")
        else:
            parts.append("\\restoregeometry")
        current_width = desired

    for i, (level, name) in enumerate(nodes):
        cmd = HEADING_CMD.get(level, "subsubsection")
        if level == 0:
            current_folder = folder_for_section(name)
            page = current_folder / f"{current_folder.name}.md"
            if not page.is_file():
                page = find_page(current_folder, name)
        else:
            page = find_page(current_folder, name) if current_folder else None

        has_page = page is not None and page.is_file()
        if not has_page and not node_has_children(nodes, i):
            continue

        in_derivation = (
            current_folder is not None and current_folder.name == DERIVATION_FOLDER
        )

        parts.append("%----------------------------------------------------------------------------")
        if level == 0:
            set_page_width("default")
            parts.append("\\newpage")

        raw = page.read_text(encoding="utf-8") if has_page else ""
        if in_derivation and has_page:
            width = page_width_directive(raw) or "default"
            set_page_width(width)
        elif not in_derivation:
            set_page_width("default")

        parts.append(f"\\{cmd}{{{name}}}")

        if has_page:
            body = md_to_tex(raw)
            if body:
                parts.append(body)
        parts.append("")

    set_page_width("default")

    if BIBLIOGRAPHY.is_file():
        bib = md_to_tex(BIBLIOGRAPHY.read_text(encoding="utf-8"))
        parts.append("%----------------------------------------------------------------------------")
        parts.append("\\newpage")
        parts.append("\\section*{Bibliography}")
        if bib:
            parts.append(bib)
        parts.append("")

    parts.append("\\end{document}")
    parts.append("")
    TEX.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {TEX}")


if __name__ == "__main__":
    try:
        export()
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
