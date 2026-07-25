# Norm

A norm is a function that associates a real number with a vector, that is used for measuring the distance between vectors.

<i>

**definition [d]** (*Norm*) From Kreyszig: a norm on a real or complex vector space $X$ is a real-valued function on $X$ whose value at an $x \in X$ is denoted by $\lVert x \rVert$ and which has the properties

- (N1) $\lVert x \rVert \geq 0$
- (N2) $\lVert x \rVert = 0$ if and only if $x = 0$
- (N3) $\lVert \alpha x \rVert = |\alpha|\, \lVert x \rVert$
- (N4) $\lVert x + y \rVert \leq \lVert x \rVert + \lVert y \rVert$ (Triangle inequality)

here $x$ and $y$ are arbitrary vectors in $X$ and $\alpha$ is any scalar.

where

- $X$ is a real or complex vector space.
- $\lVert x \rVert$ is the norm of $x$.
- $\alpha$ is a scalar.
- $|\alpha|$ is the absolute value of $\alpha$.

Note:

- Kreyszig: a norm on $X$ defines a metric $d$ on $X$ by $d(x,y) = \lVert x - y \rVert$, called the metric induced by the norm.
- The normed space is denoted $(X, \lVert\cdot\rVert)$ or simply $X$.

</i>

## Elementary Example
### Simple

A norm assigns a nonnegative length to each vector. On $\mathbb{R}^{2}$ use the Euclidean length.

$$
X = \mathbb{R}^{2}
$$

$$
\lVert (x_{1},x_{2}) \rVert = \sqrt{x_{1}^{2} + x_{2}^{2}}
$$

$$
\lVert (3,4) \rVert = 5,\quad \lVert (0,0) \rVert = 0
$$

where

- $\lVert x \rVert$ is the norm of the vector $x$.
- $X$ is the vector space.

### General

On $\mathbb{R}^{3}$ the same Euclidean norm has three squared components, and it induces the metric $d(x,y) = \lVert x - y \rVert$.

$$
\lVert (x_{1},x_{2},x_{3}) \rVert = \sqrt{x_{1}^{2} + x_{2}^{2} + x_{3}^{2}}
$$

$$
d(x,y) = \lVert x - y \rVert
$$

where

- $d$ is the metric induced by the norm.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Norm axioms (N1)–(N4); metric induced by the norm $d(x,y)=\lVert x-y\rVert$.
