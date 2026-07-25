# Alternating Function

A property of a function under which swapping two inputs multiplies the value by minus one that is used to build determinants of matrices.

<i>

**definition** (*Alternating Function*) A property of a $k$-linear function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where the following conditions apply:

- $T(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\text{sgn } \sigma) T(v_1, \dots, v_k)$ for every permutation $\sigma \in S_k$.
- $T(v_1, \dots, v_i, \dots, v_j, \dots, v_k) = -T(v_1, \dots, v_j, \dots, v_i, \dots, v_k)$ for any interchange of two arguments.
- $T(v_1, \dots, v_k) = 0$ whenever two of the vectors $v_1, \dots, v_k$ are equal.

where

- $V$ is a vector space.
- $V^k$ is the $k$-fold Cartesian product $V \times \dots \times V$.
- $S_k$ is the permutation group of $k$ objects.
- $\text{sgn } \sigma$ is the sign of the permutation $\sigma$, which is $+1$ if the permutation is even and $-1$ if it is odd.
- $v_1, \dots, v_k$ are vectors in $V$.
- $k$ is a positive integer representing the degree of the function.

</i>

## Elementary Example

An alternating map on pairs of vectors changes sign when the two inputs swap, and gives zero when the two inputs are equal.

$$
T : V \times V \rightarrow \mathbb{R}
$$

$$
V = \{ e_{1},\ e_{2} \}
$$

$$
T(e_{1},e_{2}) = 1,\quad T(e_{2},e_{1}) = -1,\quad T(e_{1},e_{1}) = 0,\quad T(e_{2},e_{2}) = 0
$$

## References

1. Lovett, S. *Differential Geometry of Manifolds*. — alternating: sign change under swap; zero when two arguments are equal.
