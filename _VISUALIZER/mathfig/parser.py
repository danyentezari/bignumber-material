"""Parse mathematical expressions into a small typed structure tree.

The parser never emits Asymptote. Geometry rules consume ``MathStructure``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Union

_WS = re.compile(r"\s+")
_BRACE_COMP = re.compile(r"F_\{([xyz])\}")
_PLAIN_COMP = re.compile(r"F_([xyz])")
_LATEX_PARTIAL = re.compile(
    r"\\frac\{\\partial\s*F_\{?([xyz])\}?\}\{\\partial\s*([xyz])\}"
)
_UNICODE_PARTIAL = re.compile(r"∂\s*F_\{?([xyz])\}?\s*/\s*∂\s*([xyz])")
_ASCII_PARTIAL = re.compile(r"(?:d|partial|del)\s*F_([xyz])\s*/\s*(?:d|partial|del)\s*([xyz])")
_LEADING_ASSIGN = re.compile(r"^[A-Za-z]+(?:_\{?[xyz]\}?)?\s*=")


@dataclass(frozen=True)
class PartialDerivative:
    """∂F_i / ∂x_j."""

    field: str
    wrt: str

    @property
    def component(self) -> str:
        return self.field.split("_", 1)[-1]


@dataclass(frozen=True)
class DifferenceOfPartials:
    """∂u/∂a − ∂v/∂b."""

    first: PartialDerivative
    second: PartialDerivative


@dataclass(frozen=True)
class LineIntegral:
    field: str = "F"
    start: str | None = None
    end: str | None = None
    closed: bool = False


@dataclass(frozen=True)
class ClosedLoopCirculation:
    field: str = "F"
    curve: str = "C"


@dataclass(frozen=True)
class CurlComponent:
    component: str
    difference: DifferenceOfPartials


@dataclass(frozen=True)
class VectorDecomposition:
    field: str = "F"
    tangent: str = r"d\mathbf{s}"


@dataclass(frozen=True)
class TaylorDisplacement:
    variable: str = "x"
    increment: str = "h"


@dataclass(frozen=True)
class RectangleBoundaryTraversal:
    labels: tuple[str, str, str, str] = ("A", "B", "C", "D")


MathStructure = Union[
    PartialDerivative,
    DifferenceOfPartials,
    LineIntegral,
    ClosedLoopCirculation,
    CurlComponent,
    VectorDecomposition,
    TaylorDisplacement,
    RectangleBoundaryTraversal,
]

CURL_COMPONENTS: dict[str, DifferenceOfPartials] = {
    "x": DifferenceOfPartials(
        PartialDerivative("F_z", "y"),
        PartialDerivative("F_y", "z"),
    ),
    "y": DifferenceOfPartials(
        PartialDerivative("F_x", "z"),
        PartialDerivative("F_z", "x"),
    ),
    "z": DifferenceOfPartials(
        PartialDerivative("F_y", "x"),
        PartialDerivative("F_x", "y"),
    ),
}

RULE_STRUCTURES: dict[str, type[MathStructure]] = {
    "partial_derivative": PartialDerivative,
    "difference_of_cross_partials": DifferenceOfPartials,
    "line_integral": LineIntegral,
    "closed_loop_circulation": ClosedLoopCirculation,
    "curl_component": CurlComponent,
    "vector_decomposition": VectorDecomposition,
    "taylor_displacement": TaylorDisplacement,
    "rectangle_boundary_traversal": RectangleBoundaryTraversal,
}


def _strip_expression(text: str) -> str:
    body = text.strip().strip("'\"")
    body = _LEADING_ASSIGN.sub("", body).strip()
    body = body.replace("\\\\", "\\")
    return _WS.sub("", body)


def _field(component: str) -> str:
    return f"F_{component}"


def _parse_partial_token(token: str) -> PartialDerivative | None:
    for pattern in (_LATEX_PARTIAL, _UNICODE_PARTIAL, _ASCII_PARTIAL):
        match = pattern.search(token)
        if match:
            return PartialDerivative(_field(match.group(1)), match.group(2))
    return None


def _split_difference(text: str) -> tuple[str, str] | None:
    depth = 0
    for i, ch in enumerate(text):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        elif ch == "-" and depth == 0 and i > 0:
            return text[:i], text[i + 1 :]
    return None


def _from_sympy(expr: object) -> MathStructure | None:
    try:
        import sympy as sp
        from sympy.core.function import Derivative
    except ImportError:
        return None

    def as_partial(node: object) -> PartialDerivative | None:
        if not isinstance(node, Derivative):
            return None
        if len(node.variables) != 1:
            return None
        wrt = str(node.variables[0])
        field = str(node.expr)
        field = _BRACE_COMP.sub(r"F_\1", field)
        if not _PLAIN_COMP.fullmatch(field) and not field.startswith("F_"):
            return None
        if wrt not in "xyz":
            return None
        return PartialDerivative(field, wrt)

    expr = sp.expand(expr)
    partial = as_partial(expr)
    if partial is not None:
        return partial
    if isinstance(expr, sp.Add) and len(expr.args) == 2:
        terms = list(expr.args)
        pos: PartialDerivative | None = None
        neg: PartialDerivative | None = None
        for term in terms:
            coeff, rest = term.as_coeff_Mul()
            parsed = as_partial(rest) or as_partial(term)
            if parsed is None:
                return None
            if coeff < 0:
                neg = parsed
            else:
                pos = parsed
        if pos is not None and neg is not None:
            return DifferenceOfPartials(pos, neg)
    return None


def _try_sympy(text: str) -> MathStructure | None:
    try:
        from sympy.parsing.latex import parse_latex
    except ImportError:
        return None
    try:
        expr = parse_latex(text)
    except Exception:
        return None
    return _from_sympy(expr)


def parse_expression(text: str) -> MathStructure:
    """Parse LaTeX, unicode, or a few ASCII forms into a ``MathStructure``."""
    original = text.strip()
    lowered = original.lower()
    if "oint" in lowered or "closed" in lowered and "loop" in lowered:
        return ClosedLoopCirculation()
    if "oint" in original or r"\oint" in original:
        return ClosedLoopCirculation()
    if "integral" in lowered or r"\int" in original:
        closed = "closed" in lowered or r"\oint" in original
        start, end = None, None
        from_to = re.search(
            r"from\s+(\S+)\s+to\s+(\S+)", original, flags=re.IGNORECASE
        )
        if from_to:
            start, end = from_to.group(1), from_to.group(2)
        limits = re.search(r"\\int_\{([^}]+)\}\^\{([^}]+)\}", original)
        if limits:
            start, end = limits.group(1), limits.group(2)
        return LineIntegral(start=start, end=end, closed=closed)
    if "taylor" in lowered:
        return TaylorDisplacement()
    if "decomp" in lowered:
        return VectorDecomposition()
    if "rectangle" in lowered and "bound" in lowered:
        return RectangleBoundaryTraversal()

    body = _strip_expression(original)
    split = _split_difference(body)
    if split is not None:
        left, right = split
        first = _parse_partial_token(left)
        second = _parse_partial_token(right)
        if first is not None and second is not None:
            return DifferenceOfPartials(first, second)
    single = _parse_partial_token(body)
    if single is not None:
        return single

    if "\\" in original:
        sympy_result = _try_sympy(original)
        if sympy_result is not None:
            return sympy_result

    raise ValueError(f"unrecognized mathematical expression: {text!r}")


def as_curl_component(structure: MathStructure) -> CurlComponent | None:
    if isinstance(structure, CurlComponent):
        return structure
    if not isinstance(structure, DifferenceOfPartials):
        return None
    for name, expected in CURL_COMPONENTS.items():
        if structure == expected:
            return CurlComponent(component=name, difference=structure)
    return None


def validate_structure(rule_type: str, spec: dict, structure: MathStructure) -> None:
    """Reject an expression that does not match the selected rule family."""
    if rule_type not in RULE_STRUCTURES:
        raise ValueError(f"unknown figure type {rule_type!r}")

    if rule_type == "curl_component":
        curl = as_curl_component(structure)
        if curl is None:
            raise ValueError(
                "expression is not a curl component of the form "
                "∂F_k/∂u − ∂F_u/∂k"
            )
        wanted = spec.get("component")
        if wanted is not None and curl.component != str(wanted):
            raise ValueError(
                f"expression is the {curl.component}-component of curl, "
                f"but spec.component is {wanted!r}"
            )
        plane = spec.get("plane") or {}
        expected = CURL_COMPONENTS[curl.component]
        if plane.get("horizontal") and plane["horizontal"] != expected.first.wrt:
            raise ValueError(
                f"plane.horizontal should be {expected.first.wrt} "
                f"for the {curl.component}-component"
            )
        if plane.get("vertical") and plane["vertical"] != expected.second.wrt:
            raise ValueError(
                f"plane.vertical should be {expected.second.wrt} "
                f"for the {curl.component}-component"
            )
        return

    if rule_type == "difference_of_cross_partials":
        if not isinstance(structure, (DifferenceOfPartials, CurlComponent)):
            raise ValueError("expected a difference of cross-partials")
        return

    if rule_type == "partial_derivative":
        if not isinstance(structure, PartialDerivative):
            raise ValueError("expected a single partial derivative")
        return

    if rule_type == "line_integral":
        if not isinstance(structure, LineIntegral):
            raise ValueError("expected a line-integral expression")
        return

    if rule_type == "closed_loop_circulation":
        if isinstance(structure, ClosedLoopCirculation):
            return
        if isinstance(structure, LineIntegral) and structure.closed:
            return
        raise ValueError("expected a closed-loop circulation")

    expected_type = RULE_STRUCTURES[rule_type]
    if not isinstance(structure, expected_type):
        # Optional expressions for purely geometric rules may be omitted.
        if rule_type in {
            "vector_decomposition",
            "taylor_displacement",
            "rectangle_boundary_traversal",
        }:
            return
        raise ValueError(
            f"expression for {rule_type} does not match {expected_type.__name__}"
        )
