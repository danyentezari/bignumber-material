# Topology

A topology is a collection of subsets of a set that contains the empty set and the whole set and is closed under arbitrary unions and finite intersections that is used to define open sets and continuity of mappings.

<i>

**definition [d]**

A **topology** on a set $X$ is a collection $\tau$ of subsets of $X$ such that 

1. $\emptyset \in \tau$ and $X \in \tau$
2. $\tau$ is closed under arbitrary unions
3. $\tau$ is closed under finite intersections

*where*

- $\emptyset$ is the empty set
- $X$ is a set
- $\tau$ is a collection of subsets of $X$

**Note:**

- The elements of $\tau$ are called the open sets of the topology.
- A topology on $X$ makes $X$ into a topological space $(X,\tau)$.

</i>

## Elementary Example
### Simple

A topology on a three-point set lists which subsets are open. It must contain $\emptyset$ and $X$.

$$
X = \{ 1,\ 2,\ 3 \}
$$

$$
\tau = \{ \emptyset,\ \{1\},\ \{1,2\},\ X \}
$$

where

- $X$ is the underlying set.
- $\tau$ is the topology on $X$.
- members of $\tau$ are the open sets.

### General

The same axioms on a four-point set: closed under unions and finite intersections.

$$
X = \{ a,\ b,\ c,\ d \}
$$

$$
\tau = \{ \emptyset,\ \{a\},\ \{a,b\},\ \{a,b,c\},\ X \}
$$

$$
\{a\} \cup \{a,b\} = \{a,b\} \in \tau,\quad \{a,b\} \cap \{a,b,c\} = \{a,b\} \in \tau
$$

where

- $\tau$ contains $\emptyset$ and $X$.
- $\tau$ is closed under arbitrary unions and finite intersections.


## References

1. Kreyszig, *Introductory Functional Analysis with Applications*, Wiley, 1978, Definition 1.3-1.
2. Reed & Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1980, Chapter I.
