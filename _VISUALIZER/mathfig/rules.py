"""Explicit geometry rules mapping known mathematical structures to scenes."""

from __future__ import annotations

from collections.abc import Callable

from mathfig.geometry import Style, Vec2, add, as_vec2
from mathfig.parser import (
    CURL_COMPONENTS,
    DifferenceOfPartials,
    MathStructure,
    PartialDerivative,
    as_curl_component,
    parse_expression,
    validate_structure,
)
from mathfig.scene import Scene

Spec = dict
Builder = Callable[[Spec], Scene]


def style_from_spec(spec: Spec) -> Style:
    raw = spec.get("style") or {}
    thickness = raw.get("line_thickness_pt", raw.get("line_thickness", 0.4))
    return Style(
        monochrome=bool(raw.get("monochrome", True)),
        axes=bool(raw.get("axes", True)),
        labels=bool(raw.get("labels", True)),
        line_thickness_pt=float(thickness),
        unitsize_cm=float(raw.get("unitsize_cm", 1.0)),
        hatch=bool(raw.get("hatch", True)),
    )


def _region_box(spec: Spec) -> tuple[Vec2, float, float]:
    region = spec.get("region") or {}
    center = as_vec2(region.get("center") or (0.0, 0.0))
    width = float(region.get("width", 2.0))
    height = float(region.get("height", 2.0))
    return center, width, height


def _axis_span(width: float, height: float) -> float:
    return max(width, height, 2.0) * 1.5


def _maybe_parse(spec: Spec) -> MathStructure | None:
    expr = spec.get("expression")
    if not expr:
        return None
    return parse_expression(str(expr))


def _add_axes(
    scene: Scene,
    horizontal: str,
    vertical: str,
    center: Vec2,
    span: float,
) -> None:
    if not scene.style.axes:
        return
    cx, cy = center
    scene.axis(horizontal, (cx - span, cy), (cx + span, cy))
    scene.axis(vertical, (cx, cy - span), (cx, cy + span))


def _cross_partial_scene(
    spec: Spec,
    *,
    horizontal: str,
    vertical: str,
    first: PartialDerivative,
    second: PartialDerivative,
) -> Scene:
    """∂F_vertical / ∂horizontal − ∂F_horizontal / ∂vertical in a plane."""
    scene = Scene(style=style_from_spec(spec))
    center, width, height = _region_box(spec)
    cx, cy = center
    hw, hh = width / 2.0, height / 2.0
    a: Vec2 = (cx - hw, cy - hh)
    b: Vec2 = (cx + hw, cy - hh)
    c: Vec2 = (cx + hw, cy + hh)
    d: Vec2 = (cx - hw, cy + hh)
    span = _axis_span(width, height)

    if scene.style.hatch:
        scene.region("R", (a, b, c, d), hatch=True)
    scene.rectangle("R_rect", center, width, height)
    _add_axes(scene, horizontal, vertical, center, span)

    scene.point("a", a)
    scene.point("b", b)
    scene.point("c", c)
    scene.point("d", d)
    scene.arrow("a", "b", name="circ_bottom")
    scene.arrow("b", "c", name="circ_right")
    scene.arrow("c", "d", name="circ_top")
    scene.arrow("d", "a", name="circ_left")

    short_v: Vec2 = (0.0, 0.25 * height)
    long_v: Vec2 = (0.0, 0.45 * height)
    short_h: Vec2 = (0.25 * width, 0.0)
    long_h: Vec2 = (0.45 * width, 0.0)

    # F_vertical changes with the horizontal coordinate (positive contribution).
    scene.vector(
        (cx - hw, cy),
        short_v,
        label=first.field,
        name="F_vert_left",
        label_anchor="W",
    )
    scene.vector(
        (cx + hw, cy),
        long_v,
        label=first.field,
        name="F_vert_right",
        label_anchor="E",
    )
    # F_horizontal changes with the vertical coordinate (minus contribution).
    scene.vector(
        (cx, cy - hh),
        short_h,
        label=second.field,
        name="F_horz_bottom",
        label_anchor="S",
    )
    scene.vector(
        (cx, cy + hh),
        long_h,
        label=second.field,
        name="F_horz_top",
        label_anchor="N",
    )
    return scene


def build_curl_component(spec: Spec) -> Scene:
    component = str(spec.get("component") or "x")
    if component not in CURL_COMPONENTS:
        raise ValueError(f"unsupported curl component {component!r}")
    difference = CURL_COMPONENTS[component]
    plane = spec.get("plane") or {}
    horizontal = str(plane.get("horizontal") or difference.first.wrt)
    vertical = str(plane.get("vertical") or difference.second.wrt)
    return _cross_partial_scene(
        spec,
        horizontal=horizontal,
        vertical=vertical,
        first=difference.first,
        second=difference.second,
    )


def build_difference_of_cross_partials(spec: Spec) -> Scene:
    structure = _maybe_parse(spec)
    if isinstance(structure, DifferenceOfPartials):
        first, second = structure.first, structure.second
    else:
        curl = as_curl_component(structure) if structure is not None else None
        if curl is not None:
            first, second = curl.difference.first, curl.difference.second
        else:
            first = PartialDerivative("F_z", "y")
            second = PartialDerivative("F_y", "z")
    plane = spec.get("plane") or {}
    horizontal = str(plane.get("horizontal") or first.wrt)
    vertical = str(plane.get("vertical") or second.wrt)
    return _cross_partial_scene(
        spec,
        horizontal=horizontal,
        vertical=vertical,
        first=first,
        second=second,
    )


def build_partial_derivative(spec: Spec) -> Scene:
    scene = Scene(style=style_from_spec(spec))
    structure = _maybe_parse(spec)
    if isinstance(structure, PartialDerivative):
        field, wrt = structure.field, structure.wrt
    else:
        field, wrt = "F", "x"
    scene.axis(wrt, (-3, 0), (3, 0))
    scene.axis("F", (0, -1.5), (0, 3), label=field)
    scene.vector((-1, 0), (0, 0.8), label=field, name="F_left", label_anchor="W")
    scene.vector((1, 0), (0, 1.6), label=field, name="F_right", label_anchor="E")
    scene.line((-1, 0), (1, 0), dashed=True, name="dx")
    if scene.style.labels:
        scene.label(rf"\partial {field}/\partial {wrt}", (0, 2.4), anchor="N")
    return scene


def build_line_integral(spec: Spec) -> Scene:
    scene = Scene(style=style_from_spec(spec))
    scene.axis("x", (-3, 0), (3, 0))
    scene.axis("y", (0, -2), (0, 3))
    path: tuple[Vec2, ...] = (
        (-2.0, -0.8),
        (-1.0, -0.1),
        (0.0, 0.4),
        (1.0, 0.9),
        (2.0, 1.2),
    )
    scene.curve("C", path, smooth=True)
    scene.point("A", path[0])
    scene.point("B", path[-1])
    p = path[2]
    scene.point("P", p)
    scene.vector(p, (0.7, 0.5), label=r"\mathbf{F}", name="F", label_anchor="NE")
    tangent_end = add(p, (0.55, 0.22))
    scene.arrow(p, tangent_end, kind="tangent", name="dr")
    if scene.style.labels:
        scene.label("A", path[0], anchor="SW")
        scene.label("B", path[-1], anchor="NE")
        scene.label("C", (0.4, 1.15), anchor="N")
        scene.label(r"d\mathbf{s}", tangent_end, anchor="SE")
    return scene


def build_closed_loop_circulation(spec: Spec) -> Scene:
    scene = Scene(style=style_from_spec(spec))
    scene.axis("x", (-3, 0), (3, 0))
    scene.axis("y", (0, -3), (0, 3))
    if scene.style.hatch:
        scene.region(
            "A",
            (
                (1.5, 0.0),
                (0.0, 1.5),
                (-1.5, 0.0),
                (0.0, -1.5),
            ),
            hatch=True,
        )
    scene.circle("C", (0.0, 0.0), 1.5)
    scene.point("P", (0.0, 0.0))
    scene.arrow((1.35, 0.35), (1.15, 0.85), name="orient_ne")
    scene.arrow((-0.35, 1.35), (-0.85, 1.15), name="orient_nw")
    scene.arrow((-1.35, -0.35), (-1.15, -0.85), name="orient_sw")
    scene.arrow((0.35, -1.35), (0.85, -1.15), name="orient_se")
    if scene.style.labels:
        scene.label("C", (1.7, 0.9), anchor="E")
        scene.label("P", (0.0, 0.0), anchor="SW")
    return scene


def build_vector_decomposition(spec: Spec) -> Scene:
    scene = Scene(style=style_from_spec(spec))
    scene.axis("x", (-1, 0), (4, 0))
    scene.axis("y", (0, -1), (0, 4))
    origin: Vec2 = (0.5, 0.5)
    scene.point("P", origin)
    scene.vector(origin, (2.2, 1.6), label=r"\mathbf{F}", name="F", label_anchor="NE")
    scene.vector(origin, (2.2, 0.0), label=r"F_\parallel", name="F_par", label_anchor="S")
    scene.vector(
        add(origin, (2.2, 0.0)),
        (0.0, 1.6),
        label=r"F_\perp",
        name="F_perp",
        label_anchor="E",
    )
    scene.line(origin, add(origin, (2.2, 1.6)), dashed=True, name="diag")
    scene.line(
        add(origin, (2.2, 0.0)),
        add(origin, (2.2, 1.6)),
        dashed=True,
        name="upright",
    )
    return scene


def build_taylor_displacement(spec: Spec) -> Scene:
    scene = Scene(style=style_from_spec(spec))
    scene.axis("x", (-0.5, 0), (4, 0))
    scene.axis("y", (0, -0.5), (0, 3.5))
    x0, h = 1.2, 1.4
    f = lambda x: 0.35 * x * x + 0.2
    samples = [(0.4 + 0.35 * i, f(0.4 + 0.35 * i)) for i in range(10)]
    scene.curve("f", samples, smooth=True)
    p0: Vec2 = (x0, f(x0))
    p1: Vec2 = (x0 + h, f(x0 + h))
    slope = 0.7 * x0
    tangent_end: Vec2 = (x0 + h, f(x0) + slope * h)
    scene.point("x0", (x0, 0.0), draw=True)
    scene.point("xh", (x0 + h, 0.0), draw=True)
    scene.line((x0, 0.0), p0, dashed=True, name="drop0")
    scene.line((x0 + h, 0.0), p1, dashed=True, name="drop1")
    scene.arrow(p0, tangent_end, kind="tangent", name="linear")
    scene.vector(p0, (h, 0.0), name="dx")
    if scene.style.labels:
        scene.label("x", (x0, 0.0), anchor="S")
        scene.label(r"x+h", (x0 + h, 0.0), anchor="S")
        scene.label("f", samples[-1], anchor="E")
    return scene


def build_rectangle_boundary_traversal(spec: Spec) -> Scene:
    scene = Scene(style=style_from_spec(spec))
    center, width, height = _region_box(spec)
    cx, cy = center
    hw, hh = width / 2.0, height / 2.0
    a: Vec2 = (cx - hw, cy - hh)
    b: Vec2 = (cx + hw, cy - hh)
    c: Vec2 = (cx + hw, cy + hh)
    d: Vec2 = (cx - hw, cy + hh)
    span = _axis_span(width, height)
    if scene.style.hatch:
        scene.region("R", (a, b, c, d), hatch=True)
    scene.rectangle("R_rect", center, width, height)
    _add_axes(scene, "x", "y", center, span)
    scene.point("a", a)
    scene.point("b", b)
    scene.point("c", c)
    scene.point("d", d)
    scene.arrow("a", "b", name="AB")
    scene.arrow("b", "c", name="BC")
    scene.arrow("c", "d", name="CD")
    scene.arrow("d", "a", name="DA")
    if scene.style.labels:
        scene.label("A", a, anchor="SW")
        scene.label("B", b, anchor="SE")
        scene.label("C", c, anchor="NE")
        scene.label("D", d, anchor="NW")
    return scene


RULES: dict[str, Builder] = {
    "partial_derivative": build_partial_derivative,
    "difference_of_cross_partials": build_difference_of_cross_partials,
    "line_integral": build_line_integral,
    "closed_loop_circulation": build_closed_loop_circulation,
    "curl_component": build_curl_component,
    "vector_decomposition": build_vector_decomposition,
    "taylor_displacement": build_taylor_displacement,
    "rectangle_boundary_traversal": build_rectangle_boundary_traversal,
}


def scene_from_spec(spec: Spec) -> Scene:
    rule_type = spec.get("type")
    if not rule_type:
        raise ValueError("YAML spec is missing required key 'type'")
    if rule_type not in RULES:
        known = ", ".join(sorted(RULES))
        raise ValueError(f"unknown figure type {rule_type!r}; expected one of: {known}")
    structure = _maybe_parse(spec)
    if structure is not None:
        validate_structure(str(rule_type), spec, structure)
    return RULES[str(rule_type)](spec)
