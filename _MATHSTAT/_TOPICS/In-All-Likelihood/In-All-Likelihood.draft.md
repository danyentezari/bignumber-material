# In All Likelihood

A likelihood-centered program of statistical modelling and inference that is used to treat the likelihood function as the primary carrier of evidence about unknown parameters, where the likelihood function is the probability of the observed data viewed as a function of the parameter, and where evidence is relative preference among parameter values given a model.

Note: Also called likelihood-based inference in Pawitan’s sense.

Likelihood as rational belief. Given a model, $L(\theta)$ is an exact objective quantity that ranks parameter values by relative preference. It is not a probability distribution over $\theta$. This principle is used to separate likelihood from Bayesian probability as measures of uncertainty.

Definition of likelihood. For a model parameterized by fixed unknown $\theta$, the likelihood $L(\theta)$ is the probability of the observed data $x$ considered as a function of $\theta$. This principle is used to turn a sampling model into an evidence function after data arrive.

Meaningful up to a constant. Within a model $p_\theta(x)$, only likelihood ratios matter. Factors that do not involve $\theta$ may be dropped, and proportional likelihoods convey the same evidence about $\theta$. This principle is used to simplify likelihood construction.

Maximum likelihood estimator. The MLE $\hat\theta$ is a maximizer of $L(\theta)$, but the full likelihood function—not only its maximizer—captures the information in the data about $\theta$. This principle is used to estimate parameters while retaining the shape of the evidence.

Score function. The score is the derivative of the log-likelihood, $S(\theta)=\partial\log L(\theta)/\partial\theta$, and $\hat\theta$ solves $S(\theta)=0$. Under regularity, $E_\theta[S(\theta)]=0$. This principle is used to locate the MLE and to drive asymptotic theory.

The score equation is

$$
S(\theta)
=
\frac{\partial}{\partial\theta}\log L(\theta)
=
0
$$

where

- $S(\theta)$ is the score function.
- $L(\theta)$ is the likelihood.
- $\theta$ is the unknown parameter.

Observed Fisher information. At the MLE, curvature of the log-likelihood is measured by $I(\hat\theta)=-\partial^2\log L(\theta)/\partial\theta^2$ evaluated at $\hat\theta$. Large curvature means a tight peak and less uncertainty about $\theta$. This principle is used to report precision via standard errors $1/\sqrt{I(\hat\theta)}$.

The observed Fisher information is

$$
I(\theta)
=
-\frac{\partial^2}{\partial\theta^2}\log L(\theta)
$$

where

- $I(\theta)$ is the observed information.
- $\log L(\theta)$ is the log-likelihood.

Expected Fisher information. The expected information equals the variance of the score, $I(\theta)=E_\theta[I(\theta)]=\mathrm{Var}_\theta(S(\theta))$. This principle is used in asymptotic normality and efficiency arguments.

Minimal sufficiency of the likelihood. If $T$ is sufficient for $\theta$, the likelihood based on $x$ equals that based on $T$. The likelihood function is therefore minimally sufficient. This principle is used to justify reducing data to the likelihood without loss of information about $\theta$.

Weak likelihood principle. Observations from a given model with the same likelihood should lead to the same conclusion. This principle is used to equate evidential conclusions for data sharing a likelihood.

Strong likelihood principle. If two experiments yield proportional likelihoods for $\theta$, they yield the same evidence about $\theta$. Sampling scheme and stopping rules that do not enter the likelihood are irrelevant to that evidence. This principle is used to focus inference on the observed likelihood alone.

Likelihood ratio and Wilks calibration. Relative support for a hypothesized $\theta_0$ versus $\hat\theta$ is measured by $L(\theta_0)/L(\hat\theta)$. In regular one-parameter problems, Wilks’ statistic $-2\log(L(\theta_0)/L(\hat\theta))$ is approximately $\chi^2_1$ under the null. This principle is used to attach approximate $P$-values and intervals to likelihood comparisons.

Profile likelihood. For $\theta=(\psi,\lambda)$ with interest parameter $\psi$ and nuisance $\lambda$, the profile likelihood is $L_p(\psi)=\max_\lambda L(\psi,\lambda)$. It is then treated like an ordinary likelihood for $\psi$. This principle is used to eliminate nuisance parameters without abandoning the likelihood viewpoint.

The profile likelihood is

$$
L_p(\psi)
=
\max_\lambda L(\psi,\lambda)
$$

where

- $\psi$ is the parameter of interest.
- $\lambda$ is the nuisance parameter.
- $L_p(\psi)$ is the profile likelihood of $\psi$.

Extended and predictive likelihood. For observed $x$ and unobserved $y$ with joint model $p_\theta(x,y)$, the extended likelihood is $L(\theta,y)=p_\theta(x,y)$. Maximizing over $\theta$ yields a predictive likelihood for $y$. This principle is used to make predictive statements within a likelihood framework.

<!--
## Elementary Example

### Simple

Binomial experiment. Ten independent trials yield $x=8$ successes. The success probability is $\theta\in(0,1)$.

### General

Dropping the $\theta$-free binomial coefficient, the likelihood is $L(\theta)=\theta^8(1-\theta)^2$. The MLE is $\hat\theta=8/10=0.8$. Relative preference of $\theta=0.8$ against $\theta=0.3$ is about $200$ to $1$. The score $S(\theta)=8/\theta-2/(1-\theta)$ vanishes at $\hat\theta$. Observed information at the MLE is $I(\hat\theta)=62.5$, so $\mathrm{se}(\hat\theta)\approx 0.126$. Normalized-likelihood cutoffs near $15\%$ and $4\%$ give intervals roughly $(0.50,0.96)$ and $(0.41,0.98)$.

The binomial likelihood (up to a constant) is

$$
L(\theta)
=
\theta^{8}(1-\theta)^{2}
$$

where

- $\theta$ is the success probability.
- $n=10$ is the number of trials.
- $x=8$ is the number of successes.
-->

# References

1. Pawitan, Y. *In All Likelihood: Statistical Modelling and Inference Using Likelihood*. Oxford University Press, 2013. Chapter 1, §1.5, p. 17 — likelihood versus probability as measures of uncertainty; Chapter 2, §2.1, Definition 2.1, p. 23 — definition of likelihood; §2.1, pp. 22–24 — likelihood as rational belief and meaning up to a multiplicative constant; §2.1, p. 24 — binomial $n=10$, $x=8$ relative preference example; §2.5, pp. 30–32 — MLE, score, observed Fisher information (Example 2.10); §2.6, p. 37 — Wilks calibration of likelihood ratios; Figure 2.6, p. 36 — likelihood intervals; Chapter 3, §3.2, Theorem 3.2, pp. 54–57 — minimal sufficiency of the likelihood; §3.4, p. 61 — profile likelihood; Chapter 7, §7.2, pp. 194–198 — weak and strong likelihood principles; Chapter 8, §8.1–§8.2, pp. 215–219 — score expectation and expected Fisher information; Chapter 9, §9.2, p. 257 — multiparameter Wilks theorem; Chapter 16, §16.3, Definition 16.1, pp. 430–431 — extended and predictive likelihood.
