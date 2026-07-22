# Preimages and Inverse Functions

<i>

**Definition** (*Inverse Function*) A function from the codomain of a function to its domain,

$$
f^{-1} : Y \rightarrow X,
$$

where

* the following condition applies:

- $f^{-1}(y) = x \iff f(x) = y$.

where

- $f : X \rightarrow Y$ is a one-to-one and onto function.
- $X$ is the domain of $f$.
- $Y$ is the codomain of $f$.
- $x \in X, y \in Y$.

</i>

<i>

**Definition** (*Preimage*) A subset of the domain of a function,

$$
f^{-1}(Y_{subset}) \subseteq X,
$$

where

* the following condition applies:

- $f^{-1}(Y_{subset}) = \{x \in X : f(x) \in Y_{subset}\}$.

where

- $f : X \rightarrow Y$ is a function.
- $X$ is the domain of $f$.
- $Y$ is the codomain of $f$.
- $Y_{subset} \subseteq Y$.

</i>



<i>

**Definition** (_Continuity_) A property of a map between open subsets,
$f: X \rightarrow Y$, where

* the following conditions apply:

- The preimage of every open subset of $Y$ is an open subset of $X$.

where

- $X, Y \subseteq \mathbb{R}^n$
- $f^{-1}(U) = \{x \in X : f(x) \in U\}$
- $f^{-1} : \mathcal{P}(Y) \rightarrow \mathcal{P}(X)$ is the preimage map from subsets of $Y$ to subsets of $X$.
- $U \subseteq Y$
- $\mathcal{P}(X)$ is the power set of $X$

</i>

<i>

**Definition** (_Surjective_) A property of a function from a set $X$ to a set $Y$,
$F: X \rightarrow Y$, where

* the following condition applies:

- For every element $y$ in $Y$, there exists an element $x$ in $X$ such that $F(x) = y$.

where

- $X$ is the domain of $F$
- $Y$ is the co-domain of $F$
- $F(X) = Y$ (the range of the function is equal to its co-domain).
- $F(X) = \{y \in Y : y = F(x) \text{ for some } x \in X\}$ is the image of $X$ under $F$.

</i>

<i>

**Definition** (_Injective_) A property of a function from a set $X$ to a set $Y$,
$F: X \rightarrow Y$, where

* the following condition applies:

- For all elements $x_1$ and $x_2$ in $X$, if $F(x_1) = F(x_2)$, then $x_1 = x_2$.

where

- $X$ is the domain of $F$.
- $Y$ is the co-domain of $F$.
- $x_1, x_2$ are elements of $X$.

Note:

- The condition is logically equivalent to saying that if $x_1 \neq x_2$, then $F(x_1) \neq F(x_2)$.
- For an injective function, each element of the co-domain is the image of at most one element of the domain.

</i>

<i>

**Definition** (_Bijective_) A property of a function from a set $X$ to a set $Y$,
$F: X \rightarrow Y$, where

* the following conditions apply:

- The function $F$ is injective
- The function $F$ is surjective

where

- $X$ is the domain of $F$.
- $Y$ is the co-domain of $F$

</i>
