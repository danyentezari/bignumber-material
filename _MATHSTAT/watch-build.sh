#!/usr/bin/env bash
# Watch main.tex and included images; rebuild main.pdf on each change.
#
# Usage: ./watch-build.sh
# Stop:  Ctrl-C
set -euo pipefail
cd "$(dirname "$0")"

export PATH="${HOME}/Library/TinyTeX/bin/universal-darwin:${PATH}"

if ! command -v latexmk >/dev/null 2>&1; then
  echo "error: latexmk not found. Expected TinyTeX at ~/Library/TinyTeX/bin/universal-darwin" >&2
  exit 1
fi

if [[ ! -f main.tex ]]; then
  echo "error: main.tex not found in $(pwd)" >&2
  exit 1
fi

echo "Watching main.tex; rebuilding main.pdf on save (Ctrl-C to stop)..."
exec latexmk -pdf -pvc -view=none \
  -interaction=nonstopmode \
  -file-line-error \
  -synctex=1 \
  main.tex
