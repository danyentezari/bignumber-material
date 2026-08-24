from pathlib import Path

import pytest
import yaml

from mathfig.asymptote_renderer import render
from mathfig.cli import main
from mathfig.rules import RULES, scene_from_spec

from curl_x import build_curl_x_scene

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


@pytest.mark.parametrize("rule_type", sorted(RULES))
def test_every_rule_builds_a_nonempty_scene(rule_type: str) -> None:
    spec: dict = {"type": rule_type}
    if rule_type == "curl_component":
        spec["component"] = "x"
        spec["plane"] = {"horizontal": "y", "vertical": "z"}
    elif rule_type == "partial_derivative":
        spec["expression"] = r"\frac{\partial F_z}{\partial y}"
    elif rule_type == "difference_of_cross_partials":
        spec["expression"] = (
            r"\frac{\partial F_z}{\partial y}-\frac{\partial F_y}{\partial z}"
        )
        spec["plane"] = {"horizontal": "y", "vertical": "z"}
    elif rule_type == "line_integral":
        spec["expression"] = "integral from a to b of F · ds"
    elif rule_type == "closed_loop_circulation":
        spec["expression"] = r"\oint_C F \cdot ds"
    scene = scene_from_spec(spec)
    assert len(scene.items) > 0


def test_curl_y_and_z_components_use_the_matching_plane() -> None:
    y_scene = scene_from_spec(
        {
            "type": "curl_component",
            "component": "y",
            "plane": {"horizontal": "z", "vertical": "x"},
        }
    )
    z_scene = scene_from_spec(
        {
            "type": "curl_component",
            "component": "z",
            "plane": {"horizontal": "x", "vertical": "y"},
        }
    )
    assert y_scene.get("z")
    assert y_scene.get("x")
    assert z_scene.get("x")
    assert z_scene.get("y")
    assert any(v.label == "F_x" for v in y_scene.vectors())
    assert any(v.label == "F_y" for v in z_scene.vectors())


def test_unknown_type_rejected() -> None:
    with pytest.raises(ValueError):
        scene_from_spec({"type": "manifold_chart"})


def test_cli_writes_asy_without_invoking_renderer(tmp_path: Path) -> None:
    output = tmp_path / "curl_x.png"
    code = main(
        [
            str(EXAMPLES / "curl_x.yaml"),
            "--output",
            str(output),
            "--asy-only",
        ]
    )
    assert code == 0
    asy = tmp_path / "curl_x.asy"
    assert asy.is_file()
    text = asy.read_text(encoding="utf-8")
    assert 'label("$y$"' in text
    assert "(1,0)--(1,0.9)" in text


def test_render_invoke_false_only_writes_asy(tmp_path: Path) -> None:
    result = render(build_curl_x_scene(), tmp_path / "fig.png", invoke=False)
    assert result.asy.is_file()
    assert result.png is None
    assert result.pdf is None
    assert result.svg is None


def test_render_writes_png(tmp_path: Path) -> None:
    result = render(build_curl_x_scene(), tmp_path / "curl_x.png", invoke=True)
    assert result.png is not None and result.png.is_file()
    assert result.png.stat().st_size > 0
    assert result.pdf is None
    assert result.svg is None


@pytest.mark.integration
def test_asy_renders_when_installed(tmp_path: Path) -> None:
    import shutil

    if shutil.which("asy") is None:
        pytest.skip("asy not installed")
    spec = yaml.safe_load((EXAMPLES / "curl_x.yaml").read_text(encoding="utf-8"))
    scene = scene_from_spec(spec)
    result = render(scene, tmp_path / "curl_x.png", invoke=True)
    assert result.png is not None and result.png.is_file()
