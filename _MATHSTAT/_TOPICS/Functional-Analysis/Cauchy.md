# Cauchy

A sequence that is used to analyze convergence without first identifying a limit, where convergence is approach to a fixed element and where a sequence is an ordered collection of elements.

<!-- >
Metric-space Cauchy sequence. A sequence is Cauchy when its terms become arbitrarily close to one another after a sufficiently large index. A metric space is a set equipped with a distance function. This principle is used to test convergence using only distances between terms.

The metric-space Cauchy condition is

$$
\forall\epsilon>0,\ 
\exists N\in\mathbb{N}
\text{ such that }
m,n>N
\implies
d(x_m,x_n)<\epsilon
$$

where

- $\epsilon$ is a positive real number.
- $N$ is a natural-number threshold that depends on $\epsilon$.
- $m$ and $n$ are sequence indices beyond $N$.
- $x_m$ and $x_n$ are terms of the sequence.
- $d$ is the metric that measures distance.

Normed-space Cauchy sequence. In a normed vector space, distance is measured by the norm of the difference between two terms. A normed vector space is a vector space equipped with a function that measures vector length. This principle is used to study convergence in linear spaces.

The normed-space Cauchy condition is

$$
\forall\epsilon>0,\ 
\exists N\in\mathbb{N}
\text{ such that }
m,n>N
\implies
\|x_m-x_n\|<\epsilon
$$

where

- $\epsilon$ is a positive real number.
- $N$ is a natural-number threshold that depends on $\epsilon$.
- $m$ and $n$ are sequence indices beyond $N$.
- $x_m$ and $x_n$ are vectors in the normed space.
- $\|\cdot\|$ is the norm.

Convergent-sequence property. Every convergent sequence in a metric space is Cauchy. The triangle inequality shows that two sufficiently late terms are close because each is close to the same limit. This principle is used to establish a necessary condition for convergence.

The triangle-inequality bound is

$$
d(x_n,x_m)
\le
d(x_n,x)+d(x,x_m)
$$

where

- $d$ is the metric.
- $x_n$ and $x_m$ are terms of the sequence.
- $x$ is the limit of the sequence.

Completeness. A metric space is complete when every Cauchy sequence converges to an element of that space. This principle is used to guarantee that limits produced by approximation do not leave the space.

The completeness implication is

$$
(x_n)\text{ is Cauchy in }X
\implies
\exists x\in X
\text{ such that }
x_n\to x
$$

where

- $(x_n)$ is a sequence in the metric space $X$.
- $X$ is a complete metric space.
- $x$ is the limit of the sequence and belongs to $X$.
- $\to$ denotes convergence in the metric of $X$.

Banach and Hilbert spaces. A Banach space is a complete normed vector space. A Hilbert space is a complete inner-product space whose norm is induced by its inner product. This principle is used to guarantee convergence of Cauchy sequences in the principal spaces of functional analysis.

The Hilbert-space norm is

$$
\|x\|
=
\sqrt{\langle x,x\rangle}
$$

where

- $x$ is a vector in the Hilbert space.
- $\langle x,x\rangle$ is the inner product of $x$ with itself.
- $\|x\|$ is the norm induced by the inner product.

Cauchy-subsequence property. If a Cauchy sequence has a subsequence that converges to an element, then the entire sequence converges to that same element. A subsequence is a sequence formed by retaining terms in their original order. This principle is used to prove convergence by finding one convergent subsequence.

The subsequence condition is

$$
x_{n_i}\to x
\implies
x_n\to x
$$

where

- $(x_n)$ is a Cauchy sequence.
- $(x_{n_i})$ is a subsequence of $(x_n)$.
- $(n_i)$ is a strictly increasing sequence of natural numbers.
- $x$ is the common limit.

Concrete example. The real sequence $x_n=1/n$ is Cauchy under the absolute-value metric because sufficiently late terms are arbitrarily close. This principle is used to illustrate a Cauchy sequence that converges to zero.

The distance bound is

$$
\left|\frac{1}{n}-\frac{1}{m}\right|
\le
\frac{1}{n}+\frac{1}{m}
$$

where

- $m$ and $n$ are positive sequence indices.
- $1/m$ and $1/n$ are terms of the sequence.
- $|\cdot|$ is the absolute-value metric on $\mathbb{R}$.

<!-- -->

# References

1. Erwin Kreyszig, *Introductory Functional Analysis with Applications*, Wiley, 1989. Chapter 1, §1.4, Definition 1.4-3, p. 28 — Cauchy sequences in metric spaces.
2. Erwin Kreyszig, *Introductory Functional Analysis with Applications*, Wiley, 1989. Chapter 1, §1.4, Theorem 1.4-5, p. 29 — convergent sequences, Cauchy sequences, and completeness.
3. Erwin Kreyszig, *Introductory Functional Analysis with Applications*, Wiley, 1989. Chapter 2, §2.2, Definition 2.2-1, p. 58 — Banach spaces.
4. Erwin Kreyszig, *Introductory Functional Analysis with Applications*, Wiley, 1989. Chapter 3, §3.1, Definition 3.1-1, p. 128 — Hilbert spaces.

<!--
Cauchy criterion. A sequence $(x_n)$ is Cauchy when its terms become arbitrarily close to one another: for every $\epsilon>0$, there exists $N$ such that $\|x_n-x_m\|<\epsilon$ whenever $m,n\ge N$. This principle is used to test convergence without first knowing the limit.

Convergence implies Cauchy. Every convergent sequence in a normed space is a Cauchy sequence. This principle is used to obtain a necessary condition for convergence from the metric structure induced by the norm.

Completeness principle. A normed space is complete precisely when every Cauchy sequence converges to an element of the space. This principle is used to distinguish Banach spaces from incomplete normed spaces.

Closed subspace principle. A closed linear subspace of a Banach space is complete under the inherited norm. Conversely, a complete linear subspace of a normed space is closed. This principle is used to relate topological closedness to completeness.

Cauchy series criterion. In a Banach space, a series $\sum_{k=1}^{\infty}x_k$ converges exactly when its sequence of partial sums is Cauchy. This principle is used to reduce convergence of infinite series to estimates of finite tails.

Equivalent norm principle. Equivalent norms generate the same Cauchy sequences and therefore preserve completeness. This principle is used to show that completeness depends on the norm topology rather than a particular equivalent choice of norm.

## Problems

- Establish that every convergent sequence in a normed space is Cauchy.
- Show that a normed space is Banach exactly when every Cauchy sequence has a limit in the space.
- Establish that every closed linear subspace of a Banach space is complete.
- Show that every complete linear subspace of a normed space is closed.
- Obtain the convergence criterion for $\sum_{k=1}^{\infty}x_k$ from the Cauchy property of its partial sums.
- Show that absolute convergence of $\sum\|x_k\|$ implies convergence of $\sum x_k$ in a Banach space.
- Establish that equivalent norms have the same Cauchy sequences and preserve completeness.

## Textbooks

- Erwin Kreyszig, *Introductory Functional Analysis with Applications*, Chapter 1, sections on metric spaces, normed spaces, completeness, and Banach spaces.
- Walter Rudin, *Functional Analysis*, Chapter 1, sections on topological vector spaces, normed spaces, and completeness.
- John B. Conway, *A Course in Functional Analysis*, Chapter 1, sections on normed spaces and Banach spaces.
- George F. Simmons, *Introduction to Topology and Modern Analysis*, chapters on metric spaces and Banach spaces.
- A. N. Kolmogorov and S. V. Fomin, *Introductory Real Analysis*, chapters on metric spaces, complete spaces, and normed linear spaces.
-->
