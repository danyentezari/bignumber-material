# Hausdorff Space

A Hausdorff space is a topological space in which any two distinct points have disjoint neighborhoods that is used to guarantee uniqueness of limits.

<i>

**Definition** (_Hausdorff Space_) A Hausdorff space is a topological space, $X$, that satisfies the following condition:

- Disjoint neighborhoods: $U_1 \cap U_2 = \empty$, for any pair of points $p_1,p_2 \in X$

where

- $U_1, U_2$ are neighborhoods
- $p_1,p_2 \in X$ are distinct points
- $X$ is a topological space

</i>

## Elementary Example
### Simple

In a Hausdorff space, distinct points have disjoint neighborhoods.

$$
X = \{ 1,\ 2,\ 3 \}
$$

$$
\tau = \mathcal{P}(X)
$$

$$
p_{1} = 1,\ p_{2} = 2,\quad U_{1} = \{1\},\ U_{2} = \{2\}
$$

$$
U_{1} \cap U_{2} = \emptyset
$$

where

- $U_{1}, U_{2}$ are neighborhoods of $p_{1}, p_{2}$.
- $\mathcal{P}(X)$ is the discrete topology.

### General

On four points with the discrete topology, every pair of distinct points separates.

$$
X = \{ a,\ b,\ c,\ d \}
$$

$$
\tau = \mathcal{P}(X)
$$

$$
U_{p} = \{p\}\ \text{for each } p \in X
$$

where

- $U_{p} \cap U_{q} = \emptyset$ whenever $p \neq q$.

