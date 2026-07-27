# Lorentz Transformations

The coordinate transformation that is used to convert spacetime coordinates between inertial frames moving at constant relative velocity.

Note: Also called a Lorentz boost when the frames differ by a constant velocity along one axis.

<i>

**definition [d]** (*Lorentz Transformations*) From Knight: the Lorentz transformations relating the coordinates $(x,y,z,t)$ of an event in one inertial frame to the coordinates $(x',y',z',t')$ in a second inertial frame moving at constant velocity $v$ along the shared $x$-axis are

- $x' = \gamma(x - vt)$ ,
- $y' = y$ ,
- $z' = z$ ,
- $t' = \gamma\left(t - \dfrac{vx}{c^{2}}\right)$ ,

with inverse

- $x = \gamma(x' + vt')$ ,
- $y = y'$ ,
- $z = z'$ ,
- $t = \gamma\left(t' + \dfrac{vx'}{c^{2}}\right)$ ,

where

- $(x,y,z,t)$ are spacetime coordinates in the first inertial frame.
- $(x',y',z',t')$ are spacetime coordinates in the second inertial frame.
- $v$ is the constant relative velocity of the primed frame along $x$.
- $c$ is the speed of light in vacuum.
- $\gamma = \dfrac{1}{\sqrt{1 - \dfrac{v^{2}}{c^{2}}}} = \dfrac{1}{\sqrt{1 - \beta^{2}}}$ is the Lorentz factor.
- $\beta = \dfrac{v}{c}$ is the relative speed in units of $c$.

</i>

<i>

**definition [d]** (*Lorentz Transformations*) From Griffiths: with the Lorentz factor

- $\gamma = \dfrac{1}{\sqrt{1 - \dfrac{v^{2}}{c^{2}}}}$ ,

the boost takes the form

- $\bar{x} = \gamma(x - vt)$ ,
- $\bar{y} = y$ ,
- $\bar{z} = z$ ,
- $\bar{t} = \gamma\left(t - \dfrac{v}{c^{2}}x\right)$ .

where

- $(\bar{x},\bar{y},\bar{z},\bar{t})$ are the coordinates in the moving frame.
- $v$ is the relative velocity along $x$.
- $c$ is the speed of light.

</i>

## Elementary Example

### Simple

For a relative speed $v = 0.6c$, the Lorentz factor is

$$
\gamma = \dfrac{1}{\sqrt{1 - 0.36}} = 1.25
$$

$$
x' = 1.25(x - 0.6ct)
$$

where

- $\gamma$ stretches both space and time mixing terms.

### General

An event at the origin of the moving frame, $x' = 0$, satisfies $x = vt$ in the lab frame, and the lab time and moving time are related by

$$
t' = \gamma\left(t - \dfrac{vx}{c^{2}}\right) = \dfrac{t}{\gamma}
$$

when $x = vt$.

where

- this is the time-dilation relation for a clock at rest in the primed frame.

## References

1. Knight, R. D. *Physics for Scientists and Engineers: A Strategic Approach with Modern Physics*. Pearson, 2023. — Lorentz transformations and $\gamma = \dfrac{1}{\sqrt{1-\dfrac{v^{2}}{c^{2}}}}$.
2. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — Lorentz boost with factor $\gamma$.
3. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — Lorentz transformations in terms of $\beta$ and $\gamma$.
