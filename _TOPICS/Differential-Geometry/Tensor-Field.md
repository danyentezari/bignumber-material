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

## References

1. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — tensor field $T:U\to T^{r}_{s}(M)$; $T(P)\in T^{r}_{s,P}(M)$.
2. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — tensor fields as differentiable, coordinate-independent fields; sections.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — tensor fields via component transformation laws.
