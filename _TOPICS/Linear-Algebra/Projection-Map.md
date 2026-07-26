# Projection Map

A linear transformation that maps every vector into a fixed subspace and leaves vectors in that subspace unchanged that is used to extract the component along a chosen subspace.

Note: Also called projection. Also called projection operator. Also called orthogonal projection when the leftover part is perpendicular to the subspace.

<i>

**definition [d]** (*Orthogonal Projection*) From Axler: suppose $U$ is a finite-dimensional subspace of $V$. The orthogonal projection of $V$ onto $U$ is the operator $P_{U} \in \mathcal{L}(V)$ defined as follows. For each $v \in V$, write $v = u + w$, where $u \in U$ and $w \in U^{\perp}$. Then let

- $P_{U} v = u$ .

where

- $V$ is an inner product space.
- $U$ is a finite-dimensional subspace of $V$.
- $U^{\perp}$ is the orthogonal complement of $U$.
- $P_{U}$ is the orthogonal projection onto $U$.

</i>

<i>

**definition [d]** (*Projection*) From Hubbard and Hubbard: a square $n \times n$ matrix $P$ such that

- $P^{2} = P$

is called a projection.

where

- $P$ is an $n \times n$ matrix.
- $P^{2}$ means the matrix product $PP$.

</i>

<i>

**definition [d]** (*Projection Operator*) From Griffel: let $S$ be a subspace of the Hilbert space $H$. The operator $P: H \rightarrow S$ defined by $Px = y$, where $y$ is the projection of $x$ onto $S$, is called the projection operator onto $S$. Here each $x \in H$ has a unique splitting $x = y + z$ with $y \in S$ and $z$ orthogonal to $S$.

where

- $H$ is a Hilbert space.
- $S$ is a subspace of $H$.
- $y$ is the projection of $x$ onto $S$.
- $P$ is the projection operator onto $S$.

</i>

## Elementary Example

### Simple

Projection onto the $x$-axis in the plane maps $(x,y)$ to $(x,0)$ and satisfies $P^{2}=P$.

$$
P\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x \\ 0 \end{pmatrix}
$$

$$
P = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix},\quad P^{2} = P
$$

where

- $P$ is the projection map onto the $x$-axis.
- $x$ and $y$ are real coordinates.

### General

Orthogonal projection onto the $xy$-plane in three dimensions keeps the first two coordinates and drops the third.

$$
P_{U}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} x \\ y \\ 0 \end{pmatrix}
$$

$$
U = \left\{ \begin{pmatrix} a \\ b \\ 0 \end{pmatrix} : a,b \in \mathbb{R} \right\}
$$

$$
v = u + w,\quad P_{U} v = u
$$

where

- $U$ is the $xy$-plane subspace.
- $u$ is the part of $v$ in $U$.
- $w$ is the leftover part orthogonal to $U$.

## References

1. Axler, S. *Linear Algebra Done Right*, 4th ed. Springer, 2024. — Def. 6.55: orthogonal projection $P_{U}$ with $v = u + w$, $u \in U$, $w \in U^{\perp}$, and $P_{U}v = u$.
2. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. Matrix Editions, 2015. — Ex. 2.18: a square matrix $P$ with $P^{2} = P$ is a projection.
3. Griffel, D. H. *Applied Functional Analysis*. Ellis Horwood, 1981/1985. — Def. 9.34: projection operator $P: H \rightarrow S$ with $Px = y$ the projection of $x$ onto $S$.
