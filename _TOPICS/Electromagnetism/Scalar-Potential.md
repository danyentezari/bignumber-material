# Scalar Potential

A scalar field that is used to express the electric field by differentiation, alone in electrostatics and together with the vector potential in electrodynamics.

Note: Also called the electric potential. Also denoted $V$. Also denoted $\phi$.

<i>

**definition [d]** (*Scalar Potential = Electric Potential*) From Griffiths: here $O$ is some standard reference point on which we have agreed beforehand; $V$ then depends only on the point $\mathbf{r}$. It is called the electric potential.

- $V(\mathbf{r}) = -\displaystyle\int_{O}^{\mathbf{r}}\mathbf{E}\cdot d\mathbf{l}$ .

In the static case this implies

- $\mathbf{E} = -\nabla V$ .

In the time-dependent case, with vector potential $\mathbf{A}$,

- $\mathbf{E} = -\nabla V - \dfrac{\partial\mathbf{A}}{\partial t}$ .

where

- $V$ is the electric scalar potential.
- $\mathbf{E}$ is the electric field.
- $O$ is a chosen reference point.
- $\mathbf{A}$ is the magnetic vector potential.

</i>

<i>

**definition [d]** (*Scalar Potential*) From Emam: the potentials $V$ and $\mathbf{A}$ can be viewed as components of the potential $4$-vector

- $A^{\alpha} = \left(\dfrac{V}{c},\, \mathbf{A}\right)$ ,

so the time component is the electric scalar potential $V$.

where

- $V$ is the electric scalar potential.
- $\mathbf{A}$ is the magnetic vector potential.
- $A^{\alpha}$ is the potential $4$-vector.
- $c$ is the speed of light.

</i>

<i>

**definition [d]** (*Scalar Function in Gauge Freedom*) From Susskind and Friedman: gauge invariance has to do with changes that you can make to the vector potential without affecting the physics. Gauge invariance makes a bold claim: dream up any scalar function you like, add its gradient to the vector potential, and the equations of motion stay exactly the same.

where

- the scalar function is an arbitrary gauge function.
- its gradient may be added to the vector potential without changing the physics.

</i>

## Elementary Example

### Simple

In electrostatics with $\mathbf{A} = \mathbf{0}$ and $V(x) = -Ex$ for constant $E$,

$$
\mathbf{E} = -\nabla V = E\,\hat{\mathbf{x}}
$$

where

- $V$ is linear and $\mathbf{E}$ is uniform.

### General

With $V(\mathbf{r}) = \dfrac{kQ}{r}$ for a point charge at the origin,

$$
\mathbf{E} = -\nabla V = \dfrac{kQ}{r^{2}}\,\hat{\mathbf{r}}
$$

where

- $V$ is the Coulomb scalar potential.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — $V(\mathbf{r})=-\int_{O}^{\mathbf{r}}\mathbf{E}\cdot d\mathbf{l}$; $\mathbf{E}=-\nabla V-\dfrac{\partial\mathbf{A}}{\partial t}$.
2. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — $A^{\alpha}=(V/c,\mathbf{A})$.
3. Susskind, L., & Friedman, A. *Special Relativity and Classical Field Theory: The Theoretical Minimum*. Basic Books, 2017. — gauge scalar freedom of the potentials.
