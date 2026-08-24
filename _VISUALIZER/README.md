# mathfig

Scene-graph figures for textbook-style 2D mathematics, rendered with Asymptote.

```text
Mathematical expression
        ↓
SymPy / LaTeX parsing
        ↓
Mathematical structure
        ↓
Geometry interpretation rules
        ↓
Scene graph
        ↓
Asymptote renderer
        ↓
PNG
```

The renderer never sees the parser. Geometry is specified in exact Cartesian coordinates, then compiled to Asymptote.

## Setup

Python 3.11+. PNG output uses matplotlib (installed with the package). Asymptote is optional and used when `asy` is on PATH. Unit tests do not require Asymptote.

```bash
cd _VISUALIZER
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python -m pytest
```

## CLI

```bash
python -m mathfig.cli examples/curl_x.yaml --output curl_x.png
```

Writes `curl_x.asy` and `curl_x.png`. Use `--asy-only` to skip rasterization. PDF/SVG are written only if the output suffix is `.pdf` or `.svg`.

## Scene API

```python
from mathfig import Scene

scene = Scene()
scene.axis("x", (-3, 0), (3, 0))
scene.axis("y", (0, -3), (0, 3))
scene.point("a", (-1, -1))
scene.point("b", (1, -1))
scene.arrow("a", "b")
scene.label("A", (0, 0))
```

## YAML rules

`type` selects an explicit geometry rule (`curl_component`, `partial_derivative`, `line_integral`, …). Expressions are checked against that rule; they are not free-form captions.
