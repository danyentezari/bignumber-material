# Quadratic Integrability

A property of a function under which the integral of the square of its absolute value is finite that is used to say the function has finite size under a square integral.

<i>

**definition [d]** (*Quadratic Integrability = Square Integrability*) A property of a function $f$: the integral of $|f|^{2}$ is finite.

where

- $f$ is a function on a domain of integration.
- $|f|^{2}$ is the square of the absolute value of $f$.
- the scalar field of values of $f$ may be $\mathbb{R}$.
- the scalar field of values of $f$ may be $\mathbb{C}$.

Note:

- this is the integrability condition that defines the classical space $L^{2}$.

</i>

## Elementary Example
### Simple

Quadratic integrability means $\int |f|^{2}$ is finite. On three sample points, sum the squares of absolute values.

$$
A = \{ 1,\ 2,\ 3 \}
$$

$$
f(1) = 1,\quad f(2) = -2,\quad f(3) = 1
$$

$$
\sum_{a \in A} |f(a)|^{2} = 6 < \infty
$$

where

- $|f|^{2}$ is the square of the absolute value of $f$.

### General

On an interval, square integrability is finiteness of $\int |f|^{2}$.

$$
f(x) = e^{-x^{2}}\ \text{on }\mathbb{R}
$$

$$
\int_{-\infty}^{\infty} |f(x)|^{2}\, dx < \infty
$$

where

- this is the membership condition for the classical space $L^{2}$.


## References

1. Pietsch, A. *History of Banach Spaces and Linear Operators*. Birkhäuser, 2007. — square integrability as finiteness of the integral of $|f|^{2}$; Riesz.
