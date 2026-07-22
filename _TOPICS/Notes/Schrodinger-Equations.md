# Schrodinger Equations

<i>

**definition** (*Time Dependent Schrödinger Equation 1-Dimensional*) The specific case of the fundamental law of quantum mechanics tailored for a single particle of mass $m$ constrained to move in one dimension along the $x$-axis. It serves as a direct quantum analog to Newton’s second law, determining the particle's wave function $\Psi(x, t)$ for all future time given the potential energy $V(x, t)$ and initial conditions. It is expressed as:

- $i\hbar \dfrac{\partial \Psi}{\partial t} = -\dfrac{\hbar^2}{2m} \dfrac{\partial^2 \Psi}{\partial x^2} + V\Psi$

where

- $i$ is the imaginary unit
- $\hbar$ is the reduced Planck constant
- $\Psi$ is the wave function, which depends on position $x$ and time $t$
- $m$ is the mass of the particle
- $V$ is the potential energy function
- $x$ is the position coordinate
- $t$ is time.

</i>

<i>

**definition** (*Time Dependent Schrödinger Equation — Generalized*) The coordinate-independent and dimension-independent form of the fundamental law of quantum mechanics. This abstract version represents the general principle that a quantum state changes continuously and unitarily over time, governing the evolution of any quantum system—including those with multiple particles or non-spatial degrees of freedom. The general time-dependent form is:

- $i\hbar \dfrac{\partial \Psi}{\partial t} = \hat{H}\Psi$

where

- $i$ is the imaginary unit
- $\hbar$ is the reduced Planck constant
- $\Psi$ is the state-vector representing the state of the system
- $t$ is time
- $\hat{H}$ is the Hamiltonian operator representing the total energy of the system.


Note:

- $\Psi$ is also written $|\Psi\rangle$.
- $\Psi$ is also called the wave function.
- the total energy is kinetic energy plus potential energy.
</i>



The **time-independent** version is a specific "eigenvalue equation" used when the potential energy $V$ does not change with time. It is used to find **permitted energy levels** and **stationary states**—states where the probability density remains constant even though the wave function carries a "time-dependent wiggle factor".


<i>

**definition** (*Schrödinger Equation — Time-Independent*) An eigenvalue equation used to determine the stationary states and quantized energy levels of a quantum system when the potential energy is independent of time. It determines the spatial part of the wave function $\psi$ and the allowed energy values $E$ that the system can possess. The generalized form is:

- $\hat{H}\psi = E\psi$

where

- $\hat{H}$ is the Hamiltonian operator representing the total energy of the system.
- $\psi$ is the spatial wave function.
- $E$ is the energy of the state.

Note:

- $\psi$ is lower-case psi.
- $\psi$ is an eigenfunction of $\hat{H}$.
- $E$ is the corresponding eigenvalue.

</i>

In one dimension, this is explicitly written as:

- $-\dfrac{\hbar^2}{2m} \dfrac{d^2\psi}{dx^2} + V\psi = E\psi$.