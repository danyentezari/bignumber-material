# Differential Equations and Integral Equations

## Differential Equations

An equation relating a function to its derivative that is used to calculate the change of a variable over a domain.

<i>

**definition [d]** (*Differential Equation*) From Stewart: an equation that contains an unknown function and one or more of its derivatives.

</i>

<i>

**definition [d]** (*Ordinary Differential Equation = ODE*) From Kreyszig: an equation that contains one or several derivatives of an unknown function, which we usually call $y(x)$ (or $y(t)$ if the independent variable is time $t$). The equation may also contain $y$ itself, known functions of $x$ (or $t$), and constants.

where

- $y$ is the unknown function.
- $x$ (or $t$) is the independent variable.

</i>

<i>

**definition [d]** (*Ordinary Differential Equation = ODE*) From Hassani: the most general ODE can be expressed as

- $\displaystyle G\left(x,\, y,\, \dfrac{dy}{dx},\, \dfrac{d^{2}y}{dx^{2}},\, \ldots,\, \dfrac{d^{n}y}{dx^{n}}\right) = 0$

in which $G: \mathbb{R}^{n+2} \rightarrow \mathbb{R}$ is a real-valued function of $n+2$ real variables. When $G$ depends explicitly and nontrivially on $\dfrac{d^{n}y}{dx^{n}}$, the equation is called an $n$th-order ODE.

where

- $y$ is the unknown function of $x$.
- $n$ is the order of the ODE.
- $G$ is a real-valued function of the listed arguments.

</i>

## Integral Equations

An equation containing an integral of a function that is used to determine a solution of the function over a domain.

<i>

**definition [d]** (*Integral Equation*) From Stewart: an equation that contains an unknown function $y(x)$ and an integral that involves $y(x)$.

</i>

<i>

**definition [d]** (*Integral Equation*) From Griffel: an equation in which the unknown function appears under an integral sign.

</i>

<i>

**definition [d]** (*Integral Equation*) From Hassani: if the unknown function appears only inside the integral, the integral equation is said to be of the first kind. Integral equations having the unknown function outside the integral as well as inside are said to be of the second kind. The four kinds can be written as follows:

- $\displaystyle \int_{a}^{x} K(x,t)\, u(t)\, dt = v(x)$ \quad (Volterra equation of the 1st kind)
- $\displaystyle \int_{a}^{b} K(x,t)\, u(t)\, dt = v(x)$ \quad (Fredholm equation of the 1st kind)
- $\displaystyle u(x) = v(x) + \int_{a}^{x} K(x,t)\, u(t)\, dt$ \quad (Volterra equation of the 2nd kind)
- $\displaystyle u(x) = v(x) + \int_{a}^{b} K(x,t)\, u(t)\, dt$ \quad (Fredholm equation of the 2nd kind)

In all these equations, $K(x,t)$ is called the kernel of the integral equation.

where

- $u$ is the unknown function.
- $v$ is a given function.
- $K$ is the kernel.
- $a$, $b$, $x$, $t$ are real variables in the stated ranges.

</i>

## References

1. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. — differential equation; ordinary differential equation.
2. Stewart, J. *Calculus: Early Transcendentals*. — differential equation; integral equation.
3. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006. — differential equations as equations containing derivatives.
4. Hassani, S. *Mathematical Physics*, 2nd ed. Springer. — general ODE; Volterra and Fredholm integral equations; kernel.
5. Griffel, D. H. *Applied Functional Analysis*. Ellis Horwood. — integral equation as unknown under an integral sign.
