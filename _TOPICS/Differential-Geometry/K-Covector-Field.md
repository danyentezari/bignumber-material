# k-Covector Field

A smooth mapping that assigns a k-covector to each point that is used to define differential forms.

<i>

**definition** (*k-Covector Field*) A function assigning a $k$-covector to each point of a manifold, $\omega: M \rightarrow \Lambda^k(T^*M)$, where the following condition applies:

- For each point $p$ in $M$, $\omega(p)$ is an alternating $k$-linear function on the tangent space $T_pM$.

where

- $M$ is a smooth manifold.
- $p$ is a point in $M$.
- $\omega$ is the $k$-covector field.
- $T_pM$ is the tangent space of $M$ at $p$.
- $T^*_pM$ is the cotangent space of $M$ at $p$.
- $\Lambda^k(T^*_pM)$ is the space of all alternating $k$-tensors on $T_pM$.
- $\Lambda^k(T^*M)$ is the $k$-th exterior power of the cotangent bundle.

Note:

- $\Lambda^k(T^*_pM)$ is also written $A^k(T_pM)$.
- A $k$-covector field is also called a differential $k$-form.

</i>

## Elementary Example
### Simple

A $k$-covector field assigns a $k$-covector to each point. Here $k = 1$ on three points.

$$
M = \{ p,\ q,\ r \}
$$

$$
\omega(p)(e_{1}) = 1,\quad \omega(q)(e_{1}) = 0,\quad \omega(r)(e_{1}) = 2
$$

where

- $\omega$ is the $k$-covector field.
- $M$ is the set of points.
- $\omega(p)$ is the covector at $p$.

### General

For $k = 2$, each point gets an alternating bilinear map, written with skew components.

$$
M = \{ p,\ q \}
$$

$$
\omega(p)(e_{1},e_{2}) = 3,\quad \omega(p)(e_{2},e_{1}) = -3
$$

$$
\omega(q)(e_{1},e_{2}) = -1
$$

where

- $\omega(p)$ is the $2$-covector at $p$.
