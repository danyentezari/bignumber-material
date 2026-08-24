"""Hand-specified curl X-component figure in the yz-plane.

X = ∂F_z/∂y − ∂F_y/∂z
"""

from __future__ import annotations

from pathlib import Path

from mathfig.asymptote_renderer import render
from mathfig.geometry import Style
from mathfig.scene import Scene


def build_curl_x_scene() -> Scene:
    scene = Scene(style=Style(monochrome=True, axes=True, labels=True))

    scene.region(
        "R",
        ((-1, -1), (1, -1), (1, 1), (-1, 1)),
        hatch=True,
    )
    scene.rectangle("R_rect", (0, 0), 2, 2)

    scene.axis("y", (-3, 0), (3, 0))
    scene.axis("z", (0, -3), (0, 3))

    scene.point("a", (-1, -1))
    scene.point("b", (1, -1))
    scene.point("c", (1, 1))
    scene.point("d", (-1, 1))

    scene.arrow("a", "b", name="circ_bottom")
    scene.arrow("b", "c", name="circ_right")
    scene.arrow("c", "d", name="circ_top")
    scene.arrow("d", "a", name="circ_left")

    scene.vector((-1, 0), (0, 0.5), label="F_z", name="F_vert_left", label_anchor="W")
    scene.vector((1, 0), (0, 0.9), label="F_z", name="F_vert_right", label_anchor="E")
    scene.vector((0, -1), (0.5, 0), label="F_y", name="F_horz_bottom", label_anchor="S")
    scene.vector((0, 1), (0.9, 0), label="F_y", name="F_horz_top", label_anchor="N")

    return scene


if __name__ == "__main__":
    output = Path(__file__).resolve().parent / "curl_x.png"
    scene = build_curl_x_scene()
    result = render(scene, output, invoke=True)
    print(result.png)
