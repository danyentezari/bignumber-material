# Maxwell's Equations

A set of four field equations that is used to describe how electric and magnetic fields arise from charges and currents and how the fields generate each other.

1\. Electric charge produces electric field that spreads from the charge. Charge density $\rho$ is charge per unit volume. Divergence $\nabla\cdot$ measures how much a vector field spreads from a point. This principle is used to find the electric field of a given charge distribution.

$$
\nabla\cdot\mathbf{E} = \dfrac{\rho}{\epsilon_{0}}
$$

2\. Magnetic field lines form closed loops with no beginning and no end. A magnetic monopole would be an isolated single magnetic pole; none exist. This principle is used to constrain magnetic fields so they never diverge from a point source.

$$
\nabla\cdot\mathbf{B} = 0
$$

3\. A magnetic field that changes in time produces a swirling electric field around the changing flux. Curl $\nabla\times$ measures the local swirl of a vector field. Electromagnetic induction is the generation of electric field by a changing magnetic field. This principle is used to design generators, transformers, and inductors.

$$
\nabla\times\mathbf{E} = -\dfrac{\partial\mathbf{B}}{\partial t}
$$

4\. Magnetic fields are produced by electric current and by electric fields that change in time. Current density $\mathbf{J}$ is charge flow per unit area. The displacement term $\epsilon_{0}\dfrac{\partial\mathbf{E}}{\partial t}$ is Maxwell's addition: a changing electric field sources magnetic field like a current. This principle is used to compute fields of electromagnets and to show that electromagnetic waves travel in empty space.

$$
\nabla\times\mathbf{B} = \mu_{0}\mathbf{J} + \mu_{0}\epsilon_{0}\dfrac{\partial\mathbf{E}}{\partial t}
$$

5\. Electric charge is never created and never destroyed: if charge inside a volume falls, the same charge must flow out through the surface. Local conservation means a conserved quantity moves continuously through space. This principle is used to tie charge density to current density as a consistency condition.

$$
\nabla\cdot\mathbf{J} = -\dfrac{\partial\rho}{\partial t}
$$

6\. A charge feels force from the electric field, and a moving charge feels an added force sideways to both its velocity and the magnetic field. This principle is used to predict how charged particles move in electromagnetic fields.

$$
\mathbf{F} = q\bigl(\mathbf{E} + \mathbf{v}\times\mathbf{B}\bigr)
$$

Note: These principles are Gauss's law, Gauss's law for magnetism, Faraday's law of induction, the Ampère-Maxwell law, the continuity equation, and the Lorentz force law.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §2.2.4, §5.1.1, §5.1.3, §5.3.2, §7.2.1, §7.3.1, §7.3.3, §8.1.1 — Maxwell equations, continuity, and Lorentz force.
