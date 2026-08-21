# Derivation of Taylor Expansion

A derivation that is used to obtain a polynomial approximation and exact remainder, where a remainder is the difference between the function and polynomial.

Taylor's theorem. If a function is differentiable $n+1$ times near $a$, then it equals its Taylor polynomial plus a remainder. This principle is used to express a function as a polynomial plus error.

The splitting into polynomial and remainder is

$$
f(x) = P_{n}(x) + R_{n+1}(x)
$$

where

- $f$ is the function being expanded.
- $a$ is the expansion point.
- $x$ is a nearby evaluation point.
- $P_{n}(x)$ is the Taylor polynomial of degree $n$.
- $R_{n+1}(x)$ is the remainder.

Taylor polynomial. A polynomial whose value and first $n$ derivatives at $a$ match those of $f$. This principle is used to write the degree-$n$ match to $f$ at $a$.

The Taylor polynomial is

$$
P_{n}(x)
=
f(a)
+
f'(a)(x-a)
+
\dfrac{f''(a)}{2!}(x-a)^{2}
+
\cdots
+
\dfrac{f^{(n)}(a)}{n!}(x-a)^{n}
$$

where

- $f^{(k)}(a)$ is the $k$th derivative of $f$ at $a$.
- $k!$ is the factorial of $k$.

Remainder. The difference $f(x)-P_{n}(x)$. This principle is used to isolate the approximation error.

Auxiliary functions. Helper functions of a running point $u$ that are used to apply a theorem to the remainder. This principle is used to recast the remainder as a ratio of changes.

The auxiliary functions are

$$
\phi(u)
=
f(u)
+
f'(u)(x-u)
+
\dfrac{f''(u)}{2!}(x-u)^{2}
+
\cdots
+
\dfrac{f^{(n)}(u)}{n!}(x-u)^{n}
$$

$$
\psi(u) = (x-u)^{n+1}
$$

where

- $u$ is a running point between $a$ and $x$.
- $\phi(u)$ interpolates $f$ from $u$ toward $x$.
- $\psi(u)$ is the $(n+1)$st power of the remaining distance.

At the endpoints these helpers satisfy $\phi(x)=f(x)$, $\psi(x)=0$, $\phi(a)=P_{n}(x)$, and $\psi(a)=(x-a)^{n+1}$.

Cauchy's mean-value theorem. The ratio of changes equals the ratio of derivatives at an interior point. This principle is used to replace the remainder ratio by a derivative ratio.

The Cauchy mean-value identity is

$$
\dfrac{\phi(x)-\phi(a)}{\psi(x)-\psi(a)}
=
\dfrac{\phi'(\xi)}{\psi'(\xi)}
$$

where

- $\xi$ is a point strictly between $a$ and $x$.
- $\phi'$ and $\psi'$ are the derivatives of the auxiliary functions.

Telescoping derivative. A derivative calculation that cancels all but the highest derivative term. This principle is used to evaluate the derivative ratio at the interior point.

The derivatives of the auxiliary functions are

$$
\phi'(u)
=
\dfrac{f^{(n+1)}(u)}{n!}(x-u)^{n}
\qquad
\psi'(u)
=
-(n+1)(x-u)^{n}
$$

where

- $f^{(n+1)}(u)$ is the $(n+1)$st derivative of $f$ at $u$.

Lagrange remainder. The error expressed using the next derivative at an unknown interior point. This principle is used to write an exact formula for the error.

The Lagrange remainder is

$$
R_{n+1}(x)
=
\dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
$$

where

- $\xi$ is a point strictly between $a$ and $x$.
- $R_{n+1}(x)$ is the remainder after $n$ Taylor terms.

Note: Also called Taylor's formula. Also called Taylor's theorem with remainder.

## References

1. Aleksandrov, A. D., Kolmogorov, A. N., & Lavrent’ev, M. A. *Mathematics: Its Content, Methods and Meaning*. Vol. 1. Dover, 1999. Chapter II, Section 9 — Taylor's formula via Cauchy's generalized mean-value theorem; Lagrange remainder.
2. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. 5th ed. Matrix Editions, 2015. Appendix A12 — Taylor's theorem with remainder.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*. 7th ed. Academic Press, 2013. Section 1.2 — Taylor’s expansion.
