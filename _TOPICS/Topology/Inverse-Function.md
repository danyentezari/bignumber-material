# Inverse Function

An inverse function is a mapping that reverses another mapping that is used to recover inputs from outputs when a function is bijective.

<i>

**Definition** (*Inverse Function*) A function from the codomain of a function to its domain,

$$
f^{-1} : Y \rightarrow X,
$$

where the following condition applies:

- $f^{-1}(y) = x \iff f(x) = y$.

where

- $f : X \rightarrow Y$ is a one-to-one and onto function.
- $X$ is the domain of $f$.
- $Y$ is the codomain of $f$.
- $x \in X, y \in Y$.

</i>

## Elementary Example
### Simple

An inverse function reverses a bijection: $f^{-1}(y) = x$ exactly when $f(x) = y$.

$$
f : X \rightarrow Y
$$

$$
X = \{ 1,\ 2,\ 3 \},\quad Y = \{ a,\ b,\ c \}
$$

$$
f(1)=a,\ f(2)=b,\ f(3)=c
$$

$$
f^{-1}(a)=1,\ f^{-1}(b)=2,\ f^{-1}(c)=3
$$

where

- $f$ is bijective.
- $f^{-1} : Y \rightarrow X$ is the inverse function.

### General

On four points, the inverse undoes a cyclic shift.

$$
X = Y = \{ 1,\ 2,\ 3,\ 4 \}
$$

$$
f(1)=2,\ f(2)=3,\ f(3)=4,\ f(4)=1
$$

$$
f^{-1}(2)=1,\ f^{-1}(3)=2,\ f^{-1}(4)=3,\ f^{-1}(1)=4
$$

where

- $f^{-1} \circ f$ is the identity on $X$.

