# Complex Analysis

Complex analysis is the study of complex-differentiable functions of a complex variable, where a complex-differentiable function is a function whose derivative is the same from every direction.

Here, again, we identifty the ideas that are fundamental to the study of complex analysis.

Complex differentiability. Complex differentiability is a property: the derivative is the same from every direction. Locally the function is a uniform scaling and a rotation.

Cauchy's theorem. Cauchy's theorem is a theorem: the integral of a holomorphic function around a closed loop in a simply connected region is zero. A simply connected region is a region with no holes.

Analyticity. Analyticity is a property: a holomorphic function is infinitely differentiable and equals a power series in a neighborhood of each point. A power series is an infinite sum of increasing integer powers.

<i>

**definition [d]**

A **holomorphic function** on an open set $U$ in the complex plane is a function $f: U \to \mathbb{C}$ that is complex-differentiable at every point of $U$.

The complex derivative at $z_{0}$ is

$$
f'(z_{0}) = \lim_{z \to z_{0}} \dfrac{f(z)-f(z_{0})}{z-z_{0}}
$$

*where*

- $U$ is an open set in the complex plane
- $f$ is a complex-valued function
- $z_{0}$ is a point of $U$

**Note:**

- The limit must exist and be the same along every path to $z_{0}$.

</i>

## Elementary Example
### Simple

The square function is holomorphic on the whole plane.

$$
f(z) = z^{2}
$$

where

- $z$ is a complex variable.
- $f$ is holomorphic on $\mathbb{C}$.

### General

An affine function is holomorphic on the whole plane.

$$
f(z) = az + b
$$

where

- $z$ is a complex variable.
- $a$ is a complex scalar.
- $b$ is a complex constant.

## Topics

1. [Contour Integral](contour-integral.html)

## References

1. Needham, T. *Visual Complex Analysis*. Oxford University Press. — complex differentiability as the same derivative in every direction, Cauchy's theorem, and analyticity.
2. Waleffe, F. *Vector and Complex Calculus*. — path independence of integrals of holomorphic functions.
3. Howell, K. B. notes on complex analysis. — the definition of a holomorphic function by the complex derivative.
