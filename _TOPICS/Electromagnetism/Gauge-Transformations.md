# Gauge Transformations

A change of the electromagnetic potentials that leaves the physical fields unchanged that is used to exploit freedom in choosing $V$ and $\mathbf{A}$.

Note: Also called a gauge transformation of the potentials. Closely related to [Gauge](gauge.html).

<i>

**definition [d]** (*Gauge Transformations*) From Griffiths: for any scalar function $\lambda(\mathbf{r}, t)$,

- $\mathbf{A}' = \mathbf{A} + \nabla\lambda$ ,
- $V' = V - \dfrac{\partial\lambda}{\partial t}$

are gauge transformations; $\mathbf{E}$ and $\mathbf{B}$ are unchanged.

where

- $\lambda$ is an arbitrary scalar function.
- $V$ and $\mathbf{A}$ are the potentials.

</i>

<i>

**definition [d]** (*Gauge Transformations*) From Susskind and Friedman: gauge invariance has to do with changes that you can make to the vector potential without affecting the physics. Dream up any scalar function you like, add its gradient to the vector potential, and the equations of motion stay exactly the same.

where

- the scalar function is the gauge function.

</i>

<i>

**definition [d]** (*Gauge Transformations*) From Frankel: a local change of frame in the fibers of a bundle is called in physics a gauge transformation.

where

- gauge transformations change potentials without changing field strengths.

</i>

## Elementary Example

### Simple

In magnetostatics, adding $\nabla\lambda$ to $\mathbf{A}$ leaves

$$
\mathbf{B}' = \nabla\times\mathbf{A}' = \nabla\times\mathbf{A} = \mathbf{B}
$$

where

- the curl of a gradient vanishes.

### General

A full electrodynamic gauge change is

$$
\mathbf{A}' = \mathbf{A} + \nabla\lambda,\quad V' = V - \dfrac{\partial\lambda}{\partial t}
$$

where

- both potentials change together.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — gauge transformations of $V$ and $\mathbf{A}$.
2. Susskind, L., & Friedman, A. *Special Relativity and Classical Field Theory*. Basic Books, 2017. — gauge invariance of the vector potential.
3. Frankel, T. *The Geometry of Physics*. Cambridge University Press, 2012. — gauge transformation as change of fiber frame.
