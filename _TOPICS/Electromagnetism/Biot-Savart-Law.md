# Biot-Savart Law

A law that is used to compute the magnetic field of a current element, where a current element is a short segment of wire carrying current.

The Biot–Savart law for a line current. The magnetic field of a steady line current is the integral of the Biot–Savart contribution of each length element. This principle is used to compute $\mathbf{B}$ for wires, loops, and solenoids of known shape.

The Biot–Savart law for a line current is

$$
\mathbf{B}(\mathbf{r}) = \dfrac{\mu_{0}}{4\pi}\displaystyle\int\dfrac{I\,d\mathbf{l}'\times\hat{\mathbf{r}}}{r^{2}}
$$

where

- $\mathbf{B}(\mathbf{r})$ is the magnetic field at the field point.
- $I$ is the current.
- $d\mathbf{l}'$ is a directed length element of the wire.
- $r$ is the distance from the current element to the field point.
- $\hat{\mathbf{r}}$ is the unit vector from the current element to the field point.
- $\mu_{0}$ is the permeability of free space.

The volume-current form. The same law for a volume current replaces $I\,d\mathbf{l}'$ by $\mathbf{J}\,d\tau'$. This principle is used to compute $\mathbf{B}$ of a distributed current.

The Biot–Savart law for a volume current is

$$
\mathbf{B}(\mathbf{r}) = \dfrac{\mu_{0}}{4\pi}\displaystyle\int\dfrac{\mathbf{J}(\mathbf{r}')\times\hat{\mathbf{r}}}{r^{2}}\,d\tau'
$$

where

- $\mathbf{J}$ is the volume current density.
- $d\tau'$ is the volume element.

The field of a long straight wire. The field of a long straight wire falls as the inverse of the perpendicular distance. This principle is used to recover the standard result for an infinite wire.

The magnetic field of a long straight wire is

$$
B = \dfrac{\mu_{0}I}{2\pi s}
$$

where

- $B$ is the magnitude of the magnetic field.
- $I$ is the current.
- $s$ is the perpendicular distance from the wire.
- $\mu_{0}$ is the permeability of free space.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §5.2 — Biot–Savart law.
