import pytest

from mathfig.parser import (
    ClosedLoopCirculation,
    CurlComponent,
    DifferenceOfPartials,
    LineIntegral,
    PartialDerivative,
    as_curl_component,
    parse_expression,
    validate_structure,
)


def test_parse_curl_x_latex() -> None:
    structure = parse_expression(
        r"\frac{\partial F_z}{\partial y}-\frac{\partial F_y}{\partial z}"
    )
    assert structure == DifferenceOfPartials(
        PartialDerivative("F_z", "y"),
        PartialDerivative("F_y", "z"),
    )
    curl = as_curl_component(structure)
    assert curl == CurlComponent(component="x", difference=structure)


def test_parse_assignment_and_unicode() -> None:
    structure = parse_expression("X = ∂F_z/∂y - ∂F_y/∂z")
    assert as_curl_component(structure) is not None
    assert as_curl_component(structure).component == "x"


def test_parse_single_partial() -> None:
    structure = parse_expression(r"\frac{\partial F_z}{\partial y}")
    assert structure == PartialDerivative("F_z", "y")


def test_parse_line_integral_phrase() -> None:
    structure = parse_expression("integral from a to b of F · ds")
    assert isinstance(structure, LineIntegral)
    assert structure.start == "a"
    assert structure.end == "b"
    assert structure.closed is False


def test_parse_closed_loop() -> None:
    structure = parse_expression(r"\oint_C \mathbf{F} \cdot d\mathbf{s}")
    assert isinstance(structure, ClosedLoopCirculation)


def test_validate_curl_component_rejects_mismatch() -> None:
    structure = parse_expression(
        r"\frac{\partial F_z}{\partial y}-\frac{\partial F_y}{\partial z}"
    )
    with pytest.raises(ValueError):
        validate_structure(
            "curl_component",
            {"component": "z", "plane": {"horizontal": "x", "vertical": "y"}},
            structure,
        )


def test_validate_curl_component_accepts_x() -> None:
    structure = parse_expression(
        r"\frac{\partial F_z}{\partial y}-\frac{\partial F_y}{\partial z}"
    )
    validate_structure(
        "curl_component",
        {
            "component": "x",
            "plane": {"horizontal": "y", "vertical": "z"},
        },
        structure,
    )


def test_unrecognized_expression_fails() -> None:
    with pytest.raises(ValueError):
        parse_expression("the square of the hypotenuse")
