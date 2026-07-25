# Absolute-Value-to-the-p

A function obtained by raising the absolute value of another function to a fixed parameter power that is used to build norms and integrals that measure size.

<i>

**definition [d]** (*$|f|^{p}$*) The nonnegative function obtained by raising the absolute value of $f$ to the power $p$.

where

- $f$ is a function.
- $|f|$ is the absolute value of $f$.
- $p$ is a real exponent with $p \geq 1$.
- $|f|^{p}$ is the pointwise $p$-th power of $|f|$.
- the scalar field of values of $f$ may be $\mathbb{R}$.
- the scalar field of values of $f$ may be $\mathbb{C}$.

Note:

- the integral of $|f|^{p}$ being finite is the membership condition for $L^{p}$.

</i>

## Elementary Example
### Simple

The map $f \mapsto |f|^{p}$ raises the absolute value to the power $p$. On three sample points with $p = 1$, this is just $|f|$.

$$
A = \{ 1,\ 2,\ 3 \},\quad p = 1
$$

$$
f(1) = -2,\quad f(2) = 0,\quad f(3) = 4
$$

$$
|f|^{1}(1) = 2,\quad |f|^{1}(2) = 0,\quad |f|^{1}(3) = 4
$$

where

- $f$ is the function.
- $|f|^{p}$ is the pointwise $p$-th power of $|f|$.

### General

For $p = 2$, square the absolute values on a longer sample.

$$
A = \{ 0,\ 1,\ 2,\ 3 \},\quad p = 2
$$

$$
f(0) = -1,\quad f(1) = 2,\quad f(2) = -3,\quad f(3) = 0
$$

$$
|f|^{2}(0) = 1,\quad |f|^{2}(1) = 4,\quad |f|^{2}(2) = 9,\quad |f|^{2}(3) = 0
$$

where

- finiteness of $\int |f|^{p}$ is the $L^{p}$ membership condition.


## References

1. Pietsch, A. *History of Banach Spaces and Linear Operators*. Birkhäuser, 2007. — Riesz: integrability of $|f|^{p}$; each $p$ determines a class $L^{p}$.
