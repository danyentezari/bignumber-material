# Functions

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
