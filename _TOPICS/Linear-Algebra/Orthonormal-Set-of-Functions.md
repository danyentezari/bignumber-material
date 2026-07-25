# Orthonormal Set of Functions

A set of functions whose pairwise integrals equal one for a matching pair and zero otherwise that is used to expand a function as a series in that set.

<i>

**definition [D]** (*Orthonormal Set of Functions*) A specific system of functions within a function space where each member is normalized to unity and all distinct members are mutually orthogonal. This set applies to functions in a Hilbert space, often defined over a specific interval or domain. The set must satisfy the following condition:

- The integral of the product of one function and the complex conjugate of another over the domain equals the Kronecker delta.

where

- $f(x)$ and $g(x)$ are complex-valued functions of a real variable.
- $\bar{f}$ denotes the complex conjugate of the function $f$.
- $(f, g)$ represents the inner product defined as the integral $\int f^*(x)g(x) dx$ over a fundamental domain.
- $w(x)$ is an optional positive weight function included in the integral.
- $Nf$ is the norm of the function, defined as the inner product of the function with itself.

Note:

- $\bar{f}$ is also written $f^*$.
- $(f, g)$ is also written $\langle f | g \rangle$.
- the orthogonality integral may use another function and the complex conjugate of itself.

</i>

## Elementary Example
### Simple

An orthonormal set of functions has pairwise integrals equal to $\delta_{mn}$.

$$
\{ \varphi_{1},\ \varphi_{2} \}
$$

$$
\int_{a}^{b} \varphi_{m}(x)\, \overline{\varphi_{n}(x)}\, dx = \delta_{mn}
$$

$$
\delta_{11} = 1,\quad \delta_{12} = 0
$$

where

- $\varphi_{m}, \varphi_{n}$ are functions on $[a,b]$.
- $\delta_{mn}$ is the Kronecker delta.

### General

On $[0,2\pi]$, the complex exponentials $e^{inx}/\sqrt{2\pi}$ for several integers $n$ form an orthonormal set.

$$
\varphi_{n}(x) = \dfrac{e^{i n x}}{\sqrt{2\pi}},\quad n \in \{ -1,\ 0,\ 1 \}
$$

$$
\int_{0}^{2\pi} \varphi_{m}(x)\, \overline{\varphi_{n}(x)}\, dx = \delta_{mn}
$$

where

- $n$ labels the functions in the set.

