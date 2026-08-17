# Quantum Tunneling

A process in which a particle has nonzero probability to appear beyond a classically forbidden barrier that is used to explain barrier penetration in quantum mechanics.

1\. In a region where $E<V$, a classical particle cannot enter, but the Schrödinger wavefunction decays exponentially rather than vanishing. This principle is used to assign a nonzero finding probability inside the barrier.

The decay constant in the forbidden region is

$$
\kappa = \dfrac{\sqrt{2m(V-E)}}{\hbar}
$$

where

- $\kappa$ is the decay constant.
- $m$ is the mass.
- $V$ is the potential height.
- $E$ is the energy.
- $\hbar$ is the reduced Planck constant.

2\. A wave incident on a barrier of finite width yields a nonzero transmitted amplitude on the other side. This principle is used to define tunneling as transmission with $E<V$.

3\. The transmission probability of a wide barrier falls exponentially with width and with $\kappa$. This principle is used to estimate tunneling rates.

The wide-barrier transmission is

$$
T \sim e^{-2\kappa L}
$$

where

- $T$ is the transmission probability.
- $L$ is the barrier width.
- $\kappa$ is the decay constant.

Note: These principles are exponential decay in the forbidden region, transmission with $E<V$, and the exponential dependence of $T$ on width. Also called barrier penetration. Also called tunneling.

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
