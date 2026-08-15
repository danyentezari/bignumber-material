#!/usr/bin/env python3
"""Discover topic folders and generate bookdown config plus topic index pages."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path


BOOK_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = BOOK_DIR.parent
TOPICS_DIR = REPO_ROOT / "_TOPICS"
GENERATED_DIR = BOOK_DIR / "generated"
BOOKDOWN_YML = BOOK_DIR / "_bookdown.yml"
SIDEBAR_PAGES_JSON = GENERATED_DIR / "sidebar-pages.json"
SIDEBAR_TXT = BOOK_DIR / "sidebar.txt"
BIBLIOGRAPHY_DIR = TOPICS_DIR / "Bibliography"
RESERVED_TOPIC_FOLDERS = frozenset({"Bibliography"})


def slugify_text(text: str) -> str:
    # Strip accents so bookdown HTML filenames stay ASCII-safe.
    normalized = unicodedata.normalize("NFKD", text)
    normalized = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    normalized = normalized.lower().replace("'", "")
    # Match bookdown/pandoc: drop (), commas so U(1) → u1 and Type-(0,2) → type-02.
    normalized = re.sub(r"[(),]", "", normalized)
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

    def matches_title(name: str) -> bool:
        primary = re.split(r"\s*=\s*", name, maxsplit=1)[0].strip()
        if primary.lower() == title.lower():
            return True
        primary_key = slugify_text(primary)
        title_key = slugify_text(title)
        if primary_key == title_key:
            return True
        # Allow singular/plural drift: Tensor vs Tensors, One-Form vs 1-form.
        if primary_key.rstrip("s") == title_key.rstrip("s"):
            return True
        if primary_key.replace("1-form", "one-form") == title_key:
            return True
        if title_key.replace("one-form", "1-form") == primary_key:
            return True
        return False

    # Prefer a synonym chain whose primary name matches this page's H1.
    for name in synonym_names:
        if matches_title(name):
            return name

    # Single-definition pages may use a slightly different H1 (e.g. Delta Function
    # vs Dirac Delta Function = ...); still use the chain.
    if len(names) == 1:
        return synonym_names[0]

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


def topic_index_for_siblings(
    sibling_files: list[Path],
    href_by_path: dict[Path, str] | None = None,
) -> str:
    entries = []
    for path in sibling_files:
        title = extract_title(path)
        if href_by_path is not None and path in href_by_path:
            href = href_by_path[path]
        else:
            href = f"{slugify_text(title)}.html"
        entries.append((title, href))
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
    main_file: Path | None,
    sibling_files: list[Path],
    href_by_path: dict[Path, str] | None = None,
) -> tuple[Path, str]:
    if main_file is not None:
        title, body = split_main_topic(main_file, folder)
        out_name = main_file.name
    else:
        title = folder.name.replace("-", " ")
        body = ""
        out_name = f"{folder.name}.md"

    topic_index = topic_index_for_siblings(sibling_files, href_by_path)

    generated_path = GENERATED_DIR / folder.name / out_name
    generated_path.parent.mkdir(parents=True, exist_ok=True)
    content = f"# {title}\n\n"
    if body:
        content += f"{body}\n\n"
    if topic_index:
        content += topic_index
    generated_path.write_text(content, encoding="utf-8")
    return generated_path, title


def collect_all_topic_markdown_files() -> list[Path]:
    """Every topic .md that should become a book chapter (including Bibliography)."""
    if not TOPICS_DIR.is_dir():
        return []

    files: list[Path] = []
    for folder in sorted(TOPICS_DIR.iterdir(), key=lambda p: p.name.lower()):
        if not folder.is_dir():
            continue
        files.extend(collect_markdown_files(folder))
    return files


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
        path.name: path
        for path in TOPICS_DIR.iterdir()
        if path.is_dir() and path.name not in RESERVED_TOPIC_FOLDERS
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


def load_bibliography_source() -> tuple[Path, list[Path]]:
    """Return the Bibliography main page and optional entry pages."""
    main_file = BIBLIOGRAPHY_DIR / "Bibliography.md"
    if not main_file.is_file() or not is_bookdown_safe_filename(main_file):
        raise RuntimeError(f"Missing bibliography source: {main_file}")

    markdown_files = collect_markdown_files(BIBLIOGRAPHY_DIR)
    if main_file not in markdown_files:
        raise RuntimeError(f"Bibliography main page not found in {BIBLIOGRAPHY_DIR}")

    sibling_files = [path for path in markdown_files if path != main_file]
    return main_file, sibling_files


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
    # Pass 1: discover folders and collect titles in bookdown order so href
    # collisions (e.g. algebra Field vs physics Field → field-1.html) are known
    # before topic-index links are written.
    folder_jobs: list[dict[str, object]] = []
    main_titles: list[str] = []
    sub_titles: list[str] = []
    sub_index_labels: list[str] = []
    sub_paths: list[Path] = []
    skipped: list[str] = []

    for folder in discover_topic_folders():
        markdown_files = collect_markdown_files(folder)
        if not markdown_files:
            continue

        main_file = folder / f"{folder.name}.md"
        has_main = main_file.is_file() and main_file in markdown_files
        if has_main:
            sibling_files = [path for path in markdown_files if path != main_file]
            title, body = split_main_topic(main_file, folder)
            source_main: Path | None = main_file
            if not sibling_files and not body:
                print(
                    f"warning: empty topic stub included with no entries yet: "
                    f"{main_file.relative_to(REPO_ROOT)}"
                )
        else:
            # Folder has .md pages but no Folder.md — still include every page.
            sibling_files = list(markdown_files)
            title = folder.name.replace("-", " ")
            body = ""
            source_main = None
            print(
                f"warning: missing {main_file.name}; synthesizing topic page "
                f"so {len(sibling_files)} markdown file(s) are included"
            )

        folder_jobs.append(
            {
                "folder": folder,
                "main_file": source_main,
                "sibling_files": sibling_files,
                "title": title,
            }
        )
        main_titles.append(title)
        for path in sibling_files:
            sub_paths.append(path)
            sub_titles.append(extract_title(path))
            sub_index_labels.append(extract_synonym_chain(path) or extract_title(path))

    bib_main_file, bib_sibling_files = load_bibliography_source()
    bib_sub_titles = [extract_title(path) for path in bib_sibling_files]

    # Chapter order: Introduction, mains, Index, Bibliography, subtopics, bib entries.
    main_titles_with_index = [*main_titles, "Site Index", "Bibliography"]
    all_titles = [
        "Introduction",
        *main_titles_with_index,
        *sub_titles,
        *bib_sub_titles,
    ]
    all_hrefs = assign_chapter_hrefs(all_titles)
    main_hrefs = all_hrefs[1 : 1 + len(main_titles_with_index)]
    sub_start = 1 + len(main_titles_with_index)
    sub_hrefs = all_hrefs[sub_start : sub_start + len(sub_titles)]
    bib_sub_hrefs = all_hrefs[sub_start + len(sub_titles) :]
    href_by_path = dict(zip(sub_paths, sub_hrefs))
    bib_href_by_path = dict(zip(bib_sibling_files, bib_sub_hrefs))

    # Pass 2: write generated pages with collision-aware topic-index links.
    main_chapters: list[str] = []
    sub_chapters: list[str] = []
    sidebar_topics: list[dict[str, object]] = [
        {"title": "Introduction", "href": "index.html", "children": []}
    ]
    # Site Index includes every topic/subtopic page (not just subtopics).
    site_index_entries: list[tuple[str, str]] = []

    for job, main_href in zip(folder_jobs, main_hrefs[:-2]):
        folder = job["folder"]
        main_file = job["main_file"]
        sibling_files = job["sibling_files"]
        assert isinstance(folder, Path)
        assert main_file is None or isinstance(main_file, Path)
        assert isinstance(sibling_files, list)

        topic_index = topic_index_for_siblings(sibling_files, href_by_path)
        generated_main, title = write_generated_main_topic(
            folder, main_file, sibling_files, href_by_path
        )

        main_chapters.append(relative_bookdown_path(generated_main))
        site_index_entries.append((title, main_href))
        sidebar_topics.append(
            {
                "title": title,
                "href": main_href,
                "children": [
                    {"title": extract_title(path)} for path in sibling_files
                ],
            }
        )

        for path in sibling_files:
            generated_sub = write_generated_page(folder, path, topic_index)
            sub_chapters.append(relative_bookdown_path(generated_sub))

    site_index_entries.extend(zip(sub_index_labels, sub_hrefs))

    index_path = write_site_index(site_index_entries)
    main_chapters.append(relative_bookdown_path(index_path))

    bib_topic_index = topic_index_for_siblings(bib_sibling_files, bib_href_by_path)
    bibliography_main, bib_title = write_generated_main_topic(
        BIBLIOGRAPHY_DIR,
        bib_main_file,
        bib_sibling_files,
        bib_href_by_path,
    )
    main_chapters.append(relative_bookdown_path(bibliography_main))
    site_index_entries.append((bib_title, main_hrefs[-1]))

    for path in bib_sibling_files:
        generated_bib_entry = write_generated_page(
            BIBLIOGRAPHY_DIR,
            path,
            bib_topic_index,
        )
        sub_chapters.append(relative_bookdown_path(generated_bib_entry))
    site_index_entries.extend(
        (extract_title(path), href)
        for path, href in zip(bib_sibling_files, bib_sub_hrefs)
    )

    # Rewrite Site Index once bibliography entries are known.
    write_site_index(site_index_entries)

    sidebar_topics.append(
        {
            "title": "Site Index",
            "label": "Index",
            "href": main_hrefs[-2],
            "children": [],
        }
    )
    sidebar_topics.append(
        {
            "title": "Bibliography",
            "href": main_hrefs[-1],
            "children": [
                {"title": extract_title(path)} for path in bib_sibling_files
            ],
        }
    )

    write_bookdown_yml(main_chapters, sub_chapters)
    write_sidebar_pages(sidebar_topics)

    # Fail loudly if any topic markdown file was left out of the book.
    expected_sources = {
        path.resolve() for path in collect_all_topic_markdown_files()
    }
    included_sources: set[Path] = set()
    for job in folder_jobs:
        main_file = job["main_file"]
        if isinstance(main_file, Path):
            included_sources.add(main_file.resolve())
        for path in job["sibling_files"]:  # type: ignore[union-attr]
            included_sources.add(Path(path).resolve())
    included_sources.add(bib_main_file.resolve())
    for path in bib_sibling_files:
        included_sources.add(path.resolve())

    missing = sorted(expected_sources - included_sources, key=lambda p: str(p))
    if missing:
        for path in missing:
            skipped.append(str(path.relative_to(REPO_ROOT)))
        raise RuntimeError(
            "These markdown files were not included in the book:\n  - "
            + "\n  - ".join(skipped)
        )

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
