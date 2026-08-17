# Boundary Conditions

Matching rules for the electromagnetic fields at an interface that are used to join the solutions on either side of a surface, where an interface is the surface separating two media.

1\. The discontinuity in the normal component of $\mathbf{D}$ equals the free surface charge density. This principle is used to relate the jump in the electric field to charge sitting on the boundary.

The normal boundary condition on $\mathbf{D}$ is

$$
\mathbf{D}_{2}^{\perp} - \mathbf{D}_{1}^{\perp} = \sigma_{f}
$$

where

- $\mathbf{D}$ is the electric displacement.
- $\sigma_{f}$ is the free surface charge density.
- the superscript $\perp$ marks the component normal to the surface, from side 1 toward side 2.

2\. The tangential component of $\mathbf{E}$ is continuous if the surface holds no changing magnetic flux in an infinitely thin layer. This principle is used to match the electric field along the interface.

The tangential boundary condition on $\mathbf{E}$ is

$$
\mathbf{E}_{2}^{\parallel} - \mathbf{E}_{1}^{\parallel} = 0
$$

where

- $\mathbf{E}$ is the electric field.
- the superscript $\parallel$ marks the component tangent to the surface.

3\. The normal component of $\mathbf{B}$ is continuous. This principle is used to match the magnetic field across any interface.

The normal boundary condition on $\mathbf{B}$ is

$$
\mathbf{B}_{2}^{\perp} - \mathbf{B}_{1}^{\perp} = 0
$$

where

- $\mathbf{B}$ is the magnetic field.

4\. The discontinuity in the tangential component of $\mathbf{H}$ equals the free surface current. This principle is used to relate the jump in the magnetic field to current on the boundary.

The tangential boundary condition on $\mathbf{H}$ is

$$
\mathbf{H}_{2}^{\parallel} - \mathbf{H}_{1}^{\parallel} = \mathbf{K}_{f}\times\hat{\mathbf{n}}
$$

where

- $\mathbf{H}$ is the auxiliary magnetic field.
- $\mathbf{K}_{f}$ is the free surface current density.
- $\hat{\mathbf{n}}$ is the unit normal from side 1 toward side 2.

Note: These principles are the electromagnetic interface conditions on $\mathbf{D}$, $\mathbf{E}$, $\mathbf{B}$, and $\mathbf{H}$.

## References

1. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §7.3.5 — boundary conditions on electromagnetic fields.
