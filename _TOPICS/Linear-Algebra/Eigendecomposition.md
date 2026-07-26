# Eigendecomposition

A factorization of a matrix into eigenvectors and eigenvalues that is used to rewrite the matrix as diagonal in an eigenbasis.

Note: Also called diagonalization.

<i>

**definition [d]** (*Eigendecomposition = Diagonalization*) From Cohen: eigendecomposition writes

- $A = V \Lambda V^{-1}$ ,

so that matrix $A$ is diagonal in basis $V$. That is why eigendecomposition is also sometimes called diagonalization.

where

- $A$ is a square matrix that admits an eigenbasis.
- $V$ is a matrix whose columns are eigenvectors of $A$.
- $\Lambda$ is the diagonal matrix of corresponding eigenvalues.
- $V^{-1}$ is the inverse of $V$.

</i>

<i>

**definition [d]** (*Diagonalizable*) From Axler: an operator on $V$ is called diagonalizable if the operator has a diagonal matrix with respect to some basis of $V$.

where

- $V$ is a finite-dimensional vector space.
- the basis that diagonalizes the operator is an eigenbasis when the diagonal entries are the eigenvalues.

</i>

## Elementary Example

### Simple

A diagonal matrix is already an eigendecomposition with $V = I$.

$$
A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}
$$

$$
V = I,\quad \Lambda = A,\quad A = V \Lambda V^{-1}
$$

where

- $V$ is the identity matrix.
- $\Lambda$ holds the eigenvalues $2$ and $3$.

### General

In three dimensions, a diagonalizable matrix factors as $V \Lambda V^{-1}$ with three independent eigenvectors.

$$
A = \operatorname{diag}(2,3,5)
$$

$$
V = I_{3},\quad \Lambda = \operatorname{diag}(2,3,5)
$$

$$
A = V \Lambda V^{-1}
$$

where

- $I_{3}$ is the $3 \times 3$ identity.
- the columns of $V$ are eigenvectors of $A$.

## References

1. Cohen, M. X. *Linear Algebra: Theory, Intuition, Code*. Sincxpress BV, 2021. — $A = V\Lambda V^{-1}$; eigendecomposition as diagonalization.
2. Axler, S. *Linear Algebra Done Right*. — diagonalizable means a diagonal matrix in some basis.
