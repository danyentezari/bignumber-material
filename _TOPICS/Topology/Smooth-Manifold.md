# Smooth Manifold

A set of points that can be covered by mappings to open sets of real numbers of fixed dimension that is used to do calculus on curved domains.

<i>

**definition [d]** (*Smooth Manifold = Differentiable Manifold = $C^{\infty}$ Manifold*) An $n$-dimensional Hausdorff, second-countable topological space covered by charts $\{U, \phi_{U}\}$ whose overlap transition maps are $C^{\infty}$:

- $M^{n}$ with atlas whose $f_{VU}$ are infinitely differentiable .

where

- $M^{n}$ is the manifold of dimension $n$.
- $\{U, \phi_{U}\}$ is a collection of coordinate charts.
- $U$ is an open set in $M$.
- $\phi_{U}$ is the coordinate map on $U$.
- $f_{VU}$ is the transition map between overlapping charts.
- $C^{\infty}$ means infinitely differentiable.

Note:

- locally each point has a neighborhood looking like an open set in $\mathbb{R}^{n}$.
- equivalently, points are connected smoothly so each neighborhood looks like $m$-dimensional Cartesian space.

</i>

<i>

**definition [d]** (*Smooth Manifold = Differentiable Manifold = $C^{\infty}$ Manifold*) A topological manifold $M$ with an atlas $\{(U_{\alpha}, \phi_{\alpha})\}$ such that every transition map

- $\phi_{\beta} \circ \phi_{\alpha}^{-1} : \phi_{\alpha}(U_{\alpha} \cap U_{\beta}) \rightarrow \phi_{\beta}(U_{\alpha} \cap U_{\beta})$

is of class $C^{\infty}$.

where

- $M$ is the manifold.
- $(U_{\alpha}, \phi_{\alpha})$ is a coordinate chart.
- $\phi_{\alpha}: U_{\alpha} \rightarrow \mathbb{R}^{n}$ maps an open set of $M$ into Euclidean space.
- $\phi_{\beta} \circ \phi_{\alpha}^{-1}$ is the transition map on the overlap.
- $C^{\infty}$ means infinitely differentiable.
- $\mathbb{R}^{n}$ is $n$-dimensional Euclidean space.

Note:

- $C^{\infty}$ transitions make derivatives of functions and tensors chart-independent.

</i>

## Elementary Example
### Simple

A smooth manifold has charts with $C^{\infty}$ transition maps. The line $\mathbb{R}$ with the identity chart is smooth.

$$
M = \mathbb{R},\quad n = 1
$$

$$
\phi : M \rightarrow \mathbb{R},\quad \phi(x) = x
$$

where

- $\phi$ is a coordinate chart.
- the identity transition is $C^{\infty}$.

### General

On $\mathbb{R}^{2}$, two overlapping charts with smooth overlap give a smooth atlas.

$$
M = \mathbb{R}^{2}
$$

$$
\phi(x,y) = (x,y),\quad \psi(x,y) = (x+1,y)
$$

$$
\psi \circ \phi^{-1}(u,v) = (u+1,v)
$$

where

- $\phi, \psi$ are charts.
- $\psi \circ \phi^{-1}$ is a $C^{\infty}$ transition map.


## References

1. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — $C^{\infty}$ manifold; Hausdorff, second-countable; smooth transition maps $f_{VU}$.
2. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — differentiable manifold; local Euclidean neighborhoods.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — manifolds and curvilinear coordinate patches in applications.
