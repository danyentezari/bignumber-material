# Probability Current

A vector field built from a wavefunction that is used to express the flow of probability density through space.

Note: Also called probability flux. Also called probability current density.

<i>

**definition [d]** (*Probability Flux = Probability Current*) From Sakurai: using Schrödinger’s time-dependent wave equation, it is straightforward to derive the continuity equation

- $\dfrac{\partial\rho}{\partial t} + \nabla\cdot\mathbf{j} = 0$ ,

where $\rho(x,t)$ stands for $|\psi|^{2}$ as before, and $\mathbf{j}(x,t)$, known as the probability flux, is given by

- $\mathbf{j}(x,t) = -\dfrac{i\hbar}{2m}\bigl[\psi^{*}\nabla\psi - (\nabla\psi^{*})\psi\bigr] = \dfrac{\hbar}{m}\operatorname{Im}(\psi^{*}\nabla\psi)$ .

where

- $\rho = |\psi|^{2}$ is the probability density.
- $\psi$ is the wavefunction.
- $\mathbf{j}$ is the probability flux.
- $m$ is the particle mass.
- $\hbar$ is the reduced Planck constant.

</i>

## Elementary Example

### Simple

For a real stationary wavefunction $\psi(x) = \psi^{*}(x)$, one has $\nabla\psi^{*} = \nabla\psi$, so

$$
\mathbf{j} = \mathbf{0}
$$

where

- there is no probability flux for a purely real $\psi$.

### General

For a plane wave $\psi = Ae^{ikx}$,

$$
j = \dfrac{\hbar k}{m}|A|^{2}
$$

where

- $j$ is the probability current in one dimension.
- $k$ is the wave number.

## References

1. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — probability flux $\mathbf{j}$ and continuity equation $\partial\rho/\partial t+\nabla\cdot\mathbf{j}=0$.
