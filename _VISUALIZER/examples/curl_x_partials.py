"""Plot ∂F_z/∂y and ∂F_y/∂z on a circular neighborhood in xyz."""

from __future__ import annotations

from pathlib import Path

from mathfig.asymptote_renderer import render
from mathfig.geometry import Style, Vec2
from mathfig.scene import Scene

EXAMPLE_PNG = Path(__file__).resolve().parent / "curl_x_partials.png"


def xyz(x: float, y: float, z: float) -> Vec2:
    """Right-handed math axes: y right, z up, +x out toward the lower left."""
    return (y - 0.55 * x, z - 0.35 * x)


def build_curl_x_partials_scene() -> Scene:
    origin = xyz(0.0, 0.0, 0.0)
    cx, cy, cz = 0.15, 4.20, 2.85
    radius = 2.20
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

    # ∂F_z/∂y: F_z ∥ +z at two y-stations; larger at larger y.
    scene.vector(
        xyz(cx, cy - radius - 0.15, cz - 0.35),
        (0.0, 0.85),
        name="Fz_left",
    )
    scene.vector(
        xyz(cx, cy + radius + 0.15, cz - 0.35),
        (0.0, 1.85),
        name="Fz_right",
    )
    scene.label(
        r"\partial F_z/\partial y",
        xyz(cx, cy + radius + 0.35, cz + 1.55),
        anchor="E",
        size=5.0,
    )

    # ∂F_y/∂z: F_y ∥ +y at two z-stations; larger at larger z.
    scene.vector(
        xyz(cx, cy - 0.35, cz - radius - 0.15),
        (0.85, 0.0),
        name="Fy_bottom",
    )
    scene.vector(
        xyz(cx, cy - 0.35, cz + radius + 0.15),
        (1.85, 0.0),
        name="Fy_top",
    )
    scene.label(
        r"\partial F_y/\partial z",
        xyz(cx, cy + 1.7, cz + radius + 0.35),
        anchor="N",
        size=5.0,
    )
    return scene


if __name__ == "__main__":
    result = render(build_curl_x_partials_scene(), EXAMPLE_PNG, invoke=True)
    print(result.png)
