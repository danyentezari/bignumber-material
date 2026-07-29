# Potentials

A pair of fields, a scalar potential and a vector potential, that is used to express the electric and magnetic fields by differentiation.

Note: Also called the electromagnetic potentials. Denoted $V$ and $\mathbf{A}$.

<i>

**definition [d]** (*Potentials*) From Griffiths: but $\mathbf{B}$ remains divergenceless, so we can still write $\mathbf{B} = \nabla\times\mathbf{A}$ as in magnetostatics. Putting this into Faraday's law yields $\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t} = -\dfrac{\partial}{\partial t}(\nabla\times\mathbf{A})$ or $\nabla\times\bigl(\mathbf{E} + \dfrac{\partial\mathbf{A}}{\partial t}\bigr) = 0$. Here is a quantity, unlike $\mathbf{E}$ alone, whose curl does vanish; it can therefore be written as the gradient of a scalar: $\mathbf{E} + \dfrac{\partial\mathbf{A}}{\partial t} = -\nabla V$. In terms of $V$ and $\mathbf{A}$, then,

- $\mathbf{E} = -\nabla V - \dfrac{\partial\mathbf{A}}{\partial t}$ ,
- $\mathbf{B} = \nabla\times\mathbf{A}$ .

where

- $V$ is the electric scalar potential.
- $\mathbf{A}$ is the magnetic vector potential.
- $\mathbf{E}$ is the electric field.
- $\mathbf{B}$ is the magnetic field.

</i>

## Elementary Example

### Simple

In electrostatics with $\mathbf{A} = \mathbf{0}$,

$$
\mathbf{E} = -\nabla V
$$

where

- the electric field is minus the gradient of the scalar potential.

### General

With both potentials nonzero,

$$
\mathbf{E} = -\nabla V - \dfrac{\partial\mathbf{A}}{\partial t}
$$

$$
\mathbf{B} = \nabla\times\mathbf{A}
$$

where

- $\mathbf{E}$ and $\mathbf{B}$ are recovered from $V$ and $\mathbf{A}$.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — $\mathbf{B}=\nabla\times\mathbf{A}$ and $\mathbf{E}=-\nabla V-\dfrac{\partial\mathbf{A}}{\partial t}$.
