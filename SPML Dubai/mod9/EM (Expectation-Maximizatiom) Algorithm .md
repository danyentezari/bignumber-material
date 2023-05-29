EM (Expectation-Maximizatiom) Algorithm for GMM


E-Step (Expectation)
    1. Initialization
        - mean averages
        - variance
        - covariance matrix
    2. Calculate Reponsibilities (or Posterior Probability)
        - find p(x_i | y_i)
    3. Update Reponsibilities
        - update p(x_i | y_i) based on GMM
        - normalization of responsibilities


M-Step (Maximization)
    1. Update mixture proportions
    2. Update mean average (i.e, center of component or center of class)
    3. Update covariance matrices
    4. Repeat until convergence (stabilization)

Repeat E-Step and M-Step