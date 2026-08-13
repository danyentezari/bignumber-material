# Derivation of Lagrangian

A derivation of the Lagrangian that is used to obtain $L=T-V$ as the slow-motion limit of a relativistic free particle with a potential.

<i>

**definition [d]** (*Derivation of Lagrangian*) From Schwichtenberg: start from the Lorentz-invariant free-particle Lagrangian with a potential,

- $L_{\mathrm{rel}} = -m c^{2}\sqrt{1 - \dfrac{1}{c^{2}}\left(\dfrac{dx}{dt}\right)^{2}} - V(x)$ .

For a slow particle, $\dfrac{dx}{dt} \ll c$, expand the square root,

- $\sqrt{1 - \dfrac{1}{c^{2}}\left(\dfrac{dx}{dt}\right)^{2}} \approx 1 - \dfrac{1}{2c^{2}}\left(\dfrac{dx}{dt}\right)^{2}$ ,

so that

- $L_{\mathrm{rel}} \approx -m c^{2} + \dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2} - V(x)$ .

Drop the constant $-m c^{2}$, which does not change the Euler–Lagrange equation, and identify the kinetic energy $T = \dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2}$. The non-relativistic Lagrangian is then

- $L = T - V = \dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2} - V(x)$ .

This form is required so that the Euler–Lagrange equation recovers Newton’s second law,

- $m\dfrac{d^{2}x}{dt^{2}} = -\dfrac{dV}{dx}$ .

where

- $L_{\mathrm{rel}}$ is the relativistic Lagrangian.
- $L$ is the non-relativistic Lagrangian.
- $m$ is the mass.
- $c$ is the speed of light.
- $x$ is the position.
- $t$ is time.
- $\dfrac{dx}{dt}$ is the velocity.
- $V(x)$ is the potential energy.
- $T$ is the kinetic energy.

</i>

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
