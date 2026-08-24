#!/usr/bin/env python3
"""Generate robots.txt, sitemap.xml, CNAME, and inject canonical/og:url tags."""

from __future__ import annotations

import html as html_lib
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape


BOOK_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = BOOK_DIR.parent
BOOK_OUT = BOOK_DIR / "_book"
CNAME_SRC = REPO_ROOT / "CNAME"
SITE_ORIGIN = "https://book.danyentezari.com"

CANONICAL_RE = re.compile(
    r'<link\s+rel=["\']canonical["\'][^>]*>\s*',
    re.IGNORECASE,
)
OG_URL_RE = re.compile(
    r'<meta\s+property=["\']og:url["\'][^>]*>\s*',
    re.IGNORECASE,
)
HEAD_CLOSE_RE = re.compile(r"</head>", re.IGNORECASE)


def site_url_for_html(name: str) -> str:
    if name == "index.html":
        return f"{SITE_ORIGIN}/"
    return f"{SITE_ORIGIN}/{name}"


def copy_cname() -> None:
    if not CNAME_SRC.is_file():
        print(f"warning: missing {CNAME_SRC}; skipping CNAME copy", flush=True)
        return
    BOOK_OUT.mkdir(parents=True, exist_ok=True)
    shutil.copy2(CNAME_SRC, BOOK_OUT / "CNAME")


def write_robots() -> None:
    BOOK_OUT.mkdir(parents=True, exist_ok=True)
    text = (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {SITE_ORIGIN}/sitemap.xml\n"
    )
    (BOOK_OUT / "robots.txt").write_text(text, encoding="utf-8")


def html_lastmod_map() -> dict[str, str]:
    """Map HTML filename → W3C lastmod date (YYYY-MM-DD) when known."""
    sys.path.insert(0, str(BOOK_DIR / "scripts"))
    try:
        import latest_updates as lu  # type: ignore
    except Exception:
        return {}

    try:
        href_map = lu.chapter_href_map()
        git_ts_map = lu.git_topic_timestamps()
        dirty = lu.git_dirty_topics()
    except Exception:
        return {}

    out: dict[str, str] = {}
    for rel, href in href_map.items():
        source = lu.topic_source_for_generated(rel)
        if source is None or not source.is_file():
            continue
        ts, _date = lu.update_stamp(source, git_ts_map=git_ts_map, dirty=dirty)
        out[href] = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")
    return out


def write_sitemap(lastmods: dict[str, str]) -> int:
    BOOK_OUT.mkdir(parents=True, exist_ok=True)
    pages = sorted(
        path
        for path in BOOK_OUT.glob("*.html")
        if path.name != "404.html"
    )
    # Prefer index.html first for readability.
    pages.sort(key=lambda p: (p.name != "index.html", p.name.lower()))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path in pages:
        loc = site_url_for_html(path.name)
        lines.append("  <url>")
        lines.append(f"    <loc>{xml_escape(loc)}</loc>")
        lastmod = lastmods.get(path.name)
        if lastmod:
            lines.append(f"    <lastmod>{xml_escape(lastmod)}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")
    (BOOK_OUT / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")
    return len(pages)


def canonical_tags(url: str) -> str:
    escaped = html_lib.escape(url, quote=True)
    return (
        f'<link rel="canonical" href="{escaped}">\n'
        f'<meta property="og:url" content="{escaped}">\n'
    )


def inject_canonicals() -> int:
    if not BOOK_OUT.is_dir():
        return 0
    updated = 0
    for path in BOOK_OUT.glob("*.html"):
        if path.name == "404.html":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        url = site_url_for_html(path.name)
        tags = canonical_tags(url)

        # Drop any previous canonical / og:url so rebuilds stay idempotent.
        cleaned = CANONICAL_RE.sub("", text)
        cleaned = OG_URL_RE.sub("", cleaned)

        match = HEAD_CLOSE_RE.search(cleaned)
        if not match:
            print(f"warning: no </head> in {path.name}; skipping canonical", flush=True)
            continue
        cleaned = cleaned[: match.start()] + tags + cleaned[match.start() :]
        if cleaned != text:
            path.write_text(cleaned, encoding="utf-8")
            updated += 1
    return updated


def main() -> None:
    BOOK_OUT.mkdir(parents=True, exist_ok=True)
    copy_cname()
    write_robots()
    lastmods = html_lastmod_map()
    page_count = write_sitemap(lastmods)
    canon_count = inject_canonicals()
    print(
        f"SEO files: robots.txt, sitemap.xml ({page_count} URLs), CNAME; "
        f"canonical/og:url on {canon_count} page(s).",
        flush=True,
    )


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
