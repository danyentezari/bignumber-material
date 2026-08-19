# Gauge

A choice of potentials for the electromagnetic field that is used to fix unphysical freedom while leaving the physical fields unchanged.

Gauge freedom of the potentials. The potentials $V$ and $\mathbf{A}$ are not unique. For any scalar function $\lambda$ one may shift the potentials together without changing $\mathbf{E}$ and $\mathbf{B}$. This principle is used to impose an extra condition that simplifies the equations.

A gauge transformation of the potentials is

$$
\mathbf{A}' = \mathbf{A} + \nabla\lambda
$$

$$
V' = V - \dfrac{\partial\lambda}{\partial t}
$$

where

- $V$ is the electric scalar potential.
- $\mathbf{A}$ is the magnetic vector potential.
- $\lambda$ is an arbitrary scalar function of position and time.
- $t$ is time.

The Coulomb gauge. The Coulomb gauge sets the divergence of $\mathbf{A}$ to zero. This principle is used in magnetostatics and in instantaneous Coulomb problems.

The Coulomb gauge condition is

$$
\nabla\cdot\mathbf{A} = 0
$$

where

- $\mathbf{A}$ is the vector potential.

The Lorenz gauge. The Lorenz gauge relates $V$ and $\mathbf{A}$ so that both potentials obey wave equations. This principle is used in radiation problems.

The Lorenz gauge condition is

$$
\nabla\cdot\mathbf{A} + \dfrac{1}{c^{2}}\dfrac{\partial V}{\partial t} = 0
$$

where

- $\mathbf{A}$ is the vector potential.
- $V$ is the scalar potential.
- $c$ is the speed of light.
- $t$ is time.

Note: Also called a gauge choice. Also called working in a gauge.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — gauge freedom and gauge transformations of $V$ and $\mathbf{A}$.
2. Frankel, T. *The Geometry of Physics: An Introduction*. Cambridge University Press, 2012. — gauge transformation as a local change of fiber frame.
3. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. Matrix Editions, 2015. — working in a different gauge as a change of bundle coordinates.
