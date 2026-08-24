"""Rasterize a Scene to a black-and-white PNG.

Uses matplotlib so PNG can be produced without Asymptote. The scene graph
is the only input; this module does not parse mathematics.
"""

from __future__ import annotations

from pathlib import Path

from mathfig.geometry import (
    Arrow,
    Axis,
    Circle,
    Curve,
    Label,
    Line,
    Point,
    Rectangle,
    Region,
    Style,
    Vec2,
    Vector,
)
from mathfig.scene import Scene

_ANCHOR = {
    "N": ("center", "bottom", (0, 5)),
    "S": ("center", "top", (0, -5)),
    "E": ("left", "center", (5, 0)),
    "W": ("right", "center", (-5, 0)),
    "NE": ("left", "bottom", (5, 5)),
    "NW": ("right", "bottom", (-5, 5)),
    "SE": ("left", "top", (5, -5)),
    "SW": ("right", "top", (-5, -5)),
    "C": ("center", "center", (0, 0)),
}


def _mathtext(text: str) -> str:
    body = text.strip()
    if body.startswith("$") and body.endswith("$") and len(body) >= 2:
        return body
    return f"${body}$"


def _linewidth(style: Style, thickness: float | None = None) -> float:
    pt = style.line_thickness_pt if thickness is None else thickness
    return max(0.8, pt * 2.0)


def _collect_xy(scene: Scene) -> list[Vec2]:
    points: list[Vec2] = []
    for item in scene.items:
        if isinstance(item, Point):
            points.append(item.xy)
        elif isinstance(item, (Line, Arrow, Axis)):
            points.extend((item.start, item.end))
        elif isinstance(item, Vector):
            points.extend((item.origin, item.end))
        elif isinstance(item, Label):
            points.append(item.xy)
        elif isinstance(item, Rectangle):
            points.extend(item.vertices_ccw)
        elif isinstance(item, Circle):
            cx, cy = item.center
            r = item.radius
            points.extend(((cx - r, cy - r), (cx + r, cy + r)))
        elif isinstance(item, (Curve, Region)):
            points.extend(item.points if isinstance(item, Curve) else item.vertices)
    return points


def _limits(scene: Scene) -> tuple[float, float, float, float]:
    coords = _collect_xy(scene)
    if not coords:
        return (-1.0, 1.0, -1.0, 1.0)
    xs = [p[0] for p in coords]
    ys = [p[1] for p in coords]
    pad = 0.45
    return (min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad)


def _draw_segment(ax, start: Vec2, end: Vec2, lw: float, dashed: bool, arrow: bool) -> None:
    if arrow:
        from matplotlib.patches import FancyArrowPatch

        patch = FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=lw,
            color="black",
            linestyle=(0, (3, 2)) if dashed else "solid",
            shrinkA=0,
            shrinkB=0,
            joinstyle="miter",
        )
        ax.add_patch(patch)
        return
    ax.plot(
        [start[0], end[0]],
        [start[1], end[1]],
        color="black",
        linewidth=lw,
        linestyle=(0, (3, 2)) if dashed else "solid",
        solid_capstyle="butt",
    )


def _draw_label(ax, text: str, xy: Vec2, anchor: str, style: Style) -> None:
    if not style.labels:
        return
    ha, va, offset = _ANCHOR.get(anchor, _ANCHOR["NE"])
    ax.annotate(
        _mathtext(text),
        xy=xy,
        xytext=offset,
        textcoords="offset points",
        ha=ha,
        va=va,
        color="black",
        fontsize=11,
        annotation_clip=False,
    )


def scene_to_png(scene: Scene, path: Path | str, *, dpi: int = 220) -> Path:
    """Write a monochrome PNG of ``scene`` to ``path``."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle as MplCircle
    from matplotlib.patches import Polygon

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    style = scene.style
    xmin, xmax, ymin, ymax = _limits(scene)
    width = (xmax - xmin) * style.unitsize_cm / 2.54
    height = (ymax - ymin) * style.unitsize_cm / 2.54
    fig, ax = plt.subplots(figsize=(max(width, 1.0), max(height, 1.0)))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    lw = _linewidth(style)

    items = list(scene.items)
    if not style.axes:
        items = [i for i in items if not isinstance(i, Axis)]

    for item in items:
        if isinstance(item, Region) and item.hatch and style.hatch:
            poly = Polygon(
                item.vertices,
                closed=True,
                facecolor="white",
                edgecolor="black",
                linewidth=0,
                hatch="////",
                zorder=0,
            )
            ax.add_patch(poly)
        elif isinstance(item, Rectangle) and item.draw:
            sw, se, ne, nw = item.vertices_ccw
            ax.plot(
                [sw[0], se[0], ne[0], nw[0], sw[0]],
                [sw[1], se[1], ne[1], nw[1], sw[1]],
                color="black",
                linewidth=lw,
                zorder=2,
            )
        elif isinstance(item, Axis):
            _draw_segment(ax, item.start, item.end, lw, dashed=False, arrow=True)
            if item.label:
                dx = item.end[0] - item.start[0]
                dy = item.end[1] - item.start[1]
                anchor = "E" if abs(dx) >= abs(dy) and dx >= 0 else (
                    "W" if abs(dx) >= abs(dy) else ("N" if dy >= 0 else "S")
                )
                _draw_label(ax, item.label, item.end, anchor, style)
        elif isinstance(item, Point) and item.draw:
            ax.plot(
                item.xy[0],
                item.xy[1],
                "o",
                color="black",
                markersize=3.2,
                zorder=4,
            )
        elif isinstance(item, Line):
            _draw_segment(
                ax,
                item.start,
                item.end,
                _linewidth(style, item.thickness),
                item.dashed,
                arrow=False,
            )
        elif isinstance(item, Arrow):
            _draw_segment(
                ax,
                item.start,
                item.end,
                _linewidth(style, item.thickness),
                item.dashed,
                arrow=True,
            )
        elif isinstance(item, Vector):
            _draw_segment(ax, item.origin, item.end, lw, dashed=False, arrow=True)
            if item.label:
                dx, dy = item.components
                if item.label_anchor is not None:
                    anchor = item.label_anchor
                elif abs(dx) >= abs(dy):
                    anchor = "E" if dx >= 0 else "W"
                else:
                    anchor = "N" if dy >= 0 else "S"
                _draw_label(ax, item.label, item.end, anchor, style)
        elif isinstance(item, Label):
            _draw_label(ax, item.text, item.xy, item.anchor, style)
        elif isinstance(item, Circle):
            circ = MplCircle(
                item.center,
                item.radius,
                fill=False,
                edgecolor="black",
                linewidth=lw,
                linestyle=(0, (3, 2)) if item.dashed else "solid",
            )
            ax.add_patch(circ)
        elif isinstance(item, Curve):
            xs = [p[0] for p in item.points]
            ys = [p[1] for p in item.points]
            if item.closed:
                xs.append(item.points[0][0])
                ys.append(item.points[0][1])
            ax.plot(
                xs,
                ys,
                color="black",
                linewidth=lw,
                linestyle=(0, (3, 2)) if item.dashed else "solid",
                solid_capstyle="round",
            )

    fig.savefig(
        path,
        dpi=dpi,
        facecolor="white",
        edgecolor="none",
        bbox_inches="tight",
        pad_inches=0.08,
    )
    plt.close(fig)
    return path
