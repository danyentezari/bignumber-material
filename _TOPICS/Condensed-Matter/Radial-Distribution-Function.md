# Radial Distribution Function

A function $g(r)$ that is used to say how the local density of molecules varies with distance $r$ from a chosen molecule, so that the solid, liquid, and gas phases can be told apart by the peaks and long-distance behavior of $g(r)$.

The pair-correlation function. The radial distribution function $g(r)$ is the local density of molecules at distance $r$ from a chosen molecule, divided by the bulk density. This principle is used to map where neighbors are favored to sit.

The pair-correlation function is

$$
g(r) = \dfrac{\rho(r)}{\rho_{\mathrm{bulk}}}
$$

where

- $g(r)$ is the radial distribution function.
- $\rho(r)$ is the local number density at distance $r$.
- $\rho_{\mathrm{bulk}}$ is the average number density of the sample.

Long-range order. A crystal has lasting long-range order, so $g(r)$ is a periodic array of sharp spikes at lattice spacings. Long-range order is repeating atomic arrangement that extends through the sample. This principle is used to recognize a crystal from its $g(r)$.

Short-range order. A liquid has only short-range order: a strong first peak near the nearest-neighbor distance, then weaker peaks that die out, and $g(r)$ tends to $1$ at large $r$. This principle is used to recognize a liquid from its $g(r)$.

The liquid large-distance limit is

$$
\lim_{r\to\infty} g(r) = 1
$$

where

- $r$ is the distance from a chosen molecule.
- $g(r)$ is the radial distribution function.

Gas pair correlation. In a dilute gas, $g(r)$ is $0$ below the collision diameter and is flat near $1$ beyond that distance, with no secondary shells. This principle is used to recognize a gas from its $g(r)$.

Excluded volume. At very short distances inside a dense fluid, $g(r)$ falls to $0$ because molecules cannot overlap. This principle is used to encode the finite size of molecules.

The coordination number. The first peak of $g(r)$ sits at the nearest-neighbor distance. The area under that peak is the coordination number, the number of immediate neighbors. This principle is used to count how tightly atoms pack in the first shell.

The coordination number is

$$
\mathrm{CN} = \int_{0}^{r_{\mathrm{shell}}} 4\pi\rho_{0}\,g(r)\,r^{2}\,dr
$$

where

- $\mathrm{CN}$ is the coordination number.
- $r_{\mathrm{shell}}$ is the outer radius of the first peak.
- $\rho_{0}$ is the average number density.
- $g(r)$ is the radial distribution function.
- $r$ is the distance from a chosen molecule.

Note: Also called the pair-correlation function.

## References

1. Atkins, P., de Paula, J., & Keeler, J. *Atkins’ Physical Chemistry*. — crystal $g(r)$ as sharp spikes; liquid short-range order with decaying oscillations.
2. Levine, I. N. *Physical Chemistry*. — liquid nearest-neighbor peak and shells; gas $g(r)$ flat beyond the collision diameter.
3. Shankar, R. *Fundamentals of Physics I*. — gas with no lasting positional order.
