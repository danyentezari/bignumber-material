# P-Norm

A norm defined by a parameter on a set of sequences that is used to find the distance between elements of the set.

<i>

**definition [d]** (*$p$-Norm*) From Kreyszig 2.2-3: on the space $\ell^{p}$ the norm is given by

- $\displaystyle \lVert x \rVert = \left( \sum_{j=1}^{\infty} |\xi_{j}|^{p} \right)^{1/p}$

for $x = (\xi_{j}) \in \ell^{p}$. This norm induces the metric of 1.2-3.

where

- $p \geq 1$ is a fixed real number.
- $x = (\xi_{j})$ is a sequence in $\ell^{p}$.
- $\lVert x \rVert$ is the $p$-norm of $x$.

</i>

## Elementary Example
### Simple

The $p$-norm of a finite sequence uses the power $p$ and the outer root $1/p$. Take $p = 1$.

$$
x = (1,-2,3),\quad p = 1
$$

$$
\lVert x \rVert = |1| + |-2| + |3| = 6
$$

where

- $\lVert x \rVert$ is the $p$-norm of $x$.
- $p$ is the fixed exponent.

### General

For $p = 2$ on a longer sequence, square each absolute value, sum, then take the square root.

$$
x = (1,0,-1,2),\quad p = 2
$$

$$
\lVert x \rVert = \bigl(1^{2} + 0^{2} + (-1)^{2} + 2^{2}\bigr)^{1/2} = \sqrt{6}
$$

where

- on $\ell^{p}$ the same formula uses an infinite sum $\sum_{j=1}^{\infty} |\xi_{j}|^{p}$.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — 2.2-3: $\lVert x \rVert = \bigl(\sum |\xi_{j}|^{p}\bigr)^{1/p}$ on $\ell^{p}$.
