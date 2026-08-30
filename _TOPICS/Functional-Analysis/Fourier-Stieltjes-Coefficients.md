# Fourier-Stieltjes Coefficients

A sequence of complex numbers that is used to expand a bounded nondecreasing function on a finite interval as a Fourier-Stieltjes series.

Note: Also written $c_{n}$. Also called the Fourier-Stieltjes coefficients of $F$.

<i>

**definition [d]** (*Fourier-Stieltjes Coefficients*) From Kawata: let $F(x)\in M(-\pi,\pi)$. Form

- $\displaystyle c_{n} = (2\pi)^{-1}\int_{-\pi}^{\pi} e^{-inx}\, dF(x),\quad n=0,\pm 1,\pm 2,\ldots$ .

They are called the Fourier-Stieltjes coefficients of $F(x)$ and one sometimes uses the representation

- $\displaystyle F(x)\sim\sum_{n=-\infty}^{\infty} c_{n}\, e^{inx}$ .

The series is called the Fourier-Stieltjes series.

where

- $F$ is a bounded nondecreasing function in $M(-\pi,\pi)$.
- $M(-\pi,\pi)$ is the class of such functions on $[-\pi,\pi]$.
- $c_{n}$ is the $n$th Fourier-Stieltjes coefficient of $F$.
- $n$ is an integer frequency index.
- $x$ is the integration variable.
- $i$ is the imaginary unit.
- $\displaystyle\int_{-\pi}^{\pi}\cdots\, dF(x)$ is the Lebesgue-Stieltjes integral with respect to $F$.
- $(2\pi)^{-1}$ is the normalizing constant.

</i>

Integral formula. Each coefficient is a normalized Lebesgue-Stieltjes integral of a complex exponential against $F$. This principle is used to attach one complex value to every integer frequency.

Fourier-Stieltjes series. The formal series built from the coefficients is written

$$
F(x)\sim\sum_{n=-\infty}^{\infty} c_{n}\, e^{inx}
$$

where

- $c_{n}$ is the $n$th Fourier-Stieltjes coefficient.
- $e^{inx}$ is the complex exponential of frequency $n$.

This principle is used to represent $F$ by its Fourier-Stieltjes series.

No forced decay. Unlike ordinary Fourier coefficients, the sequence $c_{n}$ need not tend to zero as $n\to\pm\infty$. This principle is used to distinguish Fourier-Stieltjes coefficients from classical Fourier coefficients of an integrable density.

## Examples

### Simple

Take the unit jump at a point $a$ with $-\pi<a<\pi$, restricted to $[-\pi,\pi]$. Then every coefficient is a pure phase.

$$
c_{n} = (2\pi)^{-1} e^{-ina},\quad n=0,\pm 1,\pm 2,\ldots
$$

where

- $a$ is the jump location in $(-\pi,\pi)$.
- $U(x-a)$ is the unit distribution function at $a$.
- $c_{n}$ does not tend to zero as $n\to\pm\infty$.

### General

For a general $F\in M(-\pi,\pi)$, each coefficient is the Stieltjes integral against the corresponding exponential.

$$
c_{n} = \dfrac{1}{2\pi}\int_{-\pi}^{\pi} e^{-inx}\, dF(x)
$$

$$
F(x)\sim\sum_{n=-\infty}^{\infty} c_{n}\, e^{inx}
$$

where

- $F$ is a bounded nondecreasing function on $[-\pi,\pi]$.
- $c_{n}$ is the $n$th Fourier-Stieltjes coefficient.
- the integral is a Lebesgue-Stieltjes integral.

## References

1. Kawata, T. *Fourier Analysis in Probability Theory*. Academic Press. Chapter III, §3.2, p. 84 — definition of Fourier-Stieltjes coefficients $c_{n}=(2\pi)^{-1}\int_{-\pi}^{\pi}e^{-inx}\,dF(x)$; Fourier-Stieltjes series; unit-jump example $c_{n}=(2\pi)^{-1}e^{-ina}$.
