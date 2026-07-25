# P-Summable Sequence

A sequence of values whose elements determine a finite norm defined by a parameter that is used to identify members belonging to a matching set of sequences.

<i>

**definition [d]** (*$p$-Summable Sequence*) From Kreyszig 1.2-3: a sequence $x = (\xi_{j}) = (\xi_{1}, \xi_{2}, \ldots)$ of numbers such that $|\xi_{1}|^{p} + |\xi_{2}|^{p} + \cdots$ converges, that is

- $\displaystyle\sum_{j=1}^{\infty} |\xi_{j}|^{p} < \infty$ \quad ($p \geq 1$, fixed).

where

- $x = (\xi_{j})$ is the sequence.
- $p \geq 1$ is a fixed real number.

</i>

## Elementary Example
### Simple

A $p$-summable sequence is a sequence with $\sum |\xi_{j}|^{p} < \infty$. For $p = 1$ take three terms.

$$
x = (2,-1,4),\quad p = 1
$$

$$
\sum_{j=1}^{3} |\xi_{j}| = 7 < \infty
$$

where

- $x = (\xi_{j})$ is the $p$-summable sequence.

### General

For $p = 2$, zero-pad a four-term list to an infinite sequence in $\ell^{2}$.

$$
x = (1,1,1,1,0,0,\ldots),\quad p = 2
$$

$$
\sum_{j=1}^{\infty} |\xi_{j}|^{2} = 4 < \infty
$$

where

- trailing zeros do not change the sum.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — 1.2-3: sequences belonging to $\ell^{p}$.
