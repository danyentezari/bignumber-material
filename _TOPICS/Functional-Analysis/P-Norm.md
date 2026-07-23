# P-Norm

A norm that assigns a real number size to a sequence using a fixed parameter power, and likewise to a function. Used to measure the length of vectors given as sequences and given as functions.

<i>

**definition [d]** (*p-Norm* — sequences) The real-valued function on $\ell^{p}$ that assigns to each sequence $x = (\xi_{j})$ the number

- $\lVert x \rVert_{p} = \left( \displaystyle\sum_{j=1}^{\infty} |\xi_{j}|^{p} \right)^{\dfrac{1}{p}}$ ,

for fixed $p \geq 1$.

where

- $\lVert x \rVert_{p}$ is the $p$-norm of $x$.
- $x = (\xi_{j})$ is a sequence in $\ell^{p}$.
- $p \geq 1$ is the exponent parameter.
- $\ell^{p}$ is the space of $p$-summable sequences.

Note:

- this norm induces the metric of the Banach space $\ell^{p}$.
- the case $p = 2$ is the Hilbert-space norm on $\ell^{2}$.

</i>

<i>

**definition [d]** (*p-Norm* — functions) The real-valued function that assigns to a continuous function $x$ on $[a,b]$ the number

- $\lVert x \rVert_{p} = \left( \displaystyle\int_{a}^{b} |x(t)|^{p}\, dt \right)^{\dfrac{1}{p}}$ ,

for fixed $p \geq 1$; the Banach space $L^{p}[a,b]$ is the completion of $C[a,b]$ under this norm.

where

- $\lVert x \rVert_{p}$ is the $p$-norm of $x$.
- $x$ is a continuous real-valued function on $[a,b]$.
- $p \geq 1$ is the exponent parameter.
- $C[a,b]$ is the space of continuous functions on $[a,b]$.
- $L^{p}[a,b]$ is the completed $p$-integrable function space.

Note:

- the same formula extends to the completed space $L^{p}[a,b]$.

</i>

<i>

**definition [d]** (*p-Norm* — finite-dimensional) The real-valued function on $\mathbb{C}^{n}$ that assigns to a vector $a = \{\alpha_{i}\}$ the number

- $\lVert a \rVert_{p} \equiv \left( \displaystyle\sum_{i=1}^{n} |\alpha_{i}|^{p} \right)^{\dfrac{1}{p}}$ ,

where $p$ is a positive integer.

where

- $\lVert a \rVert_{p}$ is the $p$-norm of $a$.
- $a = \{\alpha_{i}\}$ is a vector in $\mathbb{C}^{n}$.
- $n$ is the dimension.
- $p$ is a positive integer.

Note:

- the same formula defines a norm on $\mathbb{R}^{n}$.
- when $p = 2$, this is the Euclidean norm.

</i>

## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — $\lVert x\rVert_{p}$ on $\ell^{p}$; integral $p$-norm and completion to $L^{p}[a,b]$.
2. Gamelin, T. W., & Greene, R. E. *Introduction to Topology*, 2nd ed. Dover, 1999. — one-parameter family of $p$-norms on sequences and on $C[0,1]$.
3. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — $\lVert a\rVert_{p}$ on $\mathbb{C}^{n}$.
