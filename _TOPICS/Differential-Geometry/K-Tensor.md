# k-Tensor

A multilinear function of k vectors that is used to represent quantities independent of a change of basis.

<i>

**definition** (*k-Tensor*) A multilinear function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where the following condition applies:

- The function $T$ is linear in each of its $k$ arguments.

where

- $V$ is a vector space.
- $V^k$ is the $k$-fold Cartesian product $V \times \dots \times V$.
- $k$ is a positive integer representing the degree of the tensor.
- $\mathbb{R}$ is the set of real numbers.
- $\mathcal{L}^k(V)$ is the vector space of all $k$-tensors on $V$.

Note:

- $\mathcal{L}^k(V)$ is also written $\mathcal{J}^k(V)$.

</i>

## Elementary Example

A k-tensor is a multilinear real-valued map on k vectors. Here k equals 2.

$$
T : V \times V \rightarrow \mathbb{R}
$$

$$
V = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
T(e_{1},e_{2}) = 4,\quad T(e_{2},e_{1}) = 1,\quad T(e_{1},e_{1}) = 0
$$
