# Gibbs Sampling

A sampling method that is used to draw approximate samples from a joint distribution by updating one coordinate at a time from its conditional distribution given the other coordinates, where a joint distribution is the law of several random variables together, and where a conditional distribution is the law of one variable when the remaining variables are fixed.

Note: Also called the heat bath algorithm.

Coordinate update. At each stage, one variable is redrawn while all other variables are held fixed. This principle is used to replace a difficult joint draw by a sequence of simpler conditional draws.

Full conditional. For a random vector $X=(X_1,\ldots,X_d)$ with target joint law $\pi$, the full conditional of coordinate $j$ is the law of $X_j$ given $X_{-j}=(X_k)_{k\neq j}$. This principle is used to name the distribution from which the next update is drawn.

Systematic scan. The coordinates are updated in a fixed cycle, each time conditioning on the newest values already drawn in that cycle. This principle is used to write a deterministic schedule for one full pass through all coordinates.

Given $x^{(n)}=(x_1^{(n)},\ldots,x_d^{(n)})$, one systematic pass draws

$$
\begin{aligned}
x_1^{(n+1)}
&\sim
\pi_1(\,\cdot\mid x_2^{(n)},\ldots,x_d^{(n)})
\\
x_2^{(n+1)}
&\sim
\pi_2(\,\cdot\mid x_1^{(n+1)},x_3^{(n)},\ldots,x_d^{(n)})
\\
&\vdots
\\
x_d^{(n+1)}
&\sim
\pi_d(\,\cdot\mid x_1^{(n+1)},\ldots,x_{d-1}^{(n+1)})
\end{aligned}
$$

where

- $d$ is the number of coordinates.
- $x^{(n)}$ is the state after $n$ full updates.
- $\pi_j(\,\cdot\mid x_{-j})$ is the full conditional of coordinate $j$.

Random scan. A coordinate index is chosen at random and only that coordinate is updated from its full conditional. This principle is used to define a single-coordinate Metropolis-Hastings proposal that is always accepted.

Metropolis-Hastings special case. When the proposal for changing only coordinate $j$ is exactly the full conditional of that coordinate, the Metropolis-Hastings acceptance probability equals one. This principle is used to prove that the random-scan Gibbs sampler has the desired stationary distribution.

Reversibility. Because detailed balance holds for each coordinate update, the Gibbs sampler is a reversible Markov chain with invariant measure $\pi$. This principle is used to guarantee that the target joint distribution is stationary for the chain.

<!--
## Elementary Example

### Simple

Blitzstein: update one variable at a time from its conditional given all the others, keeping the remaining variables fixed. This is useful when those conditionals are easy to sample.

### General

Klenke: for a state with many components $x=(x_i)_{i\in\Lambda}$, the Gibbs sampler adapts the state locally to the stationary distribution as an alternative to a Metropolis chain.
-->

# References

1. Blitzstein, J. K. *Introduction to Probability*. Chapter 12, §12.2, p. 508 — definition of Gibbs sampling; Theorem 12.2.3, p. 509 — random-scan Gibbs as Metropolis-Hastings with acceptance probability one.
2. Klenke, A. *Probability Theory: A Comprehensive Course*. §18.3, p. 403 — Gibbs sampler as heat bath; local adaptation to the invariant distribution; reversibility with invariant measure $\pi$.
3. Ghoshal, S. and van der Vaart, A. W. *Fundamentals of Nonparametric Bayesian Inference*. Appendix E, p. 619 — simulation from conditionals and the Hammersley-Clifford theorem.
