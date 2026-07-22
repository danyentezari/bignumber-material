# Diag

<i>

**definition [d]** (*$\operatorname{diag}$ = Diagonal Matrix Constructor*) For scalars $a_{1},\ldots,a_{n}$, the symbol $\operatorname{diag}(a_{1},\ldots,a_{n})$ denotes the $n\times n$ matrix with those entries on the main diagonal and zeros elsewhere:

- $\operatorname{diag}(a_{1},\ldots,a_{n}) =
\begin{pmatrix}
a_{1} & 0 & \cdots & 0 \\
0 & a_{2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & a_{n}
\end{pmatrix}$ .

where

- $a_{1},\ldots,a_{n}$ are scalars.
- $n$ is the matrix size.
- $\operatorname{diag}(a_{1},\ldots,a_{n})$ is the corresponding diagonal matrix.

Note:

- example: $\eta_{\mu\nu} = \operatorname{diag}(-1,\, 1,\, 1,\, 1)$.
- example: $(g_{ij}) = \operatorname{diag}(1,\, r^{2},\, r^{2}\sin^{2}\theta)$ in spherical coordinates.

</i>

<i>

**definition [d]** (*Diagonal Array*) An array $A_{ij}$ is diagonal when every off-diagonal entry vanishes:

- $A_{ij} = 0$ whenever $i \neq j$ .

where

- $A_{ij}$ are the components of the array.
- $i, j$ are discrete indices.

Note:

- the nonzero entries then lie only on the main diagonal $A_{ii}$.
- a metric with $g_{ij} = 0$ for $i \neq j$ is called a diagonal metric in those coordinates.

</i>

## References

1. Carroll, S. *Spacetime and Geometry: An Introduction to General Relativity*. Cambridge University Press, 2021. — $\eta_{\mu\nu}=\operatorname{diag}(-1,1,1,1)$.
2. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — diagonal metric components in orthogonal coordinates.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — diagonal matrices.
