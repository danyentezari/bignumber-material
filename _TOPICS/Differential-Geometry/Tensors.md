# Tensors

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

- (Contravariant) $(T')^{i} = \displaystyle \sum_{j} \frac{\partial x^{j}}{\partial (x')^{i}}\, T^{j}$ .
- (Covariant) $(T')_{i} = \displaystyle \sum_{j} \frac{\partial (x')^{i}}{\partial x^{j}}\, T_{j}$ .
- (Mixed rank 2) $(T')^{i}_{\ j} = \displaystyle \sum_{k,l} \frac{\partial x^{k}}{\partial (x')^{i}}\, \frac{\partial (x')^{j}}{\partial x^{l}}\, T^{k}_{\ l}$ .

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

## References

1. Nash, C., & Sen, S. *Topology and Geometry for Physicists*. Academic Press, 1983. — tensor as multilinear map.
2. Carroll, S. *Spacetime and Geometry: An Introduction to General Relativity*. Cambridge University Press, 2021. — multilinear-map definition.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — component transformation laws.
4. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006. — component transformation definition.
5. Cahill, K. *Physical Mathematics*. Cambridge University Press, 2019. — component transformation definition.
