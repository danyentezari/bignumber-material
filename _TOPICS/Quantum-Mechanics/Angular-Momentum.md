# Angular Momentum

An operator equal to the cross product of position and momentum that is used to represent rotational motion of a quantum system.

Note: Also denoted $\mathbf{L}$. Also denoted $\hat{\mathbf{L}}$.

## Traits

1. Is defined classically as the cross product of position and linear momentum.
2. Is conserved when the potential is invariant under rotations.
3. Acts as the infinitesimal Hamiltonian generator of spatial rotations.
4. Has components that do not all commute with one another.
5. Has a squared total operator that commutes with each Cartesian component.
6. Is quantized so that its squared magnitude takes discrete values of the form $\ell(\ell+1)\hbar^{2}$.
7. Appears as orbital angular momentum from spatial motion or as intrinsic spin.
8. Has ladder operators that raise or lower the projection eigenvalue.
9. Shows spatial quantization: its component along a chosen axis takes discrete values.
10. Relates to a particle's magnetic dipole moment through the gyromagnetic ratio.

## Traits (Sakurai)

1. Is defined as the generator of infinitesimal rotations, not only as $\mathbf{x}\times\mathbf{p}$.
2. Obeys $[J_{i}, J_{j}] = i\hbar\epsilon_{ijk}J_{k}$.
3. Prevents simultaneous sharp values of different Cartesian components.
4. Has $J^{2}$ commuting with every Cartesian component $J_{k}$.
5. Restricts allowed $j$ values to integers or half-integers from the commutation relations alone.
6. Uses ladder operators $J_{\pm}$ to raise or lower the projection eigenvalue $m$.
7. Transforms so that expectation values of its components rotate like classical vectors.
8. Restricts the orbital case $\mathbf{L}=\mathbf{x}\times\mathbf{p}$ to integer $\ell$.
9. Commutes with parity, so rotations are compatible with space inversion.
10. Gives spin-$\tfrac{1}{2}$ states a nonclassical sign change under a $2\pi$ rotation.

## Applications

1. Derives Kepler's second law of planetary motion from angular momentum conservation.
2. Reduces central-force Schrödinger problems to a one-dimensional radial equation.
3. Explains discrete beam splitting of silver or cesium atoms in the Stern-Gerlach experiment.
4. Explains anomalous Zeeman splitting of atomic spectral lines in a magnetic field.
5. Formulates rigid-body rotation through the moment of inertia tensor.
6. Describes the precession of a gyroscope under gravitational torque.
7. Classifies atomic and molecular states into spectroscopic shells such as $s$, $p$, $d$, and $f$.
8. Sets selection rules for radiative transition probabilities.
9. Couples angular momenta of subsystems with Clebsch-Gordan coefficients.
10. Underpins discrete electronic orbits and Rydberg levels in the Bohr model.

## Applications (Sakurai)

1. Separates radial and angular variables in the Schrödinger equation for central potentials.
2. Analyzes hyperfine structure and atomic states through spin-orbit coupling $\mathbf{L}\cdot\mathbf{S}$.
3. Sorts and manipulates atomic spin states in Stern-Gerlach cesium beam experiments.
4. Studies $2\pi$ rotations of spinors with neutron interferometry.
5. Couples independent angular-momentum systems with Clebsch-Gordan coefficients.
6. Explains paramagnetic susceptibility through Brillouin's formula.
7. Maps angular probability distributions with spherical harmonics.
8. Models rotation matrices with Schwinger's two-oscillator construction.
9. Tests nonlocality with spin-singlet correlations and Bell inequalities.
10. Fixes selection rules for vector and tensor operators via the Wigner-Eckart theorem.

<i>

**definition [d]** (*Angular Momentum*) From Sakurai: the angular momentum operator is

- $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ .

where

- $\mathbf{L}$ is the angular momentum operator.
- $\mathbf{r}$ is the position operator.
- $\mathbf{p}$ is the momentum operator.

</i>

<i>

**definition [d]** (*Angular Momentum Commutation Relations*) From Hall: the components of angular momentum satisfy

- $[L_{i}, L_{j}] = i\hbar\sum_{k}\epsilon_{ijk}L_{k}$ .

where

- $L_{i}$ are the Cartesian components of $\mathbf{L}$.
- $\epsilon_{ijk}$ is the Levi-Civita symbol.
- $\hbar$ is the reduced Planck constant.

</i>

<i>

**definition [d]** (*Angular Momentum*) From Shankar: classically $\mathbf{L} = \mathbf{r}\times\mathbf{p}$, and in quantum theory the same relation holds with $\mathbf{r}$ and $\mathbf{p}$ as operators, so

- $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ .

where

- $\mathbf{L}$ is the angular momentum.
- $\mathbf{r}$ and $\mathbf{p}$ are operators.

</i>

## Elementary Example

### Simple

For motion in the $xy$-plane with $z$-component only,

$$
L_{z} = xp_{y} - yp_{x}
$$

where

- $L_{z}$ is the angular momentum about the $z$-axis.

### General

The three components obey

$$
[L_{x}, L_{y}] = i\hbar L_{z}
$$

where

- cyclic permutations give the other relations.

## References

1. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — Traits (Sakurai) and Applications (Sakurai); generators; commutation; Stern-Gerlach; Wigner-Eckart.
2. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — commutation relations; conservation under rotations.
3. Shankar, R. *Fundamentals of Physics*. Yale University Press. — classical and operator $\mathbf{L}=\mathbf{r}\times\mathbf{p}$.
4. Feynman, R. P., Leighton, R. B., & Sands, M. *The Feynman Lectures on Physics*. — cross product; gyroscope; spectroscopic shells.
5. Knight, R. D. *Physics for Scientists and Engineers: A Strategic Approach with Modern Physics*. Pearson, 2023. — quantization of $L^{2}$.
6. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*. Academic Press, 2013. — orbital vs spin; Clebsch-Gordan.
