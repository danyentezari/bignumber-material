# Differential Equations and Integral Equations

## Differential Equations

An equation relating a function to its derivatives that is used to calculate the change of a variable over a domain.

The ordinary differential equation. An ordinary differential equation relates one independent variable, one unknown function, and derivatives of that function. This principle is used to write how a state changes with a single parameter such as time.

The general ordinary differential equation is

$$
G\left(x,\, y,\, \dfrac{dy}{dx},\, \dfrac{d^{2}y}{dx^{2}},\, \ldots,\, \dfrac{d^{n}y}{dx^{n}}\right) = 0
$$

where

- $y$ is the unknown function of $x$.
- $n$ is the order of the equation.
- $G$ is a real-valued function of the listed arguments.

Order of an ODE. When $G$ depends on the $n$th derivative, the equation is an $n$th-order ordinary differential equation. The order is that highest derivative that appears. This principle is used to count how many extra conditions are needed to fix a unique solution.

The linear ordinary differential equation. A linear equation contains the unknown and its derivatives only to the first power, and never as products of those quantities. This principle is used to split a hard problem into a sum of simpler solutions.

A linear ordinary differential equation of order $n$ is

$$
p_{0}(x)y + p_{1}(x)\dfrac{dy}{dx} + \cdots + p_{n}(x)\dfrac{d^{n}y}{dx^{n}} = q(x)
$$

where

- $y$ is the unknown function.
- $p_{0},\ldots,p_{n}$ are coefficient functions of $x$.
- $q$ is a given forcing term.

Superposition for linear equations. A sum of solutions of a linear homogeneous equation, scaled by constants, is again a solution. A homogeneous linear equation is a linear equation with zero forcing term. This principle is used to build the general solution from a basic set of solutions.

The nonlinear ordinary differential equation. A nonlinear equation is any differential equation that cannot be written in linear form. This principle is used to model systems whose response is not proportional to the unknown.

## Integral Equations

An equation containing an integral of an unknown function that is used to determine that function over a domain.

The integral equation. An integral equation is an equation in which the unknown function appears under an integral sign. This principle is used to state a problem by accumulating contributions rather than by writing a derivative.

First kind and second kind. In an equation of the first kind the unknown appears only inside the integral. In an equation of the second kind the unknown appears both outside the integral and inside it. This principle is used to classify integral equations by where the unknown sits.

The Volterra integral equation. A Volterra equation integrates from a fixed start to a variable upper limit. This principle is used to describe a causal accumulation of past influence up to the present value of the independent variable.

The Fredholm integral equation. A Fredholm equation integrates over a fixed interval. This principle is used to describe a global coupling across the whole domain.

The kernel. In all four standard kinds, $K(x,t)$ is the kernel of the integral equation. A kernel is the given weighting function inside the integral. This principle is used to encode how the value at $x$ depends on the unknown at $t$.

The Volterra equation of the first kind is

$$
\int_{a}^{x} K(x,t)\, u(t)\, dt = v(x)
$$

The Fredholm equation of the first kind is

$$
\int_{a}^{b} K(x,t)\, u(t)\, dt = v(x)
$$

The Volterra equation of the second kind is

$$
u(x) = v(x) + \int_{a}^{x} K(x,t)\, u(t)\, dt
$$

The Fredholm equation of the second kind is

$$
u(x) = v(x) + \int_{a}^{b} K(x,t)\, u(t)\, dt
$$

where

- $u$ is the unknown function.
- $v$ is a given function.
- $K$ is the kernel.
- $a$, $b$, $x$, and $t$ are real variables in the stated ranges.

Note: Also called an ODE when there is a single independent variable.

## References

1. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. — differential equation; ordinary differential equation.
2. Stewart, J. *Calculus: Early Transcendentals*. — differential equation; integral equation.
3. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006. — differential equations as equations containing derivatives.
4. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — general ODE; Volterra and Fredholm integral equations; kernel.
5. Griffel, D. H. *Applied Functional Analysis*. Ellis Horwood. — integral equation as unknown under an integral sign.
