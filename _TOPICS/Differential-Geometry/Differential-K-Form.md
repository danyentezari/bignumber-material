# Differential k-Form

A smooth mapping that assigns an alternating k-linear mapping to each point that is used to integrate over k-dimensional domains.

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
### Simple

A differential $1$-form assigns a linear functional to each point of a finite base.

$$
M = \{ p,\ q,\ r \}
$$

$$
\omega(p)(e_{1}) = 1,\quad \omega(q)(e_{1}) = 0,\quad \omega(r)(e_{1}) = -2
$$

where

- $\omega$ is a differential $1$-form.
- $M$ is the set of sample points.
- $e_{1}$ is a tangent direction at each point.

### General

A differential $2$-form assigns an alternating bilinear map to each point. Sign reverses when the two tangent inputs swap.

$$
M = \{ p,\ q \}
$$

$$
\omega(p)(e_{1},e_{2}) = 1,\quad \omega(p)(e_{2},e_{1}) = -1
$$

$$
\omega(q)(e_{1},e_{2}) = 4
$$

where

- $k = 2$ is the degree of the form.
- $\omega(p)$ is the $2$-covector at $p$.
