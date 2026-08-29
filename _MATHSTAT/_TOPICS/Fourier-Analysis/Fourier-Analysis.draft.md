# Fourier Analysis

An expansion of a function in complex exponentials that is used to recover the function from frequency and to identify a probability distribution, where a complex exponential is the function $e^{itx}$ of a real frequency $t$, and where frequency is a real number that labels the rate of oscillation.

Note: Also called harmonic analysis.

Fourier series. On a bounded interval a function is written as a series of complex exponentials indexed by integers. Each coefficient is an integral of the function against one exponential. This principle is used to represent a periodic function by discrete frequencies.

The Fourier coefficients are

$$
c_{n} = \dfrac{1}{2\pi} \displaystyle\int_{-\pi}^{\pi} e^{-inx} f(x)\, dx, \quad n = 0, \pm 1, \pm 2, \ldots
$$

where

- $f$ is an integrable function on $[-\pi,\pi]$.
- $c_{n}$ is the coefficient of frequency $n$.
- $n$ is an integer frequency.
- $x$ is the integration variable.
- $i$ is the imaginary unit.

Fourier transform. An integrable function on the real line is mapped to a function of a real frequency by integrating against a complex exponential. An integrable function is a function whose absolute value has a finite integral. This principle is used to pass from a function of a real variable to a function of frequency.

The Fourier transform is

$$
\hat{f}(t) = \dfrac{1}{\sqrt{2\pi}} \displaystyle\int_{-\infty}^{\infty} e^{-ixt} f(x)\, dx
$$

where

- $f$ is an integrable function on the real line.
- $\hat{f}$ is the Fourier transform of $f$.
- $t$ is a real frequency.
- $x$ is the integration variable.

Inversion formula. The original function is recovered by integrating the transform against the conjugate exponential. This principle is used to reconstruct a function from its frequency representation.

The inversion formula is

$$
f(x) = \dfrac{1}{\sqrt{2\pi}} \displaystyle\int_{-\infty}^{\infty} e^{ixt} \hat{f}(t)\, dt
$$

where

- $f$ is the original function.
- $\hat{f}$ is the Fourier transform of $f$.
- $t$ is the frequency variable.
- $x$ is the original variable.

Convolution theorem. The transform of a convolution is the product of the transforms. A convolution is an integral that slides one function against another. This principle is used to replace addition of independent random variables by multiplication of characteristic functions.

The convolution theorem is

$$
\widehat{f * g} = \hat{f}\, \hat{g}
$$

$$
(f * g)(x) = \displaystyle\int_{-\infty}^{\infty} f(x-y) g(y)\, dy
$$

where

- $f$ and $g$ are integrable functions.
- $f * g$ is the convolution of $f$ and $g$.
- $\hat{f}$ and $\hat{g}$ are the Fourier transforms of $f$ and $g$.
- $y$ is the integration variable.

Parseval relation. The inner product of two functions equals the inner product of their transforms. This principle is used to equate the size of a function with the size of its transform.

The Parseval relation is

$$
\displaystyle\int_{-\infty}^{\infty} \lvert f(x) \rvert^{2}\, dx = \displaystyle\int_{-\infty}^{\infty} \lvert \hat{f}(t) \rvert^{2}\, dt
$$

where

- $f$ is an integrable function of finite square integral.
- $\hat{f}$ is the Fourier transform of $f$.

Note: Also called the Plancherel identity.

Uniqueness. Distinct probability distributions have distinct characteristic functions. A characteristic function is the Fourier transform of a probability distribution. This principle is used to identify a probability distribution from its characteristic function.

The characteristic function of a distribution function $F$ is

$$
\phi(t) = \displaystyle\int_{-\infty}^{\infty} e^{itx}\, dF(x)
$$

where

- $F$ is a distribution function.
- $\phi$ is the characteristic function of $F$.
- $t$ is a real frequency.
- $x$ is the integration variable.

## Elementary Example

### Simple

Take a unit jump at $0$ on $[-\pi,\pi]$. Every Fourier-Stieltjes coefficient equals the same constant.

$$
c_{n} = \dfrac{1}{2\pi}, \quad n = 0, \pm 1, \pm 2, \ldots
$$

where

- $c_{n}$ is the coefficient of integer frequency $n$.

### General

For an integrable function on the real line, the Fourier transform is the integral against a complex exponential.

$$
\hat{f}(t) = \dfrac{1}{\sqrt{2\pi}} \displaystyle\int_{-\infty}^{\infty} e^{-ixt} f(x)\, dx
$$

where

- $f$ is an integrable function on the real line.
- $\hat{f}$ is the Fourier transform of $f$.
- $t$ is a real frequency.

## Topics

1. [Limiting Distribution](limiting-distribution.html)
2. [Characteristic Function](characteristic-function.html)

## References

1. Kawata, T. *Fourier Analysis in Probability Theory*. Academic Press. Chapter 2 and Chapter 3 — Fourier transform of an integrable function; inversion formula. Chapter III, §3.2 — Fourier-Stieltjes coefficients of a unit jump.
2. Billingsley, P. *Probability and Measure*. Section 26 — the Fourier transform converts convolution to multiplication; the characteristic function is the Fourier transform in nonprobabilistic contexts.
3. Gut, A. *Probability: A Graduate Course*. Chapter 4 — the characteristic function characterizes the distribution uniquely.
4. Klenke, A. *Probability Theory: A Comprehensive Course*. Chapter 15 — characteristic functions are Fourier transforms of probability measures.
