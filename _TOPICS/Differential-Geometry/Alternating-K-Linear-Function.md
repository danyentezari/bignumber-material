# Alternating k-linear function

A multilinear mapping of several vectors that changes sign when two inputs are swapped that is used to form determinants and alternating tensors.

<i>

**definition** (*Alternating k-linear function*) A multilinear function from the $k$-fold product of a vector space to the real numbers, $f: V^k \rightarrow \mathbb{R}$, where the following conditions apply:

- $f(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\text{sgn } \sigma) f(v_1, \dots, v_k)$ for all $\sigma \in S_k$.
- $f(v_1, \dots, v_i, \dots, v_j, \dots, v_k) = -f(v_1, \dots, v_j, \dots, v_i, \dots, v_k)$ for any interchange of two arguments.
- $f(v_1, \dots, v_k) = 0$ whenever two of the vectors $v_1, \dots, v_k$ are equal.

where

- $V$ is a vector space.
- $V^k$ is the $k$-fold Cartesian product $V \times \dots \times V$.
- $k$ is a positive integer representing the degree of the function.
- $S_k$ is the permutation group of $k$ objects.
- $\text{sgn } \sigma$ is the sign of the permutation $\sigma$.
- $v_1, \dots, v_k \in V$ are vectors.
- $A^k(V)$ is the vector space of all alternating $k$-linear functions on $V$.

Note:

- $A^k(V)$ is also written $\Lambda^k(V^*)$.
- k-covector, multicovector of degree k, and alternating k-tensor are synonyms for an alternating $k$-linear function.

</i>

## Elementary Example
### Simple

An alternating $2$-linear map on three labeled vectors changes sign under a swap and vanishes on a repeated pair.

$$
f : V \times V \rightarrow \mathbb{R}
$$

$$
V = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
f(e_{1},e_{2}) = 1,\quad f(e_{2},e_{1}) = -1,\quad f(e_{1},e_{1}) = 0
$$

where

- $f$ is an alternating $2$-linear function.
- $k = 2$ is the number of vector inputs.
- $V$ is the set of input basis vectors.

### General

For $k = 3$, an alternating $3$-linear map on $\mathbb{R}^{3}$ is the determinant of the matrix with those three vectors as columns.

$$
f : \mathbb{R}^{3} \times \mathbb{R}^{3} \times \mathbb{R}^{3} \rightarrow \mathbb{R}
$$

$$
f(u,v,w) = \det\begin{pmatrix} u^{1} & v^{1} & w^{1} \\ u^{2} & v^{2} & w^{2} \\ u^{3} & v^{3} & w^{3} \end{pmatrix}
$$

$$
f(e_{1},e_{2},e_{3}) = 1,\quad f(e_{2},e_{1},e_{3}) = -1
$$

where

- $f$ is an alternating $3$-linear function.
- $e_{1}, e_{2}, e_{3}$ are the standard basis vectors of $\mathbb{R}^{3}$.
