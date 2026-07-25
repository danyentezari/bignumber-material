# Norm

A norm is a function that associates a real number with a vector, and it that is used for measuring the distance between vectors.

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

## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Norm axioms (N1)–(N4); metric induced by the norm $d(x,y)=\lVert x-y\rVert$.
