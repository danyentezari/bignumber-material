# Dipole

A localized pair of equal opposite charges that is used to describe the leading electrostatic effect of a neutral charge collection, where a localized pair is two charges confined to a bounded region, and where a neutral charge collection is a set of charges whose algebraic sum is zero.

1\. The electric dipole moment is a vector that records the strength, separation, and direction of opposite charges in a localized distribution. A localized distribution is a charge collection confined to a bounded region. This principle is used to replace many neutral charges by one vector when computing distant electrostatic effects.

The physical dipole moment is

$$
\mathbf{p} = q\mathbf{d}
$$

The continuous dipole moment is

$$
\mathbf{p} = \displaystyle\int\mathbf{r}'\rho(\mathbf{r}')\,d\tau'
$$

where

- $\mathbf{p}$ is the electric dipole moment.
- $q$ is the magnitude of each charge.
- $\mathbf{d}$ is the displacement from $-q$ to $+q$.
- $\mathbf{r}'$ is the source position.
- $\rho$ is the charge density.
- $d\tau'$ is the volume element.

2\. Far from a neutral charge distribution the electrostatic potential is dominated by a term that falls as the inverse square of distance and varies with angle from the dipole axis. Electrostatic potential is potential energy per unit charge. This principle is used to approximate the potential of polar molecules at large distance.

The electrostatic dipole potential is

$$
V_{\mathrm{dip}}(\mathbf{r}) = \dfrac{1}{4\pi\epsilon_{0}}\dfrac{\mathbf{p}\cdot\hat{\mathbf{r}}}{r^{2}}
$$

where

- $V_{\mathrm{dip}}$ is the electrostatic potential of the dipole.
- $\mathbf{r}$ is the position of the field point.
- $r$ is the distance from the dipole to the field point.
- $\hat{\mathbf{r}}$ is the unit vector from the dipole to the field point.
- $\mathbf{p}$ is the electric dipole moment.
- $\epsilon_{0}$ is the permittivity of free space.

3\. The electric field of a dipole falls as the inverse cube of distance and is twice as strong along the dipole axis as in the midplane perpendicular to the axis. This principle is used to compute forces exerted by polar molecules on nearby objects.

The electric field of a dipole is

$$
\mathbf{E}_{\mathrm{dip}}(\mathbf{r}) = \dfrac{1}{4\pi\epsilon_{0}r^{3}}\bigl[3(\mathbf{p}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{p}\bigr]
$$

where

- $\mathbf{E}_{\mathrm{dip}}$ is the electric field of the dipole.
- $\mathbf{r}$ is the position of the field point.
- $r$ is the distance from the dipole to the field point.
- $\hat{\mathbf{r}}$ is the unit vector from the dipole to the field point.
- $\mathbf{p}$ is the electric dipole moment.
- $\epsilon_{0}$ is the permittivity of free space.

4\. In a uniform external electric field the net force on a dipole vanishes, yet a torque twists the dipole into alignment with the field. A uniform field is a field with the same strength and direction everywhere. Torque is the rotational analog of force. This principle is used to predict how polar molecules rotate into an applied field.

The net force on a dipole in a uniform field is

$$
\mathbf{F}_{\mathrm{net}} = q\mathbf{E} + (-q)\mathbf{E} = 0
$$

The torque on a dipole is

$$
\mathbf{N} = \mathbf{p}\times\mathbf{E}
$$

where

- $\mathbf{F}_{\mathrm{net}}$ is the net force on the dipole.
- $q$ is the magnitude of each charge.
- $\mathbf{E}$ is the external electric field.
- $\mathbf{N}$ is the torque.
- $\mathbf{p}$ is the electric dipole moment.

5\. In a nonuniform electric field the forces on the two ends do not cancel, so a net force pulls the dipole toward stronger field. A nonuniform field is a field that changes from point to point. This principle is used to compute how polar molecules move toward regions of high field.

The force on a dipole in a nonuniform field is

$$
\mathbf{F} = (\mathbf{p}\cdot\nabla)\mathbf{E}
$$

where

- $\mathbf{F}$ is the net force on the dipole.
- $\mathbf{p}$ is the electric dipole moment.
- $\nabla$ is the del operator.
- $\mathbf{E}$ is the external electric field.

6\. Work is required to rotate a dipole away from alignment with the field, so the potential energy is lowest when the dipole is aligned with the field and highest when the dipole points opposite the field. This principle is used to compute the work of reorientation and the thermal alignment of dipoles.

The potential energy of a dipole is

$$
U = -\mathbf{p}\cdot\mathbf{E}
$$

where

- $U$ is the potential energy of the dipole.
- $\mathbf{p}$ is the electric dipole moment.
- $\mathbf{E}$ is the external electric field.

7\. An external field can pull a nucleus and an electron cloud apart in an otherwise nonpolar atom, creating a temporary induced dipole proportional to the field. Atomic polarizability is a measure of how easily that cloud deforms. This principle is used to model polarization of nonpolar matter in dielectrics.

The induced dipole moment is

$$
\mathbf{p}_{\mathrm{ind}} = \alpha\mathbf{E}
$$

where

- $\mathbf{p}_{\mathrm{ind}}$ is the induced dipole moment.
- $\alpha$ is the atomic polarizability.
- $\mathbf{E}$ is the external electric field.

Note: These principles are the electric dipole moment, the electrostatic dipole potential, the electric field of a dipole, the torque on a dipole in a uniform field, the force on a dipole in a nonuniform field, the potential energy of a dipole, and the induced dipole moment with polarizability. Also called an electric dipole.

## Elementary Example

### Simple

Charges $+2$ and $-2$ separated by $\mathbf{d} = (1, 0, 0)$ give

$$
\mathbf{p} = 2\,\hat{\mathbf{x}}
$$

where

- $\mathbf{p}$ points from $-$ to $+$.

### General

A continuous distribution with density $\rho$ has

$$
\mathbf{p} = \displaystyle\int\mathbf{r}'\rho(\mathbf{r}')\,d\tau'
$$

where

- $\mathbf{p}$ is the first moment of $\rho$.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §3.4.1, §3.4.4 — dipole moment, potential, and field. §4.1.1–4.1.3 — torque, force, and energy. Ch. 4 — induced dipoles and polarizability.
