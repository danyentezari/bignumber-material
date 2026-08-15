# Radial Distribution Function

A function $g(r)$ that is used to say how the local density of molecules varies with distance $r$ from a chosen molecule, so that the solid, liquid, and gas phases can be told apart by the peaks and long-distance behavior of $g(r)$.

Note: Also called the pair-correlation function.

1. In a crystal, $g(r)$ is a periodic array of sharp spikes at lattice spacings, which shows lasting long-range order.
2. In a liquid, $g(r)$ has a strong first peak near the nearest-neighbor distance, then weaker broader peaks that die out, and $g(r)$ tends to $1$ at large $r$, which shows only short-range order.
3. In a dilute gas, $g(r)$ is $0$ below the collision diameter and is flat near $1$ beyond that distance, with no secondary shells.
4. At very short distances inside a dense fluid, $g(r)$ falls to $0$ because molecules cannot overlap.

## Elementary Example

### Simple

Sample $g(r)$ at three distances for a dilute gas with collision diameter $1$.

$$
g(0.5) = 0,\quad g(1.5) = 1,\quad g(3) = 1
$$

### General

Sample values that mimic liquid short-range shells that fade, with $g(r)$ tending to $1$.

$$
g(1) = 2.5,\quad g(2) = 1.3,\quad g(3) = 1.05,\quad g(10) = 1
$$

where

- the larger early values mark neighbor shells
- the late value $1$ marks loss of long-range order

## References

1. Atkins, P., de Paula, J., & Keeler, J. *Atkins’ Physical Chemistry*. — crystal $g(r)$ as sharp spikes; liquid short-range order with decaying oscillations.
2. Levine, I. N. *Physical Chemistry*. — liquid nearest-neighbor peak and shells; gas $g(r)$ flat beyond the collision diameter.
3. Shankar, R. *Fundamentals of Physics I*. — gas with no lasting positional order.
