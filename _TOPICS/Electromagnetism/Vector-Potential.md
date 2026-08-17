# Vector Potential

A vector field whose curl is the magnetic field that is used, with the scalar potential, to express electromagnetic fields.

1\. Because the magnetic field is divergenceless, it is the curl of a vector potential. This principle is used to replace $\mathbf{B}$ by $\mathbf{A}$ in calculations.

The magnetic field from the vector potential is

$$
\mathbf{B} = \nabla\times\mathbf{A}
$$

where

- $\mathbf{B}$ is the magnetic field.
- $\mathbf{A}$ is the vector potential.
- $\nabla\times$ is the curl.

2\. In magnetostatics with the Coulomb gauge the vector potential obeys a Poisson equation sourced by the current. The Coulomb gauge is the condition $\nabla\cdot\mathbf{A}=0$. This principle is used to compute $\mathbf{A}$ from a known steady current.

The magnetostatic Poisson equation for $\mathbf{A}$ is

$$
\nabla^{2}\mathbf{A} = -\mu_{0}\mathbf{J}
$$

where

- $\nabla^{2}$ is the Laplacian.
- $\mathbf{A}$ is the vector potential.
- $\mathbf{J}$ is the volume current density.
- $\mu_{0}$ is the permeability of free space.

3\. The vector potential is the spatial part of the electromagnetic four-potential. This principle is used to write $V$ and $\mathbf{A}$ as one spacetime vector.

The four-potential is

$$
A^{\alpha} = \Bigl(\dfrac{V}{c},\,\mathbf{A}\Bigr)
$$

where

- $A^{\alpha}$ is the four-potential.
- $V$ is the electric scalar potential.
- $\mathbf{A}$ is the magnetic vector potential.
- $c$ is the speed of light.

Note: These principles are $\mathbf{B}=\nabla\times\mathbf{A}$, the Coulomb-gauge Poisson equation, and the four-potential. Also denoted $\mathbf{A}$. Also called the magnetic vector potential.

## Elementary Example

### Simple

For uniform $\mathbf{B} = B\hat{\mathbf{z}}$, one choice is

$$
\mathbf{A} = \dfrac{1}{2}\mathbf{B}\times\mathbf{r}
$$

where

- $\nabla\times\mathbf{A} = \mathbf{B}$.

### General

In magnetostatics with the Coulomb gauge $\nabla\cdot\mathbf{A} = 0$,

$$
\nabla^{2}\mathbf{A} = -\mu_{0}\mathbf{J}
$$

where

- $\mathbf{J}$ is the steady current density.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — $\mathbf{B}=\nabla\times\mathbf{A}$.
2. Susskind, L., & Friedman, A. *Special Relativity and Classical Field Theory*. Basic Books, 2017. — vector potential as fundamental.
3. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — $\mathbf{A}$ in the potential $4$-vector.
