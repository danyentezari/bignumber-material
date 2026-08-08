# Envelope of Tangent Lines

A curve that is used to touch each line in a one-parameter family of tangent lines at a single point.

Note: Also called the envelope of a family of curves when the family consists of lines.

## Applications

1. Recovers a graph from the family of all its tangent lines.
2. Locates caustics formed by reflected or refracted light rays.
3. Describes wave fronts as limiting curves of neighboring fronts.
4. Gives a geometric picture of the Legendre transform through supporting lines.

<i>

**definition [d]** (*Envelope of a Family of Curves*) From Riley, Hobson, and Bence: for a family of curves

- $f(x,y,\alpha) = 0$ ,

the envelope is the curve traced by the limiting intersection of neighboring members of the family. Its points satisfy

- $f(x,y,\alpha) = 0$

and

- $\dfrac{\partial f}{\partial\alpha}(x,y,\alpha) = 0$ ,

after the parameter $\alpha$ is eliminated.

where

- $f$ is a function that defines the family of curves.
- $x$ and $y$ are coordinates in the plane.
- $\alpha$ is the parameter that labels members of the family.
- $\dfrac{\partial f}{\partial\alpha}$ is the partial derivative of $f$ with respect to $\alpha$.

</i>

## Elementary Example

### Simple

For the family of tangent lines to $y = \dfrac{1}{2}x^{2}$,

$$
f(x,y,a) = y - a x + \dfrac{1}{2}a^{2} = 0
$$

$$
\dfrac{\partial f}{\partial a} = -x + a = 0
$$

so $a = x$ and the envelope is $y = \dfrac{1}{2}x^{2}$.

where

- $f$ defines the family of tangent lines.
- $a$ is the point of tangency used as a parameter.
- $x$ and $y$ are coordinates in the plane.

### General

For the family of tangent lines to $y = F(x)$ at $x = a$,

$$
f(x,y,a) = y - F(a) - \dfrac{dF}{da}(a)\,(x - a) = 0
$$

$$
\dfrac{\partial f}{\partial a} = 0
$$

eliminates $a$ and recovers the graph of $F$.

where

- $F$ is a differentiable function of one variable.
- $a$ is the parameter labeling the tangent line.
- $\dfrac{dF}{da}$ is the derivative of $F$ evaluated at $a$.
- $f$ defines the family of tangent lines.
- $x$ and $y$ are coordinates in the plane.

## References

1. Riley, K. F., Hobson, M. P., and Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006. — envelope of $f(x,y,\alpha)=0$ by eliminating $\alpha$ from $f=0$ and $\dfrac{\partial f}{\partial\alpha}=0$.
