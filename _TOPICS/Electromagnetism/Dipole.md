# Dipole

A localized pair of equal opposite charges, characterized by its dipole moment $\mathbf{p}$, that is used as the leading multipole when the total charge vanishes.

Note: Also called an electric dipole.

1\. The electric dipole moment is a vector that measures the strength, separation, and direction of opposite charges in a small localized distribution. A localized distribution is a charge collection confined to a bounded region. This principle is used to replace many neutral charges by one vector when computing distant electrostatic effects.

$$
\mathbf{p} = q\mathbf{d}
$$

$$
\mathbf{p} = \displaystyle\int\mathbf{r}'\rho(\mathbf{r}')\,d\tau'
$$

where $\mathbf{d}$ points from $-q$ to $+q$, and $\rho$ is the charge density.

2\. Far from a neutral charge distribution the electrostatic potential is dominated by a term that falls as $1/r^{2}$ and varies with angle from the dipole axis. Electrostatic potential is potential energy per unit charge. This principle is used to approximate the potential of polar molecules at large distance.

$$
V_{\mathrm{dip}}(\mathbf{r}) = \dfrac{1}{4\pi\epsilon_{0}}\dfrac{\mathbf{p}\cdot\hat{\mathbf{r}}}{r^{2}}
$$

3\. The electric field of a dipole falls as $1/r^{3}$ and is twice as strong along the dipole axis as in the midplane perpendicular to the axis. This principle is used to compute forces exerted by polar molecules on nearby objects.

$$
\mathbf{E}_{\mathrm{dip}}(\mathbf{r}) = \dfrac{1}{4\pi\epsilon_{0}r^{3}}\bigl[3(\mathbf{p}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{p}\bigr]
$$

4\. In a uniform external electric field the net force on a dipole vanishes, yet a torque twists the dipole into alignment with the field. A uniform field has the same strength and direction everywhere. Torque is the rotational analog of force. This principle is used to predict how polar molecules rotate into an applied field.

$$
\mathbf{N} = \mathbf{p}\times\mathbf{E}
$$

5\. In a nonuniform electric field the forces on the two ends do not cancel, so a net force pulls the dipole toward stronger field. A nonuniform field changes from point to point. This principle is used to compute how polar molecules move toward regions of high field.

$$
\mathbf{F} = (\mathbf{p}\cdot\nabla)\mathbf{E}
$$

6\. Work is required to rotate a dipole away from alignment with the field, so the dipole has potential energy lowest when aligned with the field and highest when anti-aligned. This principle is used to compute the work of reorientation and the thermal alignment of dipoles.

$$
U = -\mathbf{p}\cdot\mathbf{E}
$$

7\. An external field can pull a nucleus and electron cloud apart in an otherwise nonpolar atom, creating a temporary induced dipole proportional to the field. Atomic polarizability $\alpha$ measures how easily that cloud deforms. This principle is used to model polarization of nonpolar matter in dielectrics.

$$
\mathbf{p}_{\mathrm{ind}} = \alpha\mathbf{E}
$$

Note: These principles are the electric dipole moment, the electrostatic dipole potential, the electric field of a dipole, the torque on a dipole, the force on a dipole in a nonuniform field, the potential energy of a dipole, and induced dipoles with polarizability.

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
