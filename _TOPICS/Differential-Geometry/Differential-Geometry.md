# Differential Geometry

### Forms

Forms are functions that take vectors as input and return scalars. A 1-form takes a single vector as input, a 2-form takes two vectors as input, and so on.

<i>

**definition** (*1-form = linear functional = covector = covariant vector*) A linear, real-valued function of a single vector input, $\boldsymbol{\omega}: \mathbf{V} \rightarrow \mathbb{R}$, which satisfies the following conditions for all vectors and scalars:

- (Additivity) $\boldsymbol{\omega}(\mathbf{u} + \mathbf{v}) = \boldsymbol{\omega}(\mathbf{u}) + \boldsymbol{\omega}(\mathbf{v})$.
- (Homogeneity) $\boldsymbol{\omega}(k\mathbf{v}) = k \cdot \boldsymbol{\omega}(\mathbf{v})$.

where
- $\mathbf{V}$ is a real vector space.
- $\mathbb{R}$ is the set of real numbers.
- $\boldsymbol{\omega}$ is a 1-form.
- $\mathbf{u}, \mathbf{v}$ are vectors in $\mathbf{V}$.
- $k$ is a scalar.

</i>


<i>

**definition** (*2-form*) A bilinear, antisymmetric, real-valued function of two vector inputs, $\boldsymbol{\omega}: \mathbf{V} \times \mathbf{V} \rightarrow \mathbb{R}$, which satisfies the following conditions for all vectors and scalars:

- (Bilinearity) $\boldsymbol{\omega}(a\mathbf{u} + b\mathbf{u}', \mathbf{v}) = a \cdot \boldsymbol{\omega}(\mathbf{u}, \mathbf{v}) + b \cdot \boldsymbol{\omega}(\mathbf{u}', \mathbf{v})$ and $\boldsymbol{\omega}(\mathbf{u}, a\mathbf{v} + b\mathbf{v}') = a \cdot \boldsymbol{\omega}(\mathbf{u}, \mathbf{v}) + b \cdot \boldsymbol{\omega}(\mathbf{u}, \mathbf{v}')$.
- (Antisymmetry) $\boldsymbol{\omega}(\mathbf{u}, \mathbf{v}) = -\boldsymbol{\omega}(\mathbf{v}, \mathbf{u})$.

where
- $\mathbf{V}$ is a real vector space.
- $\mathbb{R}$ is the set of real numbers.
- $\boldsymbol{\omega}$ is a 2-form.
- $\mathbf{u}, \mathbf{u}', \mathbf{v}, \mathbf{v}'$ are vectors in $\mathbf{V}$.
- $a, b$ are scalars.

</i>



<i>

**definition** (*k-form*) A multilinear, completely antisymmetric, real-valued function of $k$ vector inputs, $\boldsymbol{\omega}: \mathbf{V}^k \rightarrow \mathbb{R}$, which satisfies the following conditions for all vectors and scalars:

- (k-Linearity) $\boldsymbol{\omega}(\mathbf{v}_1, \dots, a\mathbf{v}_i + b\mathbf{v}_i', \dots, \mathbf{v}_k) = a \cdot \boldsymbol{\omega}(\mathbf{v}_1, \dots, \mathbf{v}_i, \dots, \mathbf{v}_k) + b \cdot \boldsymbol{\omega}(\mathbf{v}_1, \dots, \mathbf{v}_i', \dots, \mathbf{v}_k)$ for each argument $i$ where $1 \leq i \leq k$.
- (Complete Antisymmetry) Swapping any two vector inputs reverses the sign of the output: $\boldsymbol{\omega}(\dots, \mathbf{u}, \dots, \mathbf{v}, \dots) = -\boldsymbol{\omega}(\dots, \mathbf{v}, \dots, \mathbf{u}, \dots)$.

where
- $\mathbf{V}$ is a real vector space.
- $\mathbf{V}^k$ is the $k$-fold Cartesian product of $\mathbf{V}$.
- $\mathbb{R}$ is the set of real numbers.
- $\boldsymbol{\omega}$ is a $k$-form.
- $\mathbf{v}_1, \dots, \mathbf{v}_k, \mathbf{v}_i', \mathbf{u}, \mathbf{v}$ are vectors in $\mathbf{V}$.
- $k$ is a positive integer representing the degree of the form.
- $a, b$ are scalars.

</i>


### Tensors


<i>

**definition** (*Multilinear Function*) A function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where the following conditions apply for each argument $i$ ($1 \leq i \leq k$):

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

**definition** (*k-Tensor*) A multilinear function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where the following condition applies:

- The function $T$ is linear in each of its $k$ arguments.

where
- $V$ is a vector space.
- $V^k$ is the $k$-fold Cartesian product $V \times \dots \times V$.
- $k$ is a positive integer representing the degree of the tensor.
- $\mathbb{R}$ is the set of real numbers.
- $\mathcal{L}^k(V)$ (or $\mathcal{J}^k(V)$) is the vector space of all $k$-tensors on $V$.

</i>


<i>

**definition** (*Multilinear Function*) A function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where the following conditions apply for each argument $i$ ($1 \leq i \leq k$):

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

**definition** (*k-Fold Product*) A set constructed by the Cartesian product of $k$ copies of a single set, $X^k$, where the following condition applies:

- The resulting set consists of all ordered $k$-tuples where each coordinate is an element of the original set.

where
- $k$ is a positive integer representing the number of repetitions.
- $X$ is the underlying set, topological space, or vector space.
- $X^k$ (or $V^k$) denotes the $k$-fold Cartesian product $X \times \dots \times X$.

</i>


<i>

**definition** (*Cartesian Product*) A set consisting of all possible ordered combinations of elements from a collection of sets, denoted by $X \times Y$ for two sets, $X_1 \times \dots \times X_n$ for $n$ sets, or $\prod_{\alpha \in A} X_\alpha$ for an indexed family, where the following conditions apply:

- For two sets, the product contains all ordered pairs $(x, y)$ where the first component is from the first set and the second component is from the second.
- For a finite collection, the product consists of all ordered $n$-tuples $(x_1, \dots, x_n)$ where each $x_i$ is an element of the corresponding factor $X_i$.
- For an arbitrary indexed family, the product is the set of all functions $x$ from the index set $A$ to the union of the sets such that $x(\alpha) \in X_\alpha$ for each $\alpha \in A$.

where
- $X, Y, X_i, X_\alpha$ are non-empty sets
- $(x, y)$ is an ordered pair
- $(x_1, \dots, x_n)$ is an ordered $n$-tuple
- $A$ (or $\Lambda$) is the index set used to label the family of sets
  
</i>

### Covariant, Contravariant, and Coordinate Systems

The context if this section is the following. In physics and mathematics, points exist independently of the coordinates used to represent them.

First, we begin a discussion on covariant and contravariant vectors.

Covariant vectors are linear functionals.


<i>

**definition** (*Linear Functional*) A linear transformation from a vector space $V$ to its associated field of scalars $K$, The mapping $f: V \rightarrow K$ must satisfy the following linearity condition:

- $f(ax + by) = af(x) + bf(y)$ 

where
- $x, y \in V$ are vectors
- $a, b \in K$ are scalars
- $V$ is a vector space
- $K$ is the field of scalars.

</i>




<i>

**definition** (*k-Covector*) An alternating $k$-linear function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where the following conditions apply:

- The function $T$ is linear in each of its $k$ arguments.
- $T(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\text{sgn } \sigma) T(v_1, \dots, v_k)$ for every permutation $\sigma \in S_k$.

where
- $V$ is a vector space.
- $k$ is a positive integer representing the degree of the covector.
- $v_1, \dots, v_k \in V$ are vectors.
- $A^k(V)$ (or $\Lambda^k(V^*)$) is the vector space of all $k$-covectors on $V$.
- $\text{sgn } \sigma$ is the sign of the permutation.
- A $k$-covector is also called a multicovector of degree k or an alternating k-tensor.

</i>


<i>

**definition** (*k-Covector Field*) A function assigning a $k$-covector to each point of a manifold, $\omega: M \rightarrow \Lambda^k(T^*M)$, where the following condition applies:

- For each point $p$ in $M$, $\omega(p)$ is an alternating $k$-linear function on the tangent space $T_pM$.

where
- $M$ is a smooth manifold.
- $p$ is a point in $M$.
- $T_pM$ is the tangent space of $M$ at $p$.
- $T^*_pM$ is the cotangent space of $M$ at $p$.
- $\Lambda^k(T^*_pM)$ (or $A^k(T_pM)$) is the space of all alternating $k$-tensors on the tangent space $T_pM$.
- $\Lambda^k(T^*M)$ is the $k$-th exterior power of the cotangent bundle.
- A $k$-covector field is also called a differential $k$-form.

</i>



<i>

**example** (*k-Covector*) Let

$$
V = \mathbb{R}^2.
$$

Define the function

$$
T : V^2 \rightarrow \mathbb{R}
$$

by

$$
T((a,b),(c,d))
=
ad-bc.
$$

where $$a,b,c,d \in \mathbb{R}$$.

Let

$$
v_1=(1,2),
\qquad
v_2=(3,4).
$$

Then

$$
T(v_1,v_2)
=
(1)(4)-(2)(3)
=
-2.
$$

Interchanging the vectors gives

$$
T(v_2,v_1)
=
(3)(2)-(4)(1)
=
2
=
-T(v_1,v_2).
$$

Therefore, $T$ changes sign when its arguments are exchanged, so $T$ is alternating.

Furthermore, $T$ is linear in each argument. Hence, $T$ is an alternating $2$-linear function.

Therefore, $T$ is a $2$-covector on $\mathbb{R}^2$.

</i>

### Functions

<i>

**definition** (*Alternating Function*) A property of a $k$-linear function from the $k$-fold product of a vector space to the real numbers, $T: V^k \rightarrow \mathbb{R}$, where the following conditions apply:

- $T(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\text{sgn } \sigma) T(v_1, \dots, v_k)$ for every permutation $\sigma \in S_k$.
- $T(v_1, \dots, v_i, \dots, v_j, \dots, v_k) = -T(v_1, \dots, v_j, \dots, v_i, \dots, v_k)$ for any interchange of two arguments.
- $T(v_1, \dots, v_k) = 0$ whenever two of the vectors $v_1, \dots, v_k$ are equal.

where
- $V$ is a vector space.
- $V^k$ is the $k$-fold Cartesian product $V \times \dots \times V$.
- $S_k$ is the permutation group of $k$ objects.
- $\text{sgn } \sigma$ is the sign of the permutation $\sigma$, which is $+1$ if the permutation is even and $-1$ if it is odd.
- $v_1, \dots, v_k$ are vectors in $V$.
- $k$ is a positive integer representing the degree of the function.

</i>


<i>

**definition** (*Alternating k-linear function*) A multilinear function from the $k$-fold product of a vector space to the real numbers, $f: V^k \rightarrow \mathbb{R}$, where the following conditions apply:

- $f(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\text{sgn } \sigma) f(v_1, \dots, v_k)$ for all $\sigma \in S_k$.
- $f(v_1, \dots, v_i, \dots, v_j, \dots, v_k) = -f(v_1, \dots, v_j, \dots, v_i, \dots, v_k)$ for any interchange of two arguments.
- $f(v_1, \dots, v_k) = 0$ whenever two of the vectors $v_1, \dots, v_k$ are equal.

where
- $V$ is a vector space.
- $V^k$ is the $k$-fold Cartesian product $V \times \dots \times V$.
- $k$ is a positive integer representing the degree of the function.
- $S_k$ is the permutation group of $k$ objects.
- $\text{sgn } \sigma$ is the sign of the permutation $\sigma$.
- $v_1, \dots, v_k \in V$ are vectors.
- $A^k(V)$ (or $\Lambda^k(V^*)$) is the vector space of all alternating $k$-linear functions on $V$.

k-covector, multicovector of degree k, and alternating k-tensor are synonyms for an alternating $k$-linear function.

</i>

### Differential Form

<i>

**definition** (*Differential k-Form*) A function assigning an alternating k-linear function to each point of a manifold $M$, where the following condition applies:

- For each point $p \in M$, $\omega(p)$ is a $k$-covector on the tangent space $T_pM$.

where
- $M$ is a smooth manifold.
- $k$ is a non-negative integer representing the degree of the form.
- $T_pM$ is the tangent space to $M$ at $p$.
- $T^*_p M$ (or $T^*_p(M)$) is the cotangent space at $p$, defined as the dual space of the tangent space $T_pM$.
- $\Lambda^k(T^*_p M)$ (or $A^k(T_pM)$) is the vector space of all alternating $k$-tensors (also called $k$-covectors or multicovectors) on $T_pM$.
- $\omega$ is a smooth section of the vector bundle $\Lambda^k(T^*M)$, the $k$-th exterior power of the cotangent bundle.

</i>



### Appendix

<i>

**definition** (**Linear Function**) A function from a vector space, $f: \mathbf{V} \rightarrow \mathbb{R}$, that satisfies the following conditions for all vectors and scalars:

- (Additivity) $f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})$ .
- (Homogeneity) $f(k\mathbf{v}) = k \cdot f(\mathbf{v})$.

where
- $\mathbf{V}$ is a real vector space.
- $\mathbf{u}, \mathbf{v} \in \mathbf{V}$.
- $k$ is a scalar.

</i>