# Eigenvector

A nonzero vector that a linear transformation maps to a scalar multiple of itself that is used to identify special directions of that transformation.

<i>

**definition [d]** (*Eigenvector*) From Axler: a number $\lambda \in F$ is called an eigenvalue of $T$ if there exists $v \in V$ such that $v \neq 0$ and $Tv = \lambda v$. A vector $v \in V$ with $v \neq 0$ is an eigenvector of $T$ corresponding to $\lambda$ if and only if

- $v \in \operatorname{null}(T - \lambda I)$ .

where

- $T$ is an operator on a vector space $V$ over a field $F$.
- $v$ is a nonzero eigenvector.
- $\lambda$ is the corresponding eigenvalue.
- $I$ is the identity operator on $V$.
- $\operatorname{null}(T - \lambda I)$ is the null space of $T - \lambda I$.

</i>

<i>

**definition [d]** (*Eigenvector*) From Cohen: when

- $Av = \lambda v$

is satisfied, then $v$ is an eigenvector and $\lambda$ is its associated eigenvalue.

where

- $A$ is a square matrix.
- $v$ is a nonzero vector.
- $\lambda$ is the associated eigenvalue.

</i>

## Elementary Example

### Simple

On $\mathbb{R}^{2}$, a diagonal matrix stretches the axis vectors by the diagonal entries.

$$
A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}
$$

$$
v = \begin{pmatrix} 1 \\ 0 \end{pmatrix},\quad Av = \begin{pmatrix} 2 \\ 0 \end{pmatrix} = 2 v
$$

where

- $v$ is an eigenvector of $A$.
- $\lambda = 2$ is the corresponding eigenvalue.

### General

In three dimensions, each standard basis vector can be an eigenvector of a diagonal matrix.

$$
A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{pmatrix}
$$

$$
v_{1} = e_{1},\quad A v_{1} = 2 v_{1}
$$

$$
v_{2} = e_{2},\quad A v_{2} = 3 v_{2}
$$

$$
v_{3} = e_{3},\quad A v_{3} = 5 v_{3}
$$

where

- $e_{1}, e_{2}, e_{3}$ are the standard basis vectors of $\mathbb{R}^{3}$.
- each $v_{i}$ is a nonzero eigenvector of $A$.

## References

1. Axler, S. *Linear Algebra Done Right*. — eigenvector $v \neq 0$ for $\lambda$ means $Tv = \lambda v$, equivalently $v \in \operatorname{null}(T - \lambda I)$.
2. Cohen, M. X. *Linear Algebra: Theory, Intuition, Code*. Sincxpress BV, 2021. — eigenvalue equation $Av = \lambda v$.
