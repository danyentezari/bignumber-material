# Expectation

A probability-weighted average of a random variable that is used to summarize its long-run mean value under a probability model, where a random variable is a measurable function from a sample space to the real line, and where the average is the integral of that function against the probability measure.

Note: Also called expected value or mean.

<i>

**definition [d]** (*Expectation of a Discrete Random Variable*)

The expectation of a discrete random variable $X$ whose distinct possible values are $x_1,x_2,\ldots$ is

$$
E(X)
=
\sum_{j} x_j\,P(X=x_j)
$$

where

- $X$ is a discrete random variable.
- $x_j$ are the distinct values of $X$.
- $P(X=x_j)$ is the probability that $X$ equals $x_j$.

The expectation is undefined if $\sum_j |x_j|P(X=x_j)$ diverges.

</i>

This principle is used to compute means for countable supports.

<i>

**definition [d]** (*Expectation of a Continuous Random Variable*)

The expectation of a continuous random variable $X$ with PDF $f$ is

$$
E(X)
=
\int_{-\infty}^{\infty} x\,f(x)\,dx
$$

where

- $X$ is a continuous random variable.
- $f$ is the probability density function of $X$.

provided that $\int_{-\infty}^{\infty}|x|f(x)\,dx$ is finite.

</i>

This principle is used to compute means for absolutely continuous laws.

<i>

**definition [d]** (*Expectation as a Lebesgue Integral*)

If $X$ is a random variable on a probability space $(\Omega,\mathcal{F},P)$, the expectation of $X$ is

$$
E(X)
=
\int_\Omega X\,dP
$$

where

- $(\Omega,\mathcal{F},P)$ is a probability space.
- $X$ is a random variable on that space.
- $dP$ denotes integration with respect to $P$.

provided the integral exists. If $E|X|<\infty$, then $X$ is integrable.

</i>

This principle is used to unify discrete and continuous cases as one Lebesgue integral.

Absolute integrability. $X$ is integrable if and only if $|X|$ is integrable, which requires $E|X|<\infty$ and rules out indeterminate $\infty-\infty$ forms. This principle is used to decide when $E(X)$ exists as a real number.

Linearity. For integrable $X,Y$ and constant $c$, $E(X+Y)=E(X)+E(Y)$ and $E(cX)=cE(X)$, even when $X$ and $Y$ are dependent. This principle is used to compute means of sums without joint distributions.

Monotonicity. If $X\le Y$ almost surely, then $E(X)\le E(Y)$, with equality if and only if $X=Y$ almost surely. This principle is used to compare expectations from almost-sure orderings.

Fundamental bridge. For an event $A$ with indicator $I_A$, $P(A)=E(I_A)$. This principle is used to convert probability statements into expectation statements.

<i>

**definition [d]** (*Law of the Unconscious Statistician*)

LOTUS in the discrete and continuous cases is

$$
E(g(X))
=
\sum_x g(x)\,P(X=x),
\qquad
E(g(X))
=
\int_{-\infty}^{\infty} g(x)\,f(x)\,dx
$$

where

- $g$ is a real-valued function.
- $f$ is the PDF of $X$ in the continuous case.

</i>

This principle is used to compute moments of transformed variables without first finding the law of $g(X)$.

Tower property. $E(Y)=E[E(Y\mid X)]$ whenever the expectations exist. This principle is used to compute unconditional means by conditioning.

Markov and Chebyshev. Nonnegative $g$ and $A=\{g(X)\ge a\}$ give $E[g(X)]\ge a\,P(A)$. With $g(x)=|x|$ one obtains Markov’s inequality; with $g(x)=(x-E[X])^2$ one obtains Chebyshev’s inequality. This principle is used to bound tails from moments.

<!--
## Elementary Example

### Simple

Let $X\sim\mathrm{Bin}(n,p)$. Write $X=I_1+\cdots+I_n$, where $I_j$ indicates success on trial $j$.

### General

Each trial has $E(I_j)=P(I_j=1)=p$. By linearity, even though the indicators are dependent in combinatorial counting, $E(X)=np$. The same mean follows from summing $k\binom{n}{k}p^k(1-p)^{n-k}$, but linearity with indicators is shorter.

$$
E(X)
=
\sum_{j=1}^{n} E(I_j)
=
np
$$

where

- $I_j$ is the indicator of success on trial $j$.
- $n$ is the number of trials.
- $p$ is the success probability.
-->

# References

1. Blitzstein, J. K., and Hwang, J. *Introduction to Probability*. Chapman & Hall/CRC, 2014. Chapter 4, Definition 4.1.1, p. 137 — discrete expectation; Theorem 4.2.1, p. 139 — linearity; Example 4.2.2, pp. 140–141 — binomial mean via indicators; Proposition 4.2.4, p. 142 — monotonicity; Theorem 4.4.2, p. 151 — $P(A)=E(I_A)$; Theorem 4.5.1, p. 156 — discrete LOTUS; Chapter 5, Definition 5.1.9, p. 200 — continuous expectation; Theorem 5.1.10, p. 201 — continuous LOTUS; Chapter 9, Theorem 9.3.7, p. 400 — $E(Y)=E[E(Y\mid X)]$.
2. Ash, R. B., and Doléans-Dade, C. A. *Probability & Measure Theory*. 2nd ed., Academic Press, 1999. Chapter 4, Definition 4.10.1, p. 175 — $E(X)=\int_\Omega X\,dP$.
3. Gut, A. *Probability: A Graduate Course*. Springer, 2005. Chapter 2, §4, p. 52 — $EX=\int X\,dP$ and integrability via $E|X|<\infty$.
4. Casella, G., and Berger, R. L. *Statistical Inference*. Definition 2.2.1, p. 47 — $E[g(X)]$ for discrete $X$ when the sum exists.
5. Tijms, H. *Understanding Probability*. Chapter 10, §10.2, p. 326 — continuous expectation with $\int|x|f(x)\,dx<\infty$.
6. Rosenthal, J. S. *A First Look at Rigorous Probability Theory*. Chapter 4, §§4.1–4.2, pp. 48–50 — construction via simple, nonnegative, and signed variables; Chapter 6, Theorem 6.1.1, p. 67 — change of variables for $E[f(X)]$.
7. Klenke, A. *Probability Theory: A Comprehensive Course*. Chapter 5, Theorem 5.4, p. 104 — linearity and monotonicity.
8. Pfeiffer, P. E. *Concepts of Probability Theory*. Chapter 4, §4-4, (I4), p. 166 — integrability; Chapter 5, (E1), p. 203 — $E[a I_A]=a P(A)$; (E7), p. 205 — Markov and Chebyshev from $E[g(X)]\ge a P(A)$.

<!--
Discrete expectation. For a discrete random variable, the expectation is the probability-weighted sum of its possible values. This principle is used to calculate the mean value of discrete probability distributions.

Continuous expectation. For a continuous random variable, the expectation is the integral of the variable multiplied by its probability density. This principle is used to calculate the mean value of continuous probability distributions.

Linearity of expectation. The expectation of a linear combination of random variables equals the same linear combination of their expectations. This principle is used to simplify expected values of sums without requiring independence.

Law of the unconscious statistician. The expectation of a function of a random variable can be computed directly from the distribution of the original random variable. This principle is used to calculate transformed expectations without first deriving the distribution of the transformed variable.

Conditional expectation. The conditional expectation is the expected value of a random variable given specified information about another random variable. This principle is used to update expected values when additional information is known.

Law of total expectation. The expectation of a random variable equals the expectation of its conditional expectation given another random variable. This principle is used to compute expectations by conditioning on information that makes the calculation simpler.

Expectation of products under independence. Independent integrable random variables satisfy the equality between the expectation of their product and the product of their expectations. This principle is used to simplify expected products when independence is established.

## Problems

- Obtain $E(X+Y)=E(X)+E(Y)$ without independence and without a joint distribution.
- Obtain $E[g(X)]$ from the law of $X$ without first finding the law of $g(X)$.
- Decide whether $E(X)$ exists as a finite real number by testing $E|X|<\infty$.
- Convert $P(A)$ into $E[I_A]$ for an event $A$.
- Obtain $E(Y)=E[E(Y\mid X)]$ by conditioning.
- Obtain $E(XY)=E(X)E(Y)$ for independent integrable random variables.
- Identify the $L^2$-optimal predictor of $Y$ given $X$ as $E(Y\mid X)$.

## Textbooks

- Sheldon Ross, A First Course in Probability, Chapter 4, Random Variables.
- Geoffrey Grimmett and David Stirzaker, Probability and Random Processes, Chapter 3, Discrete Random Variables, and Chapter 4, Continuous Random Variables.
- Dimitri P. Bertsekas and John N. Tsitsiklis, Introduction to Probability, Chapter 2, Discrete Random Variables, and Chapter 3, General Random Variables.
- Robert V. Hogg, Joseph W. McKean, and Allen T. Craig, Introduction to Mathematical Statistics, Chapter 1, Probability and Distributions.
- William Feller, An Introduction to Probability Theory and Its Applications, Volume I, Chapter 9, Random Variables and Expected Values.
-->
