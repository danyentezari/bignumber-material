# Characteristic Function

A complex-valued function of a real argument that is used to uniquely identify a probability distribution and to study sums of independent random variables, where a probability distribution is a rule that assigns probability to sets of outcomes, and where an independent sum is a sum of random variables that do not share common information.

Note: Also called the Fourier transform of a probability measure.

The definition of the characteristic function. For a probability measure on the line, the characteristic function at a real argument is the integral of a complex exponential against that measure. A complex exponential is the function $e^{itx}$. This principle is used to attach one complex value to every real argument.

The characteristic function of a probability measure $\mu$ is

$$
\phi(t) = \displaystyle\int_{-\infty}^{\infty} e^{itx}\, \mu(dx)
$$

where

- $\mu$ is a probability measure on the real line.
- $\phi$ is the characteristic function of $\mu$.
- $t$ is a real argument.
- $x$ is the integration variable.
- $i$ is the imaginary unit.

For a random variable $X$ with distribution $\mu$, the same function is

$$
\phi(t) = E[e^{itX}]
$$

where

- $X$ is a real-valued random variable.
- $E$ is expectation.

Universal existence. The complex exponential is bounded, so the characteristic function exists for every probability distribution. This principle is used to work with every distribution, including those that lack a moment generating function.

Convolution-to-multiplication. The characteristic function of a convolution of two probability measures is the product of their characteristic functions. A convolution is the distribution of the sum of independent random variables. This principle is used to replace addition of independent random variables by multiplication of characteristic functions.

Uniqueness. Distinct probability distributions have distinct characteristic functions. This principle is used to recover which distribution produced a given characteristic function.

Inversion. A characteristic function determines its measure through an inversion formula. An inversion formula is a rule that rebuilds the measure from the characteristic function. This principle is used to reconstruct a distribution from its characteristic function.

Continuity theorem. Pointwise convergence of characteristic functions yields weak convergence of the corresponding distributions. Weak convergence is convergence of distributions in the sense used for limiting laws. This principle is used to prove limit theorems for sequences of random variables.

<!--
## Elementary Example

### Simple

A one-point distribution at $a$ has characteristic function $e^{ita}$.

$$
\phi(t) = e^{ita}
$$

where

- $a$ is the point of unit mass.
- $t$ is a real argument.

### General

A Bernoulli distribution with success probability $p$ has characteristic function $q + p e^{it}$, where $q = 1 - p$.

$$
\phi(t) = q + p e^{it}
$$

where

- $p$ is the success probability.
- $q$ is $1-p$.
- $t$ is a real argument.
-->

## References

1. Billingsley, P. *Probability and Measure*. Section 26, pp. 342, 344 — definition $\phi(t)=\int e^{itx}\,\mu(dx)$; existence; convolution product; uniqueness; inversion; continuity theorem.
2. Gut, A. *Probability: A Graduate Course*. Chapter 4, Section 1, pp. 159–160 — one-point, Bernoulli, normal, and Cauchy examples.
3. Kawata, T. *Fourier Analysis in Probability Theory*. Chapter III, §3.10, p. 104 — Bernoulli distribution function with characteristic function $\cos t$.
