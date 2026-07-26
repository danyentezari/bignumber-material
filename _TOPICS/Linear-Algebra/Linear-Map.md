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

**example 1 [d]** (**Linear Map $\mathbb{R}^{3}\rightarrow\mathbb{R}^{2}$** — Dummit and Foote) The map $\phi : \mathbb{R}^{3} \rightarrow \mathbb{R}^{2}$ defined by

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

- $\phi$ maps a vector in $\mathbb{R}^{3}$ to a vector in $\mathbb{R}^{2}$.
- matrix multiplication by $A$ implements $\phi$ on column vectors.

</i>

## Elementary Example
### Simple

A linear map preserves linear combinations. Here a map $\mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$.

$$
T(x_{1},x_{2}) = (x_{1}+x_{2},\ 2 x_{2})
$$

$$
T(e_{1}) = (1,0),\quad T(e_{2}) = (1,2)
$$

where

- $T$ is the linear map.
- $e_{1}, e_{2}$ are the standard basis vectors of $\mathbb{R}^{2}$.

### General

A linear map $\mathbb{R}^{3} \rightarrow \mathbb{R}^{2}$ is given by a $2 \times 3$ matrix.

$$
T(\mathbf{x}) = A \mathbf{x},\quad
A = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \end{pmatrix}
$$

$$
T(1,0,0) = (1,0),\quad T(0,1,0) = (0,1),\quad T(0,0,1) = (2,-1)
$$

where

- $A$ is the matrix of $T$ in the standard bases.


## References

1. Dummit, D. S., & Foote, R. M. *Abstract Algebra*. Wiley, 2004. — linear map $\phi:\mathbb{R}^{3}\rightarrow\mathbb{R}^{2}$, $\phi(x,y,z)=(x+2y,\,x+y+z)$.
