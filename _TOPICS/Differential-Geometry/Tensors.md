# Tensors


<i>

**definition** (*Multilinear Function*) A function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where

* the following conditions apply for each argument $i$ ($1 \leq i \leq k$):

- $T(v_1, \dots, v_i + v_i', \dots, v_k) = T(v_1, \dots, v_i, \dots, v_k) + T(v_1, \dots, v_i', \dots, v_k)$.
- $T(v_1, \dots, av_i, \dots, v_k) = a \cdot T(v_1, \dots, v_i, \dots, v_k)$.

where

- $V$ is a vector space over $\mathbb{R}$.
- $V^k$ is the $k$-fold Cartesian product $V \times \dots \times V$.
- $k$ is a positive integer representing the number of arguments, also called the degree of the function.
- $v_1, \dots, v_k, v_i' \in V$ are vectors.
- $a \in \mathbb{R}$ is a scalar.

</i>


<i>

**definition** (*k-Tensor*) A multilinear function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where

* the following condition applies:

- The function $T$ is linear in each of its $k$ arguments.

where

- $V$ is a vector space.
- $V^k$ is the $k$-fold Cartesian product $V \times \dots \times V$.
- $k$ is a positive integer representing the degree of the tensor.
- $\mathbb{R}$ is the set of real numbers.
- $\mathcal{L}^k(V)$ (or $\mathcal{J}^k(V)$) is the vector space of all $k$-tensors on $V$.

</i>


<i>

**definition** (*Multilinear Function*) A function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where

* the following conditions apply for each argument $i$ ($1 \leq i \leq k$):

- $T(v_1, \dots, v_i + v_i', \dots, v_k) = T(v_1, \dots, v_i, \dots, v_k) + T(v_1, \dots, v_i', \dots, v_k)$
- $T(v_1, \dots, av_i, \dots, v_k) = a \cdot T(v_1, \dots, v_i, \dots, v_k)$

where

- $V$ is a vector space over $\mathbb{R}$.
- $V^k$ is the $k$-fold Cartesian product $V \times \dots \times V$.
- $k$ is a positive integer representing the number of arguments, also called the degree of the function.
- $v_1, \dots, v_k, v_i' \in V$ are vectors.
- $a \in \mathbb{R}$ is a scalar.
  
</i>


<i>

**definition** (*k-Fold Product*) A set constructed by the Cartesian product of $k$ copies of a single set, $X^k$, where

* the following condition applies:

- The resulting set consists of all ordered $k$-tuples where

* each coordinate is an element of the original set.

where

- $k$ is a positive integer representing the number of repetitions.
- $X$ is the underlying set, topological space, or vector space.
- $X^k$ (or $V^k$) denotes the $k$-fold Cartesian product $X \times \dots \times X$.

</i>


<i>

**definition** (*Cartesian Product*) A set consisting of all possible ordered combinations of elements from a collection of sets, denoted by $X \times Y$ for two sets, $X_1 \times \dots \times X_n$ for $n$ sets, or $\prod_{\alpha \in A} X_\alpha$ for an indexed family, where

* the following conditions apply:

- For two sets, the product contains all ordered pairs $(x, y)$ where

* the first component is from the first set and the second component is from the second.
- For a finite collection, the product consists of all ordered $n$-tuples $(x_1, \dots, x_n)$ where

* each $x_i$ is an element of the corresponding factor $X_i$.
- For an arbitrary indexed family, the product is the set of all functions $x$ from the index set $A$ to the union of the sets such that $x(\alpha) \in X_\alpha$ for each $\alpha \in A$.

where

- $X, Y, X_i, X_\alpha$ are non-empty sets
- $(x, y)$ is an ordered pair
- $(x_1, \dots, x_n)$ is an ordered $n$-tuple
- $A$ (or $\Lambda$) is the index set used to label the family of sets
  
</i>
