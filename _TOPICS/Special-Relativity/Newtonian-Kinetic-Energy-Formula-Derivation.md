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

- $v$ is the speed.
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

- $m\dfrac{d^{2}x}{dt^{2}} + \gamma\dfrac{dx}{dt} + kx = 0$ .

Multiply by the velocity $\dfrac{dx}{dt}$:

- $m\dfrac{dx}{dt}\dfrac{d^{2}x}{dt^{2}} + \gamma\left(\dfrac{dx}{dt}\right)^{2} + kx\dfrac{dx}{dt} = 0$ .

By the [chain rule](Chain-Rule.md),

- $m\dfrac{dx}{dt}\dfrac{d^{2}x}{dt^{2}} = \dfrac{d}{dt}\left(\dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2}\right)$ ,
- $kx\dfrac{dx}{dt} = \dfrac{d}{dt}\left(\dfrac{1}{2}kx^{2}\right)$ ,

so

- $\dfrac{d}{dt}\left[\dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2} + \dfrac{1}{2}kx^{2}\right] = -\gamma\left(\dfrac{dx}{dt}\right)^{2}$ .

The kinetic energy term identified in the bracket is

- $T = \dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2}$ .

where

- $x$ is the displacement.
- $x(t)$ is the displacement as a function of time.
- $\dfrac{dx}{dt}$ is the velocity.
- $\dfrac{d^{2}x}{dt^{2}}$ is the acceleration.
- $m$ is the mass.
- $\gamma$ is the damping constant.
- $k$ is the spring constant.
- $t$ is time.
- $\dfrac{d}{dt}$ is the time derivative.
- $T$ is the kinetic energy.
- $\dfrac{1}{2}kx^{2}$ is the elastic potential energy in the oscillator.

</i>

## References

1. Shankar, R. *Fundamentals of Physics I*. Yale University Press, 2019. — from $v_{2}^{2}=v_{1}^{2}+2\left(\dfrac{F}{m}\right)d$ to $K_{2}-K_{1}=W$ with $K=\dfrac{1}{2}mv^{2}$.
2. Logan, J. D. *A First Course in Differential Equations*. Springer, 2015. — multiply $m\dfrac{d^{2}x}{dt^{2}}+\gamma\dfrac{dx}{dt}+kx=0$ by $\dfrac{dx}{dt}$ to identify $T=\dfrac{1}{2}m\left(\dfrac{dx}{dt}\right)^{2}$.
