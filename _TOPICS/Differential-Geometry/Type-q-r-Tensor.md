# Type-(q,r) Tensor

<i>

**definition [d]** (*Type-$(q,r)$ Tensor = Type-$(r,s)$ Tensor = Rank $(r,s)$*) A multilinear map taking $r$ covectors and $s$ vectors to a scalar,

- $T^{r}_{\ s} : \underbrace{V^{*}\times\cdots\times V^{*}}_{r} \times \underbrace{V\times\cdots\times V}_{s} \rightarrow \mathbb{R}$ .

where

- $T^{r}_{\ s}$ is a tensor of type $(r,s)$.
- $V$ is a vector space.
- $V^{*}$ is the dual space of $V$.
- $r$ is the contravariant degree.
- $s$ is the covariant degree.
- $\mathbb{R}$ is the set of real numbers.

Note:

- type $(r,s)$ uses the same ordering as type $(q,r)$ with $q = r$ and the second slot equal to $s$.
- type $(1,0)$ is a vector; type $(0,1)$ is a covector or $1$-form.
- the space of such tensors at a point $P$ is denoted $T^{r}_{\ s,P}(M)$.

</i>

<i>

**definition [d]** (*Type-$(q,r)$ Tensor = Rank-$n$ Tensor = Tensorial Set*) A system of components with $r$ upper and $s$ lower indices that transform by the tensor law under coordinate changes,

- $T^{\mu_1\ldots\mu_r}_{\ \nu_1\ldots\nu_s}$ ,

with total rank $n = r + s$.

where

- $T^{\mu_1\ldots\mu_r}_{\ \nu_1\ldots\nu_s}$ are the components of the tensor.
- $\mu_1,\ldots,\mu_r$ are contravariant indices.
- $\nu_1,\ldots,\nu_s$ are covariant indices.
- $r$ is the contravariant rank.
- $s$ is the covariant rank.
- $n$ is the total rank or order.

Note:

- upper indices transform contravariantly; lower indices covariantly.
- also called valence $\{r,s\}$ in some texts.

</i>

## References

1. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — type-$(r,s)$ tensor as multilinear map $V^{*r}\times V^{s}\to\mathbb{R}$.
2. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — rank-$n$ tensors; component transformation laws.
3. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — multilinear tensor algebra on manifolds.
