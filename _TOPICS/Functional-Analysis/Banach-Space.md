# Banach Space

A set of vectors with a norm where every sequence of elements that get closer to each other has a limit in the set that is used to study the continuity of a mapping.

<i>

**definition [d]** (*Banach Space*) From Kreyszig Definition 2.2-1: a Banach space is a complete normed space, complete in the metric defined by the norm

- $d(x,y) = \lVert x - y \rVert$ .

where

- the underlying space is a normed space $(X, \lVert\cdot\rVert)$.
- completeness means every Cauchy sequence in $X$ converges to an element of $X$.

</i>

## Elementary Example
### Simple

A Banach space is a complete normed space. The line $\mathbb{R}$ with absolute value as norm is Banach.

$$
X = \mathbb{R},\quad \lVert x \rVert = |x|
$$

$$
d(x,y) = |x - y|
$$

where

- $(X,\lVert\cdot\rVert)$ is a normed space.
- completeness is with respect to $d(x,y) = \lVert x - y \rVert$.

### General

The space $\mathbb{R}^{3}$ with the Euclidean norm is a Banach space.

$$
X = \mathbb{R}^{3},\quad \lVert x \rVert = \sqrt{x_{1}^{2} + x_{2}^{2} + x_{3}^{2}}
$$

$$
d(x,y) = \lVert x - y \rVert
$$

where

- every Cauchy sequence in $X$ converges to an element of $X$.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Definition 2.2-1 (Banach space as complete normed space).
