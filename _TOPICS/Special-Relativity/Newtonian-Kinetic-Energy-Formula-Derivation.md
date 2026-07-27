# Newtonian Kinetic Energy Formula Derivation

A derivation of the Newtonian kinetic energy formula that is used to obtain $K = \dfrac{1}{2}mv^{2}$ from the work-energy theorem.

Note: Also called $T$ in some sources.

<i>

**definition [d]** (*Newtonian Kinetic Energy Formula Derivation*) From Shankar: start from the constant-acceleration kinematic relation

- $v_{2}^{2} = v_{1}^{2} + 2ad$ ,

with Newton’s second law $a = \dfrac{F}{m}$, so

- $v_{2}^{2} = v_{1}^{2} + 2\dfrac{F}{m}d$ .

Rearranging gives

- $\dfrac{1}{2}mv_{2}^{2} - \dfrac{1}{2}mv_{1}^{2} = Fd$ .

Defining $K = \dfrac{1}{2}mv^{2}$ and $W = Fd$ yields the work-energy theorem

- $K_{2} - K_{1} = W$ .

where

- $v_{1}$ and $v_{2}$ are the initial and final speeds.
- $a$ is the acceleration.
- $d$ is the distance traveled.
- $F$ is a constant force.
- $m$ is the mass.
- $K$ is the kinetic energy.
- $K_{1}$ and $K_{2}$ are the initial and final kinetic energies.
- $W$ is the work done by the force.

</i>

<i>

**definition [d]** (*Newtonian Kinetic Energy Formula Derivation*) From Logan: begin with the damped oscillator equation

- $mx'' + \gamma x' + kx = 0$ .

Multiply by the velocity $x'$:

- $mx'x'' + \gamma (x')^{2} + kxx' = 0$ .

By the chain rule,

- $mx'x'' = \dfrac{d}{dt}\left(\dfrac{1}{2}m(x')^{2}\right)$ ,
- $kxx' = \dfrac{d}{dt}\left(\dfrac{1}{2}kx^{2}\right)$ ,

so

- $\dfrac{d}{dt}\left[\dfrac{1}{2}m(x')^{2} + \dfrac{1}{2}kx^{2}\right] = -\gamma(x')^{2}$ .

The kinetic energy term identified in the bracket is

- $T = \dfrac{1}{2}m(x')^{2}$ .

where

- $x(t)$ is the displacement.
- $x'$ is the velocity.
- $x''$ is the acceleration.
- $m$ is the mass.
- $\gamma$ is the damping constant.
- $k$ is the spring constant.
- $t$ is time.
- $T$ is the kinetic energy.
- $\dfrac{1}{2}kx^{2}$ is the elastic potential energy in the oscillator.

</i>

## Elementary Example

### Simple

A constant force $F = 6\,\mathrm{N}$ acts through $d = 2\,\mathrm{m}$ on $m = 3\,\mathrm{kg}$ starting from rest.

$$
W = Fd = 12\,\mathrm{J}
$$

$$
K_{2} = W = \dfrac{1}{2}(3)v_{2}^{2} = 12\,\mathrm{J}
$$

where

- $K_{1} = 0$ at rest.
- $W$ is the work done by $F$.

### General

For $m = 2\,\mathrm{kg}$ and $v = 4\,\mathrm{m/s}$,

$$
K = \dfrac{1}{2}mv^{2} = 16\,\mathrm{J}
$$

where

- $K$ is the Newtonian kinetic energy.

## References

1. Shankar, R. *Fundamentals of Physics I*. Yale University Press, 2019. — from $v_{2}^{2}=v_{1}^{2}+2\left(\dfrac{F}{m}\right)d$ to $K_{2}-K_{1}=W$ with $K=\dfrac{1}{2}mv^{2}$.
2. Logan, J. D. *A First Course in Differential Equations*. Springer, 2015. — multiply $mx''+\gamma x'+kx=0$ by $x'$ to identify $T=\dfrac{1}{2}m(x')^{2}$.
