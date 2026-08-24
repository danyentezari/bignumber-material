"""Command-line entry: YAML spec → scene graph → PNG."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from mathfig.rules import scene_from_spec
from mathfig.asymptote_renderer import render


def load_spec(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        spec = yaml.safe_load(handle)
    if not isinstance(spec, dict):
        raise ValueError(f"{path} did not contain a YAML mapping")
    return spec


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="mathfig",
        description="Build textbook-style 2D mathematical figures with Asymptote.",
    )
    parser.add_argument("input", type=Path, help="YAML figure specification")
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        required=True,
        help="Output path (default format is PNG; .asy is always written)",
    )
    parser.add_argument(
        "--png",
        action="store_true",
        help="Also write PNG when the output suffix is not .png",
    )
    parser.add_argument(
        "--asy-only",
        action="store_true",
        help="Write Asymptote source without invoking asy",
    )
    args = parser.parse_args(argv)

    spec = load_spec(args.input)
    scene = scene_from_spec(spec)
    result = render(scene, args.output, png=args.png, invoke=not args.asy_only)
    print(result.asy)
    if result.pdf:
        print(result.pdf)
    if result.svg:
        print(result.svg)
    if result.png:
        print(result.png)
    return 0


if __name__ == "__main__":
    sys.exit(main())
