# Gauge Field

A field built from the curvature of a connection that is used to measure the physical strength of a gauge interaction.

Note: Also called the field strength. Also called the field tensor. Also called the curvature of the gauge potential.

<i>

**definition [d]** (*Gauge Field = Field Tensor = Curvature*) From Nash and Sen: the connection $A_{i}(x)$ is what is called the gauge potential in physics, and the curvature $F_{ij}$ is called the gauge field or field tensor. The curvature is related to the potential by

- $F = dA + A \wedge A$ .

where

- $A$ is the gauge potential, also called the connection.
- $F$ is the gauge field, also called the curvature.
- $d$ is the exterior derivative.
- $\wedge$ is the wedge product of forms.

</i>

## Elementary Example

### Simple

In electromagnetism the gauge group is abelian, so $A \wedge A = 0$ and the field strength reduces to

$$
F = dA
$$

$$
\mathbf{B} = \nabla \times \mathbf{A}
$$

where

- $\mathbf{A}$ is the vector potential.
- $\mathbf{B}$ is the magnetic field from that potential.

### General

In a nonabelian gauge theory the quadratic term is kept.

$$
F = dA + A \wedge A
$$

$$
F' = h F h^{-1}
$$

where

- $h$ is a gauge transformation.
- $F$ transforms tensorially, while $A$ transforms as a connection.

## References

1. Nash, C., & Sen, S. *Topology and Geometry for Physicists*. Academic Press, 1983. — gauge potential as connection; gauge field as curvature $F = dA + A\wedge A$.
