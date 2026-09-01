# Statistical Learning

A set of tools that is used to understand data by estimating a function that relates inputs to an output, where a supervised method builds that function from labeled examples, and where an unsupervised method finds structure without an output variable.

Note: Also called supervised learning when the task is to predict an output from inputs.

Statistical learning. Statistical learning refers to approaches for estimating an unknown function $f$ that links predictors $X$ to a response $Y$ in the model $Y=f(X)+\epsilon$. This principle is used to organize prediction and inference under a common function-approximation view.

Supervised learning. Supervised learning builds a model that predicts or estimates an output from one or more inputs, using training examples for which the correct outputs are supplied. This principle is used to learn from labeled data across scientific and applied domains.

Prediction. When the goal is accurate forecasts of $Y$, the fitted $\hat f$ may be treated as a black box so long as predictions are accurate. This principle is used when decision making depends on $\hat Y$ rather than on the form of $\hat f$.

Inference. When the goal is to understand how $X$ relates to $Y$, the form of $\hat f$ must be interpretable. This principle is used when scientific interest lies in associations and effects of individual predictors.

Reducible and irreducible error. Prediction error splits into error from imperfect estimation of $f$ and error from the unobservable noise $\epsilon$. Even a perfect $\hat f$ cannot remove $\mathrm{Var}(\epsilon)$. This principle is used to set a bound on attainable prediction accuracy.

$$
E(Y-\hat Y)^2
=
\left[f(X)-\hat f(X)\right]^2
+
\mathrm{Var}(\epsilon)
$$

where

- $Y$ is the response.
- $\hat Y$ is the predicted response.
- $f$ is the true regression function.
- $\hat f$ is the estimated function.
- $\epsilon$ is the irreducible error term.

Regression and classification. Quantitative responses define regression problems. Qualitative responses with finitely many classes define classification problems. This principle is used to match methods to the type of $Y$.

Training error and test error. Training mean squared error measures fit on the data used to estimate the model. Interest centers on test error on previously unseen observations. This principle is used to evaluate generalization rather than in-sample fit.

Overfitting. As flexibility rises, training error falls, but test error may rise when the procedure captures chance patterns in the training sample. A method with small training error and large test error overfits. This principle is used to diagnose excess complexity.

Bias–variance trade-off. Expected test MSE at a point decomposes into variance of $\hat f$, squared bias of $\hat f$, and $\mathrm{Var}(\epsilon)$. More flexible methods tend to lower bias and raise variance. This principle is used to choose a flexibility level with low total expected error.

$$
E\!\left(y_0-\hat f(x_0)\right)^2
=
\mathrm{Var}\!\left(\hat f(x_0)\right)
+
\left[\mathrm{Bias}\!\left(\hat f(x_0)\right)\right]^2
+
\mathrm{Var}(\epsilon)
$$

where

- $x_0$ is a fixed test input.
- $y_0$ is the associated test response.
- $\hat f(x_0)$ is the prediction at $x_0$.

Flexibility and interpretability. As a method becomes more flexible, it typically becomes harder to interpret. Restrictive models such as linear regression are often preferred when inference is the goal. This principle is used to balance accuracy against clarity of the fitted relationship.

<!--
## Elementary Example

### Simple

Advertising data. Across $200$ markets, predictors are TV, radio, and newspaper advertising budgets, and the response is product sales.

### General

The learning model is $Y=f(X)+\epsilon$. Inference asks which media drive sales and by how much, suggesting an interpretable linear form. Prediction asks for sales given a fixed budget mix. Even with a perfect $f$, irreducible noise from unmeasured factors remains.

$$
\mathrm{sales}
\approx
\beta_0
+
\beta_1\,\mathrm{TV}
+
\beta_2\,\mathrm{radio}
+
\beta_3\,\mathrm{newspaper}
$$

where

- $\mathrm{TV}$, $\mathrm{radio}$, and $\mathrm{newspaper}$ are advertising expenditures.
- $\mathrm{sales}$ is product sales.
- $\beta_j$ are regression coefficients.
-->

# References

1. James, G., Witten, D., Hastie, T., and Tibshirani, R. *An Introduction to Statistical Learning with Applications in R*. Springer. Chapter 1, §1.1, p. 1 — definition of statistical learning and supervised learning; Chapter 2, §2.1, p. 15 — statistical learning as estimating $f$; §2.1.1, pp. 17–19 — prediction versus inference and reducible versus irreducible error; §2.1.3, pp. 24–25 — flexibility versus interpretability; §2.1.5, p. 28 — regression versus classification; §2.2.1, pp. 29–32 — training versus test MSE and overfitting; §2.2.2, pp. 33–36 — bias–variance trade-off; Advertising example, Chapter 2, §2.1, pp. 15–16 and Chapter 3, pp. 59–61.
2. Hastie, T., Tibshirani, R., and Friedman, J. *The Elements of Statistical Learning*. Springer. Chapter 2, §2.1, p. 9 — supervised learning from inputs to outputs; §2.6.3, p. 30 — supervised learning as function approximation; Chapter 7, §7.2, p. 221 — training error falling with complexity; §7.4, p. 228 — optimism of training error; Chapter 14, §14.1, p. 437 — learning with a teacher.
