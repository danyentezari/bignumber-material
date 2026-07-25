# Smooth Mapping

A smooth mapping is a mapping of a vector to another vector where every derivative of the mapping satisfies continuity that is used to calculate a change in a variable value that satisfies continuity.

Note: Also called smooth map. Also called $C^{\infty}$ map.

<i>

**definition [d]** (*Smooth Mapping = Smooth Map*) From Kosinski: let $f: M \rightarrow N$ where $M$, $N$ are differential manifolds. The mapping $f$ is smooth if there are atlases $\{U_{\alpha}, h_{\alpha}\}$ on $M$ and $\{V_{\beta}, g_{\beta}\}$ on $N$ such that the maps

- $g_{\beta} \circ f \circ h_{\alpha}^{-1}$

are smooth wherever they are defined. The mapping $f$ is a diffeomorphism if it is smooth and has a smooth inverse.

where

- $M$, $N$ are differential manifolds.
- $f$ is the mapping being tested for smoothness.
- $\{U_{\alpha}, h_{\alpha}\}$ is an atlas on $M$.
- $\{V_{\beta}, g_{\beta}\}$ is an atlas on $N$.

</i>

<i>

**definition [d]** (*Smooth Mapping = $C^{\infty}$ Map*) From Tu: let $N$ and $M$ be manifolds of dimension $n$ and $m$ respectively. A continuous map $F: N \rightarrow M$ is $C^{\infty}$ at a point $p$ in $N$ if there are charts $(V,\psi)$ about $F(p)$ in $M$ and $(U,\phi)$ about $p$ in $N$ such that the composition

- $\psi \circ F \circ \phi^{-1}$

a map from the open subset $\phi\bigl(F^{-1}(V) \cap U\bigr)$ of $\mathbb{R}^{n}$ to $\mathbb{R}^{m}$, is $C^{\infty}$ at $\phi(p)$. The continuous map $F: N \rightarrow M$ is said to be $C^{\infty}$ if it is $C^{\infty}$ at every point of $N$.

where

- $F$ is the continuous map.
- $(U,\phi)$ is a chart about $p$ in $N$.
- $(V,\psi)$ is a chart about $F(p)$ in $M$.
- $\psi \circ F \circ \phi^{-1}$ is the local Euclidean representative.
- $C^{\infty}$ means infinitely differentiable.

</i>


## Elementary Example

A smooth mapping sends each domain point to a unique image point. Here a finite sample of the rule.

$$
f : A \rightarrow B
$$

$$
A = \{ 0,\ 1,\ 2,\ 3 \}
$$

$$
B = \{ 0,\ 1,\ 4,\ 9 \}
$$

$$
f(0) = 0,\quad f(1) = 1,\quad f(2) = 4,\quad f(3) = 9
$$

## References

1. Kosinski, A. A. *Differential Manifolds*. — Definition (1.6): smooth maps via $g_{\beta} \circ f \circ h_{\alpha}^{-1}$; diffeomorphism.
2. Tu, L. W. *An Introduction to Manifolds*. — Definition 6.5: $C^{\infty}$ at a point via $\psi \circ F \circ \phi^{-1}$.
