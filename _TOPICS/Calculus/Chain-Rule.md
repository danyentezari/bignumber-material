# Chain Rule

A differentiation rule for a composition of functions that is used to compute the derivative of a composite mapping from the derivatives of its inner and outer factors.

Note: Also called the composite function rule.

<i>

**definition [d]** (*Chain Rule*) From Stewart: if $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then the composite $F = f \circ g$ defined by $F(x) = f(g(x))$ is differentiable at $x$ and

- $\dfrac{dF}{dx} = \dfrac{df}{du}\bigg|_{u=g(x)}\, \dfrac{dg}{dx}$ .

Equivalently, if $y = f(u)$ and $u = g(x)$, then

- $\dfrac{dy}{dx} = \dfrac{dy}{du}\, \dfrac{du}{dx}$ .

where

- $g$ is the inner function.
- $f$ is the outer function.
- $F = f \circ g$ is the composite function.
- $x$ is the independent variable.
- $u = g(x)$ is the intermediate variable.
- $y = f(u)$ is the dependent variable.
- $\dfrac{dF}{dx}$ is the derivative of $F$ with respect to $x$.
- $\dfrac{df}{du}\bigg|_{u=g(x)}$ is the derivative of $f$ with respect to $u$, evaluated at $u = g(x)$.
- $\dfrac{dg}{dx}$ is the derivative of $g$ with respect to $x$.
- $\dfrac{dy}{dx}$ is the derivative of $y$ with respect to $x$.
- $\dfrac{dy}{du}$ is the derivative of $y$ with respect to $u$.
- $\dfrac{du}{dx}$ is the derivative of $u$ with respect to $x$.

</i>

<i>

**definition [d]** (*Chain Rule*) From Stewart: if $n$ is any real number and $u = g(x)$ is differentiable, then

- $\dfrac{d}{dx}\bigl[u^{n}\bigr] = n u^{n-1}\, \dfrac{du}{dx}$ .

where

- $n$ is a real exponent.
- $u = g(x)$ is a differentiable function of $x$.
- $x$ is the independent variable.
- $\dfrac{d}{dx}$ is differentiation with respect to $x$.
- $\dfrac{du}{dx}$ is the derivative of $u$ with respect to $x$.

</i>

## Elementary Example

### Simple

For $y = (x^{2} + 1)^{3}$, take $u = x^{2} + 1$ and $y = u^{3}$.

$$
\dfrac{dy}{dx} = 3u^{2}\, \dfrac{du}{dx} = 3(x^{2} + 1)^{2}\cdot (2x) = 6x(x^{2} + 1)^{2}
$$

where

- $x$ is the independent variable.
- $u = x^{2} + 1$ is the inner function.
- $y = u^{3}$ is the outer function of $u$.
- $\dfrac{du}{dx} = 2x$ is the derivative of the inner function.
- $\dfrac{dy}{du} = 3u^{2}$ is the derivative of the outer function.
- $\dfrac{dy}{dx}$ is the derivative of the composite.

### General

For $T = \dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2}$ with $x = x(t)$, the chain rule gives

$$
\dfrac{dT}{dt} = m\, \dfrac{dx}{dt}\, \dfrac{d^{2}x}{dt^{2}}
$$

where

- $t$ is time.
- $x(t)$ is the displacement.
- $\dfrac{dx}{dt}$ is the velocity.
- $\dfrac{d^{2}x}{dt^{2}}$ is the acceleration.
- $m$ is the mass.
- $T$ is the kinetic energy.
- $\dfrac{dT}{dt}$ is the time derivative of $T$.

## References

1. Stewart, J. *Calculus*. — chain rule $\dfrac{dF}{dx}=\dfrac{df}{du}\dfrac{dg}{dx}$; Leibniz form $\dfrac{dy}{dx}=\dfrac{dy}{du}\dfrac{du}{dx}$; power form $\dfrac{d}{dx}[u^{n}]=nu^{n-1}\dfrac{du}{dx}$.
