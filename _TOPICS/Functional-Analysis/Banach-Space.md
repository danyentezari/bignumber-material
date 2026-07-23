# Banach Space

A set of vectors equipped with a norm in which every sequence that gets arbitrarily close within itself has a limit in the set. Used to solve equations and to study limits of sequences of vectors.

<i>

**definition [d]** (*Banach Space*) A complete normed space, that is, a normed space that is complete in the metric defined by the norm.

where

- the underlying set is a vector space equipped with a norm.
- completeness means every Cauchy sequence converges to a limit in the space.
- the metric induced by the norm is $d(x, y) = \lVert x - y \rVert$.

Note:

- also called a complete normed vector space.
- also called a complete normed linear space.

</i>

<i>

**definition [d]** (*Banach Space*) A complete normed vector space.

where

- the underlying set is a vector space equipped with a norm.
- completeness means every Cauchy sequence converges to a limit in the space.

Note:

- the completeness is with respect to the metric induced by the norm.

</i>

## Examples

<i>

**example [d]** (**Sequence Space $\ell^{p}$** — Gamelin and Greene) For $1 \leq p < \infty$, as a set,

- $\ell^{p} = \left\{ x = \{x_{j}\}_{j=1}^{\infty} \;\middle|\; \displaystyle\sum_{j=1}^{\infty} |x_{j}|^{p} < \infty \right\}$ ,

with norm $\lVert x \rVert_{p} = \left( \sum_{j=1}^{\infty} |x_{j}|^{p} \right)^{\dfrac{1}{p}}$. This is a Banach space.

where

- $\ell^{p}$ is the space of $p$-summable sequences.
- $x = \{x_{j}\}$ is a real or complex sequence.
- $p$ is a fixed real number with $1 \leq p < \infty$.

Note:

- the case $p = 2$ recovers the Hilbert space $\ell^{2}$.

</i>

<i>

**example [d]** (**Bounded Sequences $\ell^{\infty}$** — Gamelin and Greene, Kreyszig) As a set,

- $\ell^{\infty} = \left\{ x = \{x_{j}\}_{j=1}^{\infty} \;\middle|\; \sup_{1 \leq j < \infty} |x_{j}| < \infty \right\}$ ,

with norm $\lVert x \rVert_{\infty} = \sup_{j} |x_{j}|$. This is a Banach space.

where

- $\ell^{\infty}$ is the space of bounded sequences.
- $x = \{x_{j}\}$ is a real or complex sequence.

Note:

- Kreyszig takes as underlying set all bounded complex sequences $x = (\xi_{j})$ with $|\xi_{j}| \leq c_{x}$ for all $j$.

</i>

<i>

**example [d]** (**Continuous Functions $C[a,b]$** — Kreyszig) As a set,

- $C[a,b] = \{ x : [a,b] \rightarrow \mathbb{R} \mid x \text{ is continuous on } [a,b] \}$ ,

with norm $\lVert x \rVert = \max_{t \in [a,b]} |x(t)|$. This is a Banach space.

where

- $C[a,b]$ is the space of continuous real-valued functions on $[a,b]$.
- $x$ is a continuous function on the closed interval $[a,b]$.

Note:

- completeness of $C[a,b]$ under the maximum norm is proved in Kreyszig §1.5-5.

</i>

## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Definition 2.2-1: Banach space as complete normed space; $C[a,b]$; $\ell^{\infty}$.
2. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — Banach space as complete normed vector space.
3. Gamelin, T. W., & Greene, R. E. *Introduction to Topology*, 2nd ed. Dover, 1999. — $\ell^{p}$ and $\ell^{\infty}$ in set-builder notation.
