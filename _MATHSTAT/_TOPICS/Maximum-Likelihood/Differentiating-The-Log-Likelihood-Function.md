# Differentiating the Log-Likelihood Function

Differentiating the log-likelihood function, $\ell(x_1, \dots, x_n,\theta)$, is done to find the critical values of the function. The critical value would then be the value at which the likelihood functions yield the maximum likelihood.

Since the (log) likelihood is a function of multiple variables, we apply the partial derivative to the likelihood function,

$$ \frac{\partial}{\partial x_i} \ell(x_i; \theta) = \frac{\partial}{\partial x} \ln( L(x_i; \theta) ) $$
