#!/usr/bin/env python3
"""Regenerate main.tex from _TOPICS, following structure.txt.

Omits markdown Topics and References sections. Citations live in Bibliography.
"""

from __future__ import annotations

import re
import sys
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
        # Keep *.draft.md in git; never include them in the PDF export.
        return (
            path.is_file()
            and path.suffix.lower() == ".md"
            and not path.name.endswith(".draft.md")
        )

    # Prefer an exact stem match (Frequency-Domain.md for "Frequency Domain").
    for path in folder.iterdir():
        if is_topic_md(path) and slugify_text(path.stem) == key:
            return path
    for path in folder.iterdir():
        if is_topic_md(path) and slugify_text(extract_title(path)) == key:
            return path
    if hub.is_file() and not hub.name.endswith(".draft.md"):
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
        if re.match(r"^##\s+(Topics|References)\s*$", line, re.I):
            skipping = True
            continue
        if skipping and re.match(r"^##\s+\S", line):
            skipping = False
        if skipping:
            continue
        kept.append(line)
    return "\n".join(kept).strip()


def protect_math(text: str) -> tuple[str, list[str]]:
    chunks: list[str] = []

    def stash(match: re.Match[str]) -> str:
        chunks.append(match.group(0))
        return f"@@MATH{len(chunks) - 1}@@"

    text = re.sub(r"\$\$[\s\S]*?\$\$", stash, text)
    text = re.sub(r"\$[^$]+\$", stash, text)
    return text, chunks


def restore_math(text: str, chunks: list[str]) -> str:
    for i, chunk in enumerate(chunks):
        text = text.replace(f"@@MATH{i}@@", chunk)
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


def md_to_tex(text: str) -> str:
    text = strip_h1_and_book_nav(text)
    if not text:
        return ""
    if not text.endswith("\n"):
        text += "\n"

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

    text = re.sub(r"^## (.+)$", r"\\subsubsection{\1}", text, flags=re.MULTILINE)

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
    return match.group(1).rstrip()


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

        parts.append("%----------------------------------------------------------------------------")
        if level == 0:
            parts.append("\\newpage")
        parts.append(f"\\{cmd}{{{name}}}")

        if has_page:
            body = md_to_tex(page.read_text(encoding="utf-8"))
            if body:
                parts.append(body)
        parts.append("")

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
