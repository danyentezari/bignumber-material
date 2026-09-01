# Bayes Theorem

Frequentist statistics treats parameters as fixed and probabilities as long-run frequencies of repeated data.

Bayesian statistics treats unknown parameters and hypotheses probabilistically, combining prior information with observed data to produce posterior probabilities.

Fundamentally, it goes like this:

Frequentist: $P(\text{data}\mid\text{hypothesis})$

Bayesian: $P(\text{hypothesis}\mid\text{data})$

Bayes theorem is given by

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.
$$

For a partition $\{B_i\}$,

$$
P(B_k\mid A)=\frac{P(A\mid B_k)P(B_k)}{\sum_i P(A\mid B_i)P(B_i)}.
$$

where

- $P(A)$ is the prior probability of $A$.
- $P(B\mid A)$ is the likelihood of $B$ given $A$.
- $P(B)$ is the marginal probability of $B$.
- $P(A\mid B)$ is the posterior probability of $A$ given $B$.
- $B_k$ is one cell of the partition.
- $P(B_k)$ is the prior probability of $B_k$.
- $P(A\mid B_k)$ is the likelihood of $A$ given $B_k$.

<!--
Bayes theorem. For events $A$ and $B$ with positive required probabilities, $P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$. This principle is used to reverse the direction of conditioning between two events.

Inversion of conditioning. Bayes theorem converts a conditional probability in one direction into the corresponding conditional probability in the reverse direction. This principle is used to obtain $P(A\mid B)$ when $P(B\mid A)$ and the marginal probabilities are known.

Partition form. For a partition $\{B_i\}$, Bayes theorem gives $P(B_k\mid A)$ from the conditional probabilities and prior probabilities of the partition elements. This principle is used to redistribute probability among mutually exclusive exhaustive events after conditioning on $A$.

Prior probability. The prior probability $P(B_k)$ represents the probability assigned to $B_k$ before conditioning on $A$. This principle is used to provide the initial probability entering Bayes theorem.

Posterior probability. The posterior probability $P(B_k\mid A)$ represents the probability of $B_k$ after conditioning on $A$. This principle is used to express the probability resulting from the Bayesian inversion.

Normalization. The denominator in the partition form is $P(A)=\sum_i P(A\mid B_i)P(B_i)$. This principle is used to normalize the posterior probabilities so that their sum across the partition equals one.

## Problems

- Obtain $P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$ when the required probabilities are positive.
- Obtain $P(B_k\mid A)$ from $P(A\mid B_k)$, $P(B_k)$, and a partition $\{B_i\}$.
- Obtain $P(A)=\sum_i P(A\mid B_i)P(B_i)$ as the normalizing denominator in the partition form of Bayes theorem.
- Recover $P(B\mid A)$ from $P(A\mid B)$, $P(A)$, and $P(B)$.
- Obtain posterior odds from prior odds through $\frac{P(B_2\mid A)}{P(B_1\mid A)}=\frac{P(A\mid B_2)}{P(A\mid B_1)}\frac{P(B_2)}{P(B_1)}$.
- Show that $\sum_i P(B_i\mid A)=1$ for a partition $\{B_i\}$ when $P(A)>0$.
- Obtain successive posterior probabilities when information is incorporated through repeated conditioning.

## Textbooks

- Patrick Billingsley, Probability and Measure, Chapter 4, Probability Measures.
- Rick Durrett, Probability: Theory and Examples, Chapter 1, Measure Theory.
- William Feller, An Introduction to Probability Theory and Its Applications, Volume I, Chapter 5, Conditional Probability and Stochastic Independence.
- Geoffrey Grimmett and David Stirzaker, Probability and Random Processes, Chapter 1, Events and Their Probabilities.
- Sheldon Ross, A First Course in Probability, Chapter 3, Conditional Probability and Conditional Independence.
-->
