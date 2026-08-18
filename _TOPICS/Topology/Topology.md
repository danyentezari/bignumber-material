# Topology

Topology is the study of geometric properties that persist despite deformations, such as stretching and twisting without tearing.

A topology is a collection of subsets of a set that contains the empty set and the whole set and is closed under arbitrary unions and finite intersections that is used to define open sets and continuity of mappings.

Here are the ideas that are fundamental to the study of topology.

Open sets. Open sets are the subsets that specify nearness in a space without measuring distance. A neighborhood is a set containing an open set around a point.

Continuity. A map is continuous when the preimage of every open set is open. A preimage is the set of domain points sent into a given target set.

Compactness. Compactness is a property of a space: every covering by open sets has a finite subcovering. An open cover is a collection of open sets whose union is the whole space.

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

1. Mendelson, B. *Introduction to Topology*. Dover, 1990. — open sets as the structure of nearness without distance.
2. Lee, J. M. *Introduction to Topological Manifolds*. Springer, 2011. — continuity as preservation of open sets under preimage.
3. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1978. Definition 1.3-1 — compactness as a finite-subcover property.
4. Reed, M., & Simon, B. *Methods of Modern Mathematical Physics I: Functional Analysis*. Academic Press, 1980. Chapter I.
