# State Space

A set that is used to name every possible value of a Markov chain, where a Markov chain is a sequence of random variables whose next state depends only on the present state, and where a state is one admissible value of that sequence.

Note: Also called phase space.

Discrete state space. When the set of states is finite or countably infinite, each state can be listed and assigned a probability. This principle is used to write one-step moves as a transition matrix.

Billingsley introduces a discrete chain by taking a finite or countable set $S$ as the common range of the variables $X_0,X_1,\ldots$, calling $S$ the state space of the process.

Continuous state space. When the set of states is uncountable, singletons may have probability zero, so moves are described by probabilities of measurable sets. This principle is used to replace a transition matrix by a transition kernel.

Standard notation. Authors write $S$ or $I$ for a discrete state space and $E$ for a general Polish state space with Borel $\sigma$-algebra $\mathcal{B}(E)$. A state is an element $i \in S$ or $x \in E$. This principle is used to read textbook formulas without changing symbols.

Transition matrix. On a discrete state space, the one-step dynamics are a matrix $P=(p_{ij})_{i,j \in S}$ with

$$
p_{ij}
=
P(X_{n+1}=j \mid X_n=i)
$$

and

$$
\sum_{j \in S} p_{ij} = 1
$$

for each $i$. This principle is used to compute the law of the next state from the current state.

where

- $S$ is the discrete state space.
- $i$ is the current state.
- $j$ is the next state.
- $p_{ij}$ is the one-step transition probability from $i$ to $j$.
- $P$ is the transition matrix.

Transition kernel. On a general state space $(E,\mathcal{E})$, the one-step dynamics are a kernel $\kappa(x,A)$ such that $A \mapsto \kappa(x,A)$ is a probability measure for each $x$ and $x \mapsto \kappa(x,A)$ is measurable for each measurable $A$. This principle is used to specify

$$
\kappa(x,A)
=
P(X_{n+1} \in A \mid X_n = x).
$$

where

- $E$ is the general state space.
- $x$ is the current state.
- $A$ is a measurable subset of $E$.
- $\kappa(x,A)$ is the probability of moving from $x$ into $A$.

<!--
## Elementary Example

### Simple

For the three-state random walk on $S=\{1,2,3\}$, the state space is exactly those three integers, and every $X_n$ takes a value in $S$.

### General

Blitzstein: the set of possible values of the $X_n$ is the state space, while the index $n$ records the evolution of the process over time.
-->

# References

1. Billingsley, P. *Probability and Measure*. Chapter 1, §8, p. 111 — definition of the state space $S$ and transition probabilities $p_{ij}$.
2. Blitzstein, J. K. *Introduction to Probability*. Chapter 11, §11.1, p. 459 — state space as the set of possible values of $X_n$.
3. Pfeiffer, P. E. *Concepts of Probability Theory*. Chapter 7, §7-2, p. 353 — state space as the discrete set of system states between transitions.
4. Rosenthal, J. S. *A First Look at Rigorous Probability Theory*. §15.2, p. 179 — general state space with transition probabilities $P(x,A)$.
5. Klenke, A. *Probability Theory: A Comprehensive Course*. §17.1, p. 351 — Polish state space $E$ with Borel $\sigma$-algebra.
