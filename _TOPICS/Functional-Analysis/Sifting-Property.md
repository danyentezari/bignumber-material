# Sifting Property

A property of an integral that picks out the value of a function at one point that is used to simplify equations that involve a concentrated source.

<i>

**definition [d]** (*Sifting Property = Sifting Formula*) The defining property of the Dirac delta function $\delta$: integrating it against a continuous function $f$ sifts out the value of $f$ at the point where the delta is centered:

- $\displaystyle \int_{-\infty}^{\infty} f(x)\, \delta(x - a)\, dx = f(a)$ .

where

- $\delta$ is the Dirac delta function.
- $f$ is a continuous test function.
- $a \in \mathbb{R}$ is the point at which $\delta$ is centered.
- $x$ is the variable of integration.

Note:

- the identity holds provided the interval of integration contains $a$; otherwise the integral is $0$.

</i>

## Elementary Example
### Simple

The sifting property picks out $f(a)$ from an integral against $\delta(x-a)$.

$$
\int_{-\infty}^{\infty} f(x)\, \delta(x - a)\, dx = f(a)
$$

$$
a = 1,\quad f(x) = 3x,\quad \text{result } = 3
$$

where

- $\delta$ is the Dirac delta.
- $f$ is a continuous test function.
- $a$ is the center point.

### General

If the integration interval does not contain $a$, the integral is $0$. If it does, the value is $f(a)$.

$$
\int_{0}^{2} x^{2}\, \delta(x - 1)\, dx = 1
$$

$$
\int_{3}^{5} x^{2}\, \delta(x - 1)\, dx = 0
$$

where

- the first interval contains $a = 1$.
- the second interval does not contain $a = 1$.


## References

1. Kreyszig, E. *Advanced Engineering Mathematics*, 10th ed. Wiley, 2011. — sifting property and sifting formula.
2. Griffel, D. H. *Applied Functional Analysis*. Ellis Horwood, 1981. — Example 1.24, sifting property.
3. Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for Physicists*, 7th ed. Elsevier / Academic Press, 2013. — defining property.
