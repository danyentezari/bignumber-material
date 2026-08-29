#!/usr/bin/env bash
# Publish main.pdf to the handbook's GitHub repo (default branch) as mathstat.pdf.
#
# Usage:
#   ./publish.sh
#   ./publish.sh -m "Your commit message"
#   ./publish.sh --message "Your commit message"
set -euo pipefail
cd "$(dirname "$0")"

DEPLOY_REPO="https://github.com/danyentezari/sprp-mathematical-statistics.git"
SOURCE_PDF="main.pdf"
PUBLISH_PDF="mathstat.pdf"
COMMIT_MSG="Publish handbook PDF $(date -u +%Y-%m-%dT%H:%MZ)"

usage() {
  cat <<'EOF'
Usage: ./publish.sh [-m MESSAGE | --message MESSAGE]

  -m, --message   Commit message for the published PDF
  -h, --help      Show this help
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -m|--message)
      if [[ $# -lt 2 || -z "${2:-}" ]]; then
        echo "error: $1 requires a non-empty message" >&2
        exit 1
      fi
      COMMIT_MSG="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "error: unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ ! -f "$SOURCE_PDF" ]]; then
  echo "error: $SOURCE_PDF not found in $(pwd). Build it first (e.g. ./build-pdf.sh)." >&2
  exit 1
fi

if ! command -v git >/dev/null 2>&1; then
  echo "error: git not found" >&2
  exit 1
fi

DEPLOY_DIR="$(mktemp -d "${TMPDIR:-/tmp}/mathstat-publish.XXXXXX")"
cleanup() { rm -rf "$DEPLOY_DIR"; }
trap cleanup EXIT

echo "Cloning $DEPLOY_REPO ..."
git clone --depth 1 "$DEPLOY_REPO" "$DEPLOY_DIR"

cp "$SOURCE_PDF" "$DEPLOY_DIR/$PUBLISH_PDF"

cd "$DEPLOY_DIR"
git add "$PUBLISH_PDF"

if git diff --cached --quiet; then
  echo "No PDF changes to publish."
  exit 0
fi

git commit -m "$COMMIT_MSG"
git push origin HEAD
echo "Published $PUBLISH_PDF to $DEPLOY_REPO"
