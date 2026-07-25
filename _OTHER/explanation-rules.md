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

For every relevant definition file, add an Elementary Example section with 1–3 finite sets of 3–7 elements that show what kind of set, function, or transformation the concept is. Prefer grounding in Gemini Notebook. Explanation prose must not exceed 40 words.

Template:

```
## Elementary Example

<at most 40 words naming the sets and the map, tied to the grounded definition>

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
f(1) = 1,\quad f(2) = 4,\quad f(3) = 9
$$
```

Approved pattern from Bundle.md: a finite trivial product illustrating Frankel’s local product structure.

```
## Elementary Example

Frankel’s local product $\pi^{-1}(U) \cong U \times F$ is here a global product of finite sets. Projection sends each pair to its base point. The fiber over a point is the copy of $F$ at that point.

$$
\pi : E \rightarrow M
$$

$$
M = \{ 1, 2, 3 \}
$$

$$
F = \{ a, b \}
$$

$$
E = M \times F = \{ (1,a),\ (1,b),\ (2,a),\ (2,b),\ (3,a),\ (3,b) \}
$$

$$
\pi(p,v) = p
$$

$$
\pi^{-1}(2) = \{ (2,a),\ (2,b) \}
$$
```
