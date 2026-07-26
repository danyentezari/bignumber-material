# Determinant

A scalar attached to a linear transformation that is used to measure signed volume scaling of a basis under that transformation.

<i>

**definition [d]** (*Determinant*) From Axler: the determinant of $T$, denoted $\det T$, is defined to be the unique number in $F$ such that

- $\alpha T = (\det T)\, \alpha$

for all $\alpha \in \Lambda^{\dim V}(V^{*})$, written in Axler’s notation as all $\alpha$ in the space of alternating forms of degree $\dim V$.

where

- $T$ is an operator on a finite-dimensional vector space $V$ over a field $F$.
- $\det T$ is the determinant of $T$.
- $\alpha$ is an alternating form of top degree on $V$.

</i>

## Elementary Example

### Simple

For a $2 \times 2$ matrix, the determinant is the familiar product difference of entries.

$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$

$$
\det A = ad - bc
$$

$$
A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix},\quad \det A = 6
$$

where

- $a, b, c, d$ are scalars.
- $\det A$ is the determinant of $A$.

### General

For a $3 \times 3$ diagonal matrix, the determinant is the product of the diagonal entries.

$$
A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{pmatrix}
$$

$$
\det A = 2 \cdot 3 \cdot 5 = 30
$$

where

- $\det A$ equals the product of the eigenvalues when $A$ is diagonal.

## References

1. Axler, S. *Linear Algebra Done Right*. — $\det T$ is the unique scalar with $\alpha T = (\det T)\, \alpha$ for top-degree alternating forms $\alpha$.
