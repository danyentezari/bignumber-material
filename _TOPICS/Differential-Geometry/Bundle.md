# Bundle

A set that locally looks like a Cartesian product of a base set and a fiber set that is used to represent fields of vectors attached to each point.

<i>

**definition [d]** (*Bundle = Fibre Bundle = Fiber Bundle*) A fiber manifold $F^{k}$, total space $E$, and base $M^{n}$, together with a projection $\pi: E \rightarrow M^{n}$ that is locally trivial: every point of $M$ has a neighborhood $U$ with

- $\pi^{-1}(U) \cong U \times F$ .

where

- $F^{k}$ is the typical fiber, of dimension $k$.
- $E$ is the total space.
- $M^{n}$ is the base manifold, of dimension $n$.
- $\pi: E \rightarrow M^{n}$ is the projection map.
- $U$ is an open neighborhood in $M$.
- $\pi^{-1}(U)$ is the preimage of $U$ under $\pi$.

Note:

- $E_{p} = \pi^{-1}(p)$ is the fiber over $p$.
- globally $E$ need not equal the product $M \times F$.

</i>

<i>

**definition [d]** (*Bundle = Tensor Bundle = Bundle of Tensors*) The bundle of type-$(r,s)$ tensors over $M$,

- $T^{r}_{\ s}(M) = \bigcup_{P \in M} T^{r}_{\ s,P}(M)$ ,

with projection sending each tensor to its base point $P$.

where

- $M$ is a smooth manifold.
- $P$ is a point of $M$.
- $T^{r}_{\ s,P}(M)$ is the space of type-$(r,s)$ tensors at $P$.
- $T^{r}_{\ s}(M)$ is the tensor bundle of type $(r,s)$.
- $r$ is the contravariant degree.
- $s$ is the covariant degree.

Note:

- a smooth section of $T^{r}_{\ s}(M)$ is a smooth type-$(r,s)$ tensor field.
- special cases: $T(M) = T^{1}_{\ 0}(M)$ is the tangent bundle; $T^{*}(M) = T^{0}_{\ 1}(M)$ is the cotangent bundle.

</i>

## Elementary Example
### Simple

A trivial bundle is the product of a base and a fiber. The projection $\pi$ sends each pair to its base point.

$$
\pi : E \rightarrow M
$$

$$
M = \{ 1,\ 2,\ 3 \}
$$

$$
F = \{ a,\ b \}
$$

$$
E = M \times F = \{ (1,a),\ (1,b),\ (2,a),\ (2,b),\ (3,a),\ (3,b) \}
$$

$$
\pi(p,v) = p,\quad \pi^{-1}(2) = \{ (2,a),\ (2,b) \}
$$

where

- $M$ is the base set.
- $F$ is the fiber set.
- $E$ is the total space.
- $\pi$ is the projection map.
- $\pi^{-1}(2)$ is the fiber over the point $2$.

### General

Local triviality means every base point has a neighborhood $U$ with $\pi^{-1}(U) \cong U \times F$. Here two charts cover a four-point base.

$$
M = \{ 1,\ 2,\ 3,\ 4 \}
$$

$$
U = \{ 1,\ 2 \},\quad W = \{ 3,\ 4 \}
$$

$$
F = \{ a,\ b,\ c \}
$$

$$
\pi^{-1}(U) = U \times F,\quad \pi^{-1}(W) = W \times F
$$

where

- $U$ and $W$ are neighborhoods covering $M$.
- $\pi^{-1}(U) \cong U \times F$ is Frankel’s local product condition.

## References

1. Frankel, T. *The Geometry of Physics*, 3rd ed. Cambridge University Press. — fiber bundles; local triviality; tensor bundles.
2. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — $T^{r}_{s}(M)=\bigcup_{P} T^{r}_{s,P}(M)$.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — tensor fields on coordinate patches in the component view.
