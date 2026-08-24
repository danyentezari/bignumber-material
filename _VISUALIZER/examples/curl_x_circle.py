"""Output of X = ∂F_z/∂y − ∂F_y/∂z in a right-handed xyz frame.

The difference is the x-component of curl: one vector, normal to a
circular neighborhood in a plane parallel to yz, away from the origin.
"""

from __future__ import annotations

from pathlib import Path

from mathfig.asymptote_renderer import render
from mathfig.geometry import Style, Vec2
from mathfig.scene import Scene

EXAMPLE_PNG = Path(__file__).resolve().parent / "curl_x_circle.png"


def xyz(x: float, y: float, z: float) -> Vec2:
    """Right-handed math axes: y right, z up, +x out toward the lower left."""
    return (y - 0.55 * x, z - 0.35 * x)


def build_curl_x_circle_scene() -> Scene:
    origin = xyz(0.0, 0.0, 0.0)
    # Wide layout so a large circle fills the 610x365 frame.
    cx, cy, cz = 0.15, 4.20, 2.55
    radius = 2.40
    center = xyz(cx, cy, cz)

    scene = Scene(
        style=Style(
            monochrome=True,
            axes=True,
            labels=True,
            hatch=False,
            line_thickness_pt=0.14,
            label_pt=7.0,
            png_width_px=610,
            png_height_px=365,
        )
    )
    scene.axis("x", origin, xyz(2.8, 0.0, 0.0), label="x")
    scene.axis("y", origin, xyz(0.0, 8.2, 0.0), label="y")
    scene.axis("z", origin, xyz(0.0, 0.0, 5.4), label="z")
    scene.circle("C", center, radius)
    tip = xyz(cx + 1.5, cy, cz)
    scene.arrow(center, tip, kind="vector")
    scene.label(
        r"(\partial F_z/\partial y-\partial F_y/\partial z,\,0,\,0)",
        xyz(cx, cy + radius + 0.25, cz),
        anchor="E",
        size=4.5,
    )
    return scene


if __name__ == "__main__":
    result = render(build_curl_x_circle_scene(), EXAMPLE_PNG, invoke=True)
    print(result.png)
