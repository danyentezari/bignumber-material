# Bayes Theorem and Conditional Probability


Frequentist statistics treats parameters as fixed and probabilities as long-run frequencies of repeated data.

Bayesian statistics treats unknown parameters and hypotheses probabilistically, combining prior information with observed data to produce posterior probabilities.

Fundamentally:

Frequentist: $P(\text{data}\mid\text{hypothesis})$

Bayesian: $P(\text{hypothesis}\mid\text{data})$

<i>

**definition [d]** (*Bayes Theorem*) 

The *bayesian theorem* is given by
$$ P(A_i | B)  = \frac{P(A_i) \times P(B|A_i)}{ \sum_{i=k}^{n} P(B|A_i) } $$
where 

- $A_i$ is a given a-priori event
- $B$ is the a-posteriori event

</i>