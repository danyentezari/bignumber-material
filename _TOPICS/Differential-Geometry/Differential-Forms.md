# Differential Forms

A field of alternating multilinear mappings attached to each point that is used to integrate over curved domains.

<i>

**definition** (*Differential k-Form*) A function assigning an alternating k-linear function to each point of a manifold $M$, where the following condition applies:

- For each point $p \in M$, $\omega(p)$ is a $k$-covector on the tangent space $T_pM$.

where

- $M$ is a smooth manifold.
- $k$ is a non-negative integer representing the degree of the form.
- $T_pM$ is the tangent space to $M$ at $p$.
- $T^*_p M$ is the cotangent space at $p$, defined as the dual space of the tangent space $T_pM$.
- $\Lambda^k(T^*_p M)$ is the vector space of all alternating $k$-tensors on $T_pM$.
- $\omega$ is a smooth section of the vector bundle $\Lambda^k(T^*M)$, the $k$-th exterior power of the cotangent bundle.

Note:

- $T^*_p M$ is also written $T^*_p(M)$.
- $\Lambda^k(T^*_p M)$ is also written $A^k(T_pM)$.
- Alternating $k$-tensors are also called $k$-covectors.
- Alternating $k$-tensors are also called multicovectors.

</i>

## Elementary Example

A differential form assigns an alternating map to each point. Here two points each get a 1-form on three directions.

$$
M = \{ p,\ q \}
$$

$$
T_{p}M = \{ e_{1},\ e_{2},\ e_{3} \}
$$

$$
\omega(p)(e_{1}) = 1,\quad \omega(p)(e_{2}) = 0,\quad \omega(q)(e_{1}) = 2
$$
