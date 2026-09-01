# Cauchy–Schwarz Inequality

An inequality that is used to bound the absolute value of an inner product or of $E[XY]$ by the product of the corresponding $L^2$ norms, where an inner product is a bilinear pairing that induces a length, and where the $L^2$ norm of a square-integrable random variable $X$ is $\|X\|_2=\sqrt{E[X^2]}$.

Note: Also called the Cauchy–Schwarz–Bunyakovsky inequality, or Schwarz’s inequality.

Expectation form. For random variables $X$ and $Y$ with finite second moments,

$$
|E[XY]|
\le
E[|XY|]
\le
\|X\|_2\,\|Y\|_2
=
\sqrt{E[X^2]\,E[Y^2]}
$$

where

- $X$ and $Y$ are real random variables.
- $E$ is expectation.
- $\|X\|_2=\sqrt{E[X^2]}$ is the $L^2$ norm of $X$.

This principle is used to control products of random variables by their second moments.

Inner-product form. In an inner-product space $L$ with $\langle\cdot,\cdot\rangle$ and $\|x\|=\sqrt{\langle x,x\rangle}$, for all $x,y\in L$,

$$
|\langle x,y\rangle|
\le
\|x\|\,\|y\|
$$

where

- $\langle x,y\rangle$ is the inner product of $x$ and $y$.
- $\|x\|$ is the norm induced by the inner product.

This principle is used to relate angles and lengths in abstract geometry, including $L^2$.

Equality condition. Equality holds if and only if the two elements are linearly dependent: in $L^2$, iff there is a constant $\lambda$ such that $\lambda X+Y=0$ almost surely (or both are zero). This principle is used to characterize when the bound is sharp.

Positivity proof. For every real $t$, $E[(Y-tX)^2]\ge 0$. Expanding and optimizing in $t$ yields the expectation form. This principle is used to derive Cauchy–Schwarz from nonnegativity of a quadratic.

$L^2$ as an inner-product space. On centered square-integrable random variables, $\langle U,V\rangle=\mathrm{Cov}(U,V)=E[UV]$ is an inner product, and $\|X\|_2$ is a length. Uncorrelated variables are orthogonal. This principle is used to read covariance geometrically.

Correlation bound. Applying Cauchy–Schwarz to $X-E[X]$ and $Y-E[Y]$ gives $|\mathrm{Cov}(X,Y)|\le\sqrt{\mathrm{Var}(X)\,\mathrm{Var}(Y)}$, hence $|\rho_{X,Y}|\le 1$, with $|\rho|=1$ iff the centered variables are linearly dependent a.s. This principle is used to place correlation in $[-1,1]$.

Hölder specialization. Cauchy–Schwarz is Hölder’s inequality at $p=q=2$. This principle is used to nest Cauchy–Schwarz inside the broader $L^p$ toolkit.

<!--
## Elementary Example

### Simple

Let $X\ge 0$ have finite variance. Write $X=X\cdot I(X>0)$.

### General

Cauchy–Schwarz on $X$ and $I(X>0)$ yields

$$
E[X]
=
E\!\left[X\cdot I(X>0)\right]
\le
\sqrt{E[X^2]\,P(X>0)},
$$

hence

$$
P(X>0)
\ge
\frac{(E[X])^2}{E[X^2]}.
$$

This second-moment bound shows a nonnegative random variable is positive with probability controlled by its first two moments.

where

- $I(X>0)$ is the indicator that $X$ is strictly positive.
- $P(X>0)$ is the probability that $X$ is strictly positive.
-->

## Problems

- Lower-bound $P(X>0)$ by $(E[X])^2/E[X^2]$ for nonnegative random variables.
- Derive the Cramér–Rao lower bound for unbiased estimators from covariance Cauchy–Schwarz.
- Prove $|\rho(X,Y)|\le 1$, with equality if $Y=aX+b$ almost surely.
- Prove $E[X]\,E[1/X]\ge 1$ for strictly positive random variables.
- Prove the triangle inequality $\|u+v\|\le\|u\|+\|v\|$ in an inner-product space.
- Minimize $\|x-y\|_2$ by orthogonal projection in an inner-product space. [ChatGPT]
- Derive Cauchy–Schwarz as Hölder’s inequality with $p=q=2$. [ChatGPT]

# References

1. Gut, A. *Probability: A Graduate Course*. Springer, 2005. Chapter 3, Theorem 3.1, p. 130 — expectation form $|E[XY]|\le E[|XY|]\le\|X\|_2\|Y\|_2$; Chapter 3, §3, p. 131 — $|\mathrm{Cov}(X,Y)|\le\sqrt{\mathrm{Var}\,X\cdot\mathrm{Var}\,Y}$ and $|\rho|\le 1$.
2. Blitzstein, J. K., and Hwang, J. *Introduction to Probability*. Chapman & Hall/CRC, 2014. Chapter 10, Theorem 10.1.1, p. 422 — $|E(XY)|\le\sqrt{E(X^2)E(Y^2)}$ and positivity proof via $E(Y-tX)^2$; Example 10.1.3, pp. 423–424 — second-moment method; Chapter 7, §7.3, p. 306 — $L^2$ geometry of covariance.
3. Ash, R. B., and Doléans-Dade, C. A. *Probability & Measure Theory*. 2nd ed., Academic Press, 1999. Chapter 3, §3.2.1, p. 104 — inner-product Cauchy–Schwarz and equality iff linear dependence; Chapter 4, §4.10, p. 182 — $|\rho|\le 1$ and equality condition.
4. Almudevar, A. *Theory of Statistical Inference*. Equation 1.15, p. 7 — $E[|XY|]^2\le E[X^2]E[Y^2]$ and equality $X=aY$; Hölder with $p=q=2$.
5. Florescu, I., and Tudor, C. A. *Handbook of Probability*. Appendix B, Lemma 14.7, p. 437 — $X,Y\in L^2$ implies $|E[XY]|\le E[|XY|]\le\|X\|_2\|Y\|_2$.
6. Kallenberg, O. *Foundations of Modern Probability*. Chapter 1, p. 15 — Cauchy–Buniakovsky as Hölder at $p=q=2$.
7. Kreyszig, E. *Advanced Engineering Mathematics*. Wiley. §9.2, p. 363; §20.1, p. 863 — vector form $|x^\top y|\le\|x\|_2\|y\|_2$.
