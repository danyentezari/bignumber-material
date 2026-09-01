# Likelihood Function

The likelihood function is denoted by
$$ L(x_1, \dots, x_n; \theta) $$
where 

- $ x_1, \dots, x_n $ are variables
- $\theta$ is the parameter to be estimated

Note that the likelihood function can output very small probabilities, which is why it is necessary to apply the logarithm function to the likelihood function (see Log-Likelihood).

<!--
Likelihood Function. The likelihood function treats the observed data as fixed and the unknown parameter as variable. It measures how strongly each parameter value supports the observed sample. This principle is used to compare candidate parameter values from the same statistical model.

Joint Likelihood. For independent observations, the likelihood is the product of the individual probability functions evaluated at the observed values. This principle is used to construct the likelihood of an entire sample from a parametric model.

Likelihood Proportionality. Factors that do not depend on the unknown parameter can be removed when maximizing the likelihood. They do not affect which parameter value gives the maximum. This principle is used to simplify likelihood expressions before optimization.

Relative Likelihood. Likelihood values are meaningful through comparison across parameter values for the same observed data. A larger likelihood indicates stronger support from the data. This principle is used to rank parameter values and form likelihood ratios.

Log-Likelihood Transformation. Taking the logarithm of the likelihood converts products into sums while preserving the maximizing parameter value. This principle is used to simplify algebra, differentiation, and numerical computation.

Parameter-Dependent Support. When the possible data values depend on the parameter, the likelihood must include the corresponding restrictions. This principle is used to correctly estimate parameters in models such as uniform and Pareto distributions.

## Problems

- Compare $L(\theta_1;x)$ and $L(\theta_2;x)$ for a fixed observed sample $x$.
- Form the likelihood ratio $L(\theta_0;x)/L(\theta_1;x)$ for two parameter values.
- Drop multiplicative factors of $L(\theta;x)$ that do not depend on $\theta$.
- Write the joint likelihood of an independent sample as a product of marginal likelihood contributions.
- Identify the likelihood when the support of the model depends on the unknown parameter.

## Textbooks

- George Casella and Roger L. Berger, Statistical Inference, Chapter 7, Point Estimation.
- Robert V. Hogg, Joseph W. McKean, and Allen T. Craig, Introduction to Mathematical Statistics, Chapter 6, Maximum Likelihood Methods.
- Yudi Pawitan, In All Likelihood: Statistical Modelling and Inference Using Likelihood, Chapter 2, Likelihood.
- John A. Rice, Mathematical Statistics and Data Analysis, Chapter 8, Estimation of Parameters and Fitting of Probability Distributions.
- Larry Wasserman, All of Statistics: A Concise Course in Statistical Inference, Chapter 9, Parametric Inference.
-->
