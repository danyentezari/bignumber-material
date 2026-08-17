# Quantum Chemistry

A branch of physical chemistry that is used to determine the structures, bonding, stabilities, and light-related properties of molecules from the laws of physics.

1\. Every molecule is made of positively charged nuclei and negatively charged electrons held by electrostatic forces. These particles are too small for ordinary Newtonian mechanics. This principle is used to replace classical trajectories by a wavefunction whose allowed energies are discrete.

The time-independent Schrödinger equation is

$$
\hat{H}\psi = E\psi
$$

where

- $\hat{H}$ is the Hamiltonian operator.
- $\psi$ is the wavefunction.
- $E$ is the energy eigenvalue.

2\. Nuclei are far heavier than electrons, so nuclei move slowly while electrons adjust quickly around them. This principle is used to hold the nuclei fixed while solving for the electrons.

The electronic Schrödinger equation at fixed nuclei is

$$
\hat{H}_{\mathrm{el}}\psi_{\mathrm{el}} = E_{\mathrm{el}}(R)\psi_{\mathrm{el}}
$$

where

- $\hat{H}_{\mathrm{el}}$ is the electronic Hamiltonian.
- $\psi_{\mathrm{el}}$ is the electronic wavefunction.
- $E_{\mathrm{el}}(R)$ is the electronic energy at nuclear geometry $R$.

3\. The true ground-state energy is never higher than the energy computed from a trial wavefunction. A trial wavefunction is an approximate wavefunction with adjustable parameters. This principle is used to improve approximate molecular wavefunctions by lowering the computed energy.

The variational theorem is

$$
E_{\mathrm{trial}} = \dfrac{\displaystyle\int\psi^{*}\hat{H}\psi\,d\tau}{\displaystyle\int\psi^{*}\psi\,d\tau} \geq E_{0}
$$

where

- $E_{\mathrm{trial}}$ is the energy of the trial function.
- $E_{0}$ is the true ground-state energy.
- $\psi$ is the trial wavefunction.
- $\hat{H}$ is the Hamiltonian.
- $d\tau$ is the volume element.

4\. Mapping where electrons are likely to be shows which atom arrangements sit lowest in energy and form stable bonds. This principle is used to predict shapes, stabilities, and how molecules take up or give off light.

Note: These principles are the molecular Schrödinger equation, the Born-Oppenheimer approximation, the variational theorem, and the use of electron distributions to predict structure and spectra.

## References

1. Levine, I. N. *Physical Chemistry*. Ch. 18 — atomic structure. Ch. 19 — molecular electronic structure.
2. McQuarrie, D. A., & Simon, J. D. *Physical Chemistry: A Molecular Approach*. Ch. 8 — multielectron atoms. Ch. 9 — the chemical bond.
