# Ell P

A set of sequences of values where each sequence has a finite norm defined by a parameter that is used to find the distance between sequences.

<i>

**definition [d]** (*$\ell^{p}$*) From Kreyszig 1.2-3: let $p \geq 1$ be a fixed real number. By definition, each element in the space $\ell^{p}$ is a sequence $x = (\xi_{j}) = (\xi_{1}, \xi_{2}, \ldots)$ of numbers such that $|\xi_{1}|^{p} + |\xi_{2}|^{p} + \cdots$ converges; thus

- $\displaystyle\sum_{j=1}^{\infty} |\xi_{j}|^{p} < \infty$ \quad ($p \geq 1$, fixed)

and the metric is defined by

- $\displaystyle d(x,y) = \left( \sum_{j=1}^{\infty} |\xi_{j} - \eta_{j}|^{p} \right)^{1/p}$

where $y = (\eta_{j})$ and $\sum |\eta_{j}|^{p} < \infty$.

From Kreyszig 2.2-3: the space $\ell^{p}$ is a Banach space with norm

- $\displaystyle \lVert x \rVert = \left( \sum_{j=1}^{\infty} |\xi_{j}|^{p} \right)^{1/p}$ .

where

- $p \geq 1$ is a fixed real number.
- $x = (\xi_{j})$ is a sequence of scalars.
- $y = (\eta_{j})$ is another such sequence.

</i>

## Elementary Example
### Simple

The space $\ell^{p}$ consists of $p$-summable sequences with the $p$-norm. For $p = 1$, a three-term sequence is an element after zero-padding.

$$
p = 1,\quad x = (1,-2,3,0,0,\ldots)
$$

$$
\lVert x \rVert = |1| + |-2| + |3| = 6
$$

where

- $\ell^{p}$ is the set of all such sequences.
- $\lVert x \rVert$ is the $\ell^{p}$ norm.

### General

For $p = 2$, distance between two sequences uses the $\ell^{2}$ metric.

$$
x = (1,0,0,\ldots),\quad y = (0,1,0,\ldots),\quad p = 2
$$

$$
d(x,y) = \bigl(|1-0|^{2} + |0-1|^{2}\bigr)^{1/2} = \sqrt{2}
$$

where

- $d(x,y) = \lVert x - y \rVert$ is Kreyszig’s metric on $\ell^{p}$.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — 1.2-3 Space $\ell^{p}$; 2.2-3 Space $\ell^{p}$ as Banach space with $p$-norm.
