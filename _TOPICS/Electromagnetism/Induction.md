# Induction

A process in which a changing magnetic flux through a loop produces an electromotive force that is used to generate electric current from magnetic change.

Note: Also called electromagnetic induction. Also called Faraday induction.

<i>

**definition [d]** (*Electromagnetic Induction = Faraday’s Law*) From Needham: if the surface $S$ spans a loop of wire $\partial S$, and the field lines of a varying magnetic field pass through it, then an electromotive force is induced in the loop that is equal to the negative of the rate of change of the magnetic flux through $S$:

- $\displaystyle \oint_{\partial S} \mathbf{E}\cdot d\mathbf{r} = -\dfrac{\partial}{\partial t}\iint_{S} \mathbf{B}\cdot\hat{\mathbf{n}}\, dA$ .

where

- $S$ is a surface spanning the wire loop $\partial S$.
- $\mathbf{E}$ is the electric field along the loop.
- $\mathbf{B}$ is the magnetic field.
- $\hat{\mathbf{n}}$ is the unit normal to $S$.

</i>

<i>

**definition [d]** (*Faraday’s Law*) From Griffiths: converted to differential form by Stokes’s theorem,

- $\nabla \times \mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}$ .

where

- $\mathbf{E}$ is the electric field.
- $\mathbf{B}$ is the magnetic field.
- $t$ is time.

</i>

## Elementary Example

### Simple

A loop of area $A$ in a uniform field $B(t)$ has flux $\Phi = BA$.

$$
\mathcal{E} = -\dfrac{d\Phi}{dt} = -A\dfrac{dB}{dt}
$$

where

- $\mathcal{E}$ is the induced emf around the loop.

### General

For three loops with the same area but different $dB/dt$, the induced emf scales with that rate.

$$
\mathcal{E}_{i} = -A\dfrac{dB_{i}}{dt},\quad i \in \{1,2,3\}
$$

where

- each $\mathcal{E}_{i}$ is the emf for the corresponding field ramp.

## References

1. Needham, T. *Visual Differential Geometry and Forms*. Princeton University Press, 2021. — Faraday’s law of electromagnetic induction in integral form.
2. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — $\nabla\times\mathbf{E}=-\partial\mathbf{B}/\partial t$.
