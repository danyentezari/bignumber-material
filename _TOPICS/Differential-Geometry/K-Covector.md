# k-Covector

An alternating multilinear mapping on k vectors that is used to span the set of alternating tensors of that degree.

<i>

**definition** (*k-Covector*) An alternating $k$-linear function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where the following conditions apply:

- The function $T$ is linear in each of its $k$ arguments.
- $T(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\text{sgn } \sigma) T(v_1, \dots, v_k)$ for every permutation $\sigma \in S_k$.

where

- $V$ is a vector space.
- $k$ is a positive integer representing the degree of the covector.
- $v_1, \dots, v_k \in V$ are vectors.
- $A^k(V)$ is the vector space of all $k$-covectors on $V$.
- $\text{sgn } \sigma$ is the sign of the permutation $\sigma$.
- $S_k$ is the symmetric group on $k$ letters.
- $\mathbb{R}$ is the set of real numbers.

Note:

- $A^k(V)$ is also written $\Lambda^k(V^*)$.
- A $k$-covector is also called a multicovector of degree $k$.
- A $k$-covector is also called an alternating $k$-tensor.

</i>

## Elementary Example
### Simple

A $2$-covector is an alternating bilinear map on vectors.

$$
\omega : V \times V \rightarrow \mathbb{R}
$$

$$
V = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
\omega(e_{1},e_{2}) = 1,\quad \omega(e_{2},e_{1}) = -1
$$

where

- $\omega$ is a $k$-covector with $k = 2$.
- $V$ is the set of input basis vectors.

### General

On $\mathbb{R}^{3}$, a $2$-covector has skew components $\omega_{ij}$ in a $3 \times 3$ matrix.

$$
(\omega_{ij}) = \begin{pmatrix} 0 & 1 & -1 \\ -1 & 0 & 2 \\ 1 & -2 & 0 \end{pmatrix}
$$

$$
\omega(u,v) = \sum_{i,j} \omega_{ij}\, u^{i}\, v^{j}
$$

where

- $\omega_{ij} = -\omega_{ji}$ are the components of $\omega$.
