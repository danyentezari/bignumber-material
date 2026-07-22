# Normed Space

<i>

**definition [d]** (*Normed Space = Normed Vector Space = Normed Linear Space*) A vector space with a norm defined on it.

where

- the underlying set is a vector space.
- the scalar field is typically $\mathbb{R}$.
- the scalar field is also typically $\mathbb{C}$.
- the norm is a real-valued function on that vector space satisfying the norm axioms.

Note:

- also called a normed vector space.
- also called a normed linear space.

</i>

<i>

**definition [d]** (*Normed Space = Normed Vector Space = Normed Linear Space*) A vector space $X$ equipped with a norm $\lVert \cdot \rVert$, inducing the metric

- $d(x, y) = \lVert x - y \rVert$ .

where

- $X$ is the underlying vector space.
- $\lVert \cdot \rVert$ is the norm on $X$.
- $d$ is the metric induced by the norm.
- $x, y \in X$ are vectors.

Note:

- a Banach space is a normed space that is complete in this metric.

</i>

## Examples

<i>

**example [d]** (**Sequence Space $\ell^{p}$** — Kreyszig) For fixed $p \geq 1$, as a set,

- $\ell^{p} = \left\{ x = (\xi_{j})_{j=1}^{\infty} \;\middle|\; \displaystyle\sum_{j=1}^{\infty} |\xi_{j}|^{p} < \infty \right\}$ ,

with norm

- $\lVert x \rVert_{p} = \left( \displaystyle\sum_{j=1}^{\infty} |\xi_{j}|^{p} \right)^{1/p}$ .

This is a normed space. It is in fact a Banach space.

where

- $\ell^{p}$ is the space of $p$-summable sequences.
- $x = (\xi_{j})$ is a sequence of scalars.
- $p \geq 1$ is a fixed real number.

Note:

- the scalars may be real.
- the scalars may be complex.
- completeness of $\ell^{p}$ under $\lVert \cdot \rVert_{p}$ is shown in Kreyszig §1.5-4.

</i>

## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Definition 2.2-1 (normed space); $\ell^{p}$ as set with $\sum|\xi_{j}|^{p}<\infty$.
