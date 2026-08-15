#!/usr/bin/env python3
"""
Rebuild Site Index from rendered HTML, then verify every topic .md chapter
appears in both Site Index and search.json.

Bookdown filenames are not a pure function of chapter titles (in-page headings
can consume electromagnetism-1, etc.), so we match chapters by their number in
the <title> tag after render.
"""

from __future__ import annotations

import html as html_lib
import json
import re
import sys
from pathlib import Path


BOOK_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = BOOK_DIR.parent
TOPICS_DIR = REPO_ROOT / "_TOPICS"
BOOK_OUT = BOOK_DIR / "_book"
SITE_INDEX_HTML = BOOK_OUT / "site-index.html"
SEARCH_JSON = BOOK_OUT / "search.json"
BOOKDOWN_YML = BOOK_DIR / "_bookdown.yml"

TITLE_RE = re.compile(
    r"<title>(\d+)\s+(.*?)\s+\|\s*[^<]*</title>",
    re.IGNORECASE | re.DOTALL,
)
TOPIC_INDEX_BLOCK_RE = re.compile(
    r'(<div class="topic-index">\s*<ul>).*?(</ul>\s*</div>)',
    re.DOTALL,
)

DEF_NAME_RE = re.compile(
    r"^\*\*[Dd]efinition(?:\s*\[[^\]]+\])?\*\*\s*"
    r"(?:"
    r"\(\*\*(?P<a>[^*]+)\*\*\)|"
    r"\(\*(?P<b>[^*]+)\*\)|"
    r"\(_(?P<c>[^_]+)_\)|"
    r"\((?P<e>[^)]+)\)"
    r")"
)


def extract_definition_names(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return []
    names: list[str] = []
    for line in text.splitlines():
        match = DEF_NAME_RE.match(line.strip())
        if not match:
            continue
        name = match.group("a") or match.group("b") or match.group("c") or match.group("e")
        if name:
            names.append(name.strip())
    return names


def extract_synonym_chain(path: Path) -> str | None:
    title = extract_title(path)
    names = extract_definition_names(path)
    synonym_names = [name for name in names if "=" in name]
    if not synonym_names:
        return None

    def slugify(text: str) -> str:
        import unicodedata

        normalized = unicodedata.normalize("NFKD", text)
        normalized = "".join(ch for ch in normalized if not unicodedata.combining(ch))
        normalized = normalized.lower().replace("'", "")
        normalized = re.sub(r"[(),]", "", normalized)
        return re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")

    def matches_title(name: str) -> bool:
        primary = re.split(r"\s*=\s*", name, maxsplit=1)[0].strip()
        if primary.lower() == title.lower():
            return True
        primary_key = slugify(primary)
        title_key = slugify(title)
        if primary_key == title_key:
            return True
        if primary_key.rstrip("s") == title_key.rstrip("s"):
            return True
        return False

    for name in synonym_names:
        if matches_title(name):
            return name
    if len(names) == 1:
        return synonym_names[0]
    return None


def expand_synonym_index_entries(label: str, href: str) -> list[tuple[str, str]]:
    parts = [part.strip() for part in re.split(r"\s*=\s*", label) if part.strip()]
    if len(parts) < 2:
        return [(label, href)]
    entries: list[tuple[str, str]] = []
    for index, part in enumerate(parts):
        others = parts[:index] + parts[index + 1 :]
        entries.append((" = ".join([part, *others]), href))
    return entries


def extract_title(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return path.stem.replace("-", " ")
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return path.stem.replace("-", " ")


def is_safe(path: Path) -> bool:
    return re.fullmatch(r"[A-Za-z0-9._-]+\.md", path.name) is not None


def bookdown_generated_md_paths() -> list[Path]:
    if not BOOKDOWN_YML.is_file():
        raise RuntimeError(f"Missing {BOOKDOWN_YML}")
    paths: list[Path] = []
    for line in BOOKDOWN_YML.read_text(encoding="utf-8").splitlines():
        match = re.search(r'"(\.\./_BOOK/generated/[^"]+\.md)"', line)
        if match:
            paths.append((BOOK_DIR / match.group(1)).resolve())
    return paths


def topic_markdown_files() -> list[Path]:
    files: list[Path] = []
    if not TOPICS_DIR.is_dir():
        return files
    for folder in sorted(TOPICS_DIR.iterdir(), key=lambda p: p.name.lower()):
        if not folder.is_dir():
            continue
        for path in sorted(folder.iterdir(), key=lambda p: p.name.lower()):
            if path.is_file() and path.suffix.lower() == ".md" and is_safe(path):
                files.append(path)
    return files


def rendered_chapters_by_number() -> dict[int, tuple[str, str]]:
    """Map chapter number -> (title, href) from rendered HTML <title> tags."""
    chapters: dict[int, tuple[str, str]] = {}
    for path in BOOK_OUT.glob("*.html"):
        if path.name == "404.html":
            continue
        # Only need the head.
        text = path.read_text(encoding="utf-8", errors="ignore")[:4000]
        match = TITLE_RE.search(text)
        if not match:
            continue
        number = int(match.group(1))
        title = html_lib.unescape(match.group(2)).strip()
        chapters[number] = (title, path.name)
    return chapters


def expected_chapters() -> list[tuple[int, str, Path | None]]:
    """
    Bookdown chapter order: 1 = Introduction (index.Rmd), then each generated md.
    Returns (number, title, source_md_or_None).
    """
    rows: list[tuple[int, str, Path | None]] = [
        (1, "Introduction", None),
    ]
    for index, path in enumerate(bookdown_generated_md_paths(), start=2):
        rows.append((index, extract_title(path), path))
    return rows


def rebuild_site_index(entries: list[tuple[str, str]]) -> None:
    """Replace the topic-index list in site-index.html with alphabetical links."""
    if not SITE_INDEX_HTML.is_file():
        raise RuntimeError(f"Missing {SITE_INDEX_HTML}")

    sorted_entries = sorted(entries, key=lambda item: item[0].lower())
    items = "\n".join(
        f'<li><a href="{html_lib.escape(href, quote=True)}">'
        f"{html_lib.escape(title)}</a></li>"
        for title, href in sorted_entries
    )
    block = f'<div class="topic-index">\n<ul>\n{items}\n</ul>\n</div>'

    html = SITE_INDEX_HTML.read_text(encoding="utf-8")
    match = TOPIC_INDEX_BLOCK_RE.search(html)
    if not match:
        raise RuntimeError("Could not find topic-index block in site-index.html")
    html = html[: match.start()] + block + html[match.end() :]

    SITE_INDEX_HTML.write_text(html, encoding="utf-8")


def paths_in_search() -> set[str]:
    if not SEARCH_JSON.is_file():
        raise RuntimeError(f"Missing {SEARCH_JSON}")
    data = json.loads(SEARCH_JSON.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise RuntimeError("search.json is not a list")
    return {entry.get("path", "") for entry in data if isinstance(entry, dict)}


def hrefs_in_site_index() -> set[str]:
    html = SITE_INDEX_HTML.read_text(encoding="utf-8")
    return set(re.findall(r'href="([^"]+\.html)"', html))


def verify_and_fix() -> None:
    rendered = rendered_chapters_by_number()
    expected = expected_chapters()

    missing_html: list[str] = []
    chapter_entries: list[tuple[str, str]] = []
    resolved: list[tuple[int, str, str, Path | None]] = []

    for number, title, source in expected:
        found = rendered.get(number)
        if found is None:
            missing_html.append(f"{number}. {title}")
            continue
        rendered_title, href = found
        chapter_entries.append((rendered_title, href))
        resolved.append((number, rendered_title, href, source))

    if missing_html:
        raise RuntimeError(
            "Missing rendered HTML for chapters:\n  - " + "\n  - ".join(missing_html)
        )

    # Prefer synonym-aware labels from source markdown; fall back to rendered titles.
    index_entries: list[tuple[str, str]] = []
    for _number, title, href, source in resolved:
        if href in {"index.html", "site-index.html"}:
            continue
        if source is not None and source.name != f"{source.parent.name}.md":
            label = extract_synonym_chain(source) or extract_title(source)
            index_entries.extend(expand_synonym_index_entries(label, href))
        else:
            index_entries.append((title, href))

    rebuild_site_index(index_entries)

    search_paths = paths_in_search()
    index_hrefs = hrefs_in_site_index()

    missing_search: list[str] = []
    missing_index: list[str] = []
    for _number, title, href, _source in resolved:
        if href == "site-index.html":
            continue
        if href not in search_paths:
            missing_search.append(f"{href} ({title})")
        if href not in {"index.html"} and href not in index_hrefs:
            missing_index.append(f"{href} ({title})")

    yml = BOOKDOWN_YML.read_text(encoding="utf-8")
    orphan_sources: list[str] = []
    for path in topic_markdown_files():
        needle = f"generated/{path.parent.name}/{path.name}"
        if needle not in yml:
            orphan_sources.append(path.relative_to(REPO_ROOT).as_posix())

    errors: list[str] = []
    if missing_search:
        errors.append(
            "Chapters missing from search.json:\n  - " + "\n  - ".join(missing_search)
        )
    if missing_index:
        errors.append(
            "Chapters missing from Site Index:\n  - " + "\n  - ".join(missing_index)
        )
    if orphan_sources:
        errors.append(
            "Topic markdown not listed in _bookdown.yml:\n  - "
            + "\n  - ".join(orphan_sources)
        )

    if errors:
        raise RuntimeError("\n\n".join(errors))

    print(
        f"Verified {len(resolved)} chapters in HTML, search.json, and Site Index "
        f"(Site Index rebuilt from rendered filenames)."
    )


if __name__ == "__main__":
    try:
        verify_and_fix()
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
