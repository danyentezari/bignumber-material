# Lorentz Force

A force on a charged particle in electric and magnetic fields that is used to determine how the particle accelerates, where a charged particle is a particle that carries electric charge.

1\. The total electromagnetic force on a charged particle is the sum of an electric force along the electric field and a magnetic force that depends on velocity. This principle is used to compute the net force on a charge that travels through both fields.

The Lorentz force law is

$$
\mathbf{F} = q\bigl(\mathbf{E} + \mathbf{v}\times\mathbf{B}\bigr)
$$

where

- $\mathbf{F}$ is the Lorentz force.
- $q$ is the electric charge.
- $\mathbf{E}$ is the electric field.
- $\mathbf{v}$ is the velocity of the particle.
- $\mathbf{B}$ is the magnetic field.

2\. A charged particle in an electric field feels a force proportional to its charge and to the local field, whether the particle is at rest or in motion. This principle is used to find the acceleration of charges in capacitors and other static electric fields.

The electric force is

$$
\mathbf{F}_{\mathrm{elec}} = q\mathbf{E}
$$

where

- $\mathbf{F}_{\mathrm{elec}}$ is the electric force.
- $q$ is the electric charge.
- $\mathbf{E}$ is the electric field.

3\. A charged particle moving through a magnetic field feels a sideways force proportional to its speed and perpendicular to both its velocity and the field. This principle is used to compute the magnetic deflection of moving charges.

The magnetic force is

$$
\mathbf{F}_{\mathrm{mag}} = q\bigl(\mathbf{v}\times\mathbf{B}\bigr)
$$

where

- $\mathbf{F}_{\mathrm{mag}}$ is the magnetic force.
- $q$ is the electric charge.
- $\mathbf{v}$ is the velocity of the particle.
- $\mathbf{B}$ is the magnetic field.

4\. The magnetic force is always perpendicular to the instantaneous velocity, so it does no work. Work is energy transferred when a force acts through a displacement. This principle is used to prove that a magnetic field alone cannot change the speed of a charged particle.

The magnetic work is

$$
dW = \mathbf{F}_{\mathrm{mag}}\cdot d\mathbf{l} = q\bigl(\mathbf{v}\times\mathbf{B}\bigr)\cdot\mathbf{v}\,dt = 0
$$

where

- $dW$ is the infinitesimal work.
- $\mathbf{F}_{\mathrm{mag}}$ is the magnetic force.
- $d\mathbf{l}$ is the displacement.
- $q$ is the electric charge.
- $\mathbf{v}$ is the velocity of the particle.
- $\mathbf{B}$ is the magnetic field.
- $t$ is time.

5\. A wire that carries current in a magnetic field feels a mechanical force equal to the sum of the magnetic forces on the moving charges inside the wire. Current is charge flow per unit time. This principle is used to compute forces in motors and between current-carrying wires.

The force on a current-carrying wire is

$$
\mathbf{F}_{\mathrm{mag}} = I\displaystyle\int\bigl(d\mathbf{l}\times\mathbf{B}\bigr)
$$

where

- $\mathbf{F}_{\mathrm{mag}}$ is the magnetic force on the wire.
- $I$ is the current.
- $d\mathbf{l}$ is a directed element of the wire.
- $\mathbf{B}$ is the magnetic field.

6\. The same magnetic force, written with current density, applies to charge flow on a surface or through a volume. Surface current density is current per unit width. Volume current density is current per unit area. This principle is used to compute forces on bulk conductors and current sheets.

The force on a volume current is

$$
\mathbf{F}_{\mathrm{mag}} = \displaystyle\int\bigl(\mathbf{J}\times\mathbf{B}\bigr)\,d\tau
$$

where

- $\mathbf{F}_{\mathrm{mag}}$ is the magnetic force.
- $\mathbf{J}$ is the volume current density.
- $\mathbf{B}$ is the magnetic field.
- $d\tau$ is the volume element.

7\. The trajectory of a charged particle follows Newton's second law with the Lorentz force as the force. An equation of motion is a differential equation for position and velocity in time. This principle is used to solve the path of a charge in a given electromagnetic field.

The electromagnetic equation of motion is

$$
m\dfrac{d\mathbf{v}}{dt} = q\bigl(\mathbf{E} + \mathbf{v}\times\mathbf{B}\bigr)
$$

where

- $m$ is the mass of the particle.
- $\mathbf{v}$ is the velocity of the particle.
- $t$ is time.
- $q$ is the electric charge.
- $\mathbf{E}$ is the electric field.
- $\mathbf{B}$ is the magnetic field.

Note: These principles are the Lorentz force law, the electric force, the magnetic force, the magnetic zero-work theorem, the force on a current-carrying wire, the force on a current distribution, and the electromagnetic equation of motion. Also called the Lorentz force law.

## Elementary Example

### Simple

With $\mathbf{B} = \mathbf{0}$ and $\mathbf{E} = E\hat{\mathbf{x}}$,

$$
\mathbf{F} = qE\hat{\mathbf{x}}
$$

where

- only the electric field acts.

### General

With both fields nonzero,

$$
\mathbf{F} = q\mathbf{E} + q\mathbf{v}\times\mathbf{B}
$$

where

- the magnetic term depends on velocity.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §5.1.1–5.1.3 — Lorentz force, magnetic work, force on a wire, and force on a current distribution.
2. Knight, R. D. *Physics for Scientists and Engineers*. Pearson, 2023. — Lorentz force law.
3. Susskind, L., & Friedman, A. *Special Relativity and Classical Field Theory*. Basic Books, 2017. — electromagnetic force on a charge.
