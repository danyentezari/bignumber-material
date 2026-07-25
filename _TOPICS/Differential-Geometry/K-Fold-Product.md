# k-Fold Product

A Cartesian product of k copies of one set that is used as the domain of a multilinear mapping of k inputs.

<i>

**definition** (*k-Fold Product*) A set constructed by the Cartesian product of $k$ copies of a single set, $X^k$, where the following condition applies:

- The resulting set consists of all ordered $k$-tuples where

* each coordinate is an element of the original set.

where

- $k$ is a positive integer representing the number of repetitions.
- $X$ is the underlying set.
- $X^k$ denotes the $k$-fold Cartesian product $X \times \dots \times X$.

Note:

- $X$ may be a topological space.
- $X$ may be a vector space.
- $X^k$ is also written $V^k$.

</i>

## Elementary Example
### Simple

The $2$-fold product is the Cartesian product of two copies of one set.

$$
V = \{ a,\ b,\ c \}
$$

$$
V^{2} = V \times V
$$

$$
(a,b),\ (b,a),\ (a,c) \in V^{2}
$$

where

- $V^{2}$ is the $2$-fold product.
- $k = 2$ is the number of factors.

### General

The $3$-fold product $V^{3}$ is the set of ordered triples from $V$.

$$
V = \{ a,\ b,\ c \}
$$

$$
V^{3} = V \times V \times V
$$

$$
(a,b,c),\ (c,b,a),\ (a,a,b) \in V^{3}
$$

where

- $V^{3}$ is the domain of a $3$-linear map on $V$.
