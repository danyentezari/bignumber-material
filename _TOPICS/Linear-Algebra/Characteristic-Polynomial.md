# Characteristic Polynomial

A polynomial built from a linear transformation that is used to find eigenvalues as its roots.

<i>

**definition [d]** (*Characteristic Polynomial*) From Axler: the polynomial defined by

- $z \mapsto \det(zI - T)$

is called the characteristic polynomial of $T$.

where

- $T$ is an operator on a finite-dimensional vector space.
- $I$ is the identity operator.
- $z$ is a scalar variable.
- $\det$ is the determinant.

</i>

<i>

**definition [d]** (*Characteristic Polynomial*) From Shifrin and Adams: let $A$ be a square matrix. Then

- $p(t) = p_{A}(t) = \det(A - tI)$

is called the characteristic polynomial of $A$.

where

- $A$ is a square matrix.
- $I$ is the identity matrix of the same size.
- $t$ is a scalar variable.

Note:

- Axler’s convention uses $\det(zI - T)$; Shifrin’s matrix form uses $\det(A - tI)$. The two differ by a sign factor $(-1)^{n}$ in dimension $n$.

</i>

## Elementary Example

### Simple

For a $2 \times 2$ diagonal matrix, Axler’s characteristic polynomial factors as a product of linear terms.

$$
A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}
$$

$$
zI - A = \begin{pmatrix} z-2 & 0 \\ 0 & z-3 \end{pmatrix}
$$

$$
\det(zI - A) = (z-2)(z-3)
$$

where

- the roots $z = 2$ and $z = 3$ are the eigenvalues of $A$.

### General

In three dimensions, a diagonal matrix yields a cubic characteristic polynomial.

$$
A = \operatorname{diag}(2,3,5)
$$

$$
\det(zI - A) = (z-2)(z-3)(z-5)
$$

where

- the three roots are the three eigenvalues of $A$.

## References

1. Axler, S. *Linear Algebra Done Right*. — characteristic polynomial $z \mapsto \det(zI - T)$.
2. Shifrin, T., & Adams, M. *Linear Algebra: A Geometric Approach*. W. H. Freeman, 2010. — $p_{A}(t) = \det(A - tI)$.
