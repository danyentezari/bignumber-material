# Multilinear Function

A mapping of several vectors that is linear in each vector variable separately that is used to define tensors.

<i>

**definition** (*Multilinear Function*) A function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where the following conditions apply for each argument $i$ ($1 \leq i \leq k$):

- $T(v_1, \dots, v_i + v_i', \dots, v_k) = T(v_1, \dots, v_i, \dots, v_k) + T(v_1, \dots, v_i', \dots, v_k)$
- $T(v_1, \dots, av_i, \dots, v_k) = a \cdot T(v_1, \dots, v_i, \dots, v_k)$

where

- $V$ is a vector space over $\mathbb{R}$.
- $V^k$ is the $k$-fold Cartesian product $V \times \dots \times V$.
- $k$ is a positive integer representing the number of arguments, also called the degree of the function.
- $v_1, \dots, v_k, v_i' \in V$ are vectors.
- $a \in \mathbb{R}$ is a scalar.

</i>

## Elementary Example

A multilinear map is linear in each slot. Here a bilinear map on three labeled vectors.

$$
T : V \times V \rightarrow \mathbb{R}
$$

$$
V = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
T(e_{1},e_{2}) = 5,\quad T(e_{2},e_{1}) = 3,\quad T(e_{1},e_{1}) = 2
$$
