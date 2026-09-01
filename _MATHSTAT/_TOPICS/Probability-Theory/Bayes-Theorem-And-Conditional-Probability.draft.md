# Bayes Theorem and Conditional Probability

A pair of probability rules that is used to revise the probability of one event after another event is observed, where an event is a measurable subset of the sample space, and where a sample space is the set of all outcomes under consideration.

Note: Also called Bayes’ rule for the inversion formula.

Conditional probability. For events $A$ and $B$ with $P(B)>0$, the conditional probability of $A$ given $B$ is the joint probability of both events scaled by the probability of $B$. This principle is used to measure the chance of $A$ once it is known that $B$ has occurred.

The definition of conditional probability is

$$
P(A\mid B)
=
\frac{P(A\cap B)}{P(B)}.
$$

where

- $\Omega$ is the sample space.
- $\mathcal{F}$ is the $\sigma$-algebra of events on $\Omega$.
- $A$ and $B$ are events in $\mathcal{F}$.
- $A\cap B$ is the event that both $A$ and $B$ occur.
- $P(A\cap B)$ is the joint probability of $A$ and $B$.
- $P(B)$ is the unconditional probability of $B$.
- $P(A\mid B)$ is the conditional probability of $A$ given $B$.

Multiplication rule. The probability of a joint occurrence equals the probability of the first event times the conditional probability of the second given the first. This principle is used to factor joint events into a sequence of conditionals.

$$
P(A\cap B)
=
P(B)\,P(A\mid B)
=
P(A)\,P(B\mid A).
$$

For events $A_1,\ldots,A_n$ with $P(A_1\cap\cdots\cap A_{n-1})>0$, the chain rule is

$$
P(A_1\cap\cdots\cap A_n)
=
P(A_1)\,P(A_2\mid A_1)\cdots P(A_n\mid A_1\cap\cdots\cap A_{n-1}).
$$

Law of total probability. If $A_1,\ldots,A_n$ partition the sample space and each has positive probability, then

$$
P(B)
=
\sum_{i=1}^{n}
P(B\mid A_i)\,P(A_i).
$$

where

- $A_1,\ldots,A_n$ are pairwise disjoint events whose union is the sample space.
- $B$ is an event whose unconditional probability is being expanded.
- $P(A_i)$ is the prior weight of cell $A_i$.
- $P(B\mid A_i)$ is the conditional probability of $B$ given $A_i$.

This principle is used to write a marginal probability as a weighted average of conditionals.

Bayes’ theorem. Bayes’ theorem inverts a conditional probability, expressing $P(A\mid B)$ in terms of $P(B\mid A)$ and the prior of $A$. This principle is used to update a prior assessment into a posterior assessment after evidence is observed.

The simple form is

$$
P(A\mid B)
=
\frac{P(B\mid A)\,P(A)}{P(B)}.
$$

where

- $P(A)$ is the prior probability of $A$.
- $P(B\mid A)$ is the likelihood of $B$ given $A$.
- $P(B)$ is the marginal probability of the evidence $B$.
- $P(A\mid B)$ is the posterior probability of $A$ given $B$.

Partition form. When countable pairwise disjoint events $(B_i)_{i\in I}$ cover the sample space,

$$
P(B_k\mid A)
=
\frac{P(A\mid B_k)\,P(B_k)}
{\sum_{i\in I} P(A\mid B_i)\,P(B_i)}.
$$

where

- $I$ is a countable index set.
- $(B_i)_{i\in I}$ is a partition of the sample space.
- $B_k$ is one hypothesis in the partition.
- $A$ is the observed evidence with $P(A)>0$.
- $P(B_k)$ is the prior probability of $B_k$.
- $P(A\mid B_k)$ is the likelihood of $A$ given $B_k$.
- $\sum_{i\in I} P(A\mid B_i)\,P(B_i)$ equals $P(A)$ by the law of total probability.
- $P(B_k\mid A)$ is the posterior probability of $B_k$ given $A$.

Derivation from conditional probability. Because $A\cap B=B\cap A$, the two product expansions of the joint probability are equal, and dividing by $P(B)$ yields Bayes’ rule. Expanding $P(B)$ by the law of total probability recovers the partition form. This principle is used to see Bayes’ theorem as algebra on conditional probability rather than a new axiom.

<!--
## Elementary Example

### Simple

Florescu and Tudor’s two-urn selection: two urns are equally likely, $P(\mathrm{Red}\mid\mathrm{Urn\,1})=\frac12$, and $P(\mathrm{Red}\mid\mathrm{Urn\,2})=\frac{3}{10}$. After observing red,

$$
P(\mathrm{Red})
=
\frac12\cdot\frac12+\frac{3}{10}\cdot\frac12
=
\frac25,
$$

$$
P(\mathrm{Urn\,1}\mid\mathrm{Red})
=
\frac{\frac12\cdot\frac12}{\frac25}
=
\frac58.
$$

### General

Klenke’s inspection setting: a test detects a defective device with probability $0.95$, has false-positive probability $0.10$, and the defect prevalence is $0.02$. Then

$$
P(B\mid A)
=
\frac{0.95\cdot 0.02}{0.95\cdot 0.02+0.10\cdot 0.98}
\approx
0.162.
$$
-->

# References

1. Gut, A. *Probability: A Graduate Course*. Chapter 1, Definition 4.2, p. 19 — definition of conditional probability.
2. Klenke, A. *Probability Theory: A Comprehensive Course*. Chapter 8, §8.1, Definition 8.2, pp. 169–170 — conditional probability given $B$; Theorem 8.7 — Bayes’ formula for a countable partition.
3. Billingsley, P. *Probability and Measure*. §33, p. 428 — interpretive meaning of $P(A\mid B)$ after learning that the outcome lies in $B$.
4. Gnedenko, B. V. and Khinchin, A. Ya. *An Elementary Introduction to the Theory of Probability*. Chapter 3, §3.1, p. 28 — multiplication rule; §4.3, Equation 4.10, p. 38 — Bayes’ formula for hypotheses.
5. Pfeiffer, P. E. *Concepts of Probability Theory*. §2-5, p. 39 — chain-rule product formula.
6. Tijms, H. *Understanding Probability*. §8.1.1, p. 265 — product rule for several events.
7. Blitzstein, J. K. *Introduction to Probability*. Chapter 2, Theorem 2.3.3, p. 53 — Bayes’ rule; Theorem 2.3.6, p. 55 — law of total probability.
8. Ash, R. B. *Basic Probability Theory*. §1.6, p. 36 — Bayes’ theorem and a posteriori probability.
9. Ash, R. B. and Doléans-Dade, C. A. *Probability & Measure Theory*. Chapter 1, §1.3, p. 7 — total probability as a weighted average of conditionals.
10. Florescu, I. and Tudor, C. A. *Handbook of Probability*. Chapter 2, Examples 2.7 and 2.9, pp. 34–35 — two-urn Bayes calculation.
