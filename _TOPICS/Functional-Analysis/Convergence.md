# Convergence

A sequence that gets closer to a fixed element that is used for finding the limit of a function at a real number.

<i>

**definition [d]** (*Convergence*) From Kreyszig Definition 1.4-1: a sequence $(x_{n})$ in a metric space $X = (X,d)$ is said to converge if there is an $x \in X$ such that

- $\displaystyle\lim_{n \to \infty} d(x_{n}, x) = 0$ .

The point $x$ is called the limit of $(x_{n})$ and we write

- $\displaystyle\lim_{n \to \infty} x_{n} = x$

or simply $x_{n} \to x$. We say that $(x_{n})$ converges to $x$ or has the limit $x$. If $(x_{n})$ is not convergent, it is said to be divergent.

where

- $X = (X,d)$ is a metric space.
- $(x_{n})$ is a sequence in $X$.
- $x \in X$ is the limit.
- $d$ is the metric on $X$.

</i>

## Elementary Example
### Simple

A sequence converges when its terms approach a limit in the space. On $\mathbb{R}$, $1/n$ converges to $0$.

$$
X = \mathbb{R},\quad d(x,y) = |x - y|
$$

$$
x_{n} = \dfrac{1}{n},\quad \lim_{n \to \infty} x_{n} = 0
$$

$$
d(x_{n},0) = \dfrac{1}{n} \to 0
$$

where

- $0$ is the limit of $(x_{n})$.
- $d$ is the metric on $X$.

### General

In $\mathbb{R}^{3}$, the sequence $x_{n} = (1/n, 2/n, 3/n)$ converges to the zero vector.

$$
x_{n} \to (0,0,0),\quad d(x_{n},0) = \dfrac{\sqrt{14}}{n} \to 0
$$

where

- $d$ is the Euclidean metric on $\mathbb{R}^{3}$.
- $(0,0,0)$ is the limit.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Definition 1.4-1 (Convergence of a sequence, limit).
