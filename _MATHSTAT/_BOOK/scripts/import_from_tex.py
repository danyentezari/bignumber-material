#!/usr/bin/env python3
"""Split _MATHSTAT/main.tex into _MATHSTAT/_TOPICS markdown pages in source order."""

from __future__ import annotations

import re
import shutil
import unicodedata
from pathlib import Path

MATHSTAT = Path(__file__).resolve().parents[2]
TEX = MATHSTAT / "main.tex"
TOPICS = MATHSTAT / "_TOPICS"

SECTION_FOLDERS = {
    "Probability Theory": ("Probability-Theory", "Probability Theory"),
    "Random Variables": ("Random-Variables", "Random Variables"),
    "Probability Distributions": ("Probability-Distributions", "Probability Distributions"),
    "Overview of Moments": ("Overview-of-Moments", "Overview of Moments"),
    "Maximum Likelihood": ("Maximum-Likelihood", "Maximum Likelihood"),
    "Measure Theory": ("Measure-Theory", "Measure Theory"),
    "Markov Chain Monte–Carlo": ("Markov-Chain-Monte-Carlo", "Markov Chain Monte Carlo"),
    "Markov Chain Monte-Carlo": ("Markov-Chain-Monte-Carlo", "Markov Chain Monte Carlo"),
    "Fourier Analysis": ("Fourier-Analysis", "Fourier Analysis"),
    "Convergence of Random Variables, Distributions, and Probabilities": (
        "Convergence-of-Random-Variables",
        "Convergence of Random Variables, Distributions, and Probabilities",
    ),
    "Select Topics in Stochastic Calculus": ("Stochastic-Calculus", "Stochastic Calculus"),
    "Glossary": ("Glossary", "Glossary"),
    "Mathematical Appendix": ("Mathematical-Appendix", "Mathematical Appendix"),
    "Table of Symbols": ("Symbols", "Table of Symbols"),
}

SKIP_SECTIONS = {"Preface"}

SYMBOLS_MD = """# Table of Symbols

| Symbol | Concept | Read |
| --- | --- | --- |
| $\\mu$ | Population Average | mu |
| $\\sigma$ | Population Standard Deviation | sigma |
| $s$ | Sample Standard Deviation | s |
| $\\bar{x}$ | Mean Average | bar x |
| $X$ | Random Variable | random variable X |
| $\\sigma^2$ | Population Variance | sigma squared |
| $X \\sim N(\\mu, \\sigma)$ | Normal Distribution | X "has" normal distribution |
| $\\Omega$ | Sample Space | sample space |
| $\\mathcal{F}$ | Sigma Algebra | sigma algebra or sigma field |
| $\\mathbb{P}$ | Probability Measure | probability measure |
| $(\\Omega, \\mathcal{F}, \\mathbb{P})$ | Probability Space | probability space |
| $\\mathcal{M}$ | Measure |  |
| $\\mathcal{T}$ | Topology |  |
"""



def strip_comments(text: str) -> str:
    return re.sub(r"(?m)^\s*%.*$", "", text)


def strip_heading_math(title: str) -> str:
    title = title.replace("–", "-").replace("—", "-")
    title = title.replace(r"\sigma", "sigma")
    title = title.replace(r"\chi", "chi")
    title = re.sub(r"\s*\(\s*\$[^)]*\$\s*\)", "", title)
    title = re.sub(r"\$([^$]*)\$", r"\1", title)
    title = re.sub(r"\s+", " ", title).strip(" :-")
    if title[:1].islower():
        title = title[0].upper() + title[1:]
    return title


def filename_from_title(title: str) -> str:
    title = strip_heading_math(title)
    title = unicodedata.normalize("NFKD", title)
    title = "".join(ch for ch in title if not unicodedata.combining(ch))
    title = title.replace("'", "")
    title = re.sub(r"[^\w\s-]", "", title)
    title = re.sub(r"\s+", "-", title.strip())
    parts = [part for part in title.split("-") if part]
    return "-".join(part[:1].upper() + part[1:] for part in parts)


def latex_to_md(text: str) -> str:
    text = strip_comments(text)
    text = text.replace(r"\newpage", "")
    text = text.replace(r"\hfill \break", "\n\n")
    text = text.replace(r"\hfill", "")
    text = text.replace(r"\break", "\n\n")
    text = text.replace(r"\newline", "\n")
    text = text.replace(r"\&", "&")
    text = re.sub(r"\\label\{[^}]+\}", "", text)
    text = re.sub(r"Definition \\autoref\{[^}]+\}", "this definition", text)
    text = re.sub(r"\\autoref\{[^}]+\}", "this definition", text)

    text = re.sub(
        r"\\begin\{mdframed\}\s*\\begin\{definition\}(?:\[([^\]]+)\])?",
        lambda m: f'\n\n<i>\n\n**definition [d]** (*{m.group(1) or "Definition"}*) ',
        text,
    )
    text = text.replace(r"\end{definition}", "\n\n</i>\n")
    text = text.replace(r"\end{mdframed}", "")

    text = re.sub(r"\\emph\{([^}]+)\}", r"*\1*", text)
    text = re.sub(r"\\textit\{([^}]+)\}", r"*\1*", text)
    text = re.sub(r"\\textbf\{([^}]+)\}", r"\1", text)

    def convert_list(match: re.Match[str], ordered: bool) -> str:
        body = match.group(1)
        items = re.split(r"\\item\s*", body)
        items = [item.strip() for item in items if item.strip()]
        lines = []
        for i, item in enumerate(items, start=1):
            item = re.sub(r"\s+", " ", item).strip()
            prefix = f"{i}." if ordered else "-"
            lines.append(f"{prefix} {item}")
        return "\n" + "\n".join(lines) + "\n"

    text = re.sub(
        r"\\begin\{itemize\}(.*?)\\end\{itemize\}",
        lambda m: convert_list(m, False),
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\\begin\{enumerate\}(.*?)\\end\{enumerate\}",
        lambda m: convert_list(m, True),
        text,
        flags=re.DOTALL,
    )

    def convert_table(match: re.Match[str]) -> str:
        inner = match.group(0)
        rows = []
        for row in inner.split(r"\\"):
            if "&" not in row:
                continue
            row = row.replace(r"\hline", "")
            row = re.sub(r"\\begin\{tabularx\}.*?\\hline", "", row, flags=re.DOTALL)
            cells = [c.strip() for c in row.split("&")]
            if any(c for c in cells):
                rows.append(cells)
        if not rows:
            return ""
        header, *rest = rows
        lines = [
            "| " + " | ".join(header) + " |",
            "| " + " | ".join("---" for _ in header) + " |",
        ]
        for row in rest:
            if len(row) < len(header):
                row = row + [""] * (len(header) - len(row))
            lines.append("| " + " | ".join(row[: len(header)]) + " |")
        return "\n\n" + "\n".join(lines) + "\n"

    text = re.sub(
        r"\\begin\{tabularx\}.*?\\end\{tabularx\}",
        convert_table,
        text,
        flags=re.DOTALL,
    )

    text = re.sub(r"\\paragraph\{([^}]+)\}", r"\n\n**\1:** ", text)
    text = re.sub(r"\\subsubsection\{([^}]+)\}", r"\n\n## \1\n\n", text)
    text = re.sub(r"\\subsection\{([^}]+)\}", r"\n\n## \1\n\n", text)

    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def split_units(body: str) -> list[tuple[str, str, str]]:
    """Return (kind, title, body) where kind is subsection, subsubsection, or prose."""
    pattern = re.compile(r"\\(subsection|subsubsection)\{([^}]+)\}")
    units: list[tuple[str, str, str]] = []
    last = 0
    current_kind = "prose"
    current_title = ""
    for match in pattern.finditer(body):
        chunk = body[last : match.start()]
        if last == 0 and chunk.strip():
            units.append(("prose", "", chunk))
        elif last > 0:
            units.append((current_kind, current_title, chunk))
        current_kind = match.group(1)
        current_title = match.group(2)
        last = match.end()
    tail = body[last:]
    if last == 0:
        if body.strip():
            units.append(("prose", "", body))
    else:
        units.append((current_kind, current_title, tail))
    return units


def write_page(folder: Path, filename: str, title: str, body_tex: str) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    md = latex_to_md(body_tex)
    content = f"# {title}\n\n{md}".rstrip() + "\n"
    (folder / filename).write_text(content, encoding="utf-8")


def topic_list(entries: list[tuple[str, str]]) -> str:
    if not entries:
        return ""
    lines = ["## Topics", ""]
    for i, (title, href) in enumerate(entries, start=1):
        lines.append(f"{i}. [{title}]({href})")
    return "\n".join(lines) + "\n"


def href_for(title: str) -> str:
    slug = filename_from_title(title).lower().replace("_", "-")
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return f"{slug}.html"


def import_tex() -> None:
    tex = TEX.read_text(encoding="utf-8")
    start = tex.find(r"\begin{document}")
    end = tex.find(r"\end{document}")
    body = strip_comments(tex[start:end])

    bib_match = re.search(r"\\section\*\{Bibliography\}(.*)$", body, re.DOTALL)
    bib_tex = bib_match.group(1) if bib_match else ""
    if bib_match:
        body = body[: bib_match.start()]

    section_re = re.compile(r"\\section\{([^}]+)\}")
    parts = section_re.split(body)
    sections: list[tuple[str, str]] = []
    for i in range(1, len(parts), 2):
        sections.append((parts[i].strip(), parts[i + 1]))

    if TOPICS.exists():
        shutil.rmtree(TOPICS)
    TOPICS.mkdir(parents=True, exist_ok=True)

    for title, section_body in sections:
        if title in SKIP_SECTIONS:
            continue
        mapping = SECTION_FOLDERS.get(title)
        if mapping is None:
            print(f"warning: unmapped section: {title}")
            continue
        folder_name, display = mapping
        folder = TOPICS / folder_name
        units = split_units(section_body)

        prose = ""
        children: list[tuple[str, str, str]] = []
        for kind, unit_title, unit_body in units:
            if kind == "prose":
                prose += unit_body
            elif kind in {"subsection", "subsubsection"}:
                children.append((strip_heading_math(unit_title), unit_title, unit_body))

        topic_entries: list[tuple[str, str]] = []
        for display_title, raw_title, unit_body in children:
            if not latex_to_md(unit_body).strip():
                continue
            fname = filename_from_title(raw_title) + ".md"
            write_page(folder, fname, display_title, unit_body)
            topic_entries.append((display_title, href_for(display_title)))

        hub_body = latex_to_md(prose)
        hub = f"# {display}\n\n"
        if hub_body.strip():
            hub += hub_body.rstrip() + "\n\n"
        hub += topic_list(topic_entries)
        folder.mkdir(parents=True, exist_ok=True)
        (folder / f"{folder_name}.md").write_text(hub, encoding="utf-8")
        if folder_name == "Symbols":
            (folder / "Symbols.md").write_text(SYMBOLS_MD, encoding="utf-8")

    if bib_tex.strip():
        bib_dir = TOPICS / "Bibliography"
        write_page(bib_dir, "Bibliography.md", "Bibliography", bib_tex)

    print(f"Wrote topics under {TOPICS}")


if __name__ == "__main__":
    import_tex()
