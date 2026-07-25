# Open Sets

An open set is a member of a topology on a set that is used to define neighborhoods and continuity of mappings.

The open set is central to topology, and it is required for definitions. We begin with a definition and then an example.

<i>

**Definition** (_Open Set_) A subset $U$ of a topological space, $(X,\mathcal{T})$, where the following condition applies:

- $U \in \mathcal{T}$

where

- $X$ is a set
- $\mathcal{T}$ is a topology on $X$
- $U \subseteq X$

</i>

## Elementary Example
### Simple

Open sets are the members of a topology. On $X = \{1,2,3\}$, the set $\{1\}$ is open in the listed topology.

$$
X = \{ 1,\ 2,\ 3 \}
$$

$$
\tau = \{ \emptyset,\ \{1\},\ \{1,2\},\ X \}
$$

$$
\{1\} \in \tau
$$

where

- $\tau$ is the topology.
- $\{1\}$ is an open set.

### General

Unions of open sets are open. On four points, unite two open sets.

$$
X = \{ 1,\ 2,\ 3,\ 4 \}
$$

$$
\tau = \{ \emptyset,\ \{1\},\ \{2\},\ \{1,2\},\ X \}
$$

$$
\{1\} \cup \{2\} = \{1,2\} \in \tau
$$

where

- $\{1\}$ and $\{2\}$ are open.
- their union is open.


<i>

**Example 1** (_Open Set_) Let

$$
X = \{1,2,3\}
$$

$$
\mathcal{T}
=
\{
\emptyset,
\{1\},
\{1,2\},
X
\}.
$$

Then, $(X,\mathcal{T})$ is a topological space, where

*$$
(X,\mathcal{T})
=
\left(
\{1,2,3\},
\{
\emptyset,
\{1\},
\{1,2\},
\{1,2,3\}
\}
\right)
$$

Let

$$
U = \{1,2\}.
$$

Since

$$
U \in \mathcal{T},
$$

it follows that $U$ is an open set.

Therefore,

$$
\{1,2\}
$$

is an open set in $(X,\mathcal{T})$.

</i>
