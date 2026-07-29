# Quantum Tunneling

A process in which a particle has nonzero probability to appear beyond a classically forbidden barrier that is used to explain barrier penetration in quantum mechanics.

Note: Also called barrier penetration. Also called tunneling.

<i>

**definition [d]** (*Quantum Tunneling*) From Shankar: in a region where the total energy $E$ is less than the potential $V$, the classical particle cannot enter, but the Schrödinger wavefunction is exponentially decaying rather than zero, so there is a nonzero probability to find the particle in the forbidden region. Transmission through a barrier of finite width is called tunneling.

where

- $E$ is the energy.
- $V$ is the potential height.
- the wavefunction decays but does not vanish inside the barrier.

</i>

<i>

**definition [d]** (*Quantum Tunneling*) From Hall: for a potential barrier with $E < V$ on a finite interval, the time-independent Schrödinger equation still has solutions, and a wave incident from one side yields a nonzero transmitted amplitude on the other side.

where

- transmission with $E < V$ is tunneling.

</i>

<i>

**definition [d]** (*Quantum Tunneling*) From Sakurai: barrier penetration occurs when the energy is insufficient for classical transit, yet the wavefunction connects incident and transmitted regions through the barrier.

where

- the transmitted intensity is typically exponentially small in barrier width and height.

</i>

## Elementary Example

### Simple

For a barrier of height $V = 2$ and energy $E = 1$ on an interval of width $1$, the wavefunction inside behaves like

$$
\psi(x) \propto e^{-\kappa x},\quad \kappa = \sqrt{2m(V-E)}
$$

with $\hbar = 1$.

where

- $\kappa$ sets the decay rate in the forbidden region.

### General

The transmission probability for a wide barrier scales roughly as

$$
T \sim e^{-2\kappa L}
$$

where

- $L$ is the barrier width.

## References

1. Shankar, R. *Fundamentals of Physics II*. Yale University Press, 2020. — tunneling as transmission with $E<V$.
2. Hall, B. C. *Quantum Theory for Mathematicians*. Springer, 2013. — nonzero transmission through a barrier.
3. Sakurai, J. J., & Napolitano, J. *Modern Quantum Mechanics*. Cambridge University Press, 2021. — barrier penetration.
