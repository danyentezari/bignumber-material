# Linear Algebra 

<i>

**definition** (*Linear Map*)
A map between vector spaces, $F:  \mathbf{V} \rightarrow \mathbf{W}$, is a linear map if the following conditions hold.

- **additivity** $F(\mathbf{u}+\mathbf{v}) = F(\mathbf{u}) + F(\mathbf{v})$ &nbsp; for all  $\mathbf{u},\mathbf{v} \in \mathbf{V}$
- **homogeneity** $F(c\mathbf{v}) = cF(\mathbf{v})$ &nbsp; for all $c \in \mathbb{R}, \mathbf{v} \in \mathbf{V}$

where

- $\mathbf{V}, \mathbf{W} \in \mathbb{R}^{n}$ are vector spaces.

</i>


<i>

**definition** (**Linear Function**) A function from a vector space, $f: \mathbf{V} \rightarrow \mathbb{R}$, that satisfies the following conditions for all vectors and scalars:

- (Additivity) $f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})$ .
- (Homogeneity) $f(k\mathbf{v}) = k \cdot f(\mathbf{v})$.

where

- $\mathbf{V}$ is a real vector space.
- $\mathbf{u}, \mathbf{v} \in \mathbf{V}$.
- $k$ is a scalar.

</i>


<i>

**definition [D]** (*Orthonormal*) A collection of mutually orthogonal normalized vectors in an inner product space. The set must satisfy the following conditions:

* Each vector in the set has unit length (norm of 1).
* Any two distinct vectors in the set are orthogonal, meaning their inner product is zero.

where

- $\langle \alpha_i | \alpha_j \rangle$ is the inner product of two vectors in the set.
- $\delta_{ij}$ is the Kronecker delta, which is 1 if $i = j$ and 0 otherwise.
- $\|\alpha\|$ is the norm (or length) of a vector, defined as the square root of the inner product of the vector with itself.
- $V$ is an inner product space or vector space.

</i>



<i>

**definition [D]** (*Orthonormal Set of Functions*) A specific system of functions within a function space where each member is normalized to unity and all distinct members are mutually orthogonal. This set applies to functions in a Hilbert space, often defined over a specific interval or domain. The set must satisfy the following condition:

* The integral of the product of one function and the complex conjugate of another (or itself) over the domain equals the Kronecker delta.

where

- $f(x)$ and $g(x)$ are complex-valued functions of a real variable.
- $\bar{f}$ (or $f^*$) denotes the complex conjugate of the function $f$.
- $(f, g)$ (or $\langle f | g \rangle$) represents the inner product defined as the integral $\int f^*(x)g(x) dx$ over a fundamental domain.
- $w(x)$ is an optional positive weight function included in the integral.
- $Nf$ is the norm of the function, defined as the inner product of the function with itself.

</i>



<i>

**definition [D]** (*Inner Product Space*) A vector space equipped with an inner product that associates a complex scalar with every ordered pair of vectors, where

* the following conditions apply:

- The mapping satisfies conjugate symmetry: $\langle \alpha | \beta \rangle = \langle \beta | \alpha \rangle^*$.
- The mapping is linear in the second factor: $\langle \alpha | a\beta + b\gamma \rangle = a\langle \alpha | \beta \rangle + b\langle \alpha | \gamma \rangle$.
- The mapping is positive definite: $\langle \alpha | \alpha \rangle \ge 0$, vanishing only if $\alpha = 0$.

where

- $V$ is a vector space (or linear space) over a field $K$.
- $\langle \alpha | \beta \rangle$ is the inner product (or scalar product) of vectors $\alpha$ and $\beta$.
- $K$ is the scalar field, typically the real numbers $\mathbb{R}$ or complex numbers $\mathbb{C}$.
- $\|\alpha\| = \sqrt{\langle \alpha | \alpha \rangle}$ is the norm, generalizing the concept of "length".

</i>

<i>

**definition  [D]** (*Kronecker Delta*) A discrete symbol and numerical tensor representing the components of the identity matrix, serving as the discrete analog of the Dirac delta function, where

* the following condition applies:

- The value is unity if the indices are identical and zero if they are distinct.

where

- $i, j$ are discrete indices representing rows and columns.
- $\delta_{ij}$ is the Kronecker delta symbol.
- $\delta_{ij} = 1$ if $i = j$ and $\delta_{ij} = 0$ if $i \neq j$.
- $I$ is the identity matrix with entries $I_{ik} = \delta_{ik}$.
- $\delta_{ij}$ acts as a mixed second-rank tensor that is coordinate-independent.

</i>

