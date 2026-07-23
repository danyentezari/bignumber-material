# Completeness

A property of a metric under which every sequence that gets arbitrarily close within itself has a limit in the set. Used to guarantee that limits of sequences stay inside the set.

<i>

**definition [d]** (*Completeness*) A property of a metric space $X = (X, d)$: every Cauchy sequence in $X$ converges to a limit that is an element of $X$.

where

- $X = (X, d)$ is a metric space.
- $d$ is the metric on $X$.
- a Cauchy sequence is a sequence $(x_{n})$ in $X$ such that for every $\epsilon > 0$ there exists $N$ with $d(x_{n}, x_{m}) < \epsilon$ for all $m, n > N$.

Note:

- the limit of each Cauchy sequence must lie in $X$ itself.
- the real line and the complex plane are complete metric spaces.

</i>

<i>

**definition [d]** (*Completeness*) A property of a normed space: completeness as a metric space under the metric induced by the norm,

- $d(x, y) = \lVert x - y \rVert$ .

where

- the underlying space is a normed space.
- $\lVert \cdot \rVert$ is the norm.
- $d$ is the induced metric.
- $x, y$ are vectors in the space.

Note:

- a complete normed space is a Banach space.
- completeness of a normed space is the same as completeness of $(X, d)$ with $d(x,y)=\lVert x-y\rVert$.

</i>

## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Definition 1.4-3 (Cauchy sequence, completeness); completeness via the norm metric in §2.2.
