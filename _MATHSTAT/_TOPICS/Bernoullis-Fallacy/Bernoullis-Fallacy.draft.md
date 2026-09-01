# Bernoulli's Fallacy

A critique of orthodox statistics that is used to show why sampling probabilities alone cannot settle questions about hypotheses, where a sampling probability is a probability of data given a fixed hypothesis, and where an inferential probability is a probability of a hypothesis given data.

Note: Named for Jacob Bernoulli’s inversion of the weak law of large numbers.

Bernoulli’s fallacy. The mistaken idea that sampling probabilities are sufficient to determine inferential probabilities. This principle is used to name the confusion of $P(\mathrm{data}\mid\mathrm{hypothesis})$ with $P(\mathrm{hypothesis}\mid\mathrm{data})$.

Wrong arrow of probability. Bernoulli answered a question about the probability of a hypothesis by reasoning only about the probability of an observation. Closeness of a sample ratio to an urn ratio is not the same as closeness of the urn ratio to the sample ratio. This principle is used to separate deduction about samples from induction about unknowns.

Frequentist restriction. Requiring every probability statement to refer only to frequencies in hypothetical long runs blocks the scientific question of how likely a theory is given what was observed. This principle is used to explain why the route from data to inference in orthodox practice is indirect.

Symmetric closeness illusion. Bernoulli treated “$X$ is close to $Y$” as interchangeable with “$Y$ is close to $X$” in his guarantee from the law of large numbers. Without a clear notion of conditional probability, that symmetry confuses sampling statements with inferential ones. This principle is used to locate the mathematical origin of the fallacy.

Missing ingredients. Inferential probabilities require competing hypotheses with their own sampling probabilities and prior probabilities on those hypotheses. Likelihoods alone do not determine posteriors. This principle is used to state what Bayesian analysis adds beyond sampling theory.

Reference class problem. A frequency is defined only relative to a class of repeated trials, and every event belongs to many such classes. Frequentism claims objectivity while leaving that class choice unresolved. This principle is used to challenge the claim that frequency definitions remove subjectivity.

Mind projection fallacy. Following Jaynes, probability represents incomplete information of the speaker, not a physical property of the world. Treating probability as an empirical frequency of nature confuses a mental state with external fact. This principle is used to defend an informational reading of probability.

Eclipse of inverse probability. Inverse probability under Bayes and Laplace was later displaced by Fisher, Pearson, and Neyman. This principle is used to place modern orthodoxy in historical opposition to earlier Bayesian practice.

$p$-value logic. Observing data that are unlikely under a null hypothesis is not logically the same as computing the probability that the null is true given the data. Null hypothesis significance testing answers the sampling question while advertising the inferential one. This principle is used to diagnose invalid probabilistic proof by contradiction.

Replication crisis. Filtering claims by significance based only on how likely the hypothesis makes the data allows false positives, including implausible theories, into the literature. This principle is used to tie Bernoulli’s fallacy to failures of scientific replication.

<!--
## Elementary Example

### Simple

Candy factory. The green-candy fraction $F$ is either $\frac23$ in normal operation or $\frac13$ after a rare dye mix-up. A scoop of $n=30$ candies yields $g=8$ greens.

### General

A sampling argument that treats closeness as symmetric can assign high “moral certainty” to an interval around $8/30$ that excludes $F=\frac23$. A Bayesian calculation with prior $P(F=\frac13)=0.0001$ still leaves substantial posterior mass on normal operation, because the mix-up was nearly impossible a priori. Sampling probabilities alone do not determine inferential certainty.

where

- $F$ is the unknown green fraction in the bin.
- $n$ is the sample size.
- $g$ is the number of green candies in the sample.
-->

# References

1. Clayton, A. *Bernoulli’s Fallacy: Statistical Illogic and the Crisis of Modern Science*. Columbia University Press, 2021. Introduction, pp. 8–9, 13 — wrong direction of Bernoulli’s answer; definition of Bernoulli’s fallacy; frequentism’s avoidance of “How likely is my theory?”
2. Clayton, A. *Bernoulli’s Fallacy*. Chapter 1, pp. 34–35, 50 — reference class problem; Jaynes and the mind projection fallacy.
3. Clayton, A. *Bernoulli’s Fallacy*. Chapter 2, pp. 75, 77, 79–84 — symmetric closeness in the weak law; candy-factory mishap; priors and competing hypotheses as missing ingredients; p. 83 — sampling probabilities are not sufficient for inferential probabilities.
4. Clayton, A. *Bernoulli’s Fallacy*. Chapter 4, p. 165 — Fisher’s rejection of inverse probability and Bayes’ theorem.
5. Clayton, A. *Bernoulli’s Fallacy*. Chapter 5, p. 196 — critique of orthodox statistics as a loose amalgam of half-baked ideas.
6. Clayton, A. *Bernoulli’s Fallacy*. Chapter 6, pp. 242, 268–269 — Cohen on what $p$-values do not answer; significance testing and the replication crisis.
