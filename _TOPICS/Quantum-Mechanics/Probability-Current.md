# Probability Current

A vector field built from a wavefunction that is used to express the flow of probability density through space.

1\. Probability is locally conserved: any decrease of $\rho$ in a volume equals the outward flux of the probability current. This principle is used to write a continuity equation for $|\Psi|^{2}$.

The continuity equation is

$$
\dfrac{\partial\rho}{\partial t} + \nabla\cdot\mathbf{j} = 0
$$

where

- $\rho = \lvert\Psi\rvert^{2}$ is the probability density.
- $\mathbf{j}$ is the probability current.
- $t$ is time.

2\. The probability current is built from $\Psi$ and its gradient. This principle is used to compute the flow from a known wavefunction.

The probability current is

$$
\mathbf{j} = \dfrac{\hbar}{m}\operatorname{Im}\bigl(\Psi^{*}\nabla\Psi\bigr)
$$

where

- $\mathbf{j}$ is the probability current.
- $\Psi$ is the wavefunction.
- $m$ is the particle mass.
- $\hbar$ is the reduced Planck constant.

3\. A purely real stationary wavefunction has vanishing current. This principle is used to identify bound standing waves with no net flow.

Note: These principles are the continuity equation, the formula for $\mathbf{j}$, and vanishing current for a real wavefunction. Also called probability flux. Also called probability current density.

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
