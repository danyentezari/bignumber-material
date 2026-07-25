# Covariant Rank

An integer counting how many lower indices a tensor carries that is used to track how those components change under a change of basis.

<i>

**definition [d]** (*Covariant Rank = Covariant Degree*) The integer $s$ for a type-$(r,s)$ tensor: the number of vector arguments the multilinear map consumes,

- $T^{r}_{\ s}(\omega^{1},\ldots,\omega^{r},\, \underbrace{v_{1},\ldots,v_{s}}_{s})$ .

where

- $T^{r}_{\ s}$ is a tensor of type $(r,s)$.
- $r$ is the contravariant rank.
- $s$ is the covariant rank.
- $\omega^{1},\ldots,\omega^{r}$ are covectors in $V^{*}$.
- $v_{1},\ldots,v_{s}$ are vectors in $V$.
- $V$ is a vector space.
- $V^{*}$ is the dual of $V$.

Note:

- $r$ is also called the contravariant degree.
- $s$ is also called the covariant degree.
- $s$ is the second slot in type-$(q,r)$ notation.

</i>

<i>

**definition [d]** (*Covariant Rank = Covariant Degree*) The number of subscript lower indices on the components of a tensor,

- $T^{\mu_1\ldots\mu_r}_{\ \nu_1\ldots\nu_s}$ has covariant rank $s$ ,

transforming covariantly under a change of coordinates.

where

- $T^{\mu_1\ldots\mu_r}_{\ \nu_1\ldots\nu_s}$ are the components of the tensor.
- $\mu_1,\ldots,\mu_r$ are the upper, contravariant indices.
- $\nu_1,\ldots,\nu_s$ are the lower, covariant indices.
- $r$ is the contravariant rank.
- $s$ is the covariant rank.

Note:

- the total rank is $r + s$.
- the total rank is also called the order.

</i>


## Elementary Example
### Simple

Covariant rank $s$ counts lower indices. A covector is type $(0,1)$, so $s = 1$.

$$
\omega = \omega_{1}\, e^{1} + \omega_{2}\, e^{2}
$$

$$
r = 0,\quad s = 1
$$

where

- $s$ is the covariant rank.
- $r$ is the contravariant rank.
- $\omega_{1}, \omega_{2}$ are the lower-index components of $\omega$.

### General

A type-$(0,2)$ tensor on $\mathbb{R}^{3}$ has covariant rank $s = 2$ and a $3 \times 3$ matrix of components $T_{ij}$.

$$
T : \mathbb{R}^{3} \times \mathbb{R}^{3} \rightarrow \mathbb{R}
$$

$$
(T_{ij}) = \begin{pmatrix} T_{11} & T_{12} & T_{13} \\ T_{21} & T_{22} & T_{23} \\ T_{31} & T_{32} & T_{33} \end{pmatrix}
$$

$$
r = 0,\quad s = 2
$$

where

- $T_{ij}$ are the two lower-index components of $T$.

## References

1. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — covariant degree $s$ of a type-$(r,s)$ tensor.
2. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — covariant rank equals the number of lower indices.
3. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — covariant arguments and indices.
