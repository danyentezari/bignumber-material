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
### Simple

A differential $1$-form assigns a linear functional to each point. Let $\omega$ be such an assignment on two points.

$$
M = \{ p,\ q \}
$$

$$
\omega(p)(e_{1}) = 1,\quad \omega(p)(e_{2}) = 0,\quad \omega(q)(e_{1}) = 2
$$

where

- $M$ is the base set of points.
- $\omega(p)$ is the $1$-form at the point $p$.
- $e_{1}, e_{2}$ are tangent directions at that point.

### General

A differential $2$-form assigns an alternating bilinear map to each point. On three points of a base, values may differ.

$$
M = \{ p,\ q,\ r \}
$$

$$
\omega(p)(e_{1},e_{2}) = 1,\quad \omega(p)(e_{2},e_{1}) = -1
$$

$$
\omega(q)(e_{1},e_{2}) = 0,\quad \omega(r)(e_{1},e_{2}) = 3
$$

where

- $\omega(p)$ is the alternating $2$-linear map at $p$.
- $e_{1}, e_{2}$ are tangent vectors at that point.
