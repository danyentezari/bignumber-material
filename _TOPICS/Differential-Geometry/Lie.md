# Lie

A set of matrices with a mapping for products and a mapping for inverses that is used to describe continuous change of vectors by linear transformations.

Note: Also called Lie group.

<i>

**definition [d]** (*Lie = Lie Group*) From Hassani Definition 29.1.1: a Lie group $G$ is a differentiable manifold endowed with a group structure such that the group operation $G \times G \rightarrow G$ and the map $G \rightarrow G$ given by $g \mapsto g^{-1}$ are differentiable.

</i>

<i>

**definition [d]** (*Lie = Lie Group*) From Tu Definition 15.1: a Lie group is a $C^{\infty}$ manifold $G$ that is also a group such that the multiplication map

- $\mu: G \times G \rightarrow G$

and the inverse map

- $\iota: G \rightarrow G$, \quad $\iota(x) = x^{-1}$

are both $C^{\infty}$.

where

- $G$ is the Lie group.
- $\mu$ is the multiplication map.
- $\iota$ is the inverse map.
- $C^{\infty}$ means infinitely differentiable.

</i>


## Elementary Example
### Simple

A discrete group closed under multiplication and inverses illustrates the group maps $\mu$ and $\iota$.

$$
G = \{ e,\ a,\ a^{2} \}
$$

$$
\mu(a,a) = a^{2},\quad \mu(a,a^{2}) = e,\quad \iota(a) = a^{2}
$$

where

- $G$ is the cyclic group of order three.
- $e$ is the identity element.
- $a$ is a generator with $a^{3} = e$.
- $\mu : G \times G \rightarrow G$ is multiplication.
- $\iota : G \rightarrow G$ is inversion.

### General

The fourth roots of unity form a four-element group under complex multiplication, with the same maps $\mu$ and $\iota$.

$$
G = \{ 1,\ i,\ -1,\ -i \}
$$

$$
\mu(i,i) = -1,\quad \iota(i) = -i,\quad \mu(-i,-i) = -1
$$

where

- $i$ is the imaginary unit with $i^{2} = -1$.
- $\mu$ and $\iota$ are the group multiplication and inverse maps.

## References

1. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — Definition 29.1.1 (Lie group).
2. Tu, L. W. *An Introduction to Manifolds*. Springer. — Definition 15.1 (Lie group).
