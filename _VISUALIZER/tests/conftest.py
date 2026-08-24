"""Ensure the mathfig package is importable when pytest is launched from the repo root."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"

for path in (ROOT, EXAMPLES):
    text = str(path)
    if text not in sys.path:
        sys.path.insert(0, text)
