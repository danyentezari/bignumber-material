# Improper Integral

<i>

**definition [d]** (**Improper Integral** — infinite interval) A definite integral over an infinite interval, defined as a limit:

- $\displaystyle \int_{a}^{\infty} f(x)\, dx = \lim_{t \to \infty} \int_{a}^{t} f(x)\, dx$ .
- $\displaystyle \int_{-\infty}^{b} f(x)\, dx = \lim_{t \to -\infty} \int_{t}^{b} f(x)\, dx$ .

If both $\int_{-\infty}^{a} f(x)\, dx$ and $\int_{a}^{\infty} f(x)\, dx$ converge, then

- $\displaystyle \int_{-\infty}^{\infty} f(x)\, dx = \int_{-\infty}^{a} f(x)\, dx + \int_{a}^{\infty} f(x)\, dx$ .

where

- $f$ is continuous on the finite part of the interval of integration.
- the improper integral **converges** if the limit exists as a finite number; otherwise it **diverges**.

</i>

<i>

**definition [d]** (**Improper Integral** — discontinuous integrand) A definite integral where $f$ has an infinite discontinuity on $[a,b]$, defined as a one-sided limit of proper integrals:

- (discontinuity at $b$) $\displaystyle \int_{a}^{b} f(x)\, dx = \lim_{t \to b^{-}} \int_{a}^{t} f(x)\, dx$ .
- (discontinuity at $a$) $\displaystyle \int_{a}^{b} f(x)\, dx = \lim_{t \to a^{+}} \int_{t}^{b} f(x)\, dx$ .

If the discontinuity is at an interior point $c$ ($a < c < b$), the integral is the sum of the improper integrals from $a$ to $c$ and $c$ to $b$, provided both converge.

where

- $f$ is continuous on each proper subinterval used in the limits.
- the improper integral **converges** if the limit(s) exist as finite numbers; otherwise it **diverges**.

</i>

## References

1. Stewart, J. *Calculus*. — improper integrals of Type 1 (infinite intervals) and Type 2 (discontinuous integrands); convergence / divergence.
