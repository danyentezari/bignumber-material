# Integrability

A property of a function under which the integral of its absolute value is finite that is used to say the function has finite total size under the integral.

<i>

**definition [d]** (*Integrability*) A property of a function $f$: the integral of $|f|$ is finite.

where

- $f$ is a function on a domain of integration.
- $|f|$ is the absolute value of $f$.
- the scalar field of values of $f$ may be $\mathbb{R}$.
- the scalar field of values of $f$ may be $\mathbb{C}$.

Note:

- finiteness of $\int |f|$ is the classical absolute-integrability condition associated with $L^{1}$.
- under Lebesgue theory a function is integrable exactly when it is absolutely integrable.
- the $L^{1}$-norm is $\lVert f \rVert_{1} = \int |f|\, ds$.
- Riemann integrability of a bounded function on $[a,b]$ means the limit of Riemann sums exists and is unique.
- Riemann integrability need not pass to pointwise limits of integrable functions.

</i>

## Elementary Example
### Simple

Integrability means $\int |f|$ is finite. On three sample heights, the discrete stand-in is a finite sum of absolute values.

$$
A = \{ 1,\ 2,\ 3 \}
$$

$$
f(1) = -1,\quad f(2) = 2,\quad f(3) = -3
$$

$$
\sum_{a \in A} |f(a)| = 6 < \infty
$$

where

- $f$ is the function.
- the sum is a discrete model of $\int |f|$.

### General

On an interval, absolute integrability is finiteness of the integral of $|f|$.

$$
f(x) = e^{-|x|}\ \text{on }\mathbb{R}
$$

$$
\int_{-\infty}^{\infty} |f(x)|\, dx = 2 < \infty
$$

where

- $\lVert f \rVert_{1} = \int |f|\, ds$ is the $L^{1}$-norm.


## References

1. Pietsch, A. *History of Banach Spaces and Linear Operators*. Birkhäuser, 2007. — integrability conditions underlying $L^{p}$ via integrals of powers of $|f|$.
2. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms*, 5th ed. Matrix Editions, 2015. — Lebesgue integrability as absolute integrability.
3. Stewart, J., Clegg, D., & Watson, S. *Calculus: Early Transcendentals*. Cengage Learning, 2020. — Riemann integrability via Riemann sums.
4. Gamelin, T. W., & Greene, R. E. *Introduction to Topology*, 2nd ed. Dover, 1999. — $\lVert f\rVert_{1}=\int|f|$.
