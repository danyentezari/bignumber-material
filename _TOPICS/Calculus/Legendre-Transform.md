# Legendre Transform

A mapping that is used to replace a variable in a function by the derivative of that function with respect to the variable.

Note: Also called Legendre transformation.

## Applications

1. Builds the Hamiltonian from the Lagrangian in classical mechanics.
2. Changes independent variables in variational problems to canonical form.
3. Defines thermodynamic potentials such as enthalpy and free energy.
4. Converts convex optimization problems between dual variable sets.
5. Relates action formulations that use velocity to formulations that use momentum.

<i>

**definition [d]** (*Legendre Transform*) From Courant and Hilbert: the Legendre transformation connects

- $p = \dfrac{\partial F}{\partial\!\left(\dfrac{du}{dx}\right)}$

with

- $\Phi = p\dfrac{du}{dx} - F$ ,

and the inverse is

- $\dfrac{du}{dx} = \dfrac{\partial\Phi}{\partial p}$ , $\qquad F = p\dfrac{du}{dx} - \Phi$ .

where

- $F$ is the original function.
- $u$ is the dependent variable.
- $x$ is the independent variable.
- $\dfrac{du}{dx}$ is the derivative of $u$ with respect to $x$.
- $p$ is the new independent variable.
- $\Phi$ is the Legendre transform of $F$.

</i>

<i>

**definition [d]** (*Legendre Transform*) From Cahill: for a function $A(x,y)$, set

- $v = \dfrac{\partial A}{\partial y}$

and

- $B = A(x,y) - v y$ ,

so the independent variables change from $(x,y)$ to $(x,v)$.

Note: Cahill’s form $B=A-vy$ differs in sign from $\Phi = p\dfrac{du}{dx}-F$. Both change the independent variable from the original one to its conjugate slope.

where

- $A$ is the original function.
- $x$ and $y$ are the original independent variables.
- $v$ is the new variable.
- $B$ is the Legendre transform of $A$ in the $y$ direction.
- $\dfrac{\partial A}{\partial y}$ is the partial derivative of $A$ with respect to $y$.

</i>

## Elementary Example

### Simple

For $F(x) = \dfrac{1}{2}x^{2}$,

$$
p = \dfrac{dF}{dx} = x,\qquad G(p) = p\, x - F(x) = \dfrac{1}{2}p^{2}
$$

where

- $F$ is the original function.
- $x$ is the original variable.
- $p$ is the new variable.
- $G$ is the Legendre transform.

### General

For $F(x) = \dfrac{1}{2}m x^{2}$ with constant $m > 0$,

$$
p = m x,\qquad x = \dfrac{p}{m},\qquad G(p) = \dfrac{p^{2}}{2m}
$$

where

- $F$ is the original function.
- $m$ is a positive constant.
- $x$ is the original variable.
- $p$ is the new variable.
- $G$ is the Legendre transform.

## References

1. Courant, R., and Hilbert, D. *Methods of Mathematical Physics*, Vol. 1. Wiley-VCH, 1991. — $\Phi = p\dfrac{du}{dx}-F$ with $p=\partial F/\partial(du/dx)$.
2. Cahill, K. *Physical Mathematics*. Cambridge University Press, 2019. — $v=\partial A/\partial y$ and $B=A-vy$.
3. MIT OpenCourseWare. *8.223 Classical Mechanics II*, Lecture 15 (IAP 2017). [PDF](https://ocw.mit.edu/courses/8-223-classical-mechanics-ii-january-iap-2017/09ab68ae8e7987debc025892e00c0f1f_MIT8_223IAP17_Lec15.pdf) — Hamiltonian as Legendre transform of the Lagrangian.
