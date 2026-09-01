# Bayesian versus Frequentist

A pair of statistical inference frameworks that is used to assign meaning to probability statements about unknown parameters, where a statistical inference framework is a system of rules for learning from data, and where a parameter is an unknown quantity that indexes a family of probability models.

Note: Also called classical versus Bayesian inference.

Interpretation of probability. Frequentist probability is the limiting relative frequency of an event in repeated identical trials. Bayesian probability is a numerical degree of belief about a proposition given available information. This principle is used to distinguish sampling uncertainty from updated personal uncertainty.

Casella and Berger contrast a classical 90 percent coverage assertion, which refers to a long sequence of identical trials, with a Bayesian 90 percent coverage assertion, which refers to the experimenter’s certainty after combining prior knowledge with data.

Treatment of parameters. Frequentist inference treats an unknown parameter as a fixed constant. Bayesian inference models uncertainty about that parameter by treating it as a random variable with a probability distribution. This principle is used to decide whether probability statements may be assigned directly to an unknown parameter.

Ghoshal and van der Vaart write that, for a frequentist, randomness in a scaled estimation error comes through the observation drawn from a distribution indexed by a fixed $\theta$. In the Bayesian setup $\theta$ is the variable and randomness is evaluated according to the posterior given a fixed observation.

Prior probability. Bayesian inference specifies a prior distribution for the parameter before the data are seen. Frequentist inference does not assign a probability distribution to a nonrandom parameter. This principle is used to identify the extra probability model required for Bayesian updating.

Casella and Berger call the prior a subjective distribution, based on the experimenter’s belief and formulated before the data are seen. Pawitan states that frequentists cannot accept that a parameter can have a distribution, since such a distribution does not have an external reality.

Likelihood. The likelihood function is the sampling density of the observed data viewed as a function of the parameter. It ranks parameter values by the data alone and is not a probability distribution on the parameter space. This principle is used to measure evidence from a fixed sample without treating the parameter as random.

The likelihood of parameter $\theta$ given data $x$ is

$$
L(\theta\mid x)=f(x\mid\theta).
$$

where

- $\theta$ is the unknown parameter.
- $x$ is the observed data.
- $f(x\mid\theta)$ is the sampling density of $x$ given $\theta$.
- $L(\theta\mid x)$ is the likelihood function.

Posterior. The posterior distribution is the conditional distribution of the parameter given the observed data, obtained from the prior and the likelihood by Bayes theorem. This principle is used to base all Bayesian claims about the parameter on one updated probability distribution.

The posterior density is

$$
\pi(\theta\mid x)
=
\frac{f(x\mid\theta)\,\pi(\theta)}{m(x)},
\qquad
m(x)
=
\int_{\Theta} f(x\mid\theta)\,\pi(\theta)\,d\theta.
$$

where

- $\pi(\theta)$ is the prior density of $\theta$.
- $m(x)$ is the marginal density of the data.
- $\pi(\theta\mid x)$ is the posterior density of $\theta$ given $x$.
- $\Theta$ is the parameter space.

Conditioning direction. Frequentist procedures evaluate probabilities of data given a fixed parameter. Bayesian procedures evaluate probabilities of the parameter given the observed data. This principle is used to separate $P(X\mid\theta)$ from $P(\theta\mid X)$.

Tijms states that the classical approach is based on $P(\text{data}\mid H_0)$, whereas the Bayesian approach makes use of $P(H_0\mid\text{data})$, and that the Bayesian approach uses only the observed value.

Confidence and credible intervals. A confidence set is a random set $C(X)$ whose long-run coverage of a fixed parameter is at least $1-\alpha$. A credible set is a fixed subset of the parameter space that carries posterior probability $1-\alpha$ given the observed data. This principle is used to distinguish statements about a sampling procedure from probability statements about a parameter given one sample.

The coverage requirement for a confidence set is

$$
P_{\theta}\bigl(\theta\in C(X)\bigr)\ge 1-\alpha
\quad\text{for all }\theta\in\Theta.
$$

The posterior probability of a credible set $C$ is

$$
P(\theta\in C\mid X=x)
=
\int_{C}\pi(\theta\mid x)\,d\theta
=
1-\alpha.
$$

where

- $C(X)$ is a data-dependent random set in the parameter space.
- $\alpha$ is a specified error level.
- $C$ is a subset of $\Theta$ chosen from the posterior.

Casella and Berger note that once a numerical interval is calculated, a classical claim of coverage is $0$ or $1$, whereas a Bayesian model permits a probability that is neither $0$ nor $1$, and therefore call the Bayesian sets credible sets rather than confidence sets.

# References

1. Casella, G. and Berger, R. L. *Statistical Inference*. 2nd ed. Duxbury, 2002. Chapter 7, §7.2.3, pp. 324–325 — prior as a subjective distribution formulated before the data; $\theta$ as a random variable. Chapter 8, §8.3.4, p. 392 — posterior from prior and likelihood by Bayes’ theorem. Chapter 9, §9.2.1, p. 341 and Theorem 9.2.2 — confidence sets; §9.2.4, pp. 353–354 — credible sets versus coverage probability.
2. Ghoshal, S. and van der Vaart, A. W. *Fundamentals of Nonparametric Bayesian Inference*. Cambridge University Press, 2017. Chapter 1, §1.4, p. 11 — frequentist randomness through $X^{(n)}$ at fixed $\theta$; Bayesian randomness through the posterior given a fixed observation.
3. Pawitan, Y. *In All Likelihood: Statistical Modelling and Inference Using Likelihood*. Oxford University Press, 2001. Chapter 1, §1.4, p. 12 — distribution of $\theta$ as a degree of belief; frequentist refusal of a parameter distribution without external reality.
4. Billingsley, P. *Probability and Measure*. 3rd ed. Wiley, 1995. Section 33, Problem 33.14, p. 444 — prior density, conditional density of the observation, and posterior density.
5. Blitzstein, J. K. *Introduction to Probability*. 2nd ed. CRC Press, 2019. Chapter 10, p. 448 — $L(X)$ and $U(X)$ random, $\theta$ a constant.
6. Tijms, H. *Understanding Probability*. 3rd ed. Cambridge University Press, 2012. Chapter 5, §5.12, pp. 205–206 — $P(\text{data}\mid H_0)$ versus $P(H_0\mid\text{data})$.
7. Schweder, T. and Hjort, N. L. *Confidence, Likelihood, Probability: Statistical Inference with Confidence Distributions*. Cambridge University Press, 2016. Chapter 1, §1.1, p. 2 — frequentist probability as long-run frequency in a chance setup.
8. Hastie, T., Tibshirani, R., and Friedman, J. *The Elements of Statistical Learning*. 2nd ed. Springer, 2009. Chapter 3, §3.2, p. 48 — approximate 95 percent confidence interval from $\hat\beta\pm 2\cdot\mathrm{se}(\hat\beta)$.

<!--
Interpretation of probability. Frequentist probability describes limiting frequencies under repeated sampling, while Bayesian probability represents uncertainty through probability distributions conditional on available information. This principle is used to distinguish the meanings assigned to probability statements in statistical inference.

Treatment of parameters. Frequentist inference treats an unknown parameter as fixed, while Bayesian inference represents uncertainty about it with a probability distribution. This principle is used to determine whether probability statements can be assigned directly to unknown parameters.

Likelihood and posterior. A likelihood measures relative support for parameter values from fixed observed data, while a posterior is a probability distribution over parameters conditional on the data. This principle is used to distinguish likelihood-based evidence from Bayesian probability statements about parameters.

Prior probability. Bayesian inference specifies a prior distribution for an unknown parameter before conditioning on observed data. Frequentist inference does not assign a probability distribution to a fixed parameter. This principle is used to identify the additional probability model required for Bayesian inference.

Conditioning direction. Sampling distributions describe probabilities of data conditional on parameters, while Bayesian posterior distributions describe probabilities of parameters conditional on data. This principle is used to distinguish $P(X\mid\theta)$ from $P(\theta\mid X)$.

Confidence and credible intervals. A confidence procedure has specified long-run coverage under repeated sampling, while a Bayesian credible interval contains specified posterior probability conditional on observed data. This principle is used to distinguish statements about procedures from probability statements about parameters.

## Problems

- Distinguish $P(X\mid\theta)$ from $P(\theta\mid X)$ when $\theta$ is unknown.
- Obtain a posterior density from $p(\theta\mid x)\propto p(x\mid\theta)\pi(\theta)$.
- Identify which probability statements about a fixed unknown parameter are permitted under frequentist inference.
- Establish the long-run coverage statement $P_\theta\{\theta\in C(X)\}=1-\alpha$ for a confidence procedure.
- Establish the posterior probability statement $P\{\theta\in C\mid X=x\}=1-\alpha$ for a Bayesian credible set.
- Distinguish likelihood ratios $L(\theta_1;x)/L(\theta_2;x)$ from posterior odds between $\theta_1$ and $\theta_2$.
- Obtain posterior odds as prior odds multiplied by the likelihood ratio under discrete competing parameter values.

## Textbooks

- George Casella and Roger L. Berger, Statistical Inference, Chapters 7 through 10, Point Estimation, Hypothesis Testing, Interval Estimation, and Bayesian Methods.
- James O. Berger, Statistical Decision Theory and Bayesian Analysis, Chapter 3, Bayesian Analysis.
- Bradley Efron and Trevor Hastie, Computer Age Statistical Inference, Chapters 3 and 4, Frequentist Inference and Bayesian Inference.
- Patrick Billingsley, Probability and Measure, Chapters 1 through 4, Probability Measures and Probability Models.
- William Feller, An Introduction to Probability Theory and Its Applications, Volume I, Chapters 1 and 5, Probability Foundations and Conditional Probability.
-->
