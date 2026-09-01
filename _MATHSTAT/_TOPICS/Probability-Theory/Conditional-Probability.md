# Conditional Probability

For events $A$ and $B$ with $P(B)>0$, the conditional probability of $A$ given $B$ is

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
$$

where

- $A$ and $B$ are events in the sample space.
- $P(A\cap B)$ is the joint probability of $A$ and $B$.
- $P(B)$ is the probability of $B$.
- $P(A\mid B)$ is the conditional probability of $A$ given $B$.

The multiplication rule is

$$
P(A\cap B)=P(A\mid B)P(B)=P(B\mid A)P(A).
$$

The law of total probability states that if $\{B_i\}$ is a partition of the sample space, then

$$
P(A)=\sum_i P(A\mid B_i)P(B_i).
$$

## Problems

- Obtain $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$ when $P(B)>0$.
- Obtain $P(A\cap B)=P(A\mid B)P(B)$.
- Obtain $P(A)=\sum_i P(A\mid B_i)P(B_i)$ for a countable partition $\{B_i\}$.
- Obtain $P(A_1\cap\cdots\cap A_n)=P(A_1)\prod_{i=2}^n P(A_i\mid A_1\cap\cdots\cap A_{i-1})$.
- Obtain $P(A\cap B\mid C)=P(A\mid C)P(B\mid C)$ when $A$ and $B$ are conditionally independent given $C$.
- Obtain $P(A^c\mid B)=1-P(A\mid B)$ when $P(B)>0$.
- Obtain $P(A\cup C\mid B)=P(A\mid B)+P(C\mid B)-P(A\cap C\mid B)$ when $P(B)>0$.

<!--
Conditional probability. For events $A$ and $B$ with $P(B)>0$, $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$. This principle is used to restrict probability to outcomes contained in the conditioning event.

Multiplication rule. Conditional probability gives $P(A\cap B)=P(A\mid B)P(B)$. This principle is used to express an intersection probability through a conditional probability and the probability of the conditioning event.

Law of total probability. For a countable partition $\{B_i\}$, $P(A)=\sum_i P(A\mid B_i)P(B_i)$. This principle is used to decompose an unconditional probability into conditional probabilities over mutually exclusive exhaustive events.

Chain rule. The probability of an intersection can be factored into successive conditional probabilities. This principle is used to express joint probabilities of several events through probabilities conditioned on preceding events.

Conditional independence. Events $A$ and $B$ are conditionally independent given $C$ when $P(A\cap B\mid C)=P(A\mid C)P(B\mid C)$. This principle is used to express independence after the information represented by $C$ is known.

Conditional probability measure. For fixed $B$ with $P(B)>0$, the mapping $A\mapsto P(A\mid B)$ satisfies the probability axioms. This principle is used to treat conditioning as a probability measure on the same event space.

## Problems

- Obtain $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$ when $P(B)>0$.
- Obtain $P(A\cap B)=P(A\mid B)P(B)$.
- Obtain $P(A)=\sum_i P(A\mid B_i)P(B_i)$ for a countable partition $\{B_i\}$.
- Obtain $P(A_1\cap\cdots\cap A_n)=P(A_1)\prod_{i=2}^n P(A_i\mid A_1\cap\cdots\cap A_{i-1})$.
- Obtain $P(A\cap B\mid C)=P(A\mid C)P(B\mid C)$ when $A$ and $B$ are conditionally independent given $C$.
- Obtain $P(A^c\mid B)=1-P(A\mid B)$ when $P(B)>0$.
- Obtain $P(A\cup C\mid B)=P(A\mid B)+P(C\mid B)-P(A\cap C\mid B)$ when $P(B)>0$.

## Textbooks

- Patrick Billingsley, Probability and Measure, Chapter 4, Probability Measures.
- Rick Durrett, Probability: Theory and Examples, Chapter 1, Measure Theory.
- William Feller, An Introduction to Probability Theory and Its Applications, Volume I, Chapter 5, Conditional Probability and Stochastic Independence.
- Geoffrey Grimmett and David Stirzaker, Probability and Random Processes, Chapter 1, Events and Their Probabilities.
- Sheldon Ross, A First Course in Probability, Chapter 3, Conditional Probability and Conditional Independence.
-->
