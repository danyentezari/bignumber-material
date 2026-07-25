# Completeness

A set where every sequence of elements that get closer to each other has a limit in the set that is used for finding the limit of a function.

<i>

**definition [d]** (*Completeness*) From Kreyszig Definition 1.4-3: the space $X$ is said to be complete if every Cauchy sequence in $X$ converges, that is, has a limit which is an element of $X$.

where

- $X = (X,d)$ is a metric space.
- a Cauchy sequence is as in Kreyszig Definition 1.4-3.

Note:

- Kreyszig Theorem 1.4-4: the real line and the complex plane are complete metric spaces.

</i>

## Elementary Example
### Simple

A metric space is complete when every Cauchy sequence converges in the space. The real line is complete.

$$
X = \mathbb{R},\quad d(x,y) = |x - y|
$$

$$
x_{n} = \dfrac{1}{n} \text{ is Cauchy and } x_{n} \to 0 \in \mathbb{R}
$$

where

- $X$ is the metric space.
- completeness means every Cauchy sequence has a limit in $X$.

### General

The plane $\mathbb{R}^{2}$ with the Euclidean metric is complete: every Cauchy sequence of points converges to a point of $\mathbb{R}^{2}$.

$$
X = \mathbb{R}^{2},\quad d(x,y) = \sqrt{(x_{1}-y_{1})^{2} + (x_{2}-y_{2})^{2}}
$$

where

- Kreyszig records that $\mathbb{R}$ and $\mathbb{C}$ are complete; the same holds for $\mathbb{R}^{n}$.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Definition 1.4-3 (completeness); Theorem 1.4-4 (real line, complex plane).
