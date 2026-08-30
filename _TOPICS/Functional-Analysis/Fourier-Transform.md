# Fourier Transform

An integral transform of a function that is used to express the function through continuous frequency components.

Note: Also written $\hat{f}$. Also written $\tilde{f}$. Also called the Fourier transform of $f$.

<i>

**definition [d]** (*Fourier Transform*) From Olver: the Fourier transform of a function $f(x)$ is

- $\displaystyle \hat{f}(k) = \dfrac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} f(x)\, e^{-ikx}\, dx$ .

The inverse Fourier transform recovers the original function by

- $\displaystyle f(x)\sim\dfrac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \hat{f}(k)\, e^{ikx}\, dk$ .

where

- $f$ is the original function.
- $\hat{f}$ is the Fourier transform of $f$.
- $x$ is the original variable.
- $k$ is the frequency variable.
- $i$ is the imaginary unit.

</i>

<i>

**definition [d]** (*Fourier Transform*) From Riley, Hobson, and Bence: the Fourier transform of $f(t)$ is

- $\displaystyle \tilde{f}(\omega) = \dfrac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} f(t)\, e^{-i\omega t}\, dt$ ,

and its inverse is

- $\displaystyle f(t) = \dfrac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \tilde{f}(\omega)\, e^{i\omega t}\, d\omega$ .

where

- $f$ is the original function of $t$.
- $\tilde{f}$ is the Fourier transform of $f$.
- $t$ is the original variable.
- $\omega$ is the frequency variable.
- the product of the two normalizing constants equals $\dfrac{1}{2\pi}$.

</i>

Forward transform. The transform integrates $f$ against a complex exponential of frequency $k$. This principle is used to assign a complex amplitude to each frequency.

Inverse transform. The inverse integral rebuilds $f$ from those amplitudes. This principle is used to recover the original function from its Fourier transform.

Symmetric normalization. Placing $\dfrac{1}{\sqrt{2\pi}}$ in both formulas keeps the pair as symmetric as possible. This principle is used to fix the constant factors in the transform pair.

## Examples

### Simple

Take the right-handed exponential pulse $f_{r}(x)=e^{-ax}$ for $x>0$ and $f_{r}(x)=0$ for $x<0$, with $a>0$. Its Fourier transform is

$$
\hat{f}_{r}(k) = \dfrac{1}{\sqrt{2\pi}\, (a+ik)}
$$

where

- $a$ is a positive decay rate.
- $k$ is the frequency variable.
- $\hat{f}_{r}$ is the Fourier transform of $f_{r}$.

### General

For $f(t)=0$ when $t<0$ and $f(t)=A e^{-\lambda t}$ when $t\geq 0$, with $\lambda>0$, the transform is

$$
\tilde{f}(\omega) = \dfrac{A}{\sqrt{2\pi}\, (\lambda+i\omega)}
$$

where

- $A$ is the amplitude at $t=0$.
- $\lambda$ is a positive decay rate.
- $\omega$ is the frequency variable.
- $\tilde{f}$ is the Fourier transform of $f$.

## References

1. Olver, P. J. *Introduction to Partial Differential Equations*. Springer, 2016. Chapter 7, §7.1, pp. 264–267 — Fourier transform $\hat{f}(k)$; inverse formula; exponential pulse example.
2. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. 3rd ed. Cambridge University Press, 2006. Chapter 13, §13.1, pp. 434–435 — symmetric Fourier transform pair; exponential decay example.
3. Cahill, K. *Physical Mathematics*. Cambridge University Press, 2019. Chapter 4, §4.1–4.2 — Fourier transform pair; Gaussian transform.
4. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. 5th ed. Matrix Editions, 2015. §4.11, Definition 4.11.24 — Fourier transform $\hat{f}(\xi)=\int_{\mathbb{R}} f(x)e^{2\pi i\xi x}\, dx$.
