# Neighborhood

A neighborhood is an open set containing a given point that is used to describe local behavior of a function near that point.

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

A neighborhood of a point contains an open set that contains that point.

$$
X = \{ 1,\ 2,\ 3 \}
$$

$$
\tau = \{ \emptyset,\ \{1\},\ \{1,2\},\ X \}
$$

$$
p = 1,\quad U = \{1\},\quad N = \{1,2\}
$$

$$
p \in U \subseteq N,\quad U \in \tau
$$

where

- $p$ is the point.
- $U$ is an open set.
- $N$ is a neighborhood of $p$.

### General

On four points, two different neighborhoods of the same point.

$$
X = \{ a,\ b,\ c,\ d \}
$$

$$
\tau = \{ \emptyset,\ \{a\},\ \{a,b\},\ \{a,b,c\},\ X \}
$$

$$
p = a,\quad N_{1} = \{a\},\quad N_{2} = \{a,b,c\}
$$

where

- both $N_{1}$ and $N_{2}$ are neighborhoods of $a$.

