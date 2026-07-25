# Tensors

A multilinear mapping on vectors and covectors that assigns a scalar that is used to represent quantities whose values transform consistently under a change of basis.

<i>

**definition [d]** (*Tensor = Multilinear Map*) A multilinear, real-valued function of type $(r,s)$ on a vector space $V$ and its dual $V^{*}$:

- $T : \underbrace{V^{*} \times \cdots \times V^{*}}_{r} \times \underbrace{V \times \cdots \times V}_{s} \rightarrow \mathbb{R}$ .

where

- $T$ is the tensor.
- $V$ is a vector space over $\mathbb{R}$.
- $V^{*}$ is the dual space of $V$.
- $r$ is the contravariant rank.
- $s$ is the covariant rank.
- $\mathbb{R}$ is the set of real numbers.

Note:

- $V$ may equally be a vector space over $\mathbb{C}$.
- $T$ is linear in each argument independently.
- a scalar is type $(0,0)$; a vector is type $(1,0)$; a covector is type $(0,1)$.

</i>

<i>

**definition [d]** (**Tensor**) An array of components $T^{i_1\ldots i_p}_{\ j_1\ldots j_q}$ labeled by $p$ contravariant upper and $q$ covariant lower indices, whose components transform linearly under a coordinate change $x \mapsto x'$:

- (Contravariant) $(T')^{i} = \displaystyle \sum_{j} \dfrac{\partial x^{j}}{\partial (x')^{i}}\, T^{j}$ .
- (Covariant) $(T')_{i} = \displaystyle \sum_{j} \dfrac{\partial (x')^{i}}{\partial x^{j}}\, T_{j}$ .
- (Mixed rank 2) $(T')^{i}_{\ j} = \displaystyle \sum_{k,l} \dfrac{\partial x^{k}}{\partial (x')^{i}}\, \dfrac{\partial (x')^{j}}{\partial x^{l}}\, T^{k}_{\ l}$ .

where

- $T^{i_1\ldots i_p}_{\ j_1\ldots j_q}$ are the components of the tensor.
- $p$ is the number of contravariant indices.
- $q$ is the number of covariant indices.
- $x$ and $x'$ are the old and new coordinates.
- $T^{j}$, $T_{j}$, $T^{k}_{\ l}$ are components in the old coordinates.
- $(T')^{i}$, $(T')_{i}$, $(T')^{i}_{\ j}$ are components in the new coordinates.

Note:

- the total rank is $p + q$; in $d$ dimensions a rank-$n$ tensor has $d^{n}$ components.
- upper indices transform with the Jacobian $\partial x^{j}/\partial (x')^{i}$; lower indices with its inverse $\partial (x')^{i}/\partial x^{j}$.
- the transformation laws ensure the tensor represents a coordinate-independent geometric object.

</i>

## Examples

<i>

**example [d]** (**Euclidean Metric on $\mathbb{R}^{3}$** — Frankel, Arfken) On the fixed vector space $V = \mathbb{R}^{3}$ with the standard basis, the Euclidean inner product is the type-$(0,2)$ tensor

- $g : V \times V \rightarrow \mathbb{R}$ ,
- $g(u, v) = u \cdot v = \sum_{i,j} \delta_{ij}\, u^{i}\, v^{j}$ ,

with components

- $(g_{ij}) = \operatorname{diag}(1,\, 1,\, 1) = I_{3}$ .

As a multilinear map this is one bilinear form on $V$, not a field of forms on a manifold.

where

- $V = \mathbb{R}^{3}$ is the underlying vector space.
- $u, v \in V$ are vectors.
- $u^{i}, v^{j}$ are components of $u$ and $v$ in the standard basis.
- $\delta_{ij}$ is the Kronecker delta.
- $I_{3}$ is the $3 \times 3$ identity matrix.

Note:

- this is a single tensor of type $(0,2)$ on $V$.
- contrast with a metric tensor field, whose components $g_{ij}(x)$ depend on the point.

</i>

<i>

**example [d]** (**Mixed Kronecker Tensor** — Carroll, Arfken) On a finite-dimensional vector space $V$, the identity map $\operatorname{id}_{V} : V \rightarrow V$ is the type-$(1,1)$ tensor $\delta$ with components

- $\delta^{i}_{\ j} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$ ,

so that

- $\delta(v, \omega) = \omega(v)$ ,
- $\delta^{i}_{\ j}\, v^{j} = v^{i}$ .

where

- $V$ is a finite-dimensional vector space.
- $\delta^{i}_{\ j}$ are the components of the mixed Kronecker tensor.
- $v \in V$ is a vector with components $v^{j}$.
- $\omega \in V^{*}$ is a covector.

Note:

- $\delta^{\mu}_{\ \nu}$ is the identity map on vectors and one-forms.
- the components are numerical constants, independent of any point on a manifold.

</i>

<i>

**example [d]** (**Minkowski Metric Components** — Griffiths) As an array of components, the flat spacetime metric tensor is

- $(g_{\mu\nu}) =
\begin{bmatrix}
-1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}$ .

where

- $g_{\mu\nu}$ are the components of the Minkowski metric tensor.
- $\mu, \nu$ are spacetime indices running over $0,1,2,3$.

Note:

- this is a type-$(0,2)$ tensor written as a $4 \times 4$ array of components.
- the same array is often written $\eta_{\mu\nu} = \operatorname{diag}(-1,\, 1,\, 1,\, 1)$.

</i>

## Historical Notes

Tensor calculus was established by Ricci and Levi-Cività in 1901.[8] Einstein adopted tensors for general relativity to ensure physical laws—such as the unified stress-energy-momentum tensor—remain invariant across all coordinate systems.[8]

## References

1. Nash, C., & Sen, S. *Topology and Geometry for Physicists*. Academic Press, 1983. — tensor as multilinear map.
2. Carroll, S. *Spacetime and Geometry: An Introduction to General Relativity*. Cambridge University Press, 2021. — multilinear-map definition; mixed Kronecker as type $(1,1)$.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — component transformation laws; Kronecker delta; Euclidean metric components.
4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006. — component transformation definition.
5. Cahill, K. *Physical Mathematics*. Cambridge University Press, 2019. — component transformation definition.
6. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — Euclidean metric as bilinear form.
7. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — Minkowski metric as component matrix $g_{\mu\nu}$.
8. Gowers, T., Barrow-Green, J., & Leader, I. (Eds.). *The Princeton Companion to Mathematics*. Princeton University Press, 2008. — Part VIII.7 chronology (p. 1013): Ricci and Levi-Cività, 1901, *Méthodes du Calcul Différentiel Absolut et leurs Applications*; Part IV.13 Dafermos, general covariance and the stress–energy–momentum tensor $T$.
