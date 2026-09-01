# Stationary Distribution

A distribution is stationary if it is unchanged after a transition matrix is applied to it.

Global balance. A distribution $\pi$ is stationary when the probability of each state after one step equals the same probability before the step. This principle is used to write equations that $\pi$ must solve.

<i>

**definition [d]** (*Global Balance Equations = Full Balance Equations*) 

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

</i>

# References

1. Billingsley, P. *Probability and Measure*. Chapter 1, §8, p. 125 — definition of a stationary distribution via (8.30); Theorem 8.6 on convergence to $\pi$.
2. Rosenthal, J. S. *A First Look at Rigorous Probability Theory*. §8.3, p. 90 — invariance of the initial law under one step.
3. Ash, R. B. *Basic Probability Theory*. §7.5, p. 236 — stationarity of the state distribution sequence.
4. Tijms, H. — inflow-outflow reading of the balance equations as equal average rates into and out of a state.
5. Klenke, A. *Probability Theory: A Comprehensive Course*. Chapter 19, §19.2, p. 415 — detailed balance implies stationarity.
