# P-Summable

A property of a sequence under which the series of absolute values raised to a parameter power converges that is used to identify members belonging to a matching set of sequences.

<i>

**definition [d]** (*$p$-Summable*) From Kreyszig 1.2-3: a sequence $x = (\xi_{j})$ of numbers is an element of $\ell^{p}$ when

- $\displaystyle\sum_{j=1}^{\infty} |\xi_{j}|^{p} < \infty$

for a fixed real number $p \geq 1$.

where

- $x = (\xi_{j})$ is a sequence of scalars.
- $p \geq 1$ is a fixed real number.

</i>

## Elementary Example
### Simple

A sequence is $p$-summable when $\sum |\xi_{j}|^{p}$ is finite. For $p = 1$, the finite sequence $(1,2,3)$ is $1$-summable.

$$
x = (1,2,3),\quad p = 1
$$

$$
\sum_{j=1}^{3} |\xi_{j}|^{1} = 6 < \infty
$$

where

- $p$-summable means membership in $\ell^{p}$ after zero-padding to an infinite sequence.
- $p \geq 1$ is fixed.

### General

For $p = 2$, the infinite sequence $\xi_{j} = 1/j$ is $2$-summable because $\sum 1/j^{2}$ converges.

$$
x = \left(1,\ \dfrac{1}{2},\ \dfrac{1}{3},\ \ldots\right),\quad p = 2
$$

$$
\sum_{j=1}^{\infty} \left|\dfrac{1}{j}\right|^{2} < \infty
$$

where

- $x = (\xi_{j})$ is the sequence.
- finiteness of the sum is Kreyszig’s $\ell^{p}$ membership test.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — 1.2-3: membership in $\ell^{p}$ via $\sum |\xi_{j}|^{p} < \infty$.
