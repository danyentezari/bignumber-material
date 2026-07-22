# Tensor Field

<i>

**definition [d]** (*Tensor Field = Section*) A mapping that assigns to each point of a manifold a tensor of fixed type: for $U \subset M$,

- $T : U \rightarrow T^{r}_{\ s}(M)$ ,
- $T(P) \equiv T_{P} \in T^{r}_{\ s,P}(M)$ .

where

- $M$ is a smooth manifold.
- $U$ is a subset of $M$.
- $T$ is the tensor field.
- $P$ is a point of $M$.
- $T^{r}_{\ s}(M)$ is the bundle of type-$(r,s)$ tensors on $M$.
- $T^{r}_{\ s,P}(M)$ is the space of type-$(r,s)$ tensors at $P$.
- $r$ is the contravariant degree.
- $s$ is the covariant degree.

Note:

- a smooth tensor field is a smooth such assignment, that is, a smooth section.

</i>

<i>

**definition [d]** (*Tensor Field = Section*) A coordinate-independent field on a manifold whose local components vary differentiably: at each point, a multilinear map

- $T_{P} : \underbrace{(T_{P}M)^{*}\times\cdots\times(T_{P}M)^{*}}_{r} \times \underbrace{T_{P}M\times\cdots\times T_{P}M}_{s} \rightarrow \mathbb{R}$ .

where

- $T_{P}$ is the value of the tensor field at the point $P$.
- $T_{P}M$ is the tangent space at $P$.
- $(T_{P}M)^{*}$ is the cotangent space at $P$.
- $r$ is the number of covector arguments.
- $s$ is the number of vector arguments.
- $\mathbb{R}$ is the set of real numbers.

Note:

- examples: vector fields are type $(1,0)$; covector fields type $(0,1)$; the metric type $(0,2)$.
- equivalently, a section of the tensor bundle $T^{r}_{\ s}(M)$.

</i>

## Examples

<i>

**example [d]** (**Metric Tensor Field** — Frankel) The type-$(0,2)$ metric tensor field on $\mathbb{R}^{3}$ in spherical coordinates $(r, \theta, \phi)$, with line element

- $ds^{2} = dr^{2} + r^{2}\, d\theta^{2} + r^{2}\sin^{2}\theta\, d\phi^{2}$ .

The nonzero components as functions of position are

- $g_{rr}(r, \theta, \phi) = 1$ ,
- $g_{\theta\theta}(r, \theta, \phi) = r^{2}$ ,
- $g_{\phi\phi}(r, \theta, \phi) = r^{2}\sin^{2}\theta$ .

In matrix form,

- $(g_{ij}) = \operatorname{diag}(1,\, r^{2},\, r^{2}\sin^{2}\theta)$ .

where

- $(r, \theta, \phi)$ are spherical coordinates.
- $g_{ij}$ are the components of the metric tensor field.
- $ds$ is the infinitesimal arc length.

Note:

- off-diagonal components vanish.
- this is a smooth assignment of a symmetric type-$(0,2)$ tensor to each point.

</i>

<i>

**example [d]** (**Electromagnetic Field Strength** — Carroll, Hassani) The antisymmetric type-$(0,2)$ tensor field $F_{\mu\nu}$ on Minkowski spacetime with coordinates $x^{\mu} = (t, x, y, z)$:

- $F_{\mu\nu} =
\begin{pmatrix}
0 & -E_{x} & -E_{y} & -E_{z} \\
E_{x} & 0 & -B_{z} & B_{y} \\
E_{y} & B_{z} & 0 & -B_{x} \\
E_{z} & -B_{y} & B_{x} & 0
\end{pmatrix}$ ,

where $E_{i}(t,x,y,z)$ and $B_{i}(t,x,y,z)$ are the electric and magnetic field components at each spacetime point.

As a differential form,

- $F = -E_{x}\, dt\wedge dx - E_{y}\, dt\wedge dy - E_{z}\, dt\wedge dz + B_{z}\, dx\wedge dy - B_{y}\, dx\wedge dz + B_{x}\, dy\wedge dz$ .

where

- $F_{\mu\nu}$ are the components of the electromagnetic field strength tensor field.
- $E_{x}, E_{y}, E_{z}$ are the electric field components.
- $B_{x}, B_{y}, B_{z}$ are the magnetic field components.
- $x^{\mu} = (t, x, y, z)$ are spacetime coordinates.

Note:

- $F$ assigns an antisymmetric bilinear form to each event in spacetime.
- Hassani identifies $F_{j0} = E_{j}$, $F_{12} = B_{3}$, $F_{13} = -B_{2}$, $F_{23} = B_{1}$.

</i>

## References

1. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — tensor field $T:U\to T^{r}_{s}(M)$; electromagnetic field strength $F$.
2. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — metric tensor field in spherical coordinates; $ds^{2}=dr^{2}+r^{2}d\theta^{2}+r^{2}\sin^{2}\theta\,d\phi^{2}$.
3. Carroll, S. *Spacetime and Geometry: An Introduction to General Relativity*. Cambridge University Press, 2021. — electromagnetic field strength tensor $F_{\mu\nu}$.
4. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — tensor fields via component transformation laws.
