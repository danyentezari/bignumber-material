# Induction

A process in which a changing magnetic flux through a loop produces an electromotive force that is used to generate electric current from magnetic change, where magnetic flux is the surface integral of $\mathbf{B}$.

1\. The electromotive force around a loop equals minus the rate of change of magnetic flux through any surface bounded by the loop. This principle is used to compute the induced emf from a known flux history.

Faraday's law in integral form is

$$
\oint_{\partial S} \mathbf{E}\cdot d\mathbf{r} = -\dfrac{\partial}{\partial t}\displaystyle\iint_{S} \mathbf{B}\cdot\hat{\mathbf{n}}\, dA
$$

where

- $S$ is a surface spanning the loop $\partial S$.
- $\mathbf{E}$ is the electric field along the loop.
- $\mathbf{B}$ is the magnetic field.
- $\hat{\mathbf{n}}$ is the unit normal to $S$.
- $t$ is time.

2\. In differential form a changing magnetic field produces a circulating electric field. This principle is used to write Faraday's law as a local Maxwell equation.

Faraday's law in differential form is

$$
\nabla \times \mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}
$$

where

- $\nabla\times$ is the curl.
- $\mathbf{E}$ is the electric field.
- $\mathbf{B}$ is the magnetic field.
- $t$ is time.

3\. For a loop of fixed area in a uniform field the emf is minus the area times the rate of change of $B$. This principle is used to compute the emf of a loop in a ramping laboratory field.

The emf of a fixed loop in a uniform field is

$$
\mathcal{E} = -A\dfrac{dB}{dt}
$$

where

- $\mathcal{E}$ is the induced emf.
- $A$ is the area of the loop.
- $B$ is the magnetic field through the loop.
- $t$ is time.

Note: These principles are Faraday's law in integral and differential form and the emf of a fixed loop. Also called electromagnetic induction. Also called Faraday induction.

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
