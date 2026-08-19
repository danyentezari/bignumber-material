# Coordinate Transformations

A set of equations that translate spatial and temporal measurements of events from one reference frame's coordinates into another's.

Event mapping between frames. A coordinate transformation maps the space and time labels of an event from one frame to another. A coordinate label is a set of four numbers giving position and time. A linear mapping is a rule in which those coordinates enter only to the first power. This principle is used to convert laboratory measurements into a moving frame.

Galilean versus Lorentz time. Galilean transformations treat time as the same in every frame. Lorentz transformations mix time with position. Absolute time is a time all observers assign the same value. Frame-dependent time is a time that changes with the observer's velocity. This principle is used to explain why simultaneous events in one frame need not be simultaneous in another.

The Galilean transformations are

$$
x' = x - vt
$$

$$
y' = y
$$

$$
z' = z
$$

$$
t' = t
$$

where

- $(x,y,z,t)$ are spacetime coordinates in the first inertial frame.
- $(x',y',z',t')$ are spacetime coordinates in the second inertial frame.
- $v$ is the constant relative velocity of the primed frame along $x$.

The Lorentz transformations are

$$
x' = \gamma(x - vt)
$$

$$
y' = y
$$

$$
z' = z
$$

$$
t' = \gamma\left(t - \dfrac{vx}{c^{2}}\right)
$$

where

- $c$ is the speed of light in vacuum.
- $\gamma = \dfrac{1}{\sqrt{1 - \dfrac{v^{2}}{c^{2}}}}$ is the Lorentz factor.

Preservation of the spacetime interval. Lorentz transformations are the linear maps that leave the spacetime interval unchanged. A spacetime interval is the invariant four-dimensional squared separation of two events. This principle is used to keep the speed of light the same in every inertial frame.

Low-speed Galilean correspondence. When the relative speed is much smaller than the speed of light, Lorentz transformations reduce to Galilean transformations. This principle is used to recover everyday classical coordinate changes.

## References

1. Knight, R. D. *Physics for Scientists and Engineers: A Strategic Approach with Modern Physics*. Pearson, 2023. — source for the heading explanation.
2. Knight, R. D. *Physics for Scientists and Engineers: A Strategic Approach with Modern Physics*. Pearson, 2023. — Lorentz transformations; low-speed Galilean limit.
3. Griffiths, D. J. *Introduction to Electrodynamics*. Cambridge University Press, 2024. — Galilean transformations; Lorentz boosts; frame-dependent time.
4. Emam, M. H. *Covariant Physics*. Oxford University Press, 2021. — Lorentz versus Galilean time.
5. Carroll, S. M. *Spacetime and Geometry*. Cambridge University Press. — linear maps that preserve the interval.
6. Shankar, R. *Fundamentals of Physics I*. Yale University Press, 2019. — event mapping; interval preservation; Galilean limit.
