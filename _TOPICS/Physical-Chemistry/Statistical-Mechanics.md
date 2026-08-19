# Statistical Mechanics

A mathematical bridge that is used to deduce the macroscopic properties of bulk matter from the microscopic quantum properties of its individual molecules.

The ensemble average. Everyday samples hold so many molecules that individual paths cannot be followed. A macroscopic property is then an average over the crowd of molecular states. This principle is used to replace an impossible mechanical description by a probability description.

The Boltzmann distribution. In thermal equilibrium the probability of a molecular state falls exponentially with its energy. The Boltzmann factor is that exponential weight. This principle is used to compute the fraction of molecules in each energy level.

The Boltzmann distribution is

$$
p_{i} = \dfrac{e^{-E_{i}/kT}}{Z}
$$

where

- $p_{i}$ is the probability of state $i$.
- $E_{i}$ is the energy of state $i$.
- $k$ is Boltzmann's constant.
- $T$ is the absolute temperature.
- $Z$ is the partition function.

The partition function. The partition function is the sum of the Boltzmann factors of all states. This principle is used to generate the thermodynamic functions from one molecular sum.

The molecular partition function is

$$
Z = \sum_{i} e^{-E_{i}/kT}
$$

where

- $Z$ is the partition function.
- $E_{i}$ is the energy of state $i$.
- $k$ is Boltzmann's constant.
- $T$ is the absolute temperature.

The Boltzmann entropy. Entropy measures how many microscopic arrangements share the same overall state. Multiplicity is that number of arrangements. This principle is used to give entropy a molecular meaning and to recover the Second Law.

The Boltzmann entropy is

$$
S = k\ln W
$$

where

- $S$ is the entropy.
- $k$ is Boltzmann's constant.
- $W$ is the multiplicity of the macroscopic state.

The Helmholtz energy from $Z$. The Helmholtz energy of a canonical system is determined by the partition function. A canonical system is a closed system in contact with a heat bath at fixed temperature. This principle is used to compute free energies and equilibrium constants from molecular levels.

The Helmholtz energy is

$$
F = -kT\ln Z
$$

where

- $F$ is the Helmholtz energy.
- $k$ is Boltzmann's constant.
- $T$ is the absolute temperature.
- $Z$ is the partition function.

## References

1. Levine, I. N. *Physical Chemistry*. Ch. 21 §21.1 — statistical mechanics.
2. Atkins, P., de Paula, J., & Keeler, J. *Atkins’ Physical Chemistry*. Focus 13 — statistical thermodynamics.
