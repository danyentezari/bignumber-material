from mathfig.geometry import Arrow, Label, Line, Point
from mathfig.scene import Scene, auto_anchor


def test_named_point_arrow_resolves_coordinates() -> None:
    scene = Scene()
    scene.point("a", (-1, -1))
    scene.point("b", (1, -1))
    scene.arrow("a", "b", name="ab")
    arrow = scene.get("ab")
    assert isinstance(arrow, Arrow)
    assert arrow.start == (-1.0, -1.0)
    assert arrow.end == (1.0, -1.0)
    assert scene.get_point("a").xy == (-1.0, -1.0)


def test_coordinate_arrow_and_dashed_line() -> None:
    scene = Scene()
    scene.arrow((-1, 0), (1, 0), kind="vector", name="v")
    scene.line((0, -1), (0, 1), dashed=True, name="guide")
    arrow = scene.get("v")
    line = scene.get("guide")
    assert isinstance(arrow, Arrow)
    assert arrow.kind == "vector"
    assert isinstance(line, Line)
    assert line.dashed is True
    assert line.start == (0.0, -1.0)
    assert line.end == (0.0, 1.0)


def test_label_anchor_can_be_set_or_inferred() -> None:
    scene = Scene()
    scene.label("A", (1, 1), name="q1")
    scene.label("B", (2, 0), anchor="E", name="on_axis")
    inferred = scene.get("q1")
    explicit = scene.get("on_axis")
    assert isinstance(inferred, Label)
    assert inferred.anchor == "NE"
    assert isinstance(explicit, Label)
    assert explicit.anchor == "E"


def test_auto_anchor_moves_off_axes() -> None:
    assert auto_anchor((0, 0)) == "NE"
    assert auto_anchor((2, 0)) == "N"
    assert auto_anchor((0, 2)) == "E"
    assert auto_anchor((-1, -2)) == "SW"


def test_duplicate_point_name_rejected() -> None:
    scene = Scene()
    scene.point("a", (0, 0))
    try:
        scene.point("a", (1, 1))
    except ValueError:
        return
    raise AssertionError("expected ValueError for duplicate point name")


def test_points_are_recorded() -> None:
    scene = Scene()
    scene.point("p", (0.5, -0.25), draw=False)
    point = scene.get("p")
    assert isinstance(point, Point)
    assert point.draw is False
    assert scene.named_points["p"] is point
