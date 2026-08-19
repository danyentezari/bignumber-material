# Field Theory

A continuum description of electromagnetism that is used to obtain the field equations from a local action, where a field is a physical quantity assigned at every spacetime point, and where an action is the spacetime integral of a Lagrangian density.

Hamilton's principle of stationary action. The actual history of a field makes the action stationary. Stationary means the first variation of the action vanishes. This principle is used to derive the equations of motion of the field.

The action is

$$
S = \displaystyle\int \mathcal{L}\, d^{4}x
$$

where

- $S$ is the action.
- $\mathcal{L}$ is the Lagrangian density.
- $d^{4}x$ is the spacetime volume element.

The Lagrangian density. Because a field is spread through space and time, its dynamics are described by a Lagrangian per unit spacetime volume. A Lagrangian density is that local Lagrangian. This principle is used to write an action that treats space and time on the same footing.

The Euler–Lagrange field equations. The field equations are the Euler–Lagrange equations of the Lagrangian density. This principle is used to convert a Lagrangian description into explicit differential equations for the potential.

The Euler–Lagrange equation for the potential is

$$
\dfrac{\partial\mathcal{L}}{\partial A_{\mu}} - \partial_{\nu}\left(\dfrac{\partial\mathcal{L}}{\partial(\partial_{\nu}A_{\mu})}\right) = 0
$$

where

- $\mathcal{L}$ is the Lagrangian density.
- $A_{\mu}$ is the electromagnetic potential.
- $\partial_{\nu}$ is the spacetime derivative.

The Maxwell Lagrangian. The dynamics of the electromagnetic field and its coupling to current are encoded in one Lorentz-invariant Lagrangian density. This principle is used to recover the inhomogeneous Maxwell equations as Euler–Lagrange equations.

The Maxwell Lagrangian density is

$$
\mathcal{L} = -\dfrac{1}{4\mu_{0}} F_{\mu\nu}F^{\mu\nu} - A_{\mu}J^{\mu}
$$

where

- $\mathcal{L}$ is the Lagrangian density.
- $F_{\mu\nu}$ is the electromagnetic field tensor.
- $A_{\mu}$ is the electromagnetic potential.
- $J^{\mu}$ is the four-current.
- $\mu_{0}$ is the permeability of free space.

Locality of interactions. A charge interacts with the electromagnetic field only at its own location. Disturbances in the field travel at a finite speed. This principle is used to replace instantaneous action at a distance by local field equations.

Noether's theorem. Every continuous symmetry of the action yields a conserved current. A conserved current is a four-vector whose spacetime divergence vanishes. This principle is used to obtain conservation of charge from global gauge symmetry.

The energy-momentum tensor. The energy and momentum of the field are the components of a symmetric tensor $T_{\mu\nu}$. The component $T_{00}$ is the energy density. This principle is used to compute the energy and momentum stored and carried by the field.

Gauge invariance of the action. A shift of the potential by a gradient leaves the action unchanged. This principle is used to keep only gauge-invariant field quantities in the dynamics. See [Gauge Theory](gauge-theory.html).

The electromagnetic gauge transformation is

$$
A_{\mu} \rightarrow A_{\mu} + \partial_{\mu}\Lambda
$$

where

- $A_{\mu}$ is the electromagnetic potential.
- $\Lambda$ is the gauge function.

Note: Also called classical field theory.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — Maxwell Lagrangian and electromagnetic gauge invariance.
2. Emam, M. H. *Covariant Physics: From Classical Mechanics to General Relativity and Beyond*. Oxford University Press, 2021. — stationary action, Lagrangian density, Euler–Lagrange field equations, energy-momentum tensor.
3. Carroll, S. M. *Spacetime and Geometry*. Cambridge University Press, 2019. — action for fields and the stress-energy tensor.
4. Susskind, L., & Friedman, A. *Quantum Mechanics: The Theoretical Minimum*. Basic Books, 2014. — Lagrangian density and locality of field interactions.
5. Nakahara, M. *Geometry, Topology and Physics*. Institute of Physics Publishing, 2003. — Euler–Lagrange equations for gauge potentials.
