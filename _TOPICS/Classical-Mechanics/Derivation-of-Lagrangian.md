# Derivation of Lagrangian

A derivation that is used to obtain $L=T-V$ as the slow-motion limit of a relativistic free particle with a potential, where the Lagrangian is the function whose stationary action gives the equations of motion.

1\. A free particle with a potential has a Lorentz-invariant Lagrangian built from rest energy, speed, and potential energy. Rest energy is the energy $mc^{2}$ of a particle at rest. This principle is used to start from a relativistic expression that reduces to Newtonian mechanics at low speed.

The relativistic Lagrangian is

$$
L_{\mathrm{rel}} = -m c^{2}\sqrt{1 - \dfrac{1}{c^{2}}\left(\dfrac{dx}{dt}\right)^{2}} - V(x)
$$

where

- $L_{\mathrm{rel}}$ is the relativistic Lagrangian.
- $m$ is the mass.
- $c$ is the speed of light.
- $x$ is the position.
- $t$ is time.
- $V(x)$ is the potential energy.

2\. For a slow particle the square root expands to first order in the square of the speed over $c$. A slow particle is a particle whose speed is much smaller than the speed of light. This principle is used to extract the Newtonian kinetic term from the relativistic Lagrangian.

The slow-motion expansion is

$$
\sqrt{1 - \dfrac{1}{c^{2}}\left(\dfrac{dx}{dt}\right)^{2}} \approx 1 - \dfrac{1}{2c^{2}}\left(\dfrac{dx}{dt}\right)^{2}
$$

where

- $c$ is the speed of light.
- $\dfrac{dx}{dt}$ is the velocity.

3\. Substituting the expansion produces a constant rest-energy term plus $\dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2}$ minus the potential. Kinetic energy is the energy of motion. This principle is used to identify the Newtonian kinetic energy.

The expanded Lagrangian is

$$
L_{\mathrm{rel}} \approx -m c^{2} + \dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2} - V(x)
$$

where

- $L_{\mathrm{rel}}$ is the relativistic Lagrangian.
- $m$ is the mass.
- $c$ is the speed of light.
- $\dfrac{dx}{dt}$ is the velocity.
- $V(x)$ is the potential energy.

4\. An additive constant in the Lagrangian does not change the Euler-Lagrange equation, so the rest-energy term $-mc^{2}$ may be dropped. This principle is used to pass to the standard non-relativistic Lagrangian.

The non-relativistic Lagrangian is

$$
L = T - V = \dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2} - V(x)
$$

where

- $L$ is the non-relativistic Lagrangian.
- $T$ is the kinetic energy.
- $V$ is the potential energy.
- $m$ is the mass.
- $\dfrac{dx}{dt}$ is the velocity.

5\. The Euler-Lagrange equation applied to $L=T-V$ recovers Newton's second law. This principle is used to confirm that the derived Lagrangian describes the same Newtonian motion.

The Euler-Lagrange recovery of Newton's law is

$$
m\dfrac{d^{2}x}{dt^{2}} = -\dfrac{dV}{dx}
$$

where

- $m$ is the mass.
- $x$ is the position.
- $t$ is time.
- $V$ is the potential energy.

Note: These principles are the relativistic free-particle Lagrangian with a potential, the slow-motion expansion, the identification of kinetic energy, the irrelevance of an additive constant in the Lagrangian, and the recovery of Newton's second law from the Euler-Lagrange equation.

## Elementary Example

### Simple

For $V(x) = 0$ and $\dfrac{dx}{dt} \ll c$, the expansion gives

$$
L = \dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2}
$$

where

- $L$ is the non-relativistic Lagrangian.
- $m$ is the mass.
- $\dfrac{dx}{dt}$ is the velocity.

### General

For a nonzero potential $V(x)$ in the same slow-motion limit,

$$
L = \dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2} - V(x)
$$

where

- $L$ is the non-relativistic Lagrangian.
- $m$ is the mass.
- $\dfrac{dx}{dt}$ is the velocity.
- $V(x)$ is the potential energy.

## References

1. Schwichtenberg, J. *Physics from Symmetry*. Springer, 2018. — from $L_{\mathrm{rel}}=-mc^{2}\sqrt{1-(\mathrm{d}x/\mathrm{d}t)^{2}/c^{2}}-V(x)$ to $L=\dfrac{1}{2}m(\mathrm{d}x/\mathrm{d}t)^{2}-V(x)$.
