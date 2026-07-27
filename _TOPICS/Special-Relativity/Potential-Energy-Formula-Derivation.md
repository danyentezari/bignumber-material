# Potential Energy Formula Derivation

A derivation of the potential energy formula that is used to obtain $U(x_{2})-U(x_{1})=-\displaystyle\int_{x_{1}}^{x_{2}} F(x)\, dx$ from the work-energy theorem.

Related definitions:

- [Gravitational Potential Energy Formula Derivation](Gravitational-Potential-Energy-Formula-Derivation.md)
- [Elastic Potential Energy Formula Derivation](Elastic-Potential-Energy-Formula-Derivation.md)

<i>

**definition [d]** (*Potential Energy Formula Derivation*) From Shankar: start from the rate of change of kinetic energy

- $\dfrac{dK}{dt} = \dfrac{d}{dt}\left(\dfrac{1}{2}mv^{2}\right) = m\dfrac{dv}{dt}\, v$ .

With $F(x) = m\,\dfrac{dv}{dt}$ and $v = \dfrac{dx}{dt}$,

- $\dfrac{dK}{dt} = F(x)\dfrac{dx}{dt}$ .

Integrating from $t_{1}$ to $t_{2}$ gives the work-energy theorem

- $K(t_{2}) - K(t_{1}) = \displaystyle\int_{x_{1}}^{x_{2}} F(x)\, dx$ .

Writing the integral via an antiderivative $G$ with $\dfrac{dG}{dx} = F(x)$,

- $K_{2} - K_{1} = G(x_{2}) - G(x_{1})$ ,

hence

- $K_{2} - G(x_{2}) = K_{1} - G(x_{1})$ .

Setting $U(x) = -G(x)$ so that $F(x) = -\dfrac{dU}{dx}$ yields conservation

- $K_{2} + U_{2} = K_{1} + U_{1}$

and the potential-energy change

- $U(x_{2}) - U(x_{1}) = -\displaystyle\int_{x_{1}}^{x_{2}} F(x)\, dx$ .

where

- $K$ is the kinetic energy.
- $\dfrac{dK}{dt}$ is the rate of change of kinetic energy.
- $t$ is time.
- $m$ is the mass.
- $v$ is the velocity.
- $\dfrac{dv}{dt}$ is the acceleration.
- $F(x)$ is a position-dependent force.
- $x$ is the position.
- $dx$ is the position differential.
- $\dfrac{dx}{dt}$ is the velocity written as a derivative of position.
- $t_{1}$ and $t_{2}$ are the initial and final times.
- $x_{1}$ and $x_{2}$ are the initial and final positions.
- $K(t_{1})$ and $K(t_{2})$ are the kinetic energies at those times.
- $K_{1}$ and $K_{2}$ are the same kinetic energies at $x_{1}$ and $x_{2}$.
- $G(x)$ is an antiderivative of $F$.
- $\dfrac{dG}{dx}$ is the derivative of $G$ with respect to $x$.
- $U(x)$ is the potential energy.
- $U_{1}$ and $U_{2}$ are the potential energies at $x_{1}$ and $x_{2}$.
- $U(x_{1})$ and $U(x_{2})$ are the same potential energies written as functions of position.
- $\dfrac{dU}{dx}$ is the derivative of $U$ with respect to $x$.
- $\displaystyle\int_{x_{1}}^{x_{2}} F(x)\, dx$ is the work done by $F$ from $x_{1}$ to $x_{2}$.
- $W = \displaystyle\int_{x_{1}}^{x_{2}} F(x)\, dx$ is that work.
- $\Delta U = -W$ is the change in potential energy.

</i>

## Elementary Example

### Simple

For a constant force $F = 4\,\mathrm{N}$ from $x_{1} = 0$ to $x_{2} = 3\,\mathrm{m}$,

$$
U(x_{2}) - U(x_{1}) = -\int_{0}^{3} 4\, dx = -12\,\mathrm{J}
$$

where

- $F$ is the constant force.
- $x_{1}$ is the initial position.
- $x_{2}$ is the final position.
- $dx$ is the position differential.
- $U(x_{1})$ is the initial potential energy.
- $U(x_{2})$ is the final potential energy.
- $W = \displaystyle\int_{x_{1}}^{x_{2}} F\, dx$ is the work done by $F$.
- $\Delta U = -W$ is the change in potential energy.

### General

For $F(x) = -6x$ from $x_{1} = 1$ to $x_{2} = 2$,

$$
U(2) - U(1) = -\int_{1}^{2} (-6x)\, dx = 9\,\mathrm{J}
$$

where

- $F(x)$ is the position-dependent force.
- $x$ is the position.
- $x_{1}$ is the initial position.
- $x_{2}$ is the final position.
- $dx$ is the position differential.
- $U(1)$ is the potential energy at $x = 1$.
- $U(2)$ is the potential energy at $x = 2$.
- $W = \displaystyle\int_{1}^{2} F(x)\, dx$ is the work done by $F$.
- $\Delta U = -W$ is the change in potential energy.

## References

1. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — from $\dfrac{dK}{dt} = F\,\dfrac{dx}{dt}$ to $U(x_{2})-U(x_{1})=-\int F\,dx$.
