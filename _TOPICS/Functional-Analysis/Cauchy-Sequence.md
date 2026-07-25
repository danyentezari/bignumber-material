# Cauchy Sequence

A sequence of elements whose mutual distances tend to zero that is used to test for a limit without first naming that limit.

Note: Also called fundamental sequence.

<i>

**definition [d]** (*Cauchy Sequence*) From Kreyszig Definition 1.4-3: a sequence $(x_{n})$ in a metric space $X = (X,d)$ is said to be Cauchy if for every $\epsilon > 0$ there is an $N = N(\epsilon)$ such that

- $d(x_{m}, x_{n}) < \epsilon$

for every $m, n > N$.

where

- $X = (X,d)$ is a metric space.
- $(x_{n})$ is a sequence in $X$.
- $\epsilon > 0$ is a real number.
- $N = N(\epsilon)$ is a natural number depending on $\epsilon$.
- $d$ is the metric on $X$.

</i>

## Elementary Example
### Simple

A Cauchy sequence has terms that eventually lie close to each other. On the line, the sequence $1/n$ is Cauchy.

$$
X = \mathbb{R},\quad d(x,y) = |x - y|
$$

$$
x_{n} = \dfrac{1}{n},\quad n \in \{ 1,\ 2,\ 3,\ 4,\ 5 \}
$$

$$
d(x_{4},x_{5}) = \left|\dfrac{1}{4} - \dfrac{1}{5}\right| = \dfrac{1}{20}
$$

where

- $(x_{n})$ is the sequence.
- $d$ is the metric on $X$.

### General

In $\mathbb{R}^{3}$ with the Euclidean metric, $x_{n} = (1/n, 1/n, 1/n)$ is Cauchy because all pairwise distances tend to zero.

$$
d(x_{m},x_{n}) = \sqrt{3}\,\left|\dfrac{1}{m} - \dfrac{1}{n}\right|
$$

where

- $x_{n} \in \mathbb{R}^{3}$.
- for every $\epsilon > 0$ there is $N$ such that $m,n > N$ implies $d(x_{m},x_{n}) < \epsilon$.


## References

1. Kreyszig, E. *Introductory Functional Analysis with Applications*. Wiley, 1989. — Definition 1.4-3 (Cauchy sequence, completeness).
