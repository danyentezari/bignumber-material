"""Cartesian geometry primitives for textbook-style 2D figures.

Coordinates are exact plane pairs. This module does not emit Asymptote.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Union

Vec2 = tuple[float, float]

Anchor = Literal["N", "S", "E", "W", "NE", "NW", "SE", "SW", "C"]
ArrowKind = Literal["segment", "vector", "tangent"]


def as_vec2(xy: Vec2 | tuple[float, float] | list[float]) -> Vec2:
    if len(xy) != 2:
        raise ValueError(f"expected a 2D coordinate, got {xy!r}")
    return (float(xy[0]), float(xy[1]))


def add(a: Vec2, b: Vec2) -> Vec2:
    return (a[0] + b[0], a[1] + b[1])


def sub(a: Vec2, b: Vec2) -> Vec2:
    return (a[0] - b[0], a[1] - b[1])


def scale(a: Vec2, k: float) -> Vec2:
    return (a[0] * k, a[1] * k)


def midpoint(a: Vec2, b: Vec2) -> Vec2:
    return ((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0)


def norm(a: Vec2) -> float:
    return (a[0] ** 2 + a[1] ** 2) ** 0.5


@dataclass(frozen=True)
class Style:
    monochrome: bool = True
    axes: bool = True
    labels: bool = True
    line_thickness_pt: float = 0.4
    axis_thickness_pt: float = 0.4
    unitsize_cm: float = 1.0
    hatch: bool = True
    label_pt: float = 11.0
    png_width_px: int | None = None
    png_height_px: int | None = None


@dataclass(frozen=True)
class Point:
    name: str
    xy: Vec2
    draw: bool = True


@dataclass(frozen=True)
class Line:
    start: Vec2
    end: Vec2
    dashed: bool = False
    thickness: float | None = None
    name: str = ""


@dataclass(frozen=True)
class Arrow:
    start: Vec2
    end: Vec2
    kind: ArrowKind = "segment"
    dashed: bool = False
    thickness: float | None = None
    name: str = ""


@dataclass(frozen=True)
class Curve:
    points: tuple[Vec2, ...]
    closed: bool = False
    dashed: bool = False
    smooth: bool = False
    name: str = ""


@dataclass(frozen=True)
class Rectangle:
    name: str
    center: Vec2
    width: float
    height: float
    draw: bool = True

    @property
    def corners(self) -> dict[str, Vec2]:
        cx, cy = self.center
        hw, hh = self.width / 2.0, self.height / 2.0
        return {
            "sw": (cx - hw, cy - hh),
            "se": (cx + hw, cy - hh),
            "ne": (cx + hw, cy + hh),
            "nw": (cx - hw, cy + hh),
        }

    @property
    def vertices_ccw(self) -> tuple[Vec2, Vec2, Vec2, Vec2]:
        c = self.corners
        return (c["sw"], c["se"], c["ne"], c["nw"])


@dataclass(frozen=True)
class Circle:
    name: str
    center: Vec2
    radius: float
    dashed: bool = False
    thickness: float | None = None


@dataclass(frozen=True)
class Region:
    name: str
    vertices: tuple[Vec2, ...]
    hatch: bool = True


@dataclass(frozen=True)
class Axis:
    name: str
    start: Vec2
    end: Vec2
    label: str | None = None
    thickness: float | None = None


@dataclass(frozen=True)
class Label:
    text: str
    xy: Vec2
    anchor: Anchor = "NE"
    name: str = ""
    size: float | None = None


@dataclass(frozen=True)
class Vector:
    origin: Vec2
    components: Vec2
    label: str | None = None
    name: str = ""
    label_anchor: Anchor | None = None
    thickness: float | None = None

    @property
    def end(self) -> Vec2:
        return add(self.origin, self.components)

    @property
    def magnitude(self) -> float:
        return norm(self.components)


Primitive = Union[
    Point,
    Line,
    Arrow,
    Curve,
    Rectangle,
    Circle,
    Region,
    Axis,
    Label,
    Vector,
]
