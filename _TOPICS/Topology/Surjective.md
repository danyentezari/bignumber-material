# Surjective

A surjective mapping is a function that hits every element of its target set that is used to express that a mapping covers its codomain.

<i>

**Definition** (_Surjective_) A property of a function from a set $X$ to a set $Y$,
$F: X \rightarrow Y$, where the following condition applies:

- For every element $y$ in $Y$, there exists an element $x$ in $X$ such that $F(x) = y$.

where

- $X$ is the domain of $F$.
- $Y$ is the co-domain of $F$.
- $F(X) = Y$ is the statement that the image equals the co-domain.
- $F(X) = \{y \in Y : y = F(x) \text{ for some } x \in X\}$ is the image of $X$ under $F$.

Note:

- $F(X) = Y$ means the range of the function equals its co-domain.

</i>

## Elementary Example
### Simple

A surjective map hits every element of the codomain.

$$
F : X \rightarrow Y
$$

$$
X = \{ 1,\ 2,\ 3 \},\quad Y = \{ a,\ b \}
$$

$$
F(1) = a,\quad F(2) = b,\quad F(3) = a
$$

where

- every element of $Y$ is $F(x)$ for some $x \in X$.
- $F(X) = Y$.

### General

A projection from a product onto one factor is surjective.

$$
X = \{ 1,\ 2,\ 3 \} \times \{ a,\ b \},\quad Y = \{ 1,\ 2,\ 3 \}
$$

$$
F(n,y) = n
$$

where

- $F$ hits each of $1, 2, 3$.

