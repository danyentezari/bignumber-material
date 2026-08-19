# Electromagnetic Induction

A process that is used to generate electromotive force from a changing magnetic flux, where electromotive force is the work per unit charge around a closed loop, and where magnetic flux is the amount of magnetic field through a surface.

Magnetic flux. Magnetic flux measures how much magnetic field crosses a chosen surface. This principle is used to quantify the field threading a circuit, whose change drives induction.

The magnetic flux is

$$
\Phi = \displaystyle\int\mathbf{B}\cdot d\mathbf{a}
$$

where

- $\Phi$ is the magnetic flux.
- $\mathbf{B}$ is the magnetic field.
- $d\mathbf{a}$ is an area element of the surface.

Electromotive force. Electromotive force is the net work per unit charge around a closed loop. This principle is used to compute the driving influence that maintains current in a circuit.

The electromotive force is

$$
\mathcal{E} = \oint\mathbf{f}\cdot d\mathbf{l}
$$

where

- $\mathcal{E}$ is the electromotive force.
- $\mathbf{f}$ is the force per unit charge.
- $d\mathbf{l}$ is a directed element of the loop.

Motional electromotive force. When a conductor moves through a magnetic field, charges in the conductor feel a magnetic force that drives them along the wire. This principle is used to analyze generators that convert motion into current.

The motional electromotive force is

$$
\mathcal{E} = \oint\bigl(\mathbf{v}\times\mathbf{B}\bigr)\cdot d\mathbf{l}
$$

where

- $\mathcal{E}$ is the motional electromotive force.
- $\mathbf{v}$ is the velocity of the conductor.
- $\mathbf{B}$ is the magnetic field.
- $d\mathbf{l}$ is a directed element of the wire.

Faraday's law of induction. A changing magnetic flux through a loop produces a circulating electric field whose line integral equals the negative rate of change of that flux. This principle is used to compute induced fields in transformers, inductors, and generators.

The integral form of Faraday's law is

$$
\oint\mathbf{E}\cdot d\mathbf{l} = -\dfrac{d\Phi}{dt}
$$

The differential form of Faraday's law is

$$
\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}
$$

where

- $\mathbf{E}$ is the electric field.
- $d\mathbf{l}$ is a directed element of the loop.
- $\Phi$ is the magnetic flux.
- $t$ is time.
- $\nabla\times$ is the curl.
- $\mathbf{B}$ is the magnetic field.

Lenz's law. An induced current produces a magnetic field that opposes the change of flux that created it. This principle is used to determine the direction of induced currents and the forces they exert.

Lenz's law is the minus sign in Faraday's law

$$
\mathcal{E} = -\dfrac{d\Phi}{dt}
$$

where

- $\mathcal{E}$ is the electromotive force.
- $\Phi$ is the magnetic flux.
- $t$ is time.

The induced electric field. A time-varying magnetic field produces a nonconservative electric field that curls around the changing flux and is not sourced by charge. A nonconservative field is a field whose work around a closed path need not vanish. This principle is used to compute forces on charges in induction motors and betatrons.

The induced electric field around a loop is

$$
\oint\mathbf{E}\cdot d\mathbf{l} = -\dfrac{d\Phi}{dt}
$$

where

- $\mathbf{E}$ is the induced electric field.
- $d\mathbf{l}$ is a directed element of the loop.
- $\Phi$ is the magnetic flux.
- $t$ is time.

Self-inductance with mutual inductance. A changing current induces electromotive force in its own circuit and in neighboring circuits. Self-inductance is the coupling of a circuit to its own changing current. Mutual inductance is the coupling of one circuit to the changing current of another. This principle is used to design inductors and transformers.

The self-inductance relation is

$$
\mathcal{E} = -L\dfrac{dI}{dt}
$$

The mutual inductance relation is

$$
\mathcal{E}_{2} = -M\dfrac{dI_{1}}{dt}
$$

where

- $\mathcal{E}$ is the self-induced electromotive force.
- $L$ is the self-inductance.
- $I$ is the current in the circuit.
- $\mathcal{E}_{2}$ is the electromotive force in the second circuit.
- $M$ is the mutual inductance.
- $I_{1}$ is the current in the first circuit.
- $t$ is time.

Note: Also called induction.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §7.1–7.2 — flux, electromotive force, Faraday's law, Lenz's law, and inductance.
2. Knight, R. D. *Physics for Scientists and Engineers: A Strategic Approach with Modern Physics*. Pearson, 2023. — electromagnetic induction.
