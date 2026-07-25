# Topological Spaces

A topological space is a set equipped with a topology that is used to study continuity of mappings without requiring a metric.

<i>

**Definition** (_Topological Space_) A topological space is a pair $(X, \mathcal{T})$ on $X$, where

- $X$ is a set
- $\mathcal{T}$ is a topology

</i>

**Definition** (_Hausdorff Space_) A Hausdorff space is a topological space, $X$, that satisfies the following condition:

- Disjoint neighborhoods: $U_1 \cap U_2 = \empty$, for any pair of points $p_1,p_2 \in X$

where

- $U_1, U_2$ are neighborhoods
- $p_1,p_2 \in X$ are distinct points
- $X$ is a topological space

<i>

**Definition** (_Neighborhood_) A property of a subset $N$ of a topological space $X$ with respect to a point $p \in X$, where the following condition applies:

- There exists an open set $U$ such that $p \in U \subseteq N$.

where

- $X$ is a topological space.
- $p$ is a point in $X$.
- $N$ is a subset of $X$.
- $U$ is an open subset of $X$.
</i>

## Elementary Example
### Simple

A topological space is a set with a topology. Here three points and four open sets.

$$
X = \{ 1,\ 2,\ 3 \}
$$

$$
\tau = \{ \emptyset,\ \{1\},\ \{1,2\},\ X \}
$$

where

- $(X,\tau)$ is the topological space.

### General

Hausdorff separation on a discrete four-point space: distinct points have disjoint open neighborhoods.

$$
X = \{ a,\ b,\ c,\ d \}
$$

$$
\tau = \mathcal{P}(X)
$$

$$
U_{a} = \{a\},\quad U_{b} = \{b\},\quad U_{a} \cap U_{b} = \emptyset
$$

where

- $\mathcal{P}(X)$ is the power set, the discrete topology.
- $U_{a}, U_{b}$ are disjoint neighborhoods of $a$ and $b$.

