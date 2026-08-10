# Lagrangian

A function that is used to encode the difference between kinetic energy and potential energy for the equations of motion.

Note: Also denoted $L$.

## Applications

1. Supplies the integrand of the action in the principle of least action.
2. Yields the Euler–Lagrange equations for generalized coordinates.
3. Builds the Hamiltonian by a Legendre transform in the velocities.
4. Enters the phase of the path integral in quantum mechanics.
5. Extends to relativistic and field theories through generalized Lagrangians.

<i>

**definition [d]** (*Lagrangian*) From Park: the Lagrangian is

- $L = T - V$ ,

where $T$ is the kinetic energy and $V$ is the potential energy of the whole system.

where

- $L$ is the Lagrangian.
- $T$ is the kinetic energy.
- $V$ is the potential energy.

</i>

<i>

**definition [d]** (*Lagrangian*) From Simmons: the function $L = T - V$ is called the Lagrangian, and in terms of generalized coordinates it has the form

- $L = L\left(t,\, q_{1},\ldots,q_{m},\, \dfrac{dq_{1}}{dt},\ldots,\dfrac{dq_{m}}{dt}\right)$ .

where

- $L$ is the Lagrangian.
- $T$ is the kinetic energy.
- $V$ is the potential energy.
- $t$ is time.
- $q_{1},\ldots,q_{m}$ are generalized coordinates.
- $\dfrac{dq_{1}}{dt},\ldots,\dfrac{dq_{m}}{dt}$ are generalized velocities.
- $m$ is the number of generalized coordinates.

</i>

<i>

**definition [d]** (*Lagrangian*) From Emam: the non-relativistic Lagrangian function is

- $L\left(q_{a},\, \dfrac{dq_{a}}{dt};\, t\right) = T - V$ .

where

- $L$ is the Lagrangian.
- $q_{a}$ are generalized coordinates.
- $\dfrac{dq_{a}}{dt}$ are generalized velocities.
- $t$ is time.
- $T$ is the kinetic energy.
- $V$ is the potential energy.

</i>

## Elementary Example

### Simple

For a particle of mass $m = 2$ with $V(q) = 3q^{2}$,

$$
L = \dfrac{1}{2}m\left(\dfrac{dq}{dt}\right)^{2} - V(q) = \left(\dfrac{dq}{dt}\right)^{2} - 3q^{2}
$$

where

- $L$ is the Lagrangian.
- $m$ is the mass.
- $q$ is the coordinate.
- $\dfrac{dq}{dt}$ is the velocity.
- $V(q)$ is the potential energy.

### General

For $N$ degrees of freedom with kinetic energy $T\left(q,\dfrac{dq}{dt}\right)$ and potential energy $V(q)$,

$$
L\left(q,\, \dfrac{dq}{dt},\, t\right) = T\left(q,\, \dfrac{dq}{dt}\right) - V(q)
$$

where

- $N$ is the number of degrees of freedom.
- $L$ is the Lagrangian.
- $T$ is the kinetic energy.
- $V$ is the potential energy.
- $q$ and $\dfrac{dq}{dt}$ are the coordinates and velocities.
- $t$ is time.

## References

1. Park, D. *Introduction to the Quantum Theory*. Dover, 2005. — $L=T-V$ with $T$ kinetic and $V$ potential energy of the whole system.
2. Simmons, G. F. *Differential Equations with Applications and Historical Notes*. Chapman and Hall/CRC, 2017. — $L=T-V$ as a function of $t$, $q_{j}$, and $\mathrm{d}q_{j}/\mathrm{d}t$.
3. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — $L(q_{a},\mathrm{d}q_{a}/\mathrm{d}t;t)=T-V$.
4. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — $L=T-V$ in the path-integral formulation.
