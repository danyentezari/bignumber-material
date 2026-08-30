# Fourier Series

A series of sine and cosine terms that is used to represent a periodic function on a finite interval.

Note: Also called the Fourier series of $f$. Also written with Euler formulas for its coefficients.

<i>

**definition [d]** (*Fourier Series*) From Farlow: consider representing a function $f$ by a series of the form

- $\displaystyle f(x) = \dfrac{a_{0}}{2} + \sum_{n=1}^{\infty}\left\{ a_{n}\cos\left(\dfrac{n\pi x}{L}\right) + b_{n}\sin\left(\dfrac{n\pi x}{L}\right) \right\}$ ,

where the coefficients are determined by Euler's formulas

- $\displaystyle a_{0} = \dfrac{1}{L}\int_{-L}^{L} f(x)\, dx$ ,
- $\displaystyle a_{m} = \dfrac{1}{L}\int_{-L}^{L} f(x)\cos\left(\dfrac{m\pi x}{L}\right)\, dx,\quad m=1,2,\ldots$ ,
- $\displaystyle b_{m} = \dfrac{1}{L}\int_{-L}^{L} f(x)\sin\left(\dfrac{m\pi x}{L}\right)\, dx,\quad m=1,2,\ldots$ .

The series whose coefficients are determined by Euler's formulas is called the Fourier series of $f$.

where

- $f$ is the function being expanded.
- $2L$ is the period of $f$.
- $a_{0}$, $a_{m}$, $b_{m}$ are the Fourier coefficients.
- $n$ and $m$ are positive integer indices.
- $x$ is the independent variable.

</i>

<i>

**definition [d]** (*Fourier Series on $[-\pi,\pi]$*) From Olver: the Fourier series of a function $f(x)$ defined on $-\pi\leq x\leq\pi$ is

- $\displaystyle f(x)\sim\dfrac{a_{0}}{2} + \sum_{k=1}^{\infty}\bigl[a_{k}\cos kx + b_{k}\sin kx\bigr]$ ,

with coefficients

- $\displaystyle a_{k} = \dfrac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos kx\, dx,\quad k=0,1,2,\ldots$ ,
- $\displaystyle b_{k} = \dfrac{1}{\pi}\int_{-\pi}^{\pi} f(x)\sin kx\, dx,\quad k=1,2,3,\ldots$ .

where

- $f$ is defined on $[-\pi,\pi]$.
- $a_{k}$ and $b_{k}$ are the Fourier coefficients.
- $k$ is a nonnegative integer index.
- $x$ is the independent variable.

</i>

Euler formulas. The coefficients are integrals of $f$ against cosine and sine. This principle is used to compute each term of the series from $f$.

Trigonometric expansion. The series is a constant term plus cosine and sine harmonics. This principle is used to write a periodic function as an infinite sum of elementary oscillations.

## Examples

### Simple

Take the square wave of period $2\pi$ with value $-1$ on $[-\pi,0)$ and value $1$ on $[0,\pi)$. Then $L=\pi$, every $a_{n}$ vanishes, and only odd sine terms remain.

$$
f(x) = \dfrac{4}{\pi}\left\{\sin x + \dfrac{1}{3}\sin 3x + \dfrac{1}{5}\sin 5x + \cdots\right\}
$$

where

- $f$ is the square wave of period $2\pi$.
- $b_{n} = \dfrac{4}{n\pi}$ for odd $n$ and $b_{n}=0$ for even $n$.

### General

For $f(x)=x$ on $[-\pi,\pi]$, the cosine coefficients vanish and the sine coefficients are $b_{k}=\dfrac{2}{k}(-1)^{k+1}$.

$$
x\sim 2\left(\sin x - \dfrac{\sin 2x}{2} + \dfrac{\sin 3x}{3} - \dfrac{\sin 4x}{4} + \cdots\right)
$$

where

- $f(x)=x$ is the function on $[-\pi,\pi]$.
- $a_{k}=0$ for every $k\geq 0$.
- $b_{k}$ is the $k$th sine coefficient.

## References

1. Farlow, S. J. *An Introduction to Differential Equations and Their Applications*. Dover, 2006. Chapter 9, §9.1, pp. 384–387 — Fourier series on $[-L,L]$; Euler formulas; square-wave example.
2. Olver, P. J. *Introduction to Partial Differential Equations*. Springer, 2016. Chapter 3, §3.2, Definition 3.2, p. 74 — Fourier series on $[-\pi,\pi]$; Example 3.3 for $f(x)=x$.
