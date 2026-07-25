# Smooth

A property of a function under which derivatives of all degrees exist and are continuous that is used to do calculus with well-behaved functions.

<i>

**definition [d]** (*Smooth = Infinitely Differentiable = $C^{\infty}$ = Class $C^{\infty}$*) A property of a real-valued function: all partial derivatives of all orders exist.

- $f$ is $C^{\infty}$ on an open set $U \subseteq \mathbb{R}^{n}$ .

where

- $f$ is a real-valued function.
- $U$ is an open subset of $\mathbb{R}^{n}$.
- $\mathbb{R}^{n}$ is $n$-dimensional Euclidean space.
- $C^{\infty}$ means infinitely differentiable.

Note:

- the same notion applies to Euclidean maps.
- $C^{k}$ means continuous derivatives up to order $k$; $C^{\infty}$ is the intersection of all $C^{k}$.
- smooth and infinitely differentiable are synonymous.

</i>

<i>

**definition [d]** (*Smooth = Infinitely Differentiable = $C^{\infty}$*) A property in differential geometry of manifolds, maps, and functions:

- (Manifold) transition maps $f_{VU}$ are of class $C^{\infty}$ .
- (Map $f: M \rightarrow N$) for charts $(U,\phi)$ on $M$ and $(V,\mu)$ on $N$, the composite $\mu \circ f \circ \phi^{-1}$ is $C^{\infty}$ wherever defined .
- (Function on $M$) $f \circ \phi^{-1}$ is $C^{\infty}$ in local coordinates .

where

- $M, N$ are smooth manifolds.
- $f_{VU}$ is the transition map between overlapping charts.
- $(U,\phi)$ and $(V,\mu)$ are coordinate charts.
- $\phi^{-1}$ and $\mu$ convert between manifold points and Euclidean coordinates.
- $C^{\infty}$ means infinitely differentiable.

Note:

- a tensor field is smooth when its component functions are $C^{\infty}$ in every chart.

</i>


## Elementary Example
### Simple

Smoothness means derivatives exist at sample points. Here a quadratic polynomial is smooth on a finite sample of the line.

$$
A = \{ -1,\ 0,\ 1 \}
$$

$$
f(x) = x^{2},\quad f(-1) = 1,\quad f(0) = 0,\quad f(1) = 1
$$

$$
f'(0) = 0
$$

where

- $f$ is the smooth function.
- $f'$ is its derivative.

### General

All higher derivatives of $f(x) = x^{2}$ exist. On a larger sample the same rule holds.

$$
A = \{ -2,\ -1,\ 0,\ 1,\ 2 \}
$$

$$
f(x) = x^{2},\quad f''(x) = 2,\quad f^{(n)}(x) = 0\ \text{for } n \ge 3
$$

where

- $f''(x)$ is the second derivative.
- $f^{(n)}$ is the $n$-th derivative.

## References

1. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — $C^{\infty}$ manifolds; smooth transition maps; differentiable functions on $M$.
2. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — smooth maps $f:M\to N$ via $\mu\circ f\circ\phi^{-1}$.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — smooth and differentiable fields in applied settings.
