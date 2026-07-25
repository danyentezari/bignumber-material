# Lorentzian Manifold

A smooth domain with a metric of one negative and three positive signature directions that is used to model curved spacetime.

<i>

**definition [d]** (*Lorentzian Manifold = Lorentz Manifold*) A smooth manifold $M$ equipped with a smooth, symmetric, nondegenerate metric tensor field $g$ of Lorentzian signature:

- $(M, g)$ with signature $(-+++)$ .

where

- $M$ is a smooth manifold.
- $g$ is the metric tensor field.
- $g_{p}$ is the value of $g$ at the point $p$, a symmetric nondegenerate bilinear form on $T_{p}M$.
- $T_{p}M$ is the tangent space at $p$.

Note:

- the opposite Lorentzian signature is $(+---)$.
- exactly one eigenvalue of $g$ has opposite sign to the others.
- unlike a Riemannian metric, $g$ is not positive-definite.
- the flat prototype is Minkowski spacetime with metric $\eta_{\mu\nu}$.

</i>

<i>

**definition [d]** (*Lorentzian Manifold = Lorentz Manifold*) A pseudo-Riemannian manifold $(M, g)$ whose metric has Lorentzian signature $(-+++)$:

- $g$ is smooth, symmetric, and nondegenerate on each $T_{p}M$ .

where

- $M$ is a smooth manifold.
- $g$ is the Lorentzian metric tensor field.
- $T_{p}M$ is the tangent space at $p$.

Note:

- the opposite Lorentzian signature is $(+---)$.

</i>


## Elementary Example
### Simple

A Lorentzian metric has one negative direction. Let $\eta$ be the $1+1$ Minkowski metric.

$$
\eta = \operatorname{diag}(-1,1)
$$

$$
\eta(e_{0},e_{0}) = -1,\quad \eta(e_{1},e_{1}) = 1
$$

where

- $\eta$ is the Minkowski metric tensor.
- $e_{0}, e_{1}$ are basis vectors in the two signature directions.

### General

In $1+3$ dimensions the flat Lorentzian metric is the $4 \times 4$ diagonal matrix of signature $(-+++)$.

$$
\eta = \operatorname{diag}(-1,1,1,1)
$$

$$
\{ e_{0},\ e_{1},\ e_{2},\ e_{3} \}
$$

$$
\eta(e_{0},e_{0}) = -1,\quad \eta(e_{i},e_{i}) = 1\ \text{for } i = 1,2,3
$$

where

- $(M,\eta)$ with this $\eta$ is flat Minkowski spacetime.
- signature $(-+++)$ means one negative and three positive diagonal entries.

## References

1. Carroll, S. *Spacetime and Geometry: An Introduction to General Relativity*. Cambridge University Press, 2021. — Lorentzian manifold and metric signature.
2. Nakahara, M. *Geometry, Topology and Physics*. IOP, 2003. — Lorentz manifold.
