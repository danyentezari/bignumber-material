#!/usr/bin/env bash
# Regenerate main.tex from _TOPICS and build main.pdf once.
# Topic files ending in .draft.md or .skip.md are ignored (kept in git, not exported).
#
# Derivation of Normal Distribution PDF width is per page via a topic comment:
#   <!-- pdf-page-width: default -->
#   <!-- pdf-page-width: wide -->
# (applied by _BOOK/scripts/export_to_tex.py)
#
# Usage: ./build-pdf.sh
# HTML book: ./_BOOK/build.sh
# Publish PDF: ./publish.sh
set -euo pipefail
cd "$(dirname "$0")"

export PATH="${HOME}/Library/TinyTeX/bin/universal-darwin:${PATH}"

if ! command -v latexmk >/dev/null 2>&1; then
  echo "error: latexmk not found. Expected TinyTeX at ~/Library/TinyTeX/bin/universal-darwin" >&2
  exit 1
fi

python3 _BOOK/scripts/export_to_tex.py
latexmk -pdf -interaction=nonstopmode -file-line-error -synctex=1 main.tex
echo "Built $(pwd)/main.pdf"
