# Scalar Potential

A scalar field that is used to express the electric field by differentiation, alone in electrostatics and together with the vector potential in electrodynamics.

The line-integral definition of $V$. The electrostatic potential at a point is minus the line integral of the electric field from a chosen reference point. This principle is used to assign a number $V$ that depends only on the field point.

The electrostatic potential is

$$
V(\mathbf{r}) = -\displaystyle\int_{O}^{\mathbf{r}}\mathbf{E}\cdot d\mathbf{l}
$$

where

- $V$ is the electric scalar potential.
- $O$ is the reference point.
- $\mathbf{r}$ is the field point.
- $\mathbf{E}$ is the electric field.
- $d\mathbf{l}$ is a displacement along the path.

The static gradient relation. In the static case the electric field is minus the gradient of the scalar potential. This principle is used to recover $\mathbf{E}$ from $V$.

The static field from the potential is

$$
\mathbf{E} = -\nabla V
$$

where

- $\mathbf{E}$ is the electric field.
- $\nabla$ is the gradient.
- $V$ is the electric scalar potential.

The electrodynamic reconstruction of $\mathbf{E}$. In the time-dependent case the electric field also includes minus the time derivative of the vector potential. This principle is used to reconstruct $\mathbf{E}$ from both potentials.

The electrodynamic field from the potentials is

$$
\mathbf{E} = -\nabla V - \dfrac{\partial\mathbf{A}}{\partial t}
$$

where

- $\mathbf{E}$ is the electric field.
- $V$ is the electric scalar potential.
- $\mathbf{A}$ is the magnetic vector potential.
- $t$ is time.

The four-potential. The scalar potential is the time part of the electromagnetic four-potential. This principle is used to write $V$ and $\mathbf{A}$ as one spacetime vector.

The four-potential is

$$
A^{\alpha} = \Bigl(\dfrac{V}{c},\,\mathbf{A}\Bigr)
$$

where

- $A^{\alpha}$ is the four-potential.
- $V$ is the electric scalar potential.
- $\mathbf{A}$ is the magnetic vector potential.
- $c$ is the speed of light.

Note: Also called the electric potential. Also denoted $\phi$.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — $V(\mathbf{r})=-\int_{O}^{\mathbf{r}}\mathbf{E}\cdot d\mathbf{l}$; $\mathbf{E}=-\nabla V-\dfrac{\partial\mathbf{A}}{\partial t}$.
2. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — $A^{\alpha}=(V/c,\mathbf{A})$.
3. Susskind, L., & Friedman, A. *Special Relativity and Classical Field Theory: The Theoretical Minimum*. Basic Books, 2017. — gauge scalar freedom of the potentials.
