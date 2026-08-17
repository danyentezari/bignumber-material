# Magnetostatics

A branch of electromagnetism that is used to describe magnetic fields of steady currents, where a steady current is a charge flow that does not change in time.

1\. A steady current in a wire produces a magnetic field whose contribution from each segment is proportional to the current, perpendicular to the flow, and falls as the inverse square of distance. This principle is used to compute the magnetic field of a steady current of any shape.

The Biot-Savart law is

$$
\mathbf{B}(\mathbf{r}) = \dfrac{\mu_{0}I}{4\pi}\displaystyle\int\dfrac{d\mathbf{l}'\times\hat{\mathbf{r}}}{r^{2}}
$$

where

- $\mathbf{B}(\mathbf{r})$ is the magnetic field at the field point.
- $\mu_{0}$ is the permeability of free space.
- $I$ is the steady current.
- $d\mathbf{l}'$ is a directed element of the wire.
- $\hat{\mathbf{r}}$ is the unit vector from the source element to the field point.
- $r$ is the distance from the source element to the field point.

2\. The circulation of the magnetic field around a closed path is proportional to the net current through any surface bounded by that path. Circulation is the line integral of a field around a loop. This principle is used to find magnetic fields of highly symmetric currents.

The integral form of Ampère's law is

$$
\oint\mathbf{B}\cdot d\mathbf{l} = \mu_{0}I_{\mathrm{enc}}
$$

The differential form of Ampère's law is

$$
\nabla\times\mathbf{B} = \mu_{0}\mathbf{J}
$$

where

- $\mathbf{B}$ is the magnetic field.
- $d\mathbf{l}$ is a directed element of the closed path.
- $\mu_{0}$ is the permeability of free space.
- $I_{\mathrm{enc}}$ is the enclosed current.
- $\nabla\times$ is the curl.
- $\mathbf{J}$ is the volume current density.

3\. The net magnetic flux through every closed surface is zero, so magnetic field lines form closed loops. Magnetic flux is the amount of magnetic field that crosses a surface. This principle is used to rule out isolated magnetic charges.

Gauss's law for magnetism is

$$
\nabla\cdot\mathbf{B} = 0
$$

The integral form is

$$
\oint\mathbf{B}\cdot d\mathbf{a} = 0
$$

where

- $\nabla\cdot$ is the divergence.
- $\mathbf{B}$ is the magnetic field.
- $d\mathbf{a}$ is an outward area element of the closed surface.

4\. Because the magnetic field has vanishing divergence, it is the curl of a vector potential. A vector potential is a vector field whose curl is the magnetic field. This principle is used to compute magnetic fields by first solving for that potential.

The magnetic field from the vector potential is

$$
\mathbf{B} = \nabla\times\mathbf{A}
$$

where

- $\mathbf{B}$ is the magnetic field.
- $\nabla\times$ is the curl.
- $\mathbf{A}$ is the magnetic vector potential.

5\. Far from a localized current loop the magnetic field is dominated by a dipole term fixed by the current, area, and orientation of the loop. A localized current loop is a closed circuit confined to a bounded region. This principle is used to compute distant fields of atoms, molecules, and small coils.

The magnetic dipole moment of a planar loop is

$$
\mathbf{m} = I\mathbf{a}
$$

where

- $\mathbf{m}$ is the magnetic dipole moment.
- $I$ is the current in the loop.
- $\mathbf{a}$ is the vector area of the loop.

6\. The work required to establish a set of steady currents is stored as energy in the magnetic field. This principle is used to compute the energy of inductors and other magnetostatic configurations.

The magnetic field energy is

$$
W = \dfrac{1}{2\mu_{0}}\displaystyle\int B^{2}\,d\tau
$$

where

- $W$ is the stored magnetic energy.
- $\mu_{0}$ is the permeability of free space.
- $B$ is the magnitude of the magnetic field.
- $d\tau$ is the volume element.

Note: These principles are the Biot-Savart law, Ampère's law, Gauss's law for magnetism, the magnetic vector potential, the magnetic dipole moment, and the stored energy of a magnetic field. Also called steady-state magnetism.

## Elementary Example

### Simple

A long straight wire with current $I$ produces

$$
B = \dfrac{\mu_{0}I}{2\pi r}
$$

where

- $r$ is the perpendicular distance from the wire.

### General

Steady $\mathbf{J}$ determines $\mathbf{B}$ via

$$
\nabla\times\mathbf{B} = \mu_{0}\mathbf{J},\quad \nabla\cdot\mathbf{B} = 0
$$

where

- these are the magnetostatic Maxwell equations.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §5.2–5.4, §8.2.4 — Biot-Savart law, Ampère's law, vector potential, magnetic dipole, and magnetic energy.
2. Knight, R. D. *Physics for Scientists and Engineers*. Pearson, 2023. — steady currents and magnetostatics.
3. Susskind, L., & Friedman, A. *Special Relativity and Classical Field Theory*. Basic Books, 2017. — magnetic fields from steady currents.
