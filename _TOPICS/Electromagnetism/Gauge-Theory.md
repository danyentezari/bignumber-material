# Gauge Theory

A field theory with gauge symmetries that is used to describe fundamental interactions so that physics does not depend on the descriptive choice of local frames, where a gauge symmetry is a local symmetry of the potentials, and where a local frame is a descriptive choice of phase or internal coordinates at each point.

1\. The laws of physics stay the same when the phase of a matter field is changed independently at each point. A matter field is a field that describes charged matter. This principle is used to introduce the force field that restores that local invariance.

The local phase transformation is

$$
\psi'(x) = e^{-ie\alpha(x)}\psi(x)
$$

where

- $\psi$ is the matter field.
- $e$ is the coupling constant.
- $\alpha(x)$ is a spacetime-dependent phase.

2\. Physical observables cannot depend on the local choice of phase. An observable is a quantity that can be measured. This principle is used to keep charge conservation and to require that the Lagrangian be unchanged by a gauge transformation.

Gauge invariance of the Lagrangian is

$$
\mathcal{L}(\psi, D_{\mu}\psi, F_{\mu\nu}) = \mathcal{L}(\psi', D'_{\mu}\psi', F'_{\mu\nu})
$$

where

- $\mathcal{L}$ is the Lagrangian density.
- $\psi$ is the matter field.
- $D_{\mu}$ is the covariant derivative.
- $F_{\mu\nu}$ is the gauge field strength.

3\. Local invariance requires a compensating vector field, the gauge potential, that tracks how the internal frame turns from point to point. This principle is used to define parallel transport of charged fields.

The connection one-form is

$$
\mathcal{A} = -ie A_{\mu}\,dx^{\mu}
$$

where

- $\mathcal{A}$ is the connection.
- $e$ is the coupling constant.
- $A_{\mu}$ is the gauge potential.
- $dx^{\mu}$ are the coordinate differentials.

4\. The physical field strength is the curvature of that connection. Curvature is the failure of parallel transport around a closed loop to return the same internal frame. This principle is used to compute the force field from the potential.

The curvature is related to the potential by

$$
F = dA + A \wedge A
$$

where

- $A$ is the gauge potential.
- $F$ is the gauge field.
- $d$ is the exterior derivative.
- $\wedge$ is the wedge product of forms.

5\. A gauge transformation changes the potential without changing the curvature. This principle is used to pass between equivalent potentials that describe the same physical field.

The electromagnetic gauge transformation is

$$
A'_{\mu} = A_{\mu} - \dfrac{\partial\alpha}{\partial x^{\mu}}
$$

where

- $A'_{\mu}$ is the transformed potential.
- $A_{\mu}$ is the original potential.
- $\alpha$ is the gauge function.

6\. Ordinary derivatives of a charged field pick up extra phase terms, so they are replaced by a covariant derivative that includes the potential. Minimal coupling is that replacement. This principle is used to introduce the interaction of matter with the gauge field.

The covariant derivative is

$$
D_{\mu}\psi = \Bigl(\dfrac{\partial}{\partial x^{\mu}} - ie A_{\mu}\Bigr)\psi
$$

where

- $D_{\mu}$ is the covariant derivative.
- $\psi$ is the matter field.
- $e$ is the coupling constant.
- $A_{\mu}$ is the gauge potential.

7\. Electromagnetism is the gauge theory of the group $U(1)$. An abelian group is a group whose operations commute, so the photon does not carry charge. This principle is used to recover the electromagnetic potentials and fields as the $U(1)$ connection and curvature.

The abelian field strength is

$$
F_{\mu\nu} = \dfrac{\partial A_{\nu}}{\partial x^{\mu}} - \dfrac{\partial A_{\mu}}{\partial x^{\nu}}
$$

where

- $F_{\mu\nu}$ is the electromagnetic field tensor.
- $A_{\mu}$ is the electromagnetic potential.

Note: These principles are the gauge principle, gauge symmetry, the gauge potential, the gauge field as curvature, gauge transformations, the covariant derivative with minimal coupling, and $U(1)$ gauge theory. Also called a gauge field theory.

## Elementary Example

### Simple

Classical electrodynamics is an abelian gauge theory with potentials $(V,\mathbf{A})$ and physical fields $(\mathbf{E},\mathbf{B})$.

$$
\mathbf{B} = \nabla \times \mathbf{A}
$$

$$
\mathbf{E} = -\nabla V - \dfrac{\partial\mathbf{A}}{\partial t}
$$

where

- gauge changes of $(V,\mathbf{A})$ leave $\mathbf{E}$ and $\mathbf{B}$ fixed.

### General

A nonabelian gauge theory uses a matrix-valued potential $A$ and field strength

$$
F = dA + A \wedge A
$$

where

- $A$ takes values in a Lie algebra.
- $F$ is the gauge field of the theory.

## References

1. Nakahara, M. *Geometry, Topology and Physics*. Institute of Physics Publishing, 2003. §1.8, Ch. 10 — gauge principle, connection, and curvature.
2. Emam, M. H. *Covariant Physics: From Classical Mechanics to General Relativity and Beyond*. Oxford University Press, 2021. — field theories as gauge theories with gauge symmetries.
3. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. §10.1.2 — electromagnetic gauge transformations.
