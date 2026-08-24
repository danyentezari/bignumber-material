"""mathfig: scene-graph figures rendered with Asymptote."""

from mathfig.asymptote_renderer import RenderResult, render, scene_to_asymptote
from mathfig.geometry import Style
from mathfig.parser import parse_expression
from mathfig.rules import scene_from_spec
from mathfig.scene import Scene

__all__ = [
    "RenderResult",
    "Scene",
    "Style",
    "parse_expression",
    "render",
    "scene_from_spec",
    "scene_to_asymptote",
]
