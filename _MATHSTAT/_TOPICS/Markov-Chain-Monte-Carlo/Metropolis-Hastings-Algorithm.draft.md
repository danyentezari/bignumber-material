# Metropolis-Hastings Algorithm

A sampling method that is used to build a Markov chain whose stationary distribution is a chosen target by proposing moves and then accepting or rejecting them, where a Markov chain is a sequence of random variables whose next state depends only on the present state, and where a target is the probability distribution one wants to sample from.

Note: Also called the Metropolis-Hastings sampler.

Proposal. Start from any irreducible chain on the state space and draw a candidate next state from that chain. This principle is used to generate a convenient move without already knowing how to sample from the target.

Accept-reject. Accept the candidate with a computed probability and otherwise stay at the current state. This principle is used to modify the proposal chain so that the target becomes stationary.

Acceptance probability. For a target $\pi$ and proposal kernel $q$, the acceptance probability of moving from $x$ to $y$ is

$$
\alpha(x,y)
=
\min
\left(
1,
\frac{\pi(y)\,q(x\mid y)}{\pi(x)\,q(y\mid x)}
\right).
$$

where

- $x$ is the current state.
- $y$ is the proposed state.
- $\pi$ is the target probability mass function or density.
- $q(y\mid x)$ is the proposal probability of $y$ given $x$.
- $q(x\mid y)$ is the reverse proposal probability of $x$ given $y$.
- $\alpha(x,y)$ is the probability of accepting the move from $x$ to $y$.

In discrete notation with target masses $s_i$ and proposal transitions $p_{ij}$,

$$
\alpha_{ij}
=
\min
\left(
1,
\frac{s_j\,p_{ji}}{s_i\,p_{ij}}
\right).
$$

where

- $i$ is the current state.
- $j$ is the proposed state.
- $s_i$ is the target mass at $i$.
- $p_{ij}$ is the proposal transition probability from $i$ to $j$.

Normalizing constant cancellation. If $\pi$ is known only up to a multiplicative constant, that constant cancels in the acceptance ratio. This principle is used to run the algorithm when the partition function is unavailable.

Symmetric proposal. When $q(y\mid x)=q(x\mid y)$ for all states, the acceptance probability reduces to

$$
\alpha(x,y)
=
\min
\left(
1,
\frac{\pi(y)}{\pi(x)}
\right).
$$

This principle is used to recover the classical Metropolis rule.

Detailed balance. The accept-reject correction enforces $\pi(x)q_{\mathrm{MH}}(x,y)=\pi(y)q_{\mathrm{MH}}(y,x)$, so $\pi$ is stationary for the Metropolis-Hastings chain. This principle is used to prove that long runs target $\pi$.

Ergodicity. If the proposal chain is irreducible and aperiodic, the Metropolis-Hastings chain converges to the unique stationary distribution $\pi$. This principle is used to justify approximate sampling from long trajectories.

<!--
## Elementary Example

### Simple

Initialize at a state $x_0$ with $\pi(x_0)>0$. At state $x$, propose $y\sim q(\,\cdot\mid x)$, draw $U\sim\mathrm{Uniform}(0,1)$, set the next state to $y$ if $U\le\alpha(x,y)$ and to $x$ otherwise.

### General

Blitzstein’s Zipf target on $\{1,\ldots,M\}$ uses a neighbor random-walk proposal inside Metropolis-Hastings. From an interior state, move one step left or right with equal probability. Accept a move from $i$ to $j$ with probability $\min(i^{a}/j^{a},1)$. The Zipf normalizing sum is not needed to run the chain.

$$
P(X=k)
=
\frac{k^{-a}}{\sum_{j=1}^{M} j^{-a}},
\qquad
k=1,\ldots,M
$$

where

- $M$ is the number of states.
- $a$ is the Zipf parameter.
- $k$ is a state.
-->

# References

1. Blitzstein, J. K. *Introduction to Probability*. Chapter 12, §12.1, p. 496 — Metropolis-Hastings as modifying any irreducible proposal; Algorithm 12.1.1, p. 497 — acceptance probability $\alpha_{ij}$; Example 12.1.3, pp. 498–499 — Zipf simulation.
2. Tijms, H. *Understanding Probability*. §15.5.3, pp. 497–499 — sampling when the normalizing constant is unavailable; continuous form of $\alpha(x,y)$.
3. Klenke, A. *Probability Theory: A Comprehensive Course*. Chapter 19, §19.2, p. 415 — detailed balance and reversibility.
4. Billingsley, P. *Probability and Measure*. Chapter 1, §8, Theorem 8.6, p. 125 — convergence to a unique stationary distribution for irreducible aperiodic chains.
