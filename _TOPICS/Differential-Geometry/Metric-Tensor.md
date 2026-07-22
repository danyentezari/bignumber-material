# Metric Tensor

<i>

**definition [d]** (*Metric Tensor = Riemannian Metric = Metrical Matrix = First Fundamental Form*) A symmetric, covariant second-rank tensor field $G$ giving a bilinear map on tangent vectors,

- $G(v,w) = \langle v, w \rangle = \sum_{i,j} g_{ij}\, v^{i}\, w^{j}$ ,

with local components $g_{ij}(x) = \left\langle \partial/\partial x^{i},\, \partial/\partial x^{j} \right\rangle$.

where

- $G$ is the metric tensor field.
- $v, w$ are tangent vectors.
- $g_{ij}$ are the components of $G$ in local coordinates.
- $v^{i}, w^{j}$ are the components of $v$ and $w$.
- $\langle \cdot,\, \cdot \rangle$ is the metric bilinear form.
- $x$ are local coordinates.
- $\partial / \partial x^{i}$ are the coordinate basis vectors.

Note:

- $G$ is symmetric: $g_{ij} = g_{ji}$.
- the components are differentiable functions of the coordinates.
- Riemannian if positive-definite; indefinite Lorentzian metrics are allowed in relativity.

</i>

<i>

**definition [d]** (*Metric Tensor = Riemannian Metric = Metrical Matrix = First Fundamental Form*) A symmetric second-order tensor $g_{ij}$ that fixes the square of infinitesimal arc length,

- $(ds)^{2} = g_{ij}\, du^{i}\, du^{j}$ ,

and raises and lowers indices via its inverse $g^{ik}$:

- $V_{i} = g_{ij}\, V^{j}$ ,
- $V^{i} = g^{ij}\, V_{j}$ .

where

- $g_{ij}$ are the covariant metric components.
- $g^{ik}$ are the contravariant inverse-metric components.
- $du^{i}$ are coordinate differentials.
- $ds$ is the infinitesimal arc length.
- $V^{i}$ are contravariant components of a vector.
- $V_{i}$ are covariant components of a vector.
- $\delta^{i}_{\ j}$ is the Kronecker delta.

Note:

- in spacetime, $ds$ is the infinitesimal spacetime interval.
- $g^{ik} g_{kj} = \delta^{i}_{\ j}$.
- in flat Minkowski spacetime, $g_{\mu\nu} = \eta_{\mu\nu}$.

</i>

## References

1. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — metric as symmetric covariant $2$-tensor; $g_{ij}=\langle\partial_{i},\partial_{j}\rangle$; first fundamental form.
2. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — $(ds)^{2}=g_{ij}\,du^{i}\,du^{j}$; metrical matrix.
3. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — type-$(0,2)$ tensor fields; nondegenerate metrics.
4. Reed, M., & Simon, B. *Methods of Modern Mathematical Physics I: Functional Analysis*. Academic Press. — bilinear / sesquilinear forms in the functional-analytic setting.
