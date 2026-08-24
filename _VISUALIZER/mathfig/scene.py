"""Ordered scene graph with a fluent Cartesian builder."""

from __future__ import annotations

from typing import Iterable, Sequence

from mathfig.geometry import (
    Anchor,
    Arrow,
    ArrowKind,
    Axis,
    Circle,
    Curve,
    Label,
    Line,
    Point,
    Primitive,
    Rectangle,
    Region,
    Style,
    Vec2,
    Vector,
    as_vec2,
)


def auto_anchor(xy: Vec2) -> Anchor:
    """Place a label away from the nearest axis through the origin."""
    x, y = xy
    eps = 1e-12
    on_h = abs(y) < eps
    on_v = abs(x) < eps
    if on_h and on_v:
        return "NE"
    if on_h:
        return "N"
    if on_v:
        return "E"
    if y > 0 and x > 0:
        return "NE"
    if y > 0 and x < 0:
        return "NW"
    if y < 0 and x < 0:
        return "SW"
    return "SE"


class Scene:
    """Collection of named geometry primitives drawn in insertion order."""

    def __init__(self, style: Style | None = None) -> None:
        self.style = style or Style()
        self._items: list[Primitive] = []
        self._points: dict[str, Point] = {}
        self._named: dict[str, Primitive] = {}

    @property
    def items(self) -> tuple[Primitive, ...]:
        return tuple(self._items)

    @property
    def named_points(self) -> dict[str, Point]:
        return dict(self._points)

    def get(self, name: str) -> Primitive:
        try:
            return self._named[name]
        except KeyError as exc:
            raise KeyError(f"no primitive named {name!r}") from exc

    def get_point(self, name: str) -> Point:
        try:
            return self._points[name]
        except KeyError as exc:
            raise KeyError(f"no point named {name!r}") from exc

    def points(self) -> list[Point]:
        return [p for p in self._items if isinstance(p, Point)]

    def lines(self) -> list[Line]:
        return [p for p in self._items if isinstance(p, Line)]

    def arrows(self) -> list[Arrow]:
        return [p for p in self._items if isinstance(p, Arrow)]

    def vectors(self) -> list[Vector]:
        return [p for p in self._items if isinstance(p, Vector)]

    def axes(self) -> list[Axis]:
        return [p for p in self._items if isinstance(p, Axis)]

    def labels(self) -> list[Label]:
        return [p for p in self._items if isinstance(p, Label)]

    def rectangles(self) -> list[Rectangle]:
        return [p for p in self._items if isinstance(p, Rectangle)]

    def regions(self) -> list[Region]:
        return [p for p in self._items if isinstance(p, Region)]

    def circles(self) -> list[Circle]:
        return [p for p in self._items if isinstance(p, Circle)]

    def curves(self) -> list[Curve]:
        return [p for p in self._items if isinstance(p, Curve)]

    def _store(self, item: Primitive, name: str = "") -> None:
        self._items.append(item)
        if name:
            if name in self._named:
                raise ValueError(f"duplicate primitive name {name!r}")
            self._named[name] = item

    def _resolve(self, ref: str | Vec2 | Sequence[float]) -> Vec2:
        if isinstance(ref, str):
            return self.get_point(ref).xy
        return as_vec2(ref)

    def axis(
        self,
        name: str,
        start: Vec2 | Sequence[float],
        end: Vec2 | Sequence[float],
        label: str | None = None,
        thickness: float | None = None,
    ) -> Scene:
        item = Axis(
            name=name,
            start=as_vec2(start),
            end=as_vec2(end),
            label=name if label is None else label,
            thickness=thickness,
        )
        self._store(item, name)
        return self

    def point(
        self,
        name: str,
        xy: Vec2 | Sequence[float],
        draw: bool = True,
    ) -> Scene:
        item = Point(name=name, xy=as_vec2(xy), draw=draw)
        if name in self._points:
            raise ValueError(f"duplicate point name {name!r}")
        self._points[name] = item
        self._store(item, name)
        return self

    def line(
        self,
        a: str | Vec2 | Sequence[float],
        b: str | Vec2 | Sequence[float],
        *,
        dashed: bool = False,
        thickness: float | None = None,
        name: str = "",
    ) -> Scene:
        item = Line(
            start=self._resolve(a),
            end=self._resolve(b),
            dashed=dashed,
            thickness=thickness,
            name=name,
        )
        self._store(item, name)
        return self

    def arrow(
        self,
        a: str | Vec2 | Sequence[float],
        b: str | Vec2 | Sequence[float],
        *,
        kind: ArrowKind = "segment",
        dashed: bool = False,
        thickness: float | None = None,
        name: str = "",
    ) -> Scene:
        item = Arrow(
            start=self._resolve(a),
            end=self._resolve(b),
            kind=kind,
            dashed=dashed,
            thickness=thickness,
            name=name,
        )
        self._store(item, name)
        return self

    def vector(
        self,
        origin: Vec2 | Sequence[float],
        components: Vec2 | Sequence[float],
        label: str | None = None,
        name: str = "",
        label_anchor: Anchor | None = None,
        thickness: float | None = None,
    ) -> Scene:
        item = Vector(
            origin=as_vec2(origin),
            components=as_vec2(components),
            label=label,
            name=name,
            label_anchor=label_anchor,
            thickness=thickness,
        )
        self._store(item, name)
        return self

    def rectangle(
        self,
        name: str,
        center: Vec2 | Sequence[float],
        width: float,
        height: float,
        draw: bool = True,
    ) -> Scene:
        item = Rectangle(
            name=name,
            center=as_vec2(center),
            width=float(width),
            height=float(height),
            draw=draw,
        )
        self._store(item, name)
        return self

    def region(
        self,
        name: str,
        vertices: Iterable[Vec2 | Sequence[float]],
        hatch: bool = True,
    ) -> Scene:
        verts = tuple(as_vec2(v) for v in vertices)
        if len(verts) < 3:
            raise ValueError("a region needs at least three vertices")
        item = Region(name=name, vertices=verts, hatch=hatch)
        self._store(item, name)
        return self

    def circle(
        self,
        name: str,
        center: Vec2 | Sequence[float],
        radius: float,
        dashed: bool = False,
        thickness: float | None = None,
    ) -> Scene:
        item = Circle(
            name=name,
            center=as_vec2(center),
            radius=float(radius),
            dashed=dashed,
            thickness=thickness,
        )
        self._store(item, name)
        return self

    def curve(
        self,
        name: str,
        points: Iterable[Vec2 | Sequence[float]],
        closed: bool = False,
        dashed: bool = False,
        smooth: bool = False,
    ) -> Scene:
        pts = tuple(as_vec2(p) for p in points)
        if len(pts) < 2:
            raise ValueError("a curve needs at least two points")
        item = Curve(
            name=name,
            points=pts,
            closed=closed,
            dashed=dashed,
            smooth=smooth,
        )
        self._store(item, name)
        return self

    def label(
        self,
        text: str,
        xy: Vec2 | Sequence[float],
        anchor: Anchor | None = None,
        name: str = "",
        size: float | None = None,
    ) -> Scene:
        pos = as_vec2(xy)
        item = Label(
            text=text,
            xy=pos,
            anchor=anchor if anchor is not None else auto_anchor(pos),
            name=name,
            size=size,
        )
        self._store(item, name)
        return self
