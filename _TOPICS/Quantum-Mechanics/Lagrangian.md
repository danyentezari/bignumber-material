# Lagrangian

A function that is used to encode the difference between kinetic energy and potential energy for the equations of motion and for the phase of a quantum path.

1\. The Lagrangian is kinetic energy minus potential energy. This principle is used to write $L$ for a particle in a potential.

The Lagrangian is

$$
L = T - V
$$

where

- $L$ is the Lagrangian.
- $T$ is the kinetic energy.
- $V$ is the potential energy.

2\. In generalized coordinates, $L$ is a function of the coordinates, the velocities, and possibly time. This principle is used to write the Euler-Lagrange equations.

The Lagrangian in generalized coordinates is

$$
L = L\Bigl(t,\, q_{1},\ldots,q_{m},\, \dfrac{dq_{1}}{dt},\ldots,\dfrac{dq_{m}}{dt}\Bigr)
$$

where

- $q_{1},\ldots,q_{m}$ are generalized coordinates.
- $\dfrac{dq_{i}}{dt}$ are generalized velocities.
- $t$ is time.

3\. The action is the time integral of $L$, and the classical path makes the action stationary. This principle is used to derive the equations of motion.

The action is

$$
S = \displaystyle\int_{t_{i}}^{t_{f}} L\,dt
$$

where

- $S$ is the action.
- $L$ is the Lagrangian.
- $t$ is time.

4\. In the path-integral formulation, each path contributes a phase $e^{iS/\hbar}$. This principle is used to compute quantum amplitudes from the same $L$ that governs classical motion.

Note: These principles are $L=T-V$, the generalized-coordinate Lagrangian, stationary action, and the path-integral phase. Also denoted $L$.

## References

1. Park, D. *Introduction to the Quantum Theory*. Dover, 2005. — $L=T-V$ with $T$ kinetic and $V$ potential energy of the whole system.
2. Simmons, G. F. *Differential Equations with Applications and Historical Notes*. Chapman and Hall/CRC, 2017. — $L=T-V$ as a function of $t$, $q_{j}$, and $\mathrm{d}q_{j}/\mathrm{d}t$.
3. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — $L(q_{a},\mathrm{d}q_{a}/\mathrm{d}t;t)=T-V$.
4. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — $L=T-V$ in the path-integral formulation.
