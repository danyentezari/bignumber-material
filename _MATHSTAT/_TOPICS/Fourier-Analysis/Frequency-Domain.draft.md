# Frequency Domain

A representation of a function as a function of frequency that is used to transform a problem from the original variable to frequency, where frequency is a real number that labels the rate of oscillation.

Note: Also called the frequency representation.

From Oppenheim, Willsky, and Hamid, Signals and Systems, Chapter 4, Section 4.4, p. 317:

"Rather than computing $y(t)=x(t)*h(t)$ directly, let us transform the problem into the frequency domain."

From Oppenheim, Willsky, and Hamid, Signals and Systems, Chapter 4, Section 4.2, p. 302:

"Here again, we see an illustration of the inverse relationship between the time and the frequency domains."

The phrase frequency domain does not appear in Kawata, Billingsley, Klenke, Gut, Ash, or Kallenberg. In those texts the Fourier transform is a function of a real argument $t$.

Dual representation. A function of the original variable has a companion function of frequency. This principle is used to express the same object in the original variable and in frequency.

The Fourier transform of a single impulse of area $2\pi$ at frequency $\omega_{0}$ is inverted by

$$
X(j\omega) = 2\pi\,\delta(\omega-\omega_{0})
$$

$$
x(t) = \dfrac{1}{2\pi} \displaystyle\int_{-\infty}^{\infty} 2\pi\,\delta(\omega-\omega_{0})\, e^{j\omega t}\, d\omega = e^{j\omega_{0} t}
$$

where

- $X(j\omega)$ is the frequency representation of $x$.
- $\omega$ is a real frequency.
- $\omega_{0}$ is a fixed frequency.
- $\delta$ is the unit impulse.
- $t$ is the original variable.
- $j$ is the imaginary unit.

Inverse relationship. A periodic impulse train in the original variable has a periodic impulse train in the frequency domain, with period $\dfrac{2\pi}{T}$ when the original period is $T$. This principle is used to see that stretching in the original variable compresses the frequency representation.

Differentiation as multiplication. Differentiation in the original variable becomes multiplication by $j\omega$ in the frequency domain. This principle is used to replace a derivative by an algebraic factor of frequency.

Convolution in frequency. Convolution in the original variable is replaced by a product after the problem is transformed into the frequency domain. A convolution is an integral that slides one function against another. This principle is used to compute an output by multiplying frequency representations.

Characteristic function as Fourier transform. In probability the frequency representation of a distribution is the characteristic function. From Billingsley, Probability and Measure, Section 26, p. 342: "The characteristic function in nonprobabilistic contexts is called the Fourier transform." This principle is used to put a probability distribution into the frequency domain.

The characteristic function of a probability measure $\mu$ is

$$
\phi(t) = \displaystyle\int_{-\infty}^{\infty} e^{itx}\, \mu(dx)
$$

where

- $\mu$ is a probability measure on the line.
- $\phi$ is the characteristic function of $\mu$.
- $t$ is a real argument.
- $x$ is the integration variable.

From Kawata, Fourier Analysis in Probability Theory, Chapter II, Section 2.3, p. 41:

$$
\hat{f}(t) = \dfrac{1}{\sqrt{2\pi}} \displaystyle\int_{-\infty}^{\infty} e^{-ixt} f(x)\, dx, \quad -\infty < t < \infty
$$

where

- $f$ is an integrable function on the real line.
- $\hat{f}$ is the Fourier transform of $f$.
- $t$ is the real argument of the transform.

## Elementary Example

### Simple

Oppenheim, Chapter 4, Section 4.2, p. 297. One impulse of area $2\pi$ at frequency $\omega_{0}$ inverts to a single complex exponential.

$$
X(j\omega) = 2\pi\,\delta(\omega-\omega_{0})
$$

$$
x(t) = e^{j\omega_{0} t}
$$

where

- $\omega_{0}$ is a fixed frequency.

### General

Oppenheim, Chapter 4, Section 4.2, p. 297. A linear combination of equally spaced impulses inverts to a Fourier series.

$$
X(j\omega) = \sum_{k=-\infty}^{+\infty} 2\pi a_{k}\, \delta(\omega-k\omega_{0})
$$

$$
x(t) = \sum_{k=-\infty}^{+\infty} a_{k}\, e^{jk\omega_{0} t}
$$

where

- $a_{k}$ is the coefficient of frequency $k\omega_{0}$.
- $k$ is an integer index.

## References

1. Oppenheim, A. V., Willsky, A. S., and Hamid, S. *Signals and Systems*. Prentice Hall, 1996. Chapter 4, §4.2, pp. 297, 302 — frequency-domain impulse train; inverse relationship of the original variable and frequency. §4.3.4, p. 307 — differentiation becomes multiplication by $j\omega$. §4.4, p. 317 — transform the problem into the frequency domain.
2. Billingsley, P. *Probability and Measure*. Section 26, p. 342 — characteristic function is the Fourier transform in nonprobabilistic contexts. The phrase frequency domain does not appear.
3. Kawata, T. *Fourier Analysis in Probability Theory*. Chapter II, §2.3, p. 41 — Fourier transform as a function of $t$ on $(-\infty,\infty)$. The phrase frequency domain does not appear.
