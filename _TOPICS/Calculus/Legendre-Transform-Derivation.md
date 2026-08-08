# Legendre Transform Derivation

A derivation of the Legendre transform that is used to obtain $G(p)=p\,x(p)-F(x(p))$ from a function $F(x)$.

<i>

**definition [d]** (*Legendre Transform Derivation*) From MIT OpenCourseWare 8.223 Classical Mechanics II, Lecture 15:

1. Start from a function of one independent variable, so the information in $F$ can be rewritten with a different independent variable.
   - $F = F(x)$ .

2. Require that $F$ be strictly convex and smooth, so the derivative of $F$ has a one-to-one relation with $x$.

3. Define the slope of $F$, which will serve as the new independent variable in place of $x$.
   - $p = \dfrac{dF}{dx}$ .

4. Invert the slope relation to express $x$ through $p$, so that $G$ is a function of $p$ alone.
   - $x = x(p)$ .

5. Form $G(p)=p\,x(p)-F(x(p))$, which keeps the same information while making $p$ independent.
   - $G(p) = p\, x(p) - F\bigl(x(p)\bigr)$ .

6. Differentiate $G$ with respect to $p$, which recovers $x$ and shows the transform is its own inverse.
   - $\dfrac{dG}{dp} = x(p)$ ,
   and therefore
   - $F(x) = p\, x - G(p)$ .

7. Check on a quadratic example to confirm that $G$ is well defined and invertible.
   For $F(x) = \dfrac{1}{2}m x^{2}$,
   - $p = m x$ , $\qquad x = \dfrac{p}{m}$ , $\qquad G(p) = \dfrac{p^{2}}{2m}$ .

where

- $F$ is the original function.
- $x$ is the original independent variable.
- $p$ is the new independent variable.
- $\dfrac{dF}{dx}$ is the derivative of $F$ with respect to $x$.
- $G$ is the Legendre transform of $F$.
- $\dfrac{dG}{dp}$ is the derivative of $G$ with respect to $p$.
- $m$ is a positive constant in the quadratic example.

</i>

## Elementary Example

### Simple

For $F(x) = \dfrac{1}{2}x^{2}$,

$$
p = x,\qquad G(p) = \dfrac{1}{2}p^{2}
$$

where

- $F$ is the original function.
- $x$ is the original variable.
- $p$ is the slope variable.
- $G$ is the Legendre transform.

### General

For $F(x) = \dfrac{1}{2}m x^{2}$ with $m > 0$,

$$
p = m x,\qquad G(p) = \dfrac{p^{2}}{2m}
$$

where

- $F$ is the original function.
- $m$ is a positive constant.
- $x$ is the original variable.
- $p$ is the slope variable.
- $G$ is the Legendre transform.

## References

1. MIT OpenCourseWare. *8.223 Classical Mechanics II*, Lecture 15: Introduction to Hamiltonian Mechanics (IAP 2017). [PDF](https://ocw.mit.edu/courses/8-223-classical-mechanics-ii-january-iap-2017/09ab68ae8e7987debc025892e00c0f1f_MIT8_223IAP17_Lec15.pdf) — Legendre transform $G(s)=s x(s)-F(x(s))$ with $s=\dfrac{dF}{dx}$.
2. Courant, R., and Hilbert, D. *Methods of Mathematical Physics*, Vol. 1. Wiley-VCH, 1991. — $\Phi = p\dfrac{du}{dx}-F$ with inverse $\dfrac{du}{dx}=\dfrac{\partial\Phi}{\partial p}$.
