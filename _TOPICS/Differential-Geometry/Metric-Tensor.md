# Metric Tensor

<i>

**definition [d]** (*Metric Tensor = Riemannian Metric = Metrical Matrix = First Fundamental Form*) A symmetric, covariant second-rank tensor field $G$ giving a bilinear map on tangent vectors (Frankel),

- $G(v,w) = \langle v, w \rangle = \sum_{i,j} g_{ij}\, v^{i}\, w^{j}$ ,

with local components $g_{ij}(x) = \left\langle \partial/\partial x^{i},\, \partial/\partial x^{j} \right\rangle$.

where

- $G$ is symmetric: $g_{ij} = g_{ji}$.
- the components are differentiable functions of the coordinates.
- Riemannian if positive-definite; indefinite (Lorentzian) metrics are allowed in relativity.

</i>

<i>

**definition [d]** (*Metric Tensor = Riemannian Metric = Metrical Matrix = First Fundamental Form*) A symmetric second-order tensor $g_{ij}$ that fixes the square of infinitesimal arc length (Arfken),

- $(ds)^{2} = g_{ij}\, du^{i}\, du^{j}$ ,

and raises / lowers indices via its inverse $g^{ik}$:

- $V_{i} = g_{ij}\, V^{j}$ ,
- $V^{i} = g^{ij}\, V_{j}$ .

where

- $g^{ik} g_{kj} = \delta^{i}_{\ j}$.
- in flat Minkowski spacetime, $g_{\mu\nu} = \eta_{\mu\nu}$.

</i>

## References

1. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — metric as symmetric covariant $2$-tensor; $g_{ij}=\langle\partial_{i},\partial_{j}\rangle$; first fundamental form.
2. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — $(ds)^{2}=g_{ij}\,du^{i}\,du^{j}$; metrical matrix.
3. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — type-$(0,2)$ tensor fields; nondegenerate metrics.
4. Reed, M., & Simon, B. *Methods of Modern Mathematical Physics I: Functional Analysis*. Academic Press. — bilinear / sesquilinear forms (functional-analytic setting).
