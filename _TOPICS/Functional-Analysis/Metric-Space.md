# Metric Space

A set with a metric function that is used for calculating the distance between any two elements to study limits and sequences.

Note: Also called distance function for the metric $d$.

<i>

**definition [d]** (*Metric Space*) From Kreyszig Definition 1.1-1: a metric space is a pair $(X,d)$, where $X$ is a set and $d$ is a metric on $X$, that is, a function defined on $X \times X$ such that for all $x,y,z \in X$ we have:

- (M1) $d$ is real-valued, finite and nonnegative.
- (M2) $d(x,y) = 0$ if and only if $x = y$.
- (M3) $d(x,y) = d(y,x)$ (Symmetry).
- (M4) $d(x,y) \leq d(x,z) + d(z,y)$ (Triangle inequality).

where

- $X$ is a set.
- $d$ is the metric on $X$.
- $x, y, z \in X$.

</i>

## Elementary Example
### Simple

A metric $d$ assigns a distance to each pair of points. On three points of the line, use absolute difference.

$$
X = \{ 0,\ 1,\ 2 \}
$$

$$
d(x,y) = |x - y|
$$

$$
d(0,2) = 2,\quad d(1,1) = 0
$$

where

- $X$ is the underlying set.
- $d$ is the metric on $X$.

### General

On $\mathbb{R}^{3}$ the Euclidean metric is the length of the difference vector.

$$
X = \mathbb{R}^{3}
$$

$$
d(x,y) = \sqrt{(x_{1}-y_{1})^{2} + (x_{2}-y_{2})^{2} + (x_{3}-y_{3})^{2}}
$$

where

- $x = (x_{1},x_{2},x_{3})$ and $y = (y_{1},y_{2},y_{3})$ are points of $\mathbb{R}^{3}$.
- $d$ satisfies Kreyszig’s axioms (M1)–(M4).


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Definition 1.1-1 (Metric space, metric).
