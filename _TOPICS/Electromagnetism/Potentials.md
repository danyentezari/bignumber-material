# Potentials

A pair of fields, a scalar potential and a vector potential, that is used to express the electric and magnetic fields by differentiation, where a scalar potential is a number assigned to each point in space, and where a vector potential is a vector assigned to each point in space.

The magnetic vector potential. Because the magnetic field has vanishing divergence, it is the curl of a vector potential. This principle is used to write the magnetic field so that Gauss's law for magnetism is automatic.

The magnetic field from the vector potential is

$$
\mathbf{B} = \nabla\times\mathbf{A}
$$

where

- $\mathbf{B}$ is the magnetic field.
- $\nabla\times$ is the curl.
- $\mathbf{A}$ is the magnetic vector potential.

Reconstruction of the fields from the potentials. In time-dependent electrodynamics the electric field is minus the gradient of the scalar potential minus the time derivative of the vector potential. This principle is used to recover the physical fields after the potentials have been found.

The electric field from the potentials is

$$
\mathbf{E} = -\nabla V - \dfrac{\partial\mathbf{A}}{\partial t}
$$

where

- $\mathbf{E}$ is the electric field.
- $\nabla$ is the gradient.
- $V$ is the electric scalar potential.
- $\mathbf{A}$ is the magnetic vector potential.
- $t$ is time.

Gauge freedom. The physical fields depend only on derivatives of the potentials, so many different potentials describe the same fields. Gauge freedom is that latitude in the choice of potentials. This principle is used to impose a convenient condition that simplifies Maxwell's equations.

The fields are unchanged when

$$
\nabla\times\mathbf{A}' = \nabla\times\mathbf{A}
$$

and

$$
-\nabla V' - \dfrac{\partial\mathbf{A}'}{\partial t} = -\nabla V - \dfrac{\partial\mathbf{A}}{\partial t}
$$

where

- $\mathbf{A}$ and $V$ are one pair of potentials.
- $\mathbf{A}'$ and $V'$ are another pair of potentials that give the same fields.

Gauge transformations. A gauge transformation shifts the potentials by an arbitrary scalar function without changing the fields. A gauge function is a differentiable scalar function of position and time. This principle is used to pass from one convenient potential pair to another.

The gauge transformation is

$$
\mathbf{A}' = \mathbf{A} + \nabla\lambda
$$

$$
V' = V - \dfrac{\partial\lambda}{\partial t}
$$

where

- $\mathbf{A}'$ and $V'$ are the transformed potentials.
- $\mathbf{A}$ and $V$ are the original potentials.
- $\lambda$ is the gauge function.
- $t$ is time.

The Coulomb gauge. The Coulomb gauge sets the divergence of the vector potential to zero, so the scalar potential obeys the Poisson equation of electrostatics. This principle is used when a simple scalar potential is wanted.

The Coulomb gauge condition is

$$
\nabla\cdot\mathbf{A} = 0
$$

where

- $\nabla\cdot$ is the divergence.
- $\mathbf{A}$ is the magnetic vector potential.

The Lorenz gauge. The Lorenz gauge relates the divergence of the vector potential to the time derivative of the scalar potential, so each potential obeys a wave equation. This principle is used to decouple the potential equations in electrodynamics.

The Lorenz gauge condition is

$$
\nabla\cdot\mathbf{A} = -\mu_{0}\epsilon_{0}\dfrac{\partial V}{\partial t}
$$

where

- $\nabla\cdot$ is the divergence.
- $\mathbf{A}$ is the magnetic vector potential.
- $\mu_{0}$ is the permeability of free space.
- $\epsilon_{0}$ is the permittivity of free space.
- $V$ is the electric scalar potential.
- $t$ is time.

Note: Also called the electromagnetic potentials.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §10.1 — potentials, gauge freedom, Coulomb gauge, and Lorenz gauge.
