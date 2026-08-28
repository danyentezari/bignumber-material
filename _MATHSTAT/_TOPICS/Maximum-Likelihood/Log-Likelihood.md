# Log-Likelihood

The log-likelihood function is the natural logarithm of the likelihood function. log-likelihood function is given by

$$ \ln(L(x_1, \dots, x_n; \theta)) = \ell(x_1, \dots, x_n; \theta) = \log_{e} ( L(x_1, \dots, x_n; \theta) ) $$ 

Note that $ \ln(L(x, \theta)) $ is the natural logarithm; that is, the logarithm of base e. Thus, $ \ln(L(x_1, \dots, x_n, \theta)) = \log_{e} ( L(x_1, \dots, x_n, \theta) ) $.

Also note that capital $L$ is used for likelihood and lowercase italic $l$ for log-likelihood.

Log-likelihood is used, and preferably so, because it "scales" the products of the terms in the MLE — especially when the probabilities are small (e.g, p = $10^{-10} = 0.0000000001 $).
