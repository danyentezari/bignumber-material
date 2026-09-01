# Derivation of Normal Distribution

A derivation that is used to obtain the normal density from a decay-rate rule, where a decay-rate rule is a differential equation that ties the slope of a density to its value and to its distance from the mean, and where a density is a nonnegative function whose integral over the real line equals one.

Note: Also called a derivation of the Gaussian density.

Decay-rate rule. The slope of the density is a negative constant times distance from the mean times the density itself.

The decay-rate equation is

$$
\dfrac{df}{dx} = -k(x-\mu)\, f(x)
$$

where

- $f$ is the density.
- $x$ is a real value.
- $\mu$ is the mean.
- $k$ is a positive constant.

Separated equation. Division by the density converts the rule into an equation for the logarithm of the density.

$$
\begin{aligned}
\dfrac{1}{f}\, \dfrac{df}{dx}
&= -k(x-\mu) \\
\displaystyle\int \dfrac{1}{f}\, df
&= \displaystyle\int -k(x-\mu)\, dx
\end{aligned}
$$

where

- $df$ is the differential of $f$.
- $dx$ is the differential of $x$.

Exponential solution. Integration produces a constant times an exponential of minus a square of distance from the mean.

$$
\begin{aligned}
\ln f(x)
&= -\dfrac{k}{2}(x-\mu)^{2} + C \\
f(x)
&= A\, e^{-\dfrac{k}{2}(x-\mu)^{2}}
\end{aligned}
$$

where

- $C$ is a constant of integration.
- $A = e^{C}$ is a positive amplitude.

Inflection scale. Concavity changes at one standard deviation from the mean, so the constant equals one over the variance.

$$
\begin{aligned}
\dfrac{d^{2}f}{dx^{2}}
&= f(x)\bigl(-k + k^{2}(x-\mu)^{2}\bigr) \\
(x-\mu)^{2} &= \dfrac{1}{k} \\
k &= \dfrac{1}{\sigma^{2}}
\end{aligned}
$$

where

- $\sigma$ is the standard deviation.
- $\sigma^{2}$ is the variance.

The scaled density is

$$
f(x) = A\, e^{-\dfrac{1}{2}\left(\dfrac{x-\mu}{\sigma}\right)^{2}}
$$

Unit-area factor. The remaining constant is chosen so the integral of the density over the real line equals one.

$$
\begin{aligned}
z &= \dfrac{x-\mu}{\sigma} \\
\displaystyle\int_{-\infty}^{\infty} f(x)\, dx
&= A\sigma \displaystyle\int_{-\infty}^{\infty} e^{-\dfrac{1}{2}z^{2}}\, dz \\
A\sigma\sqrt{2\pi}
&= 1 \\
A
&= \dfrac{1}{\sigma\sqrt{2\pi}}
\end{aligned}
$$

where

- $z$ is the standardized variable.

Normal density. The unique solution of the decay-rate rule with this mean, this variance, and unit area is the normal density.

The normal density is

$$
f(x) = \dfrac{1}{\sigma\sqrt{2\pi}}\, e^{-\dfrac{1}{2}\left(\dfrac{x-\mu}{\sigma}\right)^{2}}
$$

Standard form. Setting the mean to zero and the standard deviation to one recovers the standard normal density.

The standard normal density is

$$
f(z) = \dfrac{1}{\sqrt{2\pi}}\, e^{-\dfrac{1}{2}z^{2}}
$$

<!--
## Elementary Example

### Simple

Take mean $0$ and standard deviation $1$. Then $k=1$ and the density is the standard normal curve.

$$
\dfrac{df}{dz} = -z\, f(z)
$$

$$
f(z) = \dfrac{1}{\sqrt{2\pi}}\, e^{-\dfrac{1}{2}z^{2}}
$$

where

- $z$ is a real value.

### General

Take mean $5$ and standard deviation $2$. Then $k=\dfrac{1}{4}$.

$$
\dfrac{df}{dx} = -\dfrac{1}{4}(x-5)\, f(x)
$$

$$
f(x) = \dfrac{1}{2\sqrt{2\pi}}\, e^{-\dfrac{1}{2}\left(\dfrac{x-5}{2}\right)^{2}}
$$

where

- $x$ is a real value.
-->

## References

1. Oxford College of Emory University, Mathematics Center. “Normal Distributions.” MATH 117. https://mathcenter.oxford.emory.edu/site/math117/normalDistribution/ — decay-rate equation $\dfrac{df}{dx}=-k(x-\mu)f(x)$; normalized normal density; standard form; inflection at one standard deviation from the mean.
