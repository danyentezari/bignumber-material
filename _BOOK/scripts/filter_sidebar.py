#!/usr/bin/env python3
"""Rebuild the book sidebar with topic folders and nested subtopics."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


BOOK_DIR = Path(__file__).resolve().parents[1]
BOOK_OUTPUT_DIR = BOOK_DIR / "_book"
SIDEBAR_PAGES_JSON = BOOK_DIR / "generated" / "sidebar-pages.json"
TOC_PATTERN = re.compile(
    r'(<ul class="book-toc list-unstyled">)(.*?)(</ul>)',
    re.DOTALL,
)
LINK_PATTERN = re.compile(
    r'<a class="([^"]*)" href="([^"]+)"><span class="header-section-number">(\d+)</span>\s*(.*?)</a>',
    re.DOTALL,
)


def normalize_title(title: str) -> str:
    normalized = re.sub(r"\s+", " ", title.strip())
    for apostrophe in ("\u0027", "\u2019", "\u2018", "`"):
        normalized = normalized.replace(apostrophe, "'")
    return normalized.lower()


def parse_toc_links(toc_body: str) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    by_href: dict[str, dict[str, str]] = {}
    by_title: dict[str, dict[str, str]] = {}

    for match in LINK_PATTERN.finditer(toc_body):
        active_class, href, section_number, title = match.groups()
        normalized_title = normalize_title(title)
        item = {
            "href": href,
            "section_number": section_number,
            "title": re.sub(r"\s+", " ", title.strip()),
        }
        by_href[href] = item
        by_title[normalized_title] = item

    return by_href, by_title


def lookup_entry(
    entry: dict[str, object],
    by_href: dict[str, dict[str, str]],
    by_title: dict[str, dict[str, str]],
) -> dict[str, str] | None:
    href = entry.get("href")
    if isinstance(href, str) and href in by_href:
        return by_href[href]

    title = entry.get("title")
    if isinstance(title, str):
        return by_title.get(normalize_title(title))

    return None


def topic_is_open(
    main_item: dict[str, str],
    child_items: list[dict[str, str]],
    current_href: str,
) -> bool:
    if main_item["href"] == current_href:
        return True
    return any(child["href"] == current_href for child in child_items)


def render_link(item: dict[str, str], current_href: str) -> str:
    active_class = "active" if item["href"] == current_href else ""
    return (
        f'<a class="{active_class}" href="{item["href"]}">'
        f'<span class="header-section-number">{item["section_number"]}</span> '
        f'{item["title"]}</a>'
    )


def render_parent_link(
    item: dict[str, str],
    current_href: str,
    child_items: list[dict[str, str]],
) -> str:
    classes: list[str] = []
    if item["href"] == current_href:
        classes.append("active")
    elif any(child["href"] == current_href for child in child_items):
        classes.append("active-parent")
    active_class = " ".join(classes)
    class_attr = f' class="{active_class}"' if active_class else ' class=""'
    return (
        f"<a{class_attr} href=\"{item['href']}\">"
        f'<span class="header-section-number">{item["section_number"]}</span> '
        f"{item['title']}</a>"
    )


def build_sidebar_toc(
    sidebar: list[dict[str, object]],
    by_href: dict[str, dict[str, str]],
    by_title: dict[str, dict[str, str]],
    current_href: str,
) -> str:
    lines = ['<ul class="book-toc list-unstyled">']

    for entry in sidebar:
        main_item = lookup_entry(entry, by_href, by_title)
        if not main_item:
            continue

        children = entry.get("children", [])
        child_items: list[dict[str, str]] = []
        if isinstance(children, list):
            for child in children:
                if not isinstance(child, dict):
                    continue
                child_item = lookup_entry(child, by_href, by_title)
                if child_item:
                    child_items.append(child_item)

        if child_items:
            open_class = " is-open" if topic_is_open(main_item, child_items, current_href) else ""
            expanded = "true" if open_class else "false"
            lines.append(f'<li class="book-toc-topic{open_class}">')
            lines.append('<div class="book-toc-topic-header">')
            lines.append(
                f'<button type="button" class="book-toc-toggle" '
                f'aria-expanded="{expanded}" aria-label="Toggle subtopics"></button>'
            )
            lines.append(render_parent_link(main_item, current_href, child_items))
            lines.append("</div>")
            lines.append('<ul class="book-toc-section">')
            for child_item in child_items:
                lines.append(f"<li>{render_link(child_item, current_href)}</li>")
            lines.append("</ul>")
            lines.append("</li>")
        else:
            lines.append('<li class="book-toc-topic book-toc-topic--leaf">')
            lines.append('<div class="book-toc-topic-header">')
            lines.append(
                '<span class="book-toc-toggle book-toc-toggle--placeholder" '
                'aria-hidden="true"></span>'
            )
            lines.append(render_link(main_item, current_href))
            lines.append("</div>")
            lines.append("</li>")

    lines.append("</ul>")
    return "\n".join(lines)


def current_page_href(html: str, toc_body: str) -> str | None:
    for match in LINK_PATTERN.finditer(toc_body):
        active_class, href, _, _ = match.groups()
        if "active" in active_class.split():
            return href

    title_match = re.search(r"<title>(\d+)\s+(.*?)\s+\|", html)
    if not title_match:
        return None

    page_title = title_match.group(2).strip()
    _, by_title = parse_toc_links(toc_body)
    item = by_title.get(normalize_title(page_title))
    return item["href"] if item else None


def rebuild_toc(html: str, sidebar: list[dict[str, object]]) -> str:
    match = TOC_PATTERN.search(html)
    if not match:
        return html

    prefix, toc_body, suffix = match.groups()
    by_href, by_title = parse_toc_links(toc_body)
    current_href = current_page_href(html, toc_body)
    if not current_href:
        return html

    rebuilt = build_sidebar_toc(sidebar, by_href, by_title, current_href)
    return html[: match.start()] + rebuilt + html[match.end() :]


def load_sidebar_manifest() -> list[dict[str, object]]:
    raw = json.loads(SIDEBAR_PAGES_JSON.read_text(encoding="utf-8"))
    if isinstance(raw, list) and raw and all(isinstance(item, str) for item in raw):
        return [{"title": "", "href": href, "children": []} for href in raw]
    if not isinstance(raw, list):
        raise RuntimeError(f"Invalid sidebar manifest format: {SIDEBAR_PAGES_JSON}")
    return raw


def main() -> None:
    if not SIDEBAR_PAGES_JSON.is_file():
        raise RuntimeError(f"Missing sidebar manifest: {SIDEBAR_PAGES_JSON}")

    sidebar = load_sidebar_manifest()
    html_files = sorted(BOOK_OUTPUT_DIR.glob("*.html"))

    if not html_files:
        raise RuntimeError(f"No HTML files found in {BOOK_OUTPUT_DIR}")

    for path in html_files:
        if path.name == "404.html":
            continue
        html = path.read_text(encoding="utf-8")
        updated = rebuild_toc(html, sidebar)
        if updated != html:
            path.write_text(updated, encoding="utf-8")

    print(f"Rebuilt sidebar in {len(html_files) - 1} pages.")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
