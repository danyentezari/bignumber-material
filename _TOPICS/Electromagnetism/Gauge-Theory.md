# Gauge Theory

A field theory with gauge symmetries that is used to describe fundamental interactions so that physics does not depend on the descriptive choice of local frames.

Note: Also called a gauge field theory.

<i>

**definition [d]** (*Gauge Theory*) From Nakahara: at present, physically sensible theories of fundamental interactions are based on gauge theories. The gauge principle—physics should not depend on how we describe it—is in harmony with the principle of general relativity.

where

- a gauge theory is a theory of interactions built so that physical predictions are unchanged under gauge transformations.
- the gauge principle is the requirement that the description dependence cancels in observables.

</i>

<i>

**definition [d]** (*Gauge Theory*) From Emam: field theories in physics are sometimes referred to as gauge theories. The reason is that they all, including electrodynamics, have certain symmetries, known for historical reasons as gauge symmetries. These in turn are classified into groups. Electrodynamics, for instance, is defined by the rank-$1$ tensor, the $4$-potential; the electromagnetic field is the second-rank field strength built from that potential.

where

- a gauge symmetry is a local symmetry of the potentials.
- the potential determines the field strength by differentiation.

</i>

## Elementary Example

### Simple

Classical electrodynamics is an abelian gauge theory with potentials $(V,\mathbf{A})$ and physical fields $(\mathbf{E},\mathbf{B})$.

$$
\mathbf{B} = \nabla \times \mathbf{A}
$$

$$
\mathbf{E} = -\nabla V - \dfrac{\partial\mathbf{A}}{\partial t}
$$

where

- gauge changes of $(V,\mathbf{A})$ leave $\mathbf{E}$ and $\mathbf{B}$ fixed.

### General

A nonabelian gauge theory uses a matrix-valued potential $A$ and field strength

$$
F = dA + A \wedge A
$$

where

- $A$ takes values in a Lie algebra.
- $F$ is the gauge field of the theory.

## References

1. Nakahara, M. *Geometry, Topology and Physics*. Institute of Physics Publishing, 2003. — gauge theories and the gauge principle.
2. Emam, M. H. *Covariant Physics: From Classical Mechanics to General Relativity and Beyond*. Oxford University Press, 2021. — field theories as gauge theories with gauge symmetries.
