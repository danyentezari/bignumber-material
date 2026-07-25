# Injective

An injective mapping is a function that sends distinct elements to distinct values that is used to express uniqueness of solutions of mapping equations.

<i>

**Definition** (_Injective_) A property of a function from a set $X$ to a set $Y$,
$F: X \rightarrow Y$, where the following condition applies:

- For all elements $x_1$ and $x_2$ in $X$, if $F(x_1) = F(x_2)$, then $x_1 = x_2$.

where

- $F$ is a function from $X$ to $Y$.
- $X$ is the domain of $F$.
- $Y$ is the co-domain of $F$.
- $x_1, x_2$ are elements of $X$.

Note:

- the condition is logically equivalent to saying that if $x_1 \neq x_2$, then $F(x_1) \neq F(x_2)$.
- for an injective function, each element of the co-domain is the image of at most one element of the domain.

</i>

## Elementary Example
### Simple

An injective map sends distinct inputs to distinct outputs.

$$
F : X \rightarrow Y
$$

$$
X = \{ 1,\ 2,\ 3 \},\quad Y = \{ a,\ b,\ c,\ d \}
$$

$$
F(1) = a,\quad F(2) = b,\quad F(3) = d
$$

where

- $F$ is injective because all three values are different.
- $X$ is the domain and $Y$ is the codomain.

### General

On larger sets, injectivity still means $F(x_{1}) = F(x_{2})$ forces $x_{1} = x_{2}$.

$$
X = \{ 1,\ 2,\ 3,\ 4 \},\quad Y = \{ 10,\ 20,\ 30,\ 40,\ 50 \}
$$

$$
F(n) = 10n
$$

where

- $F(1), F(2), F(3), F(4)$ are four distinct values.

