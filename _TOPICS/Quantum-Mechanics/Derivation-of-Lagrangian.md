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

2\. For a slow particle the square root expands to first order in the square of the speed over $c$. A slow particle is a particle whose speed is much smaller than the speed of light. This principle is used to extract the Newtonian kinetic term.

The slow-motion expansion is

$$
\sqrt{1 - \dfrac{1}{c^{2}}\left(\dfrac{dx}{dt}\right)^{2}} \approx 1 - \dfrac{1}{2c^{2}}\left(\dfrac{dx}{dt}\right)^{2}
$$

where

- $c$ is the speed of light.
- $\dfrac{dx}{dt}$ is the velocity.

3\. Substituting the expansion and dropping the constant rest-energy term produces the non-relativistic Lagrangian. This principle is used to obtain $L=T-V$ for the Schrödinger Hamiltonian and for the path integral.

The non-relativistic Lagrangian is

$$
L = T - V = \dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2} - V(x)
$$

where

- $L$ is the non-relativistic Lagrangian.
- $T$ is the kinetic energy.
- $V$ is the potential energy.
- $m$ is the mass.

4\. In quantum mechanics the same $L$ supplies the phase $e^{iS/\hbar}$ of each path. This principle is used to connect the classical Lagrangian to quantum amplitudes.

Note: These principles are the relativistic Lagrangian, the slow-motion expansion, $L=T-V$, and the path-integral phase.

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

1. Schwichtenberg, J. *Physics from Symmetry*. Springer, 2018. — from $L_{\mathrm{rel}}$ to $L=T-V$.
2. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — $L=T-V$ in the path-integral formulation.
