from mathfig.asymptote_renderer import fmt_pair, scene_to_asymptote
from mathfig.geometry import Style
from mathfig.scene import Scene

from curl_x import build_curl_x_scene


def test_formatter_uses_compact_cartesian_pairs() -> None:
    assert fmt_pair((-1.0, -1.0)) == "(-1,-1)"
    assert fmt_pair((1.0, 0.9)) == "(1,0.9)"
    assert fmt_pair((0.0, 0.5)) == "(0,0.5)"


def test_renderer_emits_curl_coordinates_and_labels() -> None:
    source = scene_to_asymptote(build_curl_x_scene())
    for coordinate in (
        "(-1,-1)",
        "(1,-1)",
        "(1,1)",
        "(-1,1)",
        "(-1,0)--(-1,0.5)",
        "(1,0)--(1,0.9)",
        "(0,-1)--(0.5,-1)",
        "(0,1)--(0.9,1)",
        "(-3,0)--(3,0)",
        "(0,-3)--(0,3)",
    ):
        assert coordinate in source
    assert 'label("$y$"' in source
    assert 'label("$z$"' in source
    assert 'label("$F_z$"' in source
    assert 'label("$F_y$"' in source
    assert "Arrow(SimpleHead)" in source
    assert "pattern(\"hatch\")" in source
    assert "black+0.4pt" in source


def test_dashed_construction_line_in_asymptote() -> None:
    scene = Scene(style=Style())
    scene.line((0, 0), (1, 1), dashed=True)
    source = scene_to_asymptote(scene)
    assert "dashed" in source
    assert "(0,0)--(1,1)" in source


def test_axes_can_be_suppressed() -> None:
    scene = Scene(style=Style(axes=False))
    scene.axis("x", (-1, 0), (1, 0))
    scene.point("p", (0, 0))
    source = scene_to_asymptote(scene)
    assert "(-1,0)--(1,0)" not in source
    assert "dot((0,0)" in source
