#!/usr/bin/env python3
"""Discover topic folders and generate bookdown config plus topic index pages."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


BOOK_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = BOOK_DIR.parent
TOPICS_DIR = REPO_ROOT / "_TOPICS"
GENERATED_DIR = BOOK_DIR / "generated"
BOOKDOWN_YML = BOOK_DIR / "_bookdown.yml"
SIDEBAR_PAGES_JSON = GENERATED_DIR / "sidebar-pages.json"
SIDEBAR_TXT = BOOK_DIR / "sidebar.txt"


def slugify_text(text: str) -> str:
    normalized = text.lower().replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")


def extract_title(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RuntimeError(f"Unable to read {path}") from exc

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return path.stem.replace("-", " ")


def split_main_topic(path: Path, folder: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if lines and lines[0].strip().startswith("# "):
        title = lines[0].strip()[2:].strip()
        body = "\n".join(lines[1:]).lstrip("\n")
        return title, body

    title = folder.name.replace("-", " ")
    return title, text.strip()


def build_topic_index(entries: list[tuple[str, str]]) -> str:
    if not entries:
        return ""

    lines = ["::: {.topic-index}", ""]
    for title, href in entries:
        lines.append(f"- [{title}]({href})")
    lines.extend(["", ":::", ""])
    return "\n".join(lines)


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
    """Return definition display names from a markdown file."""
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
    """
    If this page is a definition file with synonyms (Name = Alias = ...),
    return that full chain; otherwise None.
    """
    title = extract_title(path)
    names = extract_definition_names(path)
    synonym_names = [name for name in names if "=" in name]
    if not synonym_names:
        return None

    # Single-definition pages: use the synonym chain even if the H1 wording differs
    # (e.g. H1 "One-Form" vs definition "1-form = linear functional = ...").
    if len(names) == 1:
        return synonym_names[0]

    title_key = slugify_text(title)
    for name in synonym_names:
        primary = re.split(r"\s*=\s*", name, maxsplit=1)[0].strip()
        if slugify_text(primary) == title_key or primary.lower() == title.lower():
            return name
    return None


def expand_synonym_index_entries(
    label: str,
    href: str,
) -> list[tuple[str, str]]:
    """
    Build site-index rows for a label. Synonym chains become one row per alias,
    each written as Alias = Other = ..., so every synonym is findable alphabetically.
    """
    parts = [part.strip() for part in re.split(r"\s*=\s*", label) if part.strip()]
    if len(parts) < 2:
        return [(label, href)]

    entries: list[tuple[str, str]] = []
    for index, part in enumerate(parts):
        others = parts[:index] + parts[index + 1 :]
        entries.append((" = ".join([part, *others]), href))
    return entries


def index_sort_key(entry: tuple[str, str]) -> str:
    primary = re.split(r"\s*=\s*", entry[0], maxsplit=1)[0].strip()
    return primary.lower()


def topic_index_for_siblings(sibling_files: list[Path]) -> str:
    entries = [
        (extract_title(path), f"{slugify_text(extract_title(path))}.html")
        for path in sibling_files
    ]
    return build_topic_index(entries)


def write_generated_page(folder: Path, source: Path, topic_index: str) -> Path:
    """Copy a topic markdown page into generated/, appending the folder topic index."""
    text = source.read_text(encoding="utf-8").rstrip()
    generated_path = GENERATED_DIR / folder.name / source.name
    generated_path.parent.mkdir(parents=True, exist_ok=True)
    content = f"{text}\n\n"
    if topic_index:
        content += topic_index
    generated_path.write_text(content, encoding="utf-8")
    return generated_path


def write_generated_main_topic(
    folder: Path,
    main_file: Path,
    sibling_files: list[Path],
) -> tuple[Path, str]:
    title, body = split_main_topic(main_file, folder)
    topic_index = topic_index_for_siblings(sibling_files)

    generated_path = GENERATED_DIR / folder.name / main_file.name
    generated_path.parent.mkdir(parents=True, exist_ok=True)
    content = f"# {title}\n\n"
    if body:
        content += f"{body}\n\n"
    if topic_index:
        content += topic_index
    generated_path.write_text(content, encoding="utf-8")
    return generated_path, title


def load_sidebar_order() -> list[str] | None:
    """Read topic folder names from sidebar.txt (one per line)."""
    if not SIDEBAR_TXT.is_file():
        return None

    names: list[str] = []
    for line in SIDEBAR_TXT.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        names.append(stripped)
    return names


def resolve_topic_folder(name: str, folders_by_name: dict[str, Path]) -> Path | None:
    if name in folders_by_name:
        return folders_by_name[name]

    # Allow "Linear Algebra" or "linear-algebra" style entries.
    normalized = name.replace(" ", "-")
    if normalized in folders_by_name:
        return folders_by_name[normalized]

    lowered = normalized.lower()
    for key, path in folders_by_name.items():
        if key.lower() == lowered:
            return path
    return None


def discover_topic_folders() -> list[Path]:
    if not TOPICS_DIR.is_dir():
        raise RuntimeError(f"Topics directory not found: {TOPICS_DIR}")

    folders_by_name = {
        path.name: path for path in TOPICS_DIR.iterdir() if path.is_dir()
    }

    order = load_sidebar_order()
    if order is not None:
        ordered: list[Path] = []
        for name in order:
            folder = resolve_topic_folder(name, folders_by_name)
            if folder is None:
                print(f"warning: sidebar.txt entry not found: {name}")
                continue
            ordered.append(folders_by_name.pop(folder.name))

        # Append any folders missing from sidebar.txt (Glossary last).
        def leftover_key(path: Path) -> tuple[int, str]:
            return (1 if path.name.lower() == "glossary" else 0, path.name.lower())

        ordered.extend(sorted(folders_by_name.values(), key=leftover_key))
        return ordered

    # Fallback: alphabetical, Glossary last.
    def sort_key(path: Path) -> tuple[int, str]:
        return (1 if path.name.lower() == "glossary" else 0, path.name.lower())

    return sorted(folders_by_name.values(), key=sort_key)


def is_bookdown_safe_filename(path: Path) -> bool:
    return re.fullmatch(r"[A-Za-z0-9._-]+\.md", path.name) is not None


def collect_markdown_files(folder: Path) -> list[Path]:
    files = sorted(
        (
            path
            for path in folder.iterdir()
            if path.is_file() and path.suffix.lower() == ".md"
        ),
        key=lambda path: extract_title(path).lower(),
    )
    safe_files: list[Path] = []
    for path in files:
        if is_bookdown_safe_filename(path):
            safe_files.append(path)
        else:
            print(f"warning: skipping unsupported filename for bookdown: {path}")
    return safe_files


def relative_bookdown_path(path: Path) -> str:
    return f"../{path.relative_to(REPO_ROOT).as_posix()}"


def write_bookdown_yml(main_chapters: list[str], sub_chapters: list[str]) -> None:
    lines = [
        'book_filename: "TOPICS"',
        "new_session: no",
        "delete_merged_file: true",
        'output_dir: "_book"',
        "rmd_files:",
        '  - "index.Rmd"',
    ]
    lines.extend(f'  - "{path}"' for path in main_chapters)
    lines.extend(f'  - "{path}"' for path in sub_chapters)
    lines.append("")
    BOOKDOWN_YML.write_text("\n".join(lines), encoding="utf-8")


def assign_chapter_hrefs(titles: list[str]) -> list[str]:
    """Match bookdown's slug collision scheme: foo.html, foo-1.html, foo-2.html, ..."""
    # Home page always owns index.html; reserve it so a chapter titled Index becomes index-1.html.
    counts: dict[str, int] = {"index": 1}
    hrefs: list[str] = []
    for index, title in enumerate(titles):
        if index == 0:
            hrefs.append("index.html")
            continue
        base = slugify_text(title)
        n = counts.get(base, 0)
        counts[base] = n + 1
        hrefs.append(f"{base}.html" if n == 0 else f"{base}-{n}.html")
    return hrefs


def write_site_index(entries: list[tuple[str, str]]) -> Path:
    """Write alphabetical site-wide subtopic index page."""
    expanded: list[tuple[str, str]] = []
    for label, href in entries:
        expanded.extend(expand_synonym_index_entries(label, href))

    sorted_entries = sorted(expanded, key=index_sort_key)
    topic_index = build_topic_index(sorted_entries)
    path = GENERATED_DIR / "Site-Index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    # Heading must not be "Index" — that would overwrite the home page index.html.
    content = "# Site Index\n\n"
    if topic_index:
        content += topic_index
    else:
        content += "No subtopics yet.\n"
    path.write_text(content, encoding="utf-8")
    return path


def write_sidebar_pages(topics: list[dict[str, object]]) -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    SIDEBAR_PAGES_JSON.write_text(json.dumps(topics, indent=2) + "\n", encoding="utf-8")


def generate() -> None:
    main_chapters: list[str] = []
    sub_chapters: list[str] = []
    main_titles: list[str] = []
    sub_titles: list[str] = []
    sub_index_labels: list[str] = []
    sidebar_topics: list[dict[str, object]] = [
        {"title": "Introduction", "href": "index.html", "children": []}
    ]

    for folder in discover_topic_folders():
        main_file = folder / f"{folder.name}.md"
        if not main_file.is_file() or not is_bookdown_safe_filename(main_file):
            continue

        markdown_files = collect_markdown_files(folder)
        if main_file not in markdown_files:
            continue

        sibling_files = [path for path in markdown_files if path != main_file]
        title, body = split_main_topic(main_file, folder)

        if not sibling_files and not body:
            print(f"warning: skipping empty main topic with no entries: {main_file}")
            continue

        generated_main, title = write_generated_main_topic(
            folder, main_file, sibling_files
        )
        main_chapters.append(relative_bookdown_path(generated_main))
        main_titles.append(title)
        sidebar_topics.append(
            {
                "title": title,
                "href": f"{slugify_text(title)}.html",
                "children": [
                    {"title": extract_title(path)} for path in sibling_files
                ],
            }
        )

        topic_index = topic_index_for_siblings(sibling_files)
        for path in sibling_files:
            generated_sub = write_generated_page(folder, path, topic_index)
            sub_chapters.append(relative_bookdown_path(generated_sub))
            # H1 titles drive bookdown HTML filenames; synonym chains are index labels only.
            sub_titles.append(extract_title(path))
            sub_index_labels.append(extract_synonym_chain(path) or extract_title(path))

    # Chapter order in the book: Introduction, mains, Index, then all subtopics.
    # Index is a root sidebar page listing every subtopic alphabetically.
    index_path = write_site_index([])  # placeholder; filled after href assignment
    main_chapters.append(relative_bookdown_path(index_path))
    main_titles.append("Site Index")

    all_titles = ["Introduction", *main_titles, *sub_titles]
    all_hrefs = assign_chapter_hrefs(all_titles)
    # Subtopic hrefs start after Introduction + all main titles (including Site Index).
    sub_start = 1 + len(main_titles)
    sub_entries = list(zip(sub_index_labels, all_hrefs[sub_start:]))
    write_site_index(sub_entries)

    index_href = all_hrefs[1 + len(main_titles) - 1]
    sidebar_topics.append(
        {
            "title": "Site Index",
            "label": "Index",
            "href": index_href,
            "children": [],
        }
    )

    write_bookdown_yml(main_chapters, sub_chapters)
    write_sidebar_pages(sidebar_topics)

    print(
        f"Generated {len(main_chapters)} sidebar topics and "
        f"{len(sub_chapters)} subpages."
    )
    print(f"Updated {BOOKDOWN_YML}")


if __name__ == "__main__":
    try:
        generate()
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
