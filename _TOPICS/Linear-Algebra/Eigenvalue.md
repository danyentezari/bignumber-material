# Eigenvalue

A scalar for which a nonzero vector is scaled by a linear transformation that is used to measure stretch along that special direction.

<i>

**definition [d]** (*Eigenvalue*) From Axler: a number $\lambda \in F$ is called an eigenvalue of $T$ if there exists $v \in V$ such that $v \neq 0$ and

- $Tv = \lambda v$ .

where

- $T$ is an operator on a vector space $V$ over a field $F$.
- $v$ is a nonzero vector in $V$.
- $\lambda$ is the eigenvalue of $T$.

</i>

<i>

**definition [d]** (*Eigenvalue*) From Cohen: when the eigenvalue equation

- $Av = \lambda v$

is satisfied, then $v$ is an eigenvector and $\lambda$ is its associated eigenvalue.

where

- $A$ is a square matrix.
- $v$ is a nonzero vector.
- $\lambda$ is the associated eigenvalue.

</i>

## Elementary Example

### Simple

A diagonal $2 \times 2$ matrix has eigenvalues equal to its diagonal entries.

$$
A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}
$$

$$
v = \begin{pmatrix} 1 \\ 0 \end{pmatrix},\quad Av = 2v
$$

$$
\lambda = 2
$$

where

- $\lambda = 2$ is an eigenvalue of $A$.
- $v$ is a corresponding eigenvector.

### General

In three dimensions, a diagonal matrix has three eigenvalues on the diagonal.

$$
A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{pmatrix}
$$

$$
\lambda_{1} = 2,\quad \lambda_{2} = 3,\quad \lambda_{3} = 5
$$

$$
A e_{i} = \lambda_{i} e_{i}
$$

where

- $\lambda_{1}, \lambda_{2}, \lambda_{3}$ are the eigenvalues of $A$.
- $e_{1}, e_{2}, e_{3}$ are the standard basis eigenvectors.

## References

1. Axler, S. *Linear Algebra Done Right*. — $\lambda \in F$ is an eigenvalue of $T$ if $Tv = \lambda v$ for some $v \neq 0$.
2. Cohen, M. X. *Linear Algebra: Theory, Intuition, Code*. Sincxpress BV, 2021. — eigenvalue equation $Av = \lambda v$.
