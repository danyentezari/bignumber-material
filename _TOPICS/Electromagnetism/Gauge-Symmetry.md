# Gauge Symmetry

A local symmetry of the potentials that is used to leave physical electromagnetic fields and observables unchanged.

1\. Many different potentials give the same $\mathbf{E}$ and $\mathbf{B}$. This principle is used to treat the physical content of electrodynamics as gauge-invariant.

The physical fields from the potentials are

$$
\mathbf{B} = \nabla\times\mathbf{A}
$$

$$
\mathbf{E} = -\nabla V - \dfrac{\partial\mathbf{A}}{\partial t}
$$

where

- $\mathbf{E}$ is the electric field.
- $\mathbf{B}$ is the magnetic field.
- $V$ is the scalar potential.
- $\mathbf{A}$ is the vector potential.
- $t$ is time.

2\. The symmetry acts by shifting the potentials with an arbitrary scalar function. This principle is used to generate the gauge transformations that leave the equations of motion unchanged.

The gauge symmetry acts as

$$
\mathbf{A}\mapsto\mathbf{A}+\nabla\lambda,\quad V\mapsto V-\dfrac{\partial\lambda}{\partial t}
$$

where

- $\lambda$ is the gauge function.
- $V$ and $\mathbf{A}$ are the potentials.
- $t$ is time.

3\. In magnetostatics the same symmetry is the invariance of $\mathbf{B}$ under $\mathbf{A}\mapsto\mathbf{A}+\nabla\lambda$. This principle is used to check gauge symmetry on $\mathbf{B}$ alone.

The magnetostatic invariance is

$$
\nabla\times\bigl(\mathbf{A}+\nabla\lambda\bigr) = \nabla\times\mathbf{A}
$$

where

- $\mathbf{A}$ is the vector potential.
- $\lambda$ is the gauge function.

Note: These principles are gauge invariance of $\mathbf{E}$ and $\mathbf{B}$, the action of the symmetry on the potentials, and the magnetostatic special case. Also called gauge invariance.

## Elementary Example

### Simple

Replacing $\mathbf{A}$ by $\mathbf{A}+\nabla\lambda$ leaves

$$
\mathbf{B} = \nabla\times\mathbf{A}
$$

unchanged.

where

- this is a magnetostatic gauge symmetry.

### General

Full electrodynamic gauge symmetry acts as

$$
\mathbf{A}\mapsto\mathbf{A}+\nabla\lambda,\quad V\mapsto V-\dfrac{\partial\lambda}{\partial t}
$$

where

- both potentials change while $\mathbf{E}$ and $\mathbf{B}$ do not.

## References

1. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — gauge symmetries in field theories.
2. Susskind, L., & Friedman, A. *Special Relativity and Classical Field Theory*. Basic Books, 2017. — gauge invariance.
3. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — gauge freedom of the potentials.
