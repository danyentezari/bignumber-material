# Metric Tensor

<i>

**definition [d]** (*Metric Tensor = Metric = First Fundamental Form*) A smooth type-$(0,2)$ tensor field $g$ that assigns to each point $p$ a symmetric, nondegenerate bilinear form on the tangent space:

- $g_{p} : T_{p}M \times T_{p}M \rightarrow \mathbb{R}$ ,
- $g(u,v) = g_{\mu\nu}\, u^{\mu}\, v^{\nu}$ .

where

- $M$ is a smooth manifold.
- $g_{\mu\nu} = g_{\nu\mu}$ (symmetry).
- nondegenerate: $g(u,v) = 0$ for all $v$ implies $u = 0$.
- Riemannian if $g$ is positive-definite; Lorentzian / pseudo-Riemannian if indefinite.

</i>

<i>

**definition [d]** (*Metric Tensor = Metric = First Fundamental Form*) The symmetric array of components $g_{\mu\nu}$ that defines infinitesimal length (or spacetime interval) via the line element

- $ds^{2} = g_{\mu\nu}\, dx^{\mu}\, dx^{\nu}$ ,

and raises / lowers indices:

- $V_{\mu} = g_{\mu\nu}\, V^{\nu}$ ,
- $V^{\mu} = g^{\mu\nu}\, V_{\nu}$ .

where

- $g^{\mu\nu}$ is the inverse metric ($g^{\mu\lambda} g_{\lambda\nu} = \delta^{\mu}_{\ \nu}$).
- in flat Minkowski spacetime, $g_{\mu\nu} = \eta_{\mu\nu}$.
- the components encode the geometry (and, in GR, the gravitational field).

</i>

## References

1. Carroll, S. *Spacetime and Geometry: An Introduction to General Relativity*. Cambridge University Press, 2021. — metric as symmetric nondegenerate $(0,2)$ tensor; line element; raising/lowering.
2. Nakahara, M. *Geometry, Topology and Physics*. IOP, 2003. — metric tensor / first fundamental form.
3. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — metric components and index gymnastics.
