# Inverse Metric

A matrix function that is the inverse of the metric matrix that is used to raise indices on tensors.

<i>

**definition [d]** (*Inverse Metric = Contravariant Metric Tensor*) The contravariant metric tensor $g^{ik}$ that is the matrix inverse of the covariant metric $g_{kj}$:

- $g^{ik}\, g_{kj} = \delta^{i}_{\ j}$ .

where

- $g^{ik}$ are the components of the inverse metric.
- $g_{kj}$ are the components of the covariant metric.
- $\delta^{i}_{\ j}$ is the Kronecker delta.
- $i, j, k$ are coordinate indices.

Note:

- $g_{kj}$ must be nondegenerate so the inverse exists.
- $g^{ik} = g^{ki}$.

</i>

<i>

**definition [d]** (*Inverse Metric = Contravariant Metric Tensor*) The type-$(2,0)$ tensor used to raise indices,

- $V^{i} = g^{ij}\, V_{j}$ ,

with $g^{ik}\, g_{kj} = \delta^{i}_{\ j}$.

where

- $g^{ij}$ are the components of the inverse metric.
- $V^{i}$ are the raised, contravariant components of a vector.
- $V_{j}$ are the lowered, covariant components of a vector.
- $\delta^{i}_{\ j}$ is the Kronecker delta.

Note:

- lowering uses the covariant metric: $V_{i} = g_{ij}\, V^{j}$.
- together, $g_{ij}$ and $g^{ij}$ identify vectors with covectors.

</i>


## Elementary Example
### Simple

Let $g$ be a diagonal metric matrix. The inverse metric $g^{-1}$ is the matrix inverse of $g$.

$$
g = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix},\quad
g^{-1} = \begin{pmatrix} \tfrac{1}{2} & 0 \\ 0 & 1 \end{pmatrix}
$$

$$
g^{ik} g_{kj} = \delta^{i}_{\ j}
$$

where

- $g_{kj}$ are components of the metric.
- $g^{ik}$ are components of the inverse metric.
- $\delta^{i}_{\ j}$ is the Kronecker symbol, equal to $1$ if $i = j$ and $0$ otherwise.

### General

In three dimensions the same rule inverts a diagonal metric with three entries.

$$
g = \operatorname{diag}(2,1,4),\quad g^{-1} = \operatorname{diag}(\tfrac{1}{2},1,\tfrac{1}{4})
$$

$$
g^{ik} g_{kj} = \delta^{i}_{\ j}
$$

where

- $\operatorname{diag}(a,b,c)$ is the diagonal matrix with those entries.
- raising an index uses $v^{i} = g^{ij} v_{j}$.

## References

1. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — contravariant metric $g^{ik}$; $g^{ik}g_{kj}=\delta^{i}_{j}$.
2. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — inverse metric and index raising.
3. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — inverse of a nondegenerate metric.
