# Stationary Distribution

A probability distribution that is used to name the long-run law of a Markov chain when that law does not change from one step to the next, where a Markov chain is a sequence of random variables whose next state depends only on the present state, and where a long-run law is the probability distribution of the state after many transitions.

Note: Also called invariant distribution. Also called equilibrium distribution. Also called steady-state distribution.

Global balance. A distribution $\pi$ is stationary when the probability of each state after one step equals the same probability before the step. This principle is used to write equations that $\pi$ must solve.

The global balance equations are

$$
\pi_j
=
\sum_{i \in S}
\pi_i
p_{ij},
\qquad
j \in S
$$

where

- $S$ is the discrete state space.
- $i$ is a current state.
- $j$ is a next state.
- $\pi_i$ is the stationary probability of state $i$.
- $\pi_j$ is the stationary probability of state $j$.
- $p_{ij}$ is the one-step transition probability from $i$ to $j$.

In matrix form,

$$
\pi P = \pi
$$

where

- $\pi$ is the row vector of stationary probabilities.
- $P$ is the one-step transition matrix.

Invariance under the initial law. If the chain starts with law $\pi$, then the law of the state at every later time is still $\pi$. This principle is used to justify calling $\pi$ stationary.

Normalization. A stationary distribution is a probability distribution, so its entries are nonnegative and sum to one. This principle is used to select a valid solution among vectors that satisfy balance.

Limiting distribution. For an irreducible aperiodic chain that has a stationary distribution $\pi$, the $n$-step transition probabilities converge to $\pi$ from every start. Irreducibility means every state can be reached from every other state. Aperiodicity means returns are not locked to a fixed cycle length. This principle is used to connect the algebraic balance equations to long-run simulation.

Uniqueness under irreducibility. On a finite irreducible chain, a stationary distribution exists and is unique and strictly positive. On a countably infinite irreducible chain, a stationary distribution exists if and only if the chain is positive recurrent. Positive recurrent means every state has a finite mean return time. This principle is used to decide when MCMC can target a unique long-run law.

Detailed balance. If $\pi_i p_{ij} = \pi_j p_{ji}$ for all states $i$ and $j$, then $\pi$ is automatically stationary. This principle is used to construct transition rules that leave a chosen target invariant.

<!--
## Elementary Example

### Simple

For a two-state chain with

$$
P
=
\begin{pmatrix}
1-a & a \\
b & 1-b
\end{pmatrix},
\qquad
0 < a,b < 1,
$$

the unique stationary distribution is

$$
\pi
=
\left(
\frac{b}{a+b},
\frac{a}{a+b}
\right).
$$

where

- $a$ is the probability of leaving state $1$ for state $2$.
- $b$ is the probability of leaving state $2$ for state $1$.

### General

Billingsley’s Theorem 8.6: if an irreducible aperiodic chain admits a stationary distribution $\pi$, then

$$
\lim_{n \to \infty} p_{ij}^{(n)} = \pi_j
$$

for all states $i$ and $j$, and $\pi$ is unique.
-->

# References

1. Billingsley, P. *Probability and Measure*. Chapter 1, §8, p. 125 — definition of a stationary distribution via (8.30); Theorem 8.6 on convergence to $\pi$.
2. Rosenthal, J. S. *A First Look at Rigorous Probability Theory*. §8.3, p. 90 — invariance of the initial law under one step.
3. Ash, R. B. *Basic Probability Theory*. §7.5, p. 236 — stationarity of the state distribution sequence.
4. Tijms, H. — inflow-outflow reading of the balance equations as equal average rates into and out of a state.
5. Klenke, A. *Probability Theory: A Comprehensive Course*. Chapter 19, §19.2, p. 415 — detailed balance implies stationarity.
