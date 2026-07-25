# Linear Map

A mapping between vector spaces that preserves addition of vectors and multiplication by scalars that is used to transform vectors from one space to another.

<i>

**definition** (*Linear Map*)
A map between vector spaces, $F:  \mathbf{V} \rightarrow \mathbf{W}$, is a linear map if the following conditions hold.

- **additivity** $F(\mathbf{u}+\mathbf{v}) = F(\mathbf{u}) + F(\mathbf{v})$ &nbsp; for all  $\mathbf{u},\mathbf{v} \in \mathbf{V}$
- **homogeneity** $F(c\mathbf{v}) = cF(\mathbf{v})$ &nbsp; for all $c \in \mathbb{R}, \mathbf{v} \in \mathbf{V}$

where

- $\mathbf{V}, \mathbf{W} \in \mathbb{R}^{n}$ are vector spaces.

</i>

## Examples

<i>

**example [d]** (**Linear Map $\mathbb{R}^{3}\rightarrow\mathbb{R}^{2}$** — Dummit and Foote) The map $\phi : \mathbb{R}^{3} \rightarrow \mathbb{R}^{2}$ defined by

- $\phi(x, y, z) = (x + 2y,\, x + y + z)$

is linear. With respect to the standard bases its matrix is

- $A =
\begin{bmatrix}
1 & 2 & 0 \\
1 & 1 & 1
\end{bmatrix}$ .

where

- $\phi$ is the linear map.
- $(x, y, z)$ are coordinates on the domain $\mathbb{R}^{3}$.
- $A$ is the matrix of $\phi$ relative to the standard bases.

Note:

- $\phi$ sends a vector in $\mathbb{R}^{3}$ to a vector in $\mathbb{R}^{2}$.
- matrix multiplication by $A$ implements $\phi$ on column vectors.

</i>

## References

1. Dummit, D. S., & Foote, R. M. *Abstract Algebra*. Wiley, 2004. — linear map $\phi:\mathbb{R}^{3}\rightarrow\mathbb{R}^{2}$, $\phi(x,y,z)=(x+2y,\,x+y+z)$.
