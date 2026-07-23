# Hilbert Space

A set of vectors with an inner product that induces a norm and in which every Cauchy sequence has a limit in the set. Used to solve equations and to expand vectors in a basis.

<i>

**definition [D]** (*Hilbert Space*) A complete inner product space, representing a linear vector space (finite or infinite-dimensional) where every Cauchy sequence of vectors converges to a limit within the space. It serves as the mathematical foundation for the states of quantum systems. A space is a Hilbert space if:

* It possesses a well-defined inner product that induces a norm and a metric.
* It is complete, meaning it has no "holes," similar to the set of real numbers.

where

- $H$ is the Hilbert space.
- $\langle \alpha | \beta \rangle$ is the inner product associating a pair of vectors with a complex scalar.
- $L^2(a, b)$ is the standard example of an infinite-dimensional Hilbert space consisting of square-integrable functions.

Note:

- $H$ is also written $\mathcal{H}$.

</i>

## Examples

<i>

**example [d]** (**Sequence Space $\ell^{2}$** — Kreyszig, Shifrin and Adams) As a set,

- $\ell^{2} = \left\{ x = (\xi_{j})_{j=1}^{\infty} \;\middle|\; \displaystyle\sum_{j=1}^{\infty} |\xi_{j}|^{2} < \infty \right\}$ .

With the inner product

- $(x, y) = \displaystyle\sum_{j=1}^{\infty} \xi_{j}\, \overline{\eta_{j}}$

and induced norm

- $\lVert x \rVert = (x, x)^{\dfrac{1}{2}} = \left( \displaystyle\sum_{j=1}^{\infty} |\xi_{j}|^{2} \right)^{\dfrac{1}{2}}$ ,

the space $\ell^{2}$ is a Hilbert space.

where

- $\ell^{2}$ is the Hilbert sequence space.
- $x = (\xi_{j})$ and $y = (\eta_{j})$ are sequences in $\ell^{2}$.
- $\overline{\eta_{j}}$ is the complex conjugate of $\eta_{j}$.

Note:

- completeness of $\ell^{2}$ is proved in Kreyszig §1.5-4.
- Shifrin and Adams write $\ell^{2} = \{ x \in \mathbb{R}^{\omega} : \sum_{k} x_{k}^{2} \text{ exists} \}$ in the real case.

</i>

<i>

**example [d]** (**Weighted $L^{2}$ Space** — Hassani) As a set, for a strictly positive weight $w$ on $[a,b]$,

- $L^{2}_{w}(a,b) = \left\{ f : [a,b] \rightarrow \mathbb{C} \;\middle|\; \displaystyle\int_{a}^{b} |f(x)|^{2}\, w(x)\, dx < \infty \right\}$ .

This is a Hilbert space under the inner product $\langle g | f \rangle = \int_{a}^{b} g^{*}(x)\, f(x)\, w(x)\, dx$.

where

- $L^{2}_{w}(a,b)$ is the weighted square-integrable function space on $[a,b]$.
- $w$ is a strictly positive weight function.
- $f, g$ are complex-valued functions on $[a,b]$.
- $g^{*}$ is the complex conjugate of $g$.

Note:

- when $w \equiv 1$, this reduces to the usual $L^{2}(a,b)$.

</i>

## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — $\ell^{2}$ as sequences with $\sum|\xi_{j}|^{2}<\infty$; completeness §1.5-4.
2. Shifrin, T., & Adams, M. *Linear Algebra: A Geometric Approach*. W. H. Freeman, 2010. — $\ell^{2}$ in set-builder notation.
3. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — $L^{2}_{w}(a,b)$ as set of square-integrable weighted functions.
