# Functional Analysis

A theory of infinite-dimensional vector spaces that is used to treat functions as vectors with length, angle, and continuous linear maps, where a vector space is a set closed under addition and scalar multiplication, and where a linear map is a map that preserves addition and scalar multiplication.

Normed linear space. A norm on a vector space assigns each vector a nonnegative length that vanishes only at the zero vector, scales by the absolute value of a scalar, and obeys the triangle inequality. A vector space with a norm is a normed linear space. This principle is used to measure the size of a vector by a single real number.

The triangle inequality is

$$
\|x+y\|\le\|x\|+\|y|
\quad\text{for all }x,y\in L.
$$

where

- $L$ is a vector space.
- $x$ and $y$ are vectors in $L$.
- $\|\cdot\|$ is a norm on $L$.

Ash and Doléans-Dade define a norm by nonnegativity, absolute homogeneity, and the triangle inequality, and they call a vector space endowed with a norm a normed linear space. The function $d(x,y)=\|x-y\|$ is the metric induced by the norm.

Banach space. A Banach space is a complete normed linear space: every Cauchy sequence of vectors converges to a limit that lies in the space. This principle is used to keep limit processes inside the space.

A sequence $(x_n)$ is Cauchy when

$$
\lim_{n,m\to\infty}\|x_n-x_m\|=0,
$$

and completeness requires a vector $x\in L$ with

$$
\lim_{n\to\infty}\|x_n-x\|=0.
$$

where

- $(x_n)$ is a sequence in $L$.
- $x$ is the limit in $L$.

Ash and Doléans-Dade state that a Banach space is a complete normed linear space relative to the metric induced by the norm. Billingsley records that $L^p$ is complete by the Riesz–Fischer theorem. Klenke states that a complete normed vector space is called a Banach space.

Inner product space. An inner product on a vector space is a scalar pairing that is linear in one argument, conjugate-symmetric, and positive definite. The pairing induces the norm $\|x\|=\sqrt{\langle x,x\rangle}$. This principle is used to introduce length, angle, and orthogonality.

Note: Also called a pre-Hilbert space.

The induced norm is

$$
\|x\|=\sqrt{\langle x,x\rangle}.
$$

where

- $\langle\cdot,\cdot\rangle$ is an inner product on $L$.
- $\|x\|$ is the norm induced by the inner product.

Ash and Doléans-Dade list linearity in the first argument, conjugate symmetry, and positive definiteness, and they note that $\sqrt{\langle x,x\rangle}$ defines a norm. Klenke gives the corresponding axioms on a real vector space.

Hilbert space. A Hilbert space is an inner product space that is complete under the metric induced by the inner product. A Hilbert space is therefore a Banach space whose norm comes from an inner product. This principle is used to extend Euclidean geometry to infinite dimensions.

Ash and Doléans-Dade state that if $L$ is complete under this norm, then $L$ is a Hilbert space. Gut states that Banach spaces with a norm derived from an inner product are called Hilbert spaces. Kokoszka and Reimherr define a Hilbert space as a complete inner product space.

Cauchy–Schwarz inequality. In an inner product space the absolute value of an inner product is at most the product of the induced norms, with equality precisely when the two vectors are linearly dependent. This principle is used to bound pairings by lengths and to obtain the triangle inequality for the induced norm.

The Cauchy–Schwarz inequality is

$$
|\langle x,y\rangle|\le\|x\|\,\|y\|
\quad\text{for all }x,y\in L.
$$

where

- $\langle x,y\rangle$ is the inner product of $x$ and $y$.
- $\|x\|$ and $\|y\|$ are the induced norms.

Ash and Doléans-Dade state the inequality and the linear-dependence equality case. Kallenberg obtains the $L^2$ form as Hölder’s inequality at $p=q=2$.

Bounded linear operator. A linear map $A$ from a normed space $L$ into a normed space $M$ is bounded when it multiplies norms by at most a finite constant. Boundedness is equivalent to continuity. This principle is used to control how a linear map stretches vectors.

Note: Also called a continuous operator.

The operator norm is

$$
\|A\|
=
\sup_{\|x\|\le 1}\|Ax\|_M
=
\sup_{x\neq 0}\frac{\|Ax\|_M}{\|x\|_L}.
$$

where

- $A$ is a linear map from $L$ to $M$.
- $\|Ax\|_M$ is the norm of the image in $M$.
- $\|A\|$ is the operator norm of $A$.

Ash and Doléans-Dade introduce the space of bounded linear operators and prove that it is complete when $M$ is complete. Kokoszka and Reimherr record that a linear operator is bounded if and only if it is continuous.

Dual space. The dual of a normed space is the Banach space of continuous linear functionals on that space. On a Hilbert space every such functional is inner product against a unique vector. This principle is used to represent continuous linear measurements by vectors in the original space.

The Riesz–Fréchet representation is

$$
F(x)=\langle y,x\rangle
\quad\text{for all }x\in H,
\qquad
\|F\|=\|y\|.
$$

where

- $H$ is a Hilbert space.
- $F$ is a continuous linear functional on $H$.
- $y$ is the unique vector in $H$ that generates $F$.
- $\|F\|$ is the dual norm of $F$.

Ash and Doléans-Dade state that the dual $L^*$ is a Banach space and that Riesz representation supplies a conjugate isometry from $H^*$ onto $H$. Klenke defines the dual and states the Riesz–Fréchet theorem. Billingsley identifies $L^q$ as the dual of $L^p$.

$L^2$ geometry of random variables. Square-integrable random variables form a Hilbert space with inner product equal to expectation of the product. Covariance is that inner product after centering. Conditional expectation is orthogonal projection onto a closed subspace of measurable square-integrable random variables. This principle is used to treat second-moment probability as Hilbert-space geometry.

The $L^2$ inner product is

$$
\langle X,Y\rangle_{L^2}=E[XY].
$$

where

- $X$ and $Y$ are square-integrable random variables.
- $E$ is expectation.

Gut notes that $L^2$ is self-dual and that covariance plays the role of an inner product. Vershynin writes $\langle X,Y\rangle_{L^2}=E[XY]$ and interprets covariance as alignment of centered vectors. Blitzstein takes $\langle U,V\rangle=\mathrm{Cov}(U,V)$ and identifies uncorrelated random variables with orthogonal vectors.

## Topics

1. [Cauchy–Schwarz Inequality](cauchy-schwarz-inequality.html)

# References

1. Ash, R. B. and Doléans-Dade, C. A. *Probability & Measure Theory*. 2nd ed. Academic Press, 1999. Chapter 3, §3.1.1, pp. 128–129 — norm, Banach space, inner product, Hilbert space; §3.2.1, p. 130 — Cauchy–Schwarz inequality; §3.3.1, Theorem 3.3.5, p. 136 — bounded operators; §3.3.5 and §3.4.1, pp. 136, 142 — dual space and Riesz representation.
2. Billingsley, P. *Probability and Measure*. 3rd ed. Wiley, 1995. Section 19, p. 250 — Banach space and completeness of $L^p$; p. 253, Theorem 19.3 — dual of $L^p$.
3. Klenke, A. *Probability Theory: A Comprehensive Course*. 2nd ed. Springer, 2014. Chapter 7, §7.1, p. 147 — completeness of $\|\cdot\|_p$ and Banach spaces; §7.3, Definition 7.19, p. 153 — inner product; §7.6, Definition 7.47 and Theorem 7.26, pp. 158, 166 — dual space and Riesz–Fréchet.
4. Gut, A. *Probability: A Graduate Course*. Springer, 2005. Chapter 3, Section 4, p. 132 — $L^2$ as a Hilbert space and covariance as inner product.
5. Kallenberg, O. *Foundations of Modern Probability*. 2nd ed. Springer, 2002. Chapter 1, p. 15 — Cauchy–Buniakovsky as Hölder at $p=q=2$.
6. Kokoszka, P. and Reimherr, M. *Introduction to Functional Data Analysis*. CRC Press, 2017. Chapter 10, §10.1, Definition 10.1.3, p. 217 — Hilbert space; §10.3, Problem 10.7, p. 231 — boundedness equivalent to continuity.
7. Vershynin, R. *High-Dimensional Probability*. Cambridge University Press, 2018. Chapter 1, §1.1, pp. 5–6 — $L^2$ inner product $E[XY]$ and covariance as alignment.
8. Blitzstein, J. K. *Introduction to Probability*. 2nd ed. CRC Press, 2019. Chapter 7, §7.3, p. 306 — covariance as inner product and uncorrelated as orthogonal.

<!--
Normed linear space. A normed linear space is a vector space equipped with a norm that defines distance through $d(x,y)=\|x-y\|$. This principle is used to define convergence, continuity, boundedness, and approximation in vector spaces.

Banach space. A Banach space is a complete normed linear space, so every Cauchy sequence converges within the space. This principle is used to ensure that limits produced by approximation remain elements of the space.

Inner product space. An inner product defines geometric structure and induces the norm $\|x\|=\sqrt{\langle x,x\rangle}$. This principle is used to define orthogonality, angles, projections, and geometric relations between vectors.

Hilbert space. A Hilbert space is a complete inner product space. This principle is used to extend Euclidean geometry to infinite-dimensional spaces while preserving convergence of Cauchy sequences.

Cauchy-Schwarz inequality. Every inner product satisfies $|\langle x,y\rangle|\le\|x\|\|y\|$. This principle is used to bound inner products and establish fundamental geometric inequalities.

Bounded linear operator. A linear operator between normed spaces is continuous exactly when it is bounded. This principle is used to characterize continuous linear transformations and define their operator norms.

Dual space. The dual space $X^*$ consists of all bounded linear functionals on a normed space $X$. This principle is used to study a space through continuous scalar-valued linear mappings.

## Problems

- Establish $|\langle x,y\rangle|\le\|x\|\|y\|$ in an inner product space.
- Obtain $\|x+y\|\le\|x\|+\|y\|$ from the Cauchy-Schwarz inequality.
- Show that a normed linear space is Banach by establishing convergence of every Cauchy sequence.
- Establish that a linear operator is continuous exactly when it is bounded.
- Obtain $\|T\|=\sup_{\|x\|\le 1}\|Tx\|$ for a bounded linear operator.
- Establish existence and uniqueness of orthogonal projection onto a closed subspace of a Hilbert space.
- Show that every bounded linear functional on a Hilbert space has the form $f(x)=\langle x,y\rangle$ for a unique $y$.
- Establish $|E[XY]|\le\sqrt{E[X^2]E[Y^2]}$ for $X,Y\in L^2$.
- Show that $E[X\mid G]$ is the orthogonal projection of $X\in L^2$ onto the closed subspace of $G$-measurable elements of $L^2$.
- Obtain $|\mathrm{Corr}(X,Y)|\le 1$ from Cauchy-Schwarz in $L^2$.

## Textbooks

- Robert B. Ash and Catherine Doléans-Dade, Probability and Measure Theory, Chapter 2, Integration Theory.
- Patrick Billingsley, Probability and Measure, Chapter 16, Integration.
- Achim Klenke, Probability Theory: A Comprehensive Course, Chapter 6, Integration.
- Allan Gut, Probability: A Graduate Course, chapters on expectation and conditional expectation.
- Erwin Kreyszig, Introductory Functional Analysis with Applications, Chapters 2 through 4, Normed Spaces, Inner Product Spaces, and Fundamental Theorems.
-->
