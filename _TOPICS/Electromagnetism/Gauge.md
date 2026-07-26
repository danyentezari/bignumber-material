# Gauge

A choice of potentials for the electromagnetic field that is used to fix unphysical freedom while leaving the physical fields unchanged.

Note: Also called a gauge choice. Also called working in a gauge.

<i>

**definition [d]** (*Gauge Freedom = Gauge Transformation*) From Griffiths: Eqs. for the potentials do not uniquely define $V$ and $\mathbf{A}$; we are free to impose extra conditions on $V$ and $\mathbf{A}$, as long as nothing happens to $\mathbf{E}$ and $\mathbf{B}$. For any scalar function $\lambda(\mathbf{r}, t)$, we can add $\nabla\lambda$ to $\mathbf{A}$, provided we simultaneously subtract $\partial\lambda/\partial t$ from $V$. This will not affect the physical quantities $\mathbf{E}$ and $\mathbf{B}$. Such changes in $V$ and $\mathbf{A}$ are called gauge transformations:

- $\mathbf{A}' = \mathbf{A} + \nabla\lambda$ ,
- $V' = V - \dfrac{\partial\lambda}{\partial t}$ .

where

- $V$ is the electric scalar potential.
- $\mathbf{A}$ is the magnetic vector potential.
- $\lambda$ is an arbitrary scalar function of position and time.
- $\mathbf{E}$ and $\mathbf{B}$ are the physical electric and magnetic fields.

</i>

<i>

**definition [d]** (*Gauge Transformation*) From Frankel: a local change of basis, such as

- $e_{V} = e_{U}\, c_{UV}$ ,

is called in physics a gauge transformation. Gauge transformations are simply changes of frames in the fibers of the bundle.

where

- $e_{U}$ and $e_{V}$ are local frames on overlapping regions.
- $c_{UV}$ is the transition function relating those frames.

</i>

## Elementary Example

### Simple

In magnetostatics, the Coulomb gauge is the choice $\nabla\cdot\mathbf{A} = 0$.

$$
\mathbf{A}' = \mathbf{A} + \nabla\lambda,\quad \nabla\cdot\mathbf{A}' = 0
$$

where

- $\lambda$ is chosen so that the new vector potential is divergenceless.

### General

A full electrodynamic gauge change shifts both potentials together.

$$
\mathbf{A}' = \mathbf{A} + \nabla\lambda
$$

$$
V' = V - \dfrac{\partial\lambda}{\partial t}
$$

$$
\mathbf{E}' = \mathbf{E},\quad \mathbf{B}' = \mathbf{B}
$$

where

- the physical fields are unchanged by the gauge choice.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — gauge freedom and gauge transformations of $V$ and $\mathbf{A}$.
2. Frankel, T. *The Geometry of Physics: An Introduction*. Cambridge University Press, 2012. — gauge transformation as a local change of fiber frame.
3. Hubbard, J. H., & Hubbard, B. B. *Vector Calculus, Linear Algebra, and Differential Forms: A Unified Approach*. Matrix Editions, 2015. — working in a different gauge as a change of bundle coordinates.
