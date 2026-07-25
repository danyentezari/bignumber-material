# Continuity

A property of a mapping under which small changes in the input produce small changes in the value that is used to ensure limits and calculus behave well.

<i>

**Definition** (_Continuity_) A property of a map between open subsets,
$f: X \rightarrow Y$, where the following conditions apply:

- The preimage of every open subset of $Y$ is an open subset of $X$.

where

- $X, Y \subseteq \mathbb{R}^n$
- $f^{-1}(U) = \{x \in X : f(x) \in U\}$
- $f^{-1} : \mathcal{P}(Y) \rightarrow \mathcal{P}(X)$ is the preimage map from subsets of $Y$ to subsets of $X$.
- $U \subseteq Y$
- $\mathcal{P}(X)$ is the power set of $X$

</i>

## Elementary Example
### Simple

A map is continuous when the preimage of every open set is open. On finite spaces, check each open set in the codomain.

$$
X = Y = \{ 1,\ 2,\ 3 \}
$$

$$
\tau = \{ \emptyset,\ \{1\},\ \{1,2\},\ X \}
$$

$$
f(1)=1,\ f(2)=1,\ f(3)=2
$$

$$
f^{-1}(\{1\}) = \{ 1,\ 2 \} \in \tau
$$

where

- $\tau$ is the topology on $X$ and on $Y$.
- $f^{-1}(\{1\})$ is open, as required.

### General

On four points with the discrete topology, every function is continuous because every subset is open.

$$
X = Y = \{ a,\ b,\ c,\ d \}
$$

$$
\tau = \mathcal{P}(X)
$$

$$
f(a)=b,\ f(b)=c,\ f(c)=d,\ f(d)=a
$$

where

- $\mathcal{P}(X)$ is the discrete topology.
- every preimage is open.

