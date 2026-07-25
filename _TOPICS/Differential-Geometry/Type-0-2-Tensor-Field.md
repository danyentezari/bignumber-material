# Type-(0,2) Tensor Field

A smooth mapping that assigns a bilinear form on tangent vectors at each point that is used to represent a metric field.

<i>

**definition [d]** (*Type-$(0,2)$ Tensor Field = Covariant Rank-2 Tensor Field = Second-Rank Covariant Tensor Field*) A smooth section of the tensor bundle $T^{0}_{\ 2}(M)$: at each point $P$, a bilinear map

- $T_{P} : T_{P}M \times T_{P}M \rightarrow \mathbb{R}$ ,

with components that are smooth functions of the coordinates.

where

- $M$ is a smooth manifold.
- $P$ is a point of $M$.
- $T_{P}$ is the value of the tensor field at $P$.
- $T_{P}M$ is the tangent space at $P$.
- $T^{0}_{\ 2}(M)$ is the bundle of type-$(0,2)$ tensors on $M$.
- $\mathbb{R}$ is the set of real numbers.

Note:

- type $(0,2)$ means two covariant indices and no contravariant indices.
- equivalently written $\sum_{i,j} T_{ij}\, du^{i}\otimes du^{j}$ in local coframes.

</i>

<i>

**definition [d]** (*Type-$(0,2)$ Tensor Field = Field of Bilinear Forms*) A smooth type-$(0,2)$ tensor field, with two important special cases:

- if $T_{ij}$ is symmetric and nondegenerate, it is a metric tensor .
- if $T_{ij}$ is totally antisymmetric, it is a differential $2$-form .

where

- $T_{ij}$ are the components of the type-$(0,2)$ tensor field.

Note:

- the metric is the fundamental physical example of a symmetric $(0,2)$ field.
- nondegeneracy means $\det(T_{ij}) \neq 0$.

</i>


## Elementary Example
### Simple

A type-$(0,2)$ tensor field assigns a bilinear form to each point.

$$
U = \{ p,\ q,\ r \}
$$

$$
T_{p}(e_{1},e_{1}) = 1,\quad T_{p}(e_{1},e_{2}) = 0
$$

where

- $T_{p}$ is the bilinear form at the point $p$.
- $e_{1}, e_{2}$ are tangent vectors at $p$.

### General

At each point the value is a $3 \times 3$ matrix of components, as for a metric field.

$$
U = \{ p,\ q \}
$$

$$
T_{p} = I_{3},\quad T_{q} = \operatorname{diag}(2,1,1)
$$

where

- $T_{p}$ is the type-$(0,2)$ tensor at $p$.
- $I_{3}$ is the $3 \times 3$ identity matrix.

## References

1. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — type-$(0,2)$ tensor fields as sections of $T^{0}_{2}(M)$.
2. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — covariant $2$-tensor fields; metric example.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — second-rank covariant tensors.
