# Log-Likelihood

The log-likelihood function is the natural logarithm of the likelihood function. log-likelihood function is given by

$$ \ln(L(x_1, \dots, x_n; \theta)) = \ell(x_1, \dots, x_n; \theta) = \log_{e} ( L(x_1, \dots, x_n; \theta) ) $$ 

Note that $ \ln(L(x, \theta)) $ is the natural logarithm; that is, the logarithm of base e. Thus, $ \ln(L(x_1, \dots, x_n, \theta)) = \log_{e} ( L(x_1, \dots, x_n, \theta) ) $.

Also note that capital $L$ is used for likelihood and lowercase italic $l$ for log-likelihood.

Log-likelihood is used, and preferably so, because it "scales" the products of the terms in the MLE — especially when the probabilities are small (e.g, p = $10^{-10} = 0.0000000001 $).

<!--
Log transformation. The log-likelihood is the natural logarithm of the likelihood function and converts products of likelihood contributions into sums. This principle is used to simplify differentiation, optimization, and numerical computation in maximum likelihood estimation.

Likelihood equivalence. The logarithm is strictly increasing, so the likelihood and log-likelihood attain their maxima at the same parameter values. This principle is used to replace likelihood maximization with mathematically simpler log-likelihood maximization.

Additivity under independence. For independent observations, the joint likelihood is a product, so the log-likelihood is a sum of individual log-likelihood contributions. This principle is used to simplify estimation for independent samples and identify each observation's contribution to the objective function.

Score equation. Differentiating the log-likelihood with respect to the parameter produces the score function, and an interior maximum satisfies a zero score. This principle is used to derive candidate maximum likelihood estimators by solving equations involving first derivatives.

Log-likelihood curvature. The second derivative of the log-likelihood describes its local curvature around a parameter value. Negative curvature at a stationary point identifies a local maximum under standard conditions. This principle is used to verify maxima and quantify the local precision of maximum likelihood estimates.

## Problems

- Replace $\prod_i f(x_i;\theta)$ by $\sum_i \log f(x_i;\theta)$ without moving the maximizer.
- Obtain the score equation $\partial\ell/\partial\theta=0$ for a parametric model.
- Obtain observed information as $-\partial^2\ell/\partial\theta^2$ evaluated at the maximizer.
- Compare nested parametric models by twice the difference of maximized log-likelihoods.
- Verify that a critical point of $\ell$ is a maximum from the sign of $\ell''$.

## Textbooks

- George Casella and Roger L. Berger, Statistical Inference, Chapter 7, Point Estimation.
- Robert V. Hogg, Joseph W. McKean, and Allen T. Craig, Introduction to Mathematical Statistics, Chapter 6, Maximum Likelihood Methods.
- Yudi Pawitan, In All Likelihood: Statistical Modelling and Inference Using Likelihood, Chapter 2, Likelihood.
- John A. Rice, Mathematical Statistics and Data Analysis, Chapter 8, Estimation of Parameters and Fitting of Probability Distributions.
- Larry Wasserman, All of Statistics: A Concise Course in Statistical Inference, Chapter 9, Parametric Inference.
-->
