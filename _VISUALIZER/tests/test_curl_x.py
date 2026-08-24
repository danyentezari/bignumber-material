from pathlib import Path

import pytest
import yaml

from mathfig.geometry import Axis, Rectangle, Vector
from mathfig.rules import scene_from_spec

from curl_x import build_curl_x_scene

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


def _yaml_scene():
    spec = yaml.safe_load((EXAMPLES / "curl_x.yaml").read_text(encoding="utf-8"))
    return scene_from_spec(spec)


@pytest.fixture(params=["hand", "yaml"])
def curl_scene(request):
    if request.param == "hand":
        return build_curl_x_scene()
    return _yaml_scene()


def test_rectangle_corners(curl_scene) -> None:
    rectangles = curl_scene.rectangles()
    assert len(rectangles) == 1
    rect = rectangles[0]
    assert isinstance(rect, Rectangle)
    assert rect.center == (0.0, 0.0)
    assert rect.width == 2.0
    assert rect.height == 2.0
    assert rect.corners == {
        "sw": (-1.0, -1.0),
        "se": (1.0, -1.0),
        "ne": (1.0, 1.0),
        "nw": (-1.0, 1.0),
    }
    assert curl_scene.get_point("a").xy == (-1.0, -1.0)
    assert curl_scene.get_point("b").xy == (1.0, -1.0)
    assert curl_scene.get_point("c").xy == (1.0, 1.0)
    assert curl_scene.get_point("d").xy == (-1.0, 1.0)


def test_yz_axes(curl_scene) -> None:
    horizontal = curl_scene.get("y")
    vertical = curl_scene.get("z")
    assert isinstance(horizontal, Axis)
    assert isinstance(vertical, Axis)
    assert horizontal.start[1] == horizontal.end[1] == 0.0
    assert horizontal.end[0] > horizontal.start[0]
    assert vertical.start[0] == vertical.end[0] == 0.0
    assert vertical.end[1] > vertical.start[1]


def test_fz_arrows_point_in_z(curl_scene) -> None:
    fz = [v for v in curl_scene.vectors() if v.label == "F_z"]
    assert len(fz) == 2
    for vector in fz:
        assert isinstance(vector, Vector)
        assert vector.components[0] == 0.0
        assert vector.components[1] > 0.0
    left = min(fz, key=lambda v: v.origin[0])
    right = max(fz, key=lambda v: v.origin[0])
    assert left.origin == (-1.0, 0.0)
    assert right.origin == (1.0, 0.0)
    assert right.magnitude > left.magnitude


def test_fy_arrows_point_in_y(curl_scene) -> None:
    fy = [v for v in curl_scene.vectors() if v.label == "F_y"]
    assert len(fy) == 2
    for vector in fy:
        assert vector.components[1] == 0.0
        assert vector.components[0] > 0.0
    bottom = min(fy, key=lambda v: v.origin[1])
    top = max(fy, key=lambda v: v.origin[1])
    assert bottom.origin == (0.0, -1.0)
    assert top.origin == (0.0, 1.0)
    assert top.magnitude > bottom.magnitude


def test_boundary_arrows_are_counterclockwise(curl_scene) -> None:
    a = curl_scene.get_point("a").xy
    b = curl_scene.get_point("b").xy
    c = curl_scene.get_point("c").xy
    d = curl_scene.get_point("d").xy
    pairs = {(arrow.start, arrow.end) for arrow in curl_scene.arrows()}
    assert (a, b) in pairs
    assert (b, c) in pairs
    assert (c, d) in pairs
    assert (d, a) in pairs


def test_hand_specified_matches_yaml_rule() -> None:
    hand = build_curl_x_scene()
    yaml_scene = _yaml_scene()
    assert [v.origin for v in hand.vectors()] == [v.origin for v in yaml_scene.vectors()]
    assert [v.components for v in hand.vectors()] == [
        v.components for v in yaml_scene.vectors()
    ]
    assert [p.xy for p in hand.points()] == [p.xy for p in yaml_scene.points()]
