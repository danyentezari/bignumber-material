# Bayes Theorem and Conditional Probability


Frequentist statistics treats parameters as fixed and probabilities as long-run frequencies of repeated data.

Bayesian statistics treats unknown parameters and hypotheses probabilistically, combining prior information with observed data to produce posterior probabilities.

Fundamentally:

Frequentist: $P(\text{data}\mid\text{hypothesis})$

Bayesian: $P(\text{hypothesis}\mid\text{data})$

<i>

**definition [d]** (*Bayes Theorem*) 

The *bayesian theorem* is given by
$$ P(A_i | B)  = \frac{P(A_i) \times P(B|A_i)}{ \sum_{i=k}^{n} P(B|A_i) } $$
where 

- $A_i$ is a given a-priori event
- $B$ is the a-posteriori event

</i>

## Problems

- Obtain $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$ when $P(B)>0$.
- Obtain $P(A\cap B)=P(A\mid B)P(B)=P(B\mid A)P(A)$.
- Obtain $P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$ when the required probabilities are positive.
- Obtain $P(A)=\sum_i P(A\mid B_i)P(B_i)$ from a partition $\{B_i\}$.
- Obtain $P(B_i\mid A)$ from $P(A\mid B_i)$, $P(B_i)$, and a partition $\{B_i\}$.
- Obtain the chain factorization $P(A_1\cap\cdots\cap A_n)=P(A_1)\prod_{i=2}^n P(A_i\mid A_1\cap\cdots\cap A_{i-1})$.
- Establish $P(A\cap B\mid C)=P(A\mid C)P(B\mid C)$ under conditional independence given $C$.


<!--
Conditional probability. For events $A$ and $B$ with $P(B)>0$, the conditional probability of $A$ given $B$ is $\frac{P(A\cap B)}{P(B)}$. This principle is used to restrict probabilities to outcomes consistent with known information.

Multiplication rule. Conditional probability gives $P(A\cap B)=P(A\mid B)P(B)$. This principle is used to express joint probabilities as products of conditional and marginal probabilities.

Bayes theorem. For events of positive probability, $P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$. This principle is used to reverse the direction of conditioning between two events.

Law of total probability. If $\{B_i\}$ forms a partition, then $P(A)=\sum_i P(A\mid B_i)P(B_i)$. This principle is used to obtain an unconditional probability by conditioning on mutually exclusive exhaustive cases.

Bayes theorem for partitions. Given a partition $\{B_i\}$, posterior probabilities satisfy $P(B_i\mid A)=\frac{P(A\mid B_i)P(B_i)}{P(A)}$. This principle is used to redistribute probability among partition elements after conditioning on an event.

Conditional independence. Events $A$ and $B$ are conditionally independent given $C$ when $P(A\cap B\mid C)=P(A\mid C)P(B\mid C)$. This principle is used to separate probabilistic dependence after specified information is known.

## Problems

- Obtain $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$ when $P(B)>0$.
- Obtain $P(A\cap B)=P(A\mid B)P(B)=P(B\mid A)P(A)$.
- Obtain $P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$ when the required probabilities are positive.
- Obtain $P(A)=\sum_i P(A\mid B_i)P(B_i)$ from a partition $\{B_i\}$.
- Obtain $P(B_i\mid A)$ from $P(A\mid B_i)$, $P(B_i)$, and a partition $\{B_i\}$.
- Obtain the chain factorization $P(A_1\cap\cdots\cap A_n)=P(A_1)\prod_{i=2}^n P(A_i\mid A_1\cap\cdots\cap A_{i-1})$.
- Establish $P(A\cap B\mid C)=P(A\mid C)P(B\mid C)$ under conditional independence given $C$.

## Textbooks

- Patrick Billingsley, Probability and Measure, Chapter 4, Probability Measures.
- Rick Durrett, Probability: Theory and Examples, Chapter 1, Measure Theory.
- William Feller, An Introduction to Probability Theory and Its Applications, Volume I, Chapter 5, Conditional Probability and Stochastic Independence.
- Geoffrey Grimmett and David Stirzaker, Probability and Random Processes, Chapter 1, Events and Their Probabilities.
- Sheldon Ross, A First Course in Probability, Chapter 3, Conditional Probability and Independence.
-->
