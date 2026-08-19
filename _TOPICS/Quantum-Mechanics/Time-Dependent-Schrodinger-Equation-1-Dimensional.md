# Time Dependent Schrodinger Equation 1-Dimensional

A linear partial differential equation that is used to compute the wavefunction of one particle moving along a single axis.

The one-dimensional time-dependent Schrödinger equation. For a particle of mass $m$ on the $x$ axis, the Schrödinger equation is the quantum analog of Newton's second law. This principle is used to determine $\Psi(x,t)$ from $V(x,t)$ and the initial wavefunction.

The one-dimensional time-dependent Schrödinger equation is

$$
i\hbar\dfrac{\partial\Psi}{\partial t} = -\dfrac{\hbar^{2}}{2m}\dfrac{\partial^{2}\Psi}{\partial x^{2}} + V\Psi
$$

where

- $i$ is the imaginary unit.
- $\hbar$ is the reduced Planck constant.
- $\Psi$ is the wavefunction.
- $m$ is the mass of the particle.
- $V$ is the potential energy.
- $x$ is the position.
- $t$ is time.

The kinetic-energy operator. The first term on the right is the kinetic-energy operator. This principle is used to identify $-\dfrac{\hbar^{2}}{2m}\dfrac{\partial^{2}}{\partial x^{2}}$ with $p^{2}/2m$.

Uniqueness from initial data. Given $\Psi(x,0)$ and $V$, the equation determines $\Psi(x,t)$ at every later time. This principle is used to treat the Schrödinger equation as an initial-value problem.

## References

1. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — one-dimensional time-dependent Schrödinger equation.
2. Griffiths, D. J. *Introduction to Quantum Mechanics*. Cambridge University Press, 2018. §1.2 — $\Psi(x,t)$ in one dimension.
