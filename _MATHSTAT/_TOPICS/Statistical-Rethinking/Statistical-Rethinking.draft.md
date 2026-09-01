# Statistical Rethinking

A Bayesian modeling program that is used to design, fit, and critically revise generative statistical models instead of choosing pre-made hypothesis tests, where a generative model is a probability model that can both simulate data and estimate unknowns, and where Bayesian inference updates relative plausibility of parameter values after observing data.

Note: Also called golem engineering in McElreath’s metaphor.

Statistical golems. Scientific models are engineered constructs for a purpose. They encode association rather than cause unless the modeler supplies causal structure. This principle is used to treat fitted procedures as tools that need guidance and skepticism.

Rethinking as strategy. Statistical inference is a set of design strategies for building and refining special-purpose procedures, not a flowchart of black-box tests. This principle is used to justify writing custom models and computing them carefully enough to interpret their output.

Bayesian data analysis as counting. Bayesian analysis counts the relative numbers of ways the data could arise under stated assumptions, using probability as a calculus of plausibility. This principle is used to process data into inference once the model is defined.

Small world and large world. The small world is the self-contained logic of the model. The large world is the empirical context in which the model is deployed. Logical optimality inside the small world does not guarantee optimality in the large world. This principle is used to keep model criticism separate from formal updating.

Data story. Before fitting, one narrates how the observations are produced. Resolving ambiguity in that story often revises the model before any fit. This principle is used to connect measurement and sampling design to the likelihood.

Prior. The prior assigns relative plausibility to parameter values before the current data are accounted for. There is no uniquely correct prior, just as there is no uniquely correct likelihood. This principle is used to encode background information and regularize estimation.

Likelihood. The likelihood gives the relative plausibility of an observation for fixed parameter values. It is often the most influential modeling choice. This principle is used to map parameters to predicted data.

Posterior. The target of Bayesian inference is the posterior distribution of parameters after accounting for the data. Bayes’ theorem is the logical rule that combines prior and likelihood. This principle is used to report relative compatibility of parameter values with data and model.

Workflow loop. McElreath’s recurrent loop is data story, update, evaluate. Model fitting can be objective given the model, while model checking is supervised and subjective. This principle is used to organize iterative model revision.

Posterior predictive checking. Supervision means simulating observations from the posterior predictive distribution and comparing them with reality. This principle is used to expose mismatches that force model revision.

MCMC computation. When exact integration is unavailable, Markov chain Monte Carlo draws representative samples from the posterior. In Statistical Rethinking, Hamiltonian Monte Carlo via Stan is the default engine for such models. This principle is used to fit multilevel and high-dimensional models.

Model comparison. Models are compared by expected out-of-sample predictive accuracy rather than by searching for significant $p$-values. This principle is used to choose among several substantive models of a phenomenon.

<!--
## Elementary Example

### Simple

Globe tossing. A globe is tossed and caught, recording Water or Land under the right index finger. One sequence is W, L, W, W, W, L, W, L, W, so $W=6$ and $L=3$.

### General

Assume independent tosses with constant water probability $p$. With a uniform prior $p\sim\mathrm{Uniform}(0,1)$ and binomial likelihood

$$
\Pr(W,L\mid p)
=
\frac{(W+L)!}{W!\,L!}
p^{W}(1-p)^{L},
$$

each new toss updates the posterior, concentrating mass near $p\approx 0.67$. Posterior predictive simulation can match the water count while understating switches, exposing a possible failure of independence.

where

- $p$ is the proportion of the globe’s surface that is water.
- $W$ is the number of water outcomes.
- $L$ is the number of land outcomes.
-->

# References

1. McElreath, R. *Statistical Rethinking: A Bayesian Course with Examples in R and Stan*. 2nd ed. CRC Press, 2020. Chapter 1, §1.1, pp. 1–3 — golems and rethinking as engineering strategies; §1.2, p. 4 — understanding model computation; §1.3, pp. 10–11 — Bayesian analysis as counting ways and information; §1.4, p. 17 — building multiple non-null models.
2. McElreath, R. *Statistical Rethinking*. Chapter 2, §2.1, p. 20 — small world and large world; §2.2, pp. 29–31 — data story, update, evaluate; globe-tossing sequence and first update; §2.3, p. 33 — primacy of the likelihood; §2.5, p. 46 — prior, likelihood, posterior, and Bayes’ theorem.
3. McElreath, R. *Statistical Rethinking*. Chapter 3, §3.3, p. 69 — supervised model checking; Chapter 4, §4.3, p. 84 — posterior plausibility; §4.4, p. 98 — priors as tools.
4. McElreath, R. *Statistical Rethinking*. Chapter 9, §9.6, p. 296 — MCMC and `ulam` with Stan HMC; Chapter 11, §11.2, p. 343 — out-of-sample accuracy and model comparison; Chapter 14, §14.6, p. 488 — generative Bayesian models.
