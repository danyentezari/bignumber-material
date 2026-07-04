#!/usr/bin/env python3
"""Copy topic image assets into the rendered book output."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


BOOK_DIR = Path(__file__).resolve().parents[1]
TOPICS_DIR = BOOK_DIR.parent / "_TOPICS"
OUTPUT_DIR = BOOK_DIR / "_book"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}


def main() -> None:
    if not TOPICS_DIR.is_dir():
        raise RuntimeError(f"Topics directory not found: {TOPICS_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    copied = 0

    for path in TOPICS_DIR.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        dest = OUTPUT_DIR / path.name
        if dest.exists() and dest.read_bytes() != path.read_bytes():
            print(f"warning: overwriting asset with same name: {path.name}")

        shutil.copy2(path, dest)
        copied += 1

    print(f"Copied {copied} topic assets to {OUTPUT_DIR}.")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
