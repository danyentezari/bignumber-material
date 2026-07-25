# Delta Function

A mapping that is zero away from one point and has a finite integral concentrated there that is used to represent a point source in an integral.

<i>

**definition [d]** (*Dirac Delta Function = Delta Function = Delta Distribution = Generalized Function*) A generalized function $\delta(x)$ characterized informally by

- $\delta(x) = 0$ for $x \neq 0$ .
- $\displaystyle \int_{-\infty}^{\infty} \delta(x)\, dx = 1$ .

and, rigorously, by the sifting property

- $\displaystyle \int_{-\infty}^{\infty} f(x)\, \delta(x - a)\, dx = f(a)$ .

where

- $f$ is a continuous test function; $a \in \mathbb{R}$.
- $\delta$ is a distribution, not an ordinary function.

</i>

## Elementary Example
### Simple

The delta distribution is concentrated at one point. Informally, it vanishes off $0$ and has total integral $1$.

$$
\delta(x) = 0\ \text{for } x \neq 0
$$

$$
\int_{-\infty}^{\infty} \delta(x)\, dx = 1
$$

where

- $\delta$ is the Dirac delta.
- $x$ is the real variable.

### General

Against a continuous test function, delta sifts out the value at the center point $a$.

$$
\int_{-\infty}^{\infty} f(x)\, \delta(x - a)\, dx = f(a)
$$

$$
a = 2,\quad f(x) = x^{2},\quad \int f(x)\, \delta(x-2)\, dx = 4
$$

where

- $f$ is a continuous test function.
- $a$ is the point where $\delta$ is centered.


## References

1. Griffel, D. H. *Applied Functional Analysis*. Ellis Horwood, 1981. — Example 1.24 (sifting property; $\delta$ as a distribution).
2. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013.
3. Riley, K. F., Hobson, M. P., & Bence, S. J. *Mathematical Methods for Physics and Engineering*. Cambridge University Press, 2006.
