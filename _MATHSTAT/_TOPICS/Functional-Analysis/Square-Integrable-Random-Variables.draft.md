# Square-Integrable Random Variables

A random variable that is used to work with finite second moments, where a random variable is a measurable real-valued function on a probability space, and where a second moment is the expected value of the square of that function.

<!-- >
Note: Also called a random variable in $L^2$.

Square-integrability. A real random variable $X$ on a probability space $(\Omega,\mathcal{F},P)$ is square-integrable when its second moment is finite. This principle is used to name the random variables that belong to $L^2$.

The square-integrability condition is

$$
E[X^2]
=
\int_\Omega X^2(\omega)\,dP(\omega)
<\infty.
$$

where

- $X$ is a real random variable.
- $E[X^2]$ is the second moment of $X$.
- $\Omega$ is the sample space.
- $\omega$ is an outcome in $\Omega$.
- $P$ is the probability measure.

Membership in $L^2$. The space $L^2(\Omega,\mathcal{F},P)$ is the collection of square-integrable random variables on that probability space. This principle is used to treat finite-second-moment random variables as a single vector space.

The space is

$$
L^2(\Omega,\mathcal{F},P)
=
\bigl\{X:\Omega\to\mathbb{R}:
X\text{ is }\mathcal{F}\text{-measurable and }
\|X\|_{L^2}<\infty\bigr\}.
$$

where

- $\mathcal{F}$ is the $\sigma$-algebra of events.
- $\|X\|_{L^2}$ is the $L^2$ norm of $X$.

Almost-sure identification. Random variables that agree almost surely represent the same element of $L^2$. An almost-sure equality is an equality that fails only on a set of probability zero. This principle is used to make the zero-norm vector the almost-surely zero random variable.

The identification is

$$
X\sim Y
\iff
P(X=Y)=1.
$$

where

- $X$ and $Y$ are square-integrable random variables.
- $\sim$ is almost-sure equality.

Square-integrability implies integrability. On a probability space, a finite second moment implies a finite first absolute moment. This principle is used to place every square-integrable random variable in $L^1$.

The moment comparison is

$$
E[|X|]
\le
\sqrt{E[X^2]}
<\infty.
$$

where

- $E[|X|]$ is the first absolute moment of $X$.
- $\sqrt{E[X^2]}$ is the $L^2$ norm of $X$.

The $L^2$ norm. The $L^2$ norm of a square-integrable random variable is the square root of its second moment. This principle is used to measure the root-mean-square size of the random variable.

The $L^2$ norm is

$$
\|X\|_{L^2}
=
\sqrt{E[X^2]}.
$$

where

- $\|X\|_{L^2}$ is the $L^2$ norm.
- $E[X^2]$ is the second moment of $X$.

Second moment and variance. The second moment is taken about zero. Variance is the second moment about the mean. This principle is used to separate raw second-moment size from centered spread.

The variance identity is

$$
\mathrm{Var}(X)
=
E[(X-E[X])^2]
=
E[X^2]-(E[X])^2.
$$

where

- $\mathrm{Var}(X)$ is the variance of $X$.
- $E[X]$ is the mean of $X$.
- $E[X^2]$ is the second moment of $X$.

Nested $L^p$ spaces. On a probability space the $L^p$ norms increase with $p$, so a random variable with a finite $q$ moment for $q\ge 2$ is square-integrable. This principle is used to pass from higher-moment assumptions down to $L^2$ and $L^1$.

The inclusions are

$$
L^q(\Omega,\mathcal{F},P)
\subset
L^2(\Omega,\mathcal{F},P)
\subset
L^1(\Omega,\mathcal{F},P)
\qquad (q\ge 2)
$$

and

$$
\|X\|_{L^1}
\le
\|X\|_{L^2}
\le
\|X\|_{L^q}.
$$

where

- $L^p(\Omega,\mathcal{F},P)$ is the space of random variables with finite $p$th absolute moment.
- $\|X\|_{L^p}$ is the $L^p$ norm of $X$.
- $q$ is an exponent at least $2$.

# References

1. Achim Klenke, *Probability Theory: A Comprehensive Course*, 2nd ed., Springer, 2014. Chapter 5, §5.1, Definition 5.1(iii), p. 101 — square-integrable random variables and variance. Chapter 7, §7.1, Definition 7.1, p. 146 — $L^p$ after almost-everywhere identification.
2. Roman Vershynin, *High-Dimensional Probability*, Cambridge University Press, 2018. Chapter 1, §1.1, pp. 5–6 — $p$th moments, the space $L^p$, and the $L^2$ norm $(E|X|^2)^{1/2}$.
3. Anthony Almudevar, *Theory of Statistical Inference*, CRC Press, 2021. Chapter 1, §1.3.2, Definition 1.3, p. 5 — $L^p$ as the collection of random variables with finite $L^p$ norm.
4. Robert B. Ash and Catherine A. Doléans-Dade, *Probability & Measure Theory*, 2nd ed., Academic Press, 1999. Chapter 3, §3.1.2, p. 129 — $L^p$ after identifying functions that agree almost everywhere. Chapter 4, §4.10, Lemma 4.10.5, p. 176 — a finite moment of order $k$ implies finite moments of lower order.
5. Patrick Billingsley, *Probability and Measure*, Anniversary Edition, Wiley, 2012. Section 21, p. 280, (21.5) — a finite absolute moment of order $k$ implies finite absolute moments of lower order.
6. Ionut Florescu and Ciprian A. Tudor, *Handbook of Probability*, Wiley, 2013. Chapter 11, §11.3, pp. 341–342, Proposition 11.5 — $L^p$ norms are nondecreasing in $p$. Chapter 13, §13.2.1, Theorem 13.11, p. 343 — $p\le q$ implies $L^q\subset L^p$ and $\|X\|_p\le\|X\|_q$.
7. Subhabrata Chakraborti and Jean Dickinson Gibbons, *Nonparametric Statistical Inference*, 5th ed., CRC Press, 2010. Chapter 1, p. 9 — variance as the second central moment.

<!--
Square integrability. A random variable $X$ is square-integrable when $E[X^2]<\infty$. This principle is used to identify the random variables that have a finite second moment.

Membership in $L^2$. The space $L^2$ consists of the square-integrable random variables on a given probability space. This principle is used to collect finite-second-moment random variables into one vector space.

Almost-sure identification. Random variables that agree almost surely represent the same element of $L^2$. This principle is used to treat almost-surely zero variables as the zero vector.

Implication of integrability. A finite second moment implies a finite first absolute moment. This principle is used to place every square-integrable random variable in $L^1$.

$L^2$ norm. The $L^2$ norm of $X$ is $\sqrt{E[X^2]}$. This principle is used to measure the root-mean-square size of a square-integrable random variable.

Second moment and variance. Variance equals $E[X^2]-(E[X])^2$. This principle is used to separate the raw second moment from centered spread.

Nested moments. On a probability space, a finite moment of order $q\ge 2$ implies square-integrability. This principle is used to pass from a higher-moment hypothesis down to $L^2$.

## Problems

- Establish that $X$ is square-integrable exactly when $\|X\|_{L^2}<\infty$.
- Show that $E[X^2]<\infty$ implies $E[|X|]<\infty$.
- Obtain $E[|X|]\le\sqrt{E[X^2]}$ on a probability space.
- Establish that $X\sim Y$ when $P(X=Y)=1$ identifies the same $L^2$ element.
- Obtain $\mathrm{Var}(X)=E[X^2]-(E[X])^2$ for square-integrable $X$.
- Show that $\mathrm{Var}(X)=E[(X-E[X])^2]$.
- Establish $\|X\|_{L^1}\le\|X\|_{L^2}$ on a probability space.
- Show that $X\in L^q$ for $q\ge 2$ implies $X\in L^2$.

## Textbooks

- Achim Klenke, Probability Theory: A Comprehensive Course, Chapter 5, Moments and Independence.
- Roman Vershynin, High-Dimensional Probability, Chapter 1, Preliminaries on random vectors.
- Robert B. Ash and Catherine Doléans-Dade, Probability and Measure Theory, Chapter 4, Integration and Differentiation.
- Patrick Billingsley, Probability and Measure, Section 21, Moments.
- Ionut Florescu and Ciprian A. Tudor, Handbook of Probability, Chapter 11, $L^p$ Spaces.
-->
