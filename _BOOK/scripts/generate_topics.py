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


def discover_topic_folders() -> list[Path]:
    if not TOPICS_DIR.is_dir():
        raise RuntimeError(f"Topics directory not found: {TOPICS_DIR}")

    folders = [path for path in TOPICS_DIR.iterdir() if path.is_dir()]
    return sorted(folders, key=lambda path: path.name.lower())


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


def write_generated_main_topic(
    folder: Path,
    main_file: Path,
    sibling_files: list[Path],
) -> tuple[Path, str]:
    title, body = split_main_topic(main_file, folder)
    entries = [
        (extract_title(path), f"{slugify_text(extract_title(path))}.html")
        for path in sibling_files
    ]
    nav = build_topic_index(entries)

    generated_path = GENERATED_DIR / folder.name / main_file.name
    generated_path.parent.mkdir(parents=True, exist_ok=True)
    content = f"# {title}\n\n"
    if body:
        content += f"{body}\n\n"
    content += nav
    generated_path.write_text(content, encoding="utf-8")
    return generated_path, title


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


def write_sidebar_pages(main_titles: list[str]) -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    pages = ["index.html", *(f"{slugify_text(title)}.html" for title in main_titles)]
    SIDEBAR_PAGES_JSON.write_text(json.dumps(pages, indent=2) + "\n", encoding="utf-8")


def generate() -> None:
    main_chapters: list[str] = []
    sub_chapters: list[str] = []
    main_titles: list[str] = []

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

        for path in sibling_files:
            sub_chapters.append(relative_bookdown_path(path))

    write_bookdown_yml(main_chapters, sub_chapters)
    write_sidebar_pages(main_titles)

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
