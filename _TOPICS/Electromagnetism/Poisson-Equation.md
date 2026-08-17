# Poisson Equation

A partial differential equation relating the Laplacian of the potential to charge density that is used to determine electrostatic potentials from sources, where the Laplacian is the divergence of the gradient.

1\. Combining $\mathbf{E} = -\nabla V$ with Gauss's law yields Poisson's equation. This principle is used to compute the potential of a known charge density.

Poisson's equation is

$$
\nabla^{2}V = -\dfrac{\rho}{\epsilon_{0}}
$$

where

- $\nabla^{2}$ is the Laplacian.
- $V$ is the electric potential.
- $\rho$ is the charge density.
- $\epsilon_{0}$ is the permittivity of free space.

2\. When the charge density vanishes, Poisson's equation reduces to Laplace's equation. This principle is used to treat empty regions as a special case of the sourced problem.

Laplace's equation is

$$
\nabla^{2}V = 0
$$

where

- $\nabla^{2}$ is the Laplacian.
- $V$ is the electric potential.

3\. The charge density sets the curvature of the potential. This principle is used to solve for $V$ inside a uniformly charged region subject to boundary values.

Note: These principles are Poisson's equation, its reduction to Laplace's equation, and the source as curvature of $V$. Also written $\nabla^{2}V=-\rho/\epsilon_{0}$.

## Elementary Example

### Simple

If $\rho = 0$, Poisson's equation becomes

$$
\nabla^{2}V = 0
$$

where

- this is Laplace's equation.

### General

For uniform $\rho$ in a region, one solves

$$
\nabla^{2}V = -\dfrac{\rho}{\epsilon_{0}}
$$

subject to boundary conditions on $V$.

where

- $\rho/\epsilon_{0}$ sets the curvature of $V$.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — $\nabla^{2}V=-\rho/\epsilon_{0}$.
2. Knight, R. D. *Physics for Scientists and Engineers*. Pearson, 2023. — Poisson equation for electrostatic potential.
3. Susskind, L., & Cabannes, A. *General Relativity: The Theoretical Minimum*. Penguin Books, 2023. — Poisson structure for potentials and sources.
