# Markov Chain Monte Carlo

A sampling method that is used to draw approximate samples from a target distribution by simulating a Markov chain whose long-run distribution is that target, where a Markov chain is a sequence of random variables whose next state depends only on the present state, and where a target distribution is the probability distribution one wants to sample from.

Note: Also called MCMC.

Markov property. Given the present state, the next state does not further depend on the past. This principle is used to specify how the chain moves without tracking the full history.

Transition kernel. A transition kernel assigns, from each current state, a probability measure on the next state. A transition probability is the chance of moving from one named state to another in one step. This principle is used to write the law of the chain’s updates.

The one-step transition probabilities of a discrete chain are

$$
p_{ij} = P(X_{n+1} = j \mid X_{n} = i)
$$

where

- $X_{n}$ is the state at step $n$.
- $i$ is the current state.
- $j$ is the next state.
- $p_{ij}$ is the probability of the move from $i$ to $j$.

Stationary distribution. A distribution $\pi$ is stationary when the chain started in $\pi$ keeps the same distribution at every later time. This principle is used to name the long-run law that MCMC is designed to hit.

Detailed balance. A chain is reversible with respect to $\pi$ when

$$
\pi(\{x\})\, p(x,y) = \pi(\{y\})\, p(y,x)
$$

for all states $x$ and $y$. Detailed balance is this pairwise equality of flow. This principle is used to build transition rules that leave a chosen $\pi$ invariant.

Ergodicity. For an irreducible aperiodic chain with a stationary distribution $\pi$, the $n$-step transition probabilities converge to $\pi$, and $\pi$ is unique. Irreducibility means every state can be reached from every other state. Aperiodicity means returns are not locked to a fixed cycle length. This principle is used to guarantee that long runs of the chain approximate draws from $\pi$.

Metropolis-Hastings. Start from any irreducible proposal chain on the state space, then accept or reject each proposed move so that the modified chain has the desired stationary distribution. A proposal is a candidate next state drawn from the original chain. This principle is used to turn a convenient proposal into a sampler for a chosen target.

Gibbs sampling. Update one coordinate at a time by drawing from the conditional distribution of that coordinate given all the others. A conditional distribution is the law of one variable when the remaining variables are fixed. This principle is used to sample from a joint distribution when the conditionals are available.

## Elementary Example

### Simple

A random walk on $\{1,2,3\}$ proposes a step to a neighbor. From $1$, stay or move to $2$ with equal probability. From $3$, stay or move to $2$ with equal probability. From $2$, move to $1$ or $3$ with equal probability.

$$
P = \begin{pmatrix}
\dfrac{1}{2} & \dfrac{1}{2} & 0 \\
\dfrac{1}{2} & 0 & \dfrac{1}{2} \\
0 & \dfrac{1}{2} & \dfrac{1}{2}
\end{pmatrix}
$$

where

- $P$ is the proposal transition matrix.
- rows are current states $1,2,3$.
- columns are next states $1,2,3$.

### General

Blitzstein’s Zipf target on $\{1,\ldots,M\}$ uses the same neighbor proposal inside Metropolis-Hastings so that the stationary distribution is Zipf with parameter $a>0$.

$$
P(X=k) = \dfrac{k^{-a}}{\sum_{j=1}^{M} j^{-a}}, \quad k=1,\ldots,M
$$

where

- $M$ is the number of states.
- $a$ is the Zipf parameter.
- $k$ is a state.

## Topics

1. [Preliminaries](preliminaries.html)
2. [Stationary Distribution](stationary-distribution.html)

## References

1. Klenke, A. *Probability Theory: A Comprehensive Course*. Chapter 18, §18.3, p. 398 — MCMC as simulating a chain whose law converges to $\pi$. Chapter 8, Definition 8.25 — transition kernel. Chapter 19, §19.2, p. 415 — detailed balance.
2. Billingsley, P. *Probability and Measure*. Chapter 1, §8, pp. 112, 125 — Markov property; stationary distribution; Theorem 8.6 on convergence to $\pi$.
3. Blitzstein, J. K. *Introduction to Probability*. Chapter 12, §§12.0–12.2, pp. 496–508 — MCMC overview; Metropolis-Hastings; Gibbs sampling; Example 12.1.3 Zipf simulation.
