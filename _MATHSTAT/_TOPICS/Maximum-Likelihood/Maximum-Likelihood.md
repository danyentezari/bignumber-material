# Maximum Likelihood

Maximum Likelihood is a technique for estimating, by maximizing likelihood, any parameter of a population given the sample.

$$ L(x_1,\dots,x_n ;\theta)=\prod_{i=1}^{n} f(x_i; \theta) $$ 

where 

- $L(x_1, \dots, x_n; \theta)$ is the likelihood function (see next section)
- $f(x_i; \theta)$ is the probability distribution function (see Probability Distribution Functions).
- $\theta$ is some parameter
- $n$ is the number of variables
- $ x_1, \dots, x_n $ are variables
- $ \prod_{i=1}^{n} $ is the product operator

## Topics

1. [Likelihood Function](likelihood-function.html)
2. [Log-Likelihood](log-likelihood.html)
3. [Differentiating the Log-Likelihood Function](differentiating-the-log-likelihood-function.html)
4. [Maximum Likelihood Estimator (MLE)](maximum-likelihood-estimator-mle.html)

<!--
Likelihood Function. The likelihood function measures how strongly parameter values support the observed data. It treats the observed sample as fixed and the unknown parameter as variable. This principle is used to compare parameter values according to how well they explain the observed sample.

Maximum Likelihood Estimator. The maximum likelihood estimator is the parameter value that maximizes the likelihood function. It selects the parameter under which the observed data are most probable. This principle is used to estimate unknown parameters from observed data.

Log-Likelihood. The log-likelihood is the logarithm of the likelihood function. It converts products into sums while preserving the location of the maximum. This principle is used to simplify differentiation and numerical optimization when calculating maximum likelihood estimates.

Score Equation. The score function is the derivative of the log-likelihood with respect to the parameter. Setting the score equal to zero identifies candidate maximum likelihood estimates. This principle is used to derive estimating equations for unknown model parameters.

Asymptotic Properties of Maximum Likelihood. Under standard conditions, maximum likelihood estimators become consistent, approximately normal, and statistically efficient as sample size increases. This principle is used to justify large-sample confidence intervals, hypothesis tests, and uncertainty estimates.

## Problems

- Obtain the parameter $\theta$ that maximizes $L(\theta;x)$ for an independent sample.
- Obtain the maximum likelihood estimator of $p$ in a Bernoulli model and of $\lambda$ in a Poisson model.
- Obtain the maximum likelihood estimator of $(\mu,\sigma^2)$ from a normal sample.
- Obtain the maximum likelihood estimator when the support of the density depends on $\theta$.
- Identify consistency and asymptotic normality of the maximum likelihood estimator under regularity conditions.

## Textbooks

- George Casella and Roger L. Berger, Statistical Inference, Chapter 7, Point Estimation.
- Robert V. Hogg, Joseph W. McKean, and Allen T. Craig, Introduction to Mathematical Statistics, Chapter 6, Maximum Likelihood Methods.
- Yudi Pawitan, In All Likelihood: Statistical Modelling and Inference Using Likelihood, Chapter 2, Likelihood.
- John A. Rice, Mathematical Statistics and Data Analysis, Chapter 8, Estimation of Parameters and Fitting of Probability Distributions.
- Larry Wasserman, All of Statistics: A Concise Course in Statistical Inference, Chapter 9, Parametric Inference.
-->
