# Legendre Transform Derivation

A derivation of the Legendre transform that is used to change the independent variables of a function by subtracting a product of conjugate variables.

<i>

**definition [d]** (*Legendre Transform Derivation*) From Boas, Chapter 4, Section 11: start from a function $f(x,y)$ and write its differential

- $df = p\, dx + q\, dy$ ,

where

- $p = \left(\dfrac{\partial f}{\partial x}\right)_{y}$ , $\qquad q = \left(\dfrac{\partial f}{\partial y}\right)_{x}$ .

To change the independent variables from $(x,y)$ to $(x,q)$, define a new function by the Legendre transformation

- $g = f - q y$ .

Its differential is

- $dg = df - q\, dy - y\, dq = (p\, dx + q\, dy) - q\, dy - y\, dq$ ,

which simplifies to

- $dg = p\, dx - y\, dq$ .

Thus $g = g(x,q)$, with

- $\left(\dfrac{\partial g}{\partial x}\right)_{q} = p$ , $\qquad \left(\dfrac{\partial g}{\partial q}\right)_{x} = -y$ .

The same method replaces the $p\, dx$ term by forming

- $h = f - x p$ ,

so that

- $dh = q\, dy - x\, dp$

and $h = h(p,y)$.

where

- $f$ is the original function.
- $x$ and $y$ are the original independent variables.
- $df$ is the total differential of $f$.
- $p$ and $q$ are the partial derivatives of $f$ that appear as coefficients in $df$.
- $g$ is the Legendre transform of $f$ that makes $q$ an independent variable.
- $dg$ is the total differential of $g$.
- $h$ is the Legendre transform of $f$ that makes $p$ an independent variable.
- $dh$ is the total differential of $h$.
- $dx$, $dy$, $dp$, and $dq$ are the differentials of $x$, $y$, $p$, and $q$.

</i>

## Elementary Example

### Simple

For $f(x,y) = \dfrac{1}{2}y^{2} + x$,

$$
q = \left(\dfrac{\partial f}{\partial y}\right)_{x} = y,\qquad g = f - q y = x - \dfrac{1}{2}q^{2}
$$

where

- $f$ is the original function.
- $x$ and $y$ are the original variables.
- $q$ is the conjugate coefficient of $dy$.
- $g$ is the Legendre transform.

### General

For $f(x,y) = \dfrac{1}{2}m y^{2} + U(x)$ with constant $m > 0$,

$$
q = m y,\qquad y = \dfrac{q}{m},\qquad g(x,q) = U(x) - \dfrac{q^{2}}{2m}
$$

where

- $f$ is the original function.
- $m$ is a positive constant.
- $U(x)$ is a function of $x$ alone.
- $q$ is the conjugate coefficient of $dy$.
- $g$ is the Legendre transform.

## References

1. Boas, M. L. *Mathematical Methods in the Physical Sciences*. 3rd ed. Wiley, 2005. Chapter 4, Section 11: Change of Variables — $df=p\,dx+q\,dy$, $g=f-qy$, $dg=p\,dx-y\,dq$, and $h=f-xp$.
