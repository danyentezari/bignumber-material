# Partial Derivative

A derivative of a function of more than one variable that is used to compute the change of the function when one variable changes and every other variable is held constant.

Note: Also written $\dfrac{\partial f}{\partial x}$. Also written $D_{i}f$. Also written $f_{x}$. Also written $z_{x}$.

<i>

**definition [d]** (*Partial Derivative = $D_{i}f$*) From Hubbard: let $U$ be an open subset of $\mathbb{R}^{n}$ and let $f:U\rightarrow\mathbb{R}$ be a function. The partial derivative of $f$ with respect to the $i$th variable, evaluated at $a$, is the limit

- $\displaystyle D_{i}f(a) = \lim_{h \to 0} \dfrac{f(a_{1},\ldots,a_{i}+h,\ldots,a_{n}) - f(a_{1},\ldots,a_{i},\ldots,a_{n})}{h}$

if the limit exists.

where

- $U$ is an open set in $\mathbb{R}^{n}$.
- $n$ is the dimension.
- $f$ is a real-valued function on $U$.
- $a = (a_{1},\ldots,a_{n})$ is a point of $U$.
- $i$ is the index of the variable that changes.
- $h$ is the increment in the $i$th variable.
- $D_{i}f(a)$ is the partial derivative of $f$ with respect to the $i$th variable at $a$.

</i>

<i>

**definition [d]** (*Partial Derivative = $\left(\dfrac{\partial z}{\partial x}\right)_{y}$*) From Levine: let $z$ be a function of $x$ and $y$, written $z = f(x,y)$. The partial derivative of $z$ with respect to $x$ is

- $\displaystyle \left(\dfrac{\partial z}{\partial x}\right)_{y} \equiv \lim_{\Delta x \to 0} \dfrac{f(x+\Delta x,y) - f(x,y)}{\Delta x}$ .

where

- $z = f(x,y)$ is a real-valued function of two variables.
- $x$ and $y$ are the independent variables.
- $\Delta x$ is the increment in $x$.
- $\left(\dfrac{\partial z}{\partial x}\right)_{y}$ is the partial derivative of $z$ with respect to $x$ with $y$ held constant.

</i>

Other variables held constant. A partial derivative in one variable treats every remaining independent variable as a constant. From Boas, hold $y$ constant and find $\dfrac{\partial z}{\partial x}$. This principle is used to reduce a function of more than one variable to a derivative in a single variable.

Difference quotient limit. The partial derivative at a point is the limit of the change in the function divided by the change in one variable, with every other variable fixed. This principle is used to define the partial derivative from the same limit that defines a derivative of a function of one variable.

The two-variable limit is

$$
\dfrac{\partial z}{\partial x} = \lim_{\Delta x \to 0} \dfrac{f(x+\Delta x,y) - f(x,y)}{\Delta x}
$$

where

- $z = f(x,y)$ is the function.
- $x$ is the variable that changes.
- $y$ is the variable held constant.
- $\Delta x$ is the increment in $x$.

First partials in each variable. A function of two variables has a first partial derivative in $x$ and a first partial derivative in $y$. This principle is used to compute each first-order derivative separately, with the other variable held constant.

## Examples

### Simple

Let $z = x^{3} - 3xy + 2y^{2}$ be a function of two real variables. Hold one variable constant and differentiate.

$$
\dfrac{\partial z}{\partial x} = 3x^{2} - 3y
$$

$$
\dfrac{\partial z}{\partial y} = -3x + 4y
$$

where

- $x$ and $y$ are the independent variables.
- $z$ is the dependent variable.

### General

Let $z = x^{2}y^{3} + e^{yx}$ be a function of the real variables $x$ and $y$. Each partial treats the other variable as a constant.

$$
\left(\dfrac{\partial z}{\partial x}\right)_{y} = 2xy^{3} + y e^{yx}
$$

$$
\left(\dfrac{\partial z}{\partial y}\right)_{x} = 3x^{2}y^{2} + x e^{yx}
$$

where

- $x$ and $y$ are the independent variables.
- $z$ is the dependent variable.
- $e^{yx}$ is the exponential of the product $yx$.

## References

1. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. 5th ed. Matrix Editions, 2015. §1.7 — Definition 1.7.3, partial derivative $D_{i}f(a)$ as a one-variable limit.
2. Levine, I. *Physical Chemistry*. 6th ed. McGraw-Hill, 2008. §1.6 — definition (1.29) of $\left(\dfrac{\partial z}{\partial x}\right)_{y}$; example $z=x^{2}y^{3}+e^{yx}$.
3. Boas, M. L. *Mathematical Methods in the Physical Sciences*. 3rd ed. Wiley, 2005. Chapter 4, §1 — hold $y$ constant and find $\dfrac{\partial z}{\partial x}$; notation $\dfrac{\partial f}{\partial x}\equiv\dfrac{\partial z}{\partial x}\equiv f_{x}\equiv z_{x}$.
4. Aleksandrov, A. D., Kolmogorov, A. N., & Lavrent’ev, M. A. *Mathematics: Its Content, Methods and Meaning*. Vol. 1. Dover, 1999. Chapter II, §12 — partial derivative with respect to $x$ denoted $\dfrac{\partial z}{\partial x}$ and $\dfrac{\partial f}{\partial x}$.
5. Bronson, R., & Costa, G. B. *Schaum's Outline of Differential Equations*. 5th ed. McGraw-Hill, 2021. Chapter 1, Lesson 3 — example $z=x^{3}-3xy+2y^{2}$ with $\dfrac{\partial z}{\partial x}=3x^{2}-3y$ and $\dfrac{\partial z}{\partial y}=-3x+4y$.
