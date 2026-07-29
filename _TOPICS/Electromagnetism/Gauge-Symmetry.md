# Gauge Symmetry

A local symmetry of the potentials that is used to leave physical electromagnetic fields and observables unchanged.

Note: Also called gauge invariance. Closely related to [Gauge Transformations](gauge-transformations.html).

<i>

**definition [d]** (*Gauge Symmetry*) From Emam: field theories in physics are sometimes referred to as gauge theories. The reason is that they all, including electrodynamics, have certain symmetries, known for historical reasons as gauge symmetries.

where

- a gauge symmetry is a local symmetry of the potentials.
- electrodynamics has an abelian gauge symmetry.

</i>

<i>

**definition [d]** (*Gauge Symmetry*) From Susskind and Friedman: gauge invariance has to do with changes that you can make to the vector potential without affecting the physics. The equations of motion stay the same under such changes.

where

- the physical content is gauge-invariant.

</i>

<i>

**definition [d]** (*Gauge Symmetry*) From Griffiths: the potentials are not unique; gauge freedom means many potentials give the same $\mathbf{E}$ and $\mathbf{B}$, which is the practical expression of gauge symmetry in classical electrodynamics.

where

- $\mathbf{E}$ and $\mathbf{B}$ are the physical fields.

</i>

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
