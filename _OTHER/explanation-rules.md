Query the appropriate Notebook LLM document. The answer must be grounded from the notebook! The answer must lead with an indefinite article and a noun, and must use at least 10 words and not exceed 100 words. The explanation must also include what it is used for. Always use "that is used" so the reader sees what the concept is, then what it is for. Never use parentheses, slashes, or "or" for synonyms. If synonyms exist, add this note after the first explanation. The only allowed mathematical terms allowed in the explanation are elementary undergraduate mathematics terms. For example:

1. Set
2. Element
3. Member
4. Subset
5. Superset
6. Empty set
7. Union
8. Intersection
9. Difference
10. Complement
11. Cartesian product
12. Relation
13. Function
14. Mapping
15. Domain
16. Codomain
17. Range
18. Image
19. Preimage
20. Value
21. Variable
22. Constant
23. Parameter
24. Real number
25. Complex number
26. Integer
27. Rational number
28. Irrational number
29. Natural number
30. Vector
31. Matrix
32. Scalar
33. Sequence
34. Series
35. Polynomial
36. Monomial
37. Degree
38. Equation
39. Inequality
40. Expression
41. Identity
42. Solution
43. Root
44. Zero
45. Limit
46. Continuity
47. Derivative
48. Integral
49. Gradient
50. Dimension
51. Basis
52. Span
53. Subspace
54. Linear transformation
55. Kernel
56. Image
57. Rank
58. Determinant
59. Eigenvalue
60. Eigenvector
61. Inner product
62. Norm
63. Distance
64. Metric
65. Open set
66. Closed set
67. Neighborhood
68. Topology
69. Probability
70. Random variable
71. Expectation
72. Variance
73. Graph
74. Vertex
75. Edge

Do not distract the reader by involving other mathematical terms outside of this list when they are not even done reading the explanation of the one they're currently reading!

## Elementary Example

For every relevant definition file, add an Elementary Example section with two parts:

1. **Simple** — a small finite instance with 1–3 sets of 3–7 elements, or the lowest-dimensional case that still matches the definition.
2. **General** — a higher-dimensional, matrix, or multi-point instance of the same definition.

Each part’s prose must not exceed 40 words. Every new symbol must be named before use, with a `where` list when needed. The example must accurately illustrate the file’s definition.

### Grounding policy

1. Gemini Notebook first. Ask for the definition and for any finite toy example in the sources.
2. If GN has the structure but no finite toy, build a small finite instance of that structure yourself. Keep the example faithful to the GN definition. Cite the GN source in References. Bundle.md is the approved pattern for this case.
3. If still stuck, draft with ChatGPT only as a fallback. The draft must include the finite sets and explicit named sources with page or section. Do not write the example into a topic file until those cites are verified.
4. Public web notes may suggest ideas. They do not replace GN. If used after verify, cite them as secondary References. Do not treat private course materials as available to scrape.
5. Never invent a source example that does not exist. Never invent a citation.

### Template

```
## Elementary Example

### Simple

<at most 40 words>

$$
f : A \rightarrow B
$$

$$
A = \{ 1, 2, 3 \}
$$

$$
B = \{ 2, 4, 9 \}
$$

$$
f(1) = 2,\quad f(2) = 4,\quad f(3) = 9
$$

### General

<at most 40 words; define every new symbol>

$$
\ldots
$$

where

- \ldots
```

Approved Simple and General pattern: see `Tensors.md`.

## Fractions

Always write fractions with `\dfrac{...}{...}`. Do not use `\frac`, `\tfrac`, or inline slash fractions such as `a/b` inside math.

## Leibniz Notation

Use Leibniz notation for all derivative and integration transformations throughout this project.

- Derivatives: write $\dfrac{dy}{dx}$, $\dfrac{d}{dx}[f(x)]$, $\dfrac{\partial f}{\partial x}$, and higher-order forms such as $\dfrac{d^{2}y}{dx^{2}}$ or $\dfrac{d^{n}f}{dx^{n}}$. Do not use prime notation such as $f'$, $y'$, $x''$, Newton dots such as $\dot{x}$, or Cauchy $f^{(n)}$ notation for derivative transformations.
- Integrals: write $\displaystyle\int f(x)\, dx$, definite integrals $\displaystyle\int_{a}^{b} f(x)\, dx$, and indefinite integrals with the differential explicit. Keep the differential ($dx$, $dt$, $du$, and so on) visible in every integral.
- Prefer explicit dependent and independent variables in Leibniz form so the quantity being differentiated or integrated is clear.
- When a source quote uses prime or dot notation, rewrite the displayed mathematics into Leibniz form while preserving the source’s meaning, and keep the citation.
- Do not rewrite non-derivative primes: primed inertial-frame coordinates such as $(x',t')$, gauge-transformed fields such as $V'$ or $\mathbf{A}'$, duals, and matrix or operator adjoints keep their conventional primes.
