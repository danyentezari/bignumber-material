# P

A parameter that is a real number at least one that is used to define a family of norms on sequences and on functions by choosing the power in a sum or integral.

<i>

**definition [d]** (*$p$ = Exponent Parameter*) A fixed real number $p \geq 1$: the power to which absolute values of sequence terms or of function values are raised in forming the $\ell^{p}$ sum or the $L^{p}$ integral, before the outer $\dfrac{1}{p}$ root that defines the $p$-norm.

where

- $p$ is the exponent parameter.
- $\ell^{p}$ is the space of $p$-summable sequences.
- $L^{p}$ is the corresponding Banach space of $p$-integrable functions.
- the $p$-norm of a sequence $x = (\xi_{j})$ is $\lVert x \rVert_{p} = \bigl(\sum_{j}|\xi_{j}|^{p}\bigr)^{\dfrac{1}{p}}$.

Note:

- Kreyszig introduces $p$ with the phrase “let $p \geq 1$ be a fixed real number.”
- for $p > 1$, the companion $q$ defined by $\dfrac{1}{p} + \dfrac{1}{q} = 1$ is the conjugate exponent.

</i>

<i>

**definition [d]** (*$p$ = Norm Family Parameter*) A real parameter in the range $1 \leq p < \infty$ that labels the one-parameter family of $p$-norms $\lVert\,\cdot\,\rVert_{p}$ on sequence spaces and on spaces of continuous functions.

where

- $p$ is the parameter of the norm family.
- $\lVert x \rVert_{p} = \bigl(\sum_{j}|x_{j}|^{p}\bigr)^{\dfrac{1}{p}}$ on $\ell^{p}$.
- $\lVert f \rVert_{p} = \bigl(\int |f|^{p}\, ds\bigr)^{\dfrac{1}{p}}$ on suitable function spaces.

Note:

- as $p \to \infty$, $\lVert\,\cdot\,\rVert_{p}$ tends to the supremum norm $\lVert\,\cdot\,\rVert_{\infty}$.
- the case $p = 2$ recovers the Euclidean and Hilbert norms associated with an inner product.

</i>

<i>

**definition [d]** (*$p$ in Mathematical Physics*) A positive integer appearing in the finite-dimensional $p$-norm on $\mathbb{C}^{n}$,

- $\lVert a \rVert_{p} \equiv \left( \displaystyle\sum_{i=1}^{n} |\alpha_{i}|^{p} \right)^{\dfrac{1}{p}}$ ,

and, in the infinite-dimensional setting of square-integrable functions, the special value $p = 2$ that is the power in the integrability condition defining $L^{2}_{w}(a,b)$.

where

- $a = \{\alpha_{i}\}$ is a vector in $\mathbb{C}^{n}$.
- $p$ is a positive integer in the finite-dimensional formula.
- $L^{2}_{w}(a,b)$ is the weighted space of square-integrable functions on $[a,b]$.
- the superscript $2$ in $L^{2}$ is this power $p = 2$.

Note:

- Hassani’s infinite-dimensional development focuses on the Hilbert case $p = 2$.
- Arfken likewise works primarily with square-integrable functions rather than general $L^{p}$.

</i>

## Historical Notes

Riesz introduced the parameter $p$ in 1910.
He replaced the assumption of quadratic integrability by the integrability of $|f|^{p}$.
Each number $p$ greater than $1$ determines a function class $L^{p}$.
The letter $p$ names that power in $|f|^{p}$.

## Elementary Example
### Simple

The parameter $p$ is a real number at least $1$. The choice $p = 1$ gives the sum of absolute values.

$$
p = 1
$$

$$
\lVert x \rVert_{1} = |\xi_{1}| + |\xi_{2}| + |\xi_{3}|
$$

$$
x = (\xi_{1},\xi_{2},\xi_{3}) = (1,-2,3),\quad \lVert x \rVert_{1} = 6
$$

where

- $p$ is the exponent parameter.
- $\lVert x \rVert_{p}$ is the $p$-norm.

### General

For $p = 2$ the same three-term sequence uses squares under a square root.

$$
p = 2
$$

$$
\lVert x \rVert_{2} = \bigl(|\xi_{1}|^{2} + |\xi_{2}|^{2} + |\xi_{3}|^{2}\bigr)^{1/2}
$$

$$
x = (1,-2,3),\quad \lVert x \rVert_{2} = \sqrt{14}
$$

where

- $p \geq 1$ labels the family of $p$-norms.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — fixed $p\geq 1$ in $\ell^{p}$ and $L^{p}$; conjugate exponents $\dfrac{1}{p} + \dfrac{1}{q}=1$.
2. Gamelin, T. W., & Greene, R. E. *Introduction to Topology*, 2nd ed. Dover, 1999. — one-parameter family of $p$-norms for $1\leq p<\infty$.
3. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — $p$-norm on $\mathbb{C}^{n}$; $L^{2}_{w}$ with power $2$.
4. Pietsch, A. *History of Banach Spaces and Linear Operators*. Birkhäuser, 2007. — Riesz and the introduction of $L^{p}$ via the power $p$ in $|f|^{p}$.
