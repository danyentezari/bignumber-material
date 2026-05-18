# Maximum Likelihood

Maximum Likelihood is a technique for estimating, with maximum probability, any parameter of a sample.

$$ L(x_1,\dots,x_n ;\theta)=\prod_{i=1}^{n} f(x_i; \theta) $$  

where  

- $L(x_1, \dots, x_n; \theta)$ is the likelihood function (see next section)
- $f(x_i; \theta)$ is the probability distribution function (see Probability Distribution Functions).
- $\theta$ is some parameter
- $n$ is the number of variables
- $x_1, \dots, x_n$ are variables
- $\prod_{i=1}^{n}$ is the product operator

## Likelihood

Likelihood is a number that is proportional to probability. Likelihood is a number that, at its largest value, represents the parameter(s) of the model that best represents some data. Thus this quantity is used to find the model that best represents some data. Recall that parameters are quantities that describe the shape of data.

## Likelihood Function

The likelihood function is denoted by  
$$ L(x_1, \dots, x_n; \theta) $$  
where  

- $x_1, \dots, x_n$ are variables
- $\theta$ is the parameter to be estimated

Note that the likelihood function can output very small probabilities, which is why it is necessary to apply the logarithm function to the likelihood function (see Log-Likelihood).

## Log-Likelihood

The log-likelihood function is the natural logarithm of the likelihood function. The log-likelihood function is given by

$$ \ln(L(x_1, \dots, x_n; \theta)) = \ell(x_1, \dots, x_n; \theta) = \log_{e} ( L(x_1, \dots, x_n; \theta) ) $$

Note that $\ln(L(x, \theta))$ is the natural logarithm; that is, the logarithm of base $e$. Thus, $\ln(L(x_1, \dots, x_n, \theta)) = \log_{e} ( L(x_1, \dots, x_n, \theta) )$.

Also note that capital $L$ is used for likelihood and lowercase italic $l$ for log-likelihood.

Log-likelihood is used, and preferably so, because it "scales" the products of the terms in the MLE — especially when the probabilities are small (e.g., $p = 10^{-10} = 0.0000000001$).

## Differentiating the Log-Likelihood Function

Differentiating the log-likelihood function, $\ell(x_1, \dots, x_n, \theta)$, is done to find the critical values of the function. The critical value would then be the value at which the likelihood functions yield the maximum likelihood.

Since the (log) likelihood is a function of multiple variables, we apply the partial derivative to the likelihood function,

$$ \frac{\partial}{\partial x_i} \ell(x_i; \theta) = \frac{\partial}{\partial x_i} \ln( L(x_i; \theta) ) $$

## Maximum Likelihood Estimator (MLE)

An estimator is a function used to estimate a parameter.

$$ \hat{\theta}(x_i) = \underset{\theta}{\text{argmax}} \: \ell(x_i; \theta) $$

where

- $\text{argmax}$ is the function that chooses the argument for which the values of some function is maximized
- $\hat{\theta}(x_i)$ is the maximum likelihood estimator
- $\theta$ is some parameter
- $\ell(x_i; \theta)$ is the log-likelihood function
- $x_i$ is some variable

## References:

1. https://github.com/danyentezari/sprp-mathematical-statistics/blob/master/mathstat.pdf