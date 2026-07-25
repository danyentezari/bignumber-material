# Preimage

A preimage is the set of domain elements sent into a given subset that is used in the open-set definition of continuity.

<i>

**Definition** (*Preimage*) A subset of the domain of a function,

$$
f^{-1}(Y_{subset}) \subseteq X,
$$

where the following condition applies:

- $f^{-1}(Y_{subset}) = \{x \in X : f(x) \in Y_{subset}\}$.

where

- $f : X \rightarrow Y$ is a function.
- $X$ is the domain of $f$.
- $Y$ is the codomain of $f$.
- $Y_{subset} \subseteq Y$.

</i>

## Elementary Example
### Simple

The preimage of a subset is the set of domain points sent into that subset.

$$
f : X \rightarrow Y
$$

$$
X = \{ 1,\ 2,\ 3 \},\quad Y = \{ a,\ b,\ c \}
$$

$$
f(1) = a,\quad f(2) = b,\quad f(3) = a
$$

$$
f^{-1}(\{a\}) = \{ 1,\ 3 \}
$$

where

- $f^{-1}(\{a\})$ is the preimage of $\{a\}$.
- $f$ is the function.

### General

Preimages of larger subsets collect all inputs hitting any member.

$$
X = \{ 1,\ 2,\ 3,\ 4 \},\quad Y = \{ a,\ b,\ c \}
$$

$$
f(1)=a,\ f(2)=b,\ f(3)=a,\ f(4)=c
$$

$$
f^{-1}(\{a,c\}) = \{ 1,\ 3,\ 4 \}
$$

where

- $f^{-1}(Y_{0}) = \{ x \in X : f(x) \in Y_{0} \}$.

