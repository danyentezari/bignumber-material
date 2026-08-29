# (Fischer) F-Distribution

The PDF of the F-distribution is given by

$$ f(x) = \begin{cases} \frac{\Gamma (\frac{v_1 + v_2}{2}) }{ \Gamma (\frac{v_1}{2}) \:  \Gamma (\frac{v_2}{2})  } v_1^{v_1/2} \: v_2^{ v_2/2} \: x^{ (v / 2)-1 } \: (v_2 + v_1 x)^{-(v_1 + v_2)/2} \enspace ; \quad x > 0 \\ 0 \enspace ; \quad x \leq 0 \end{cases} $$

where

- $v_1, v_2$ are degrees of freedom
- $\Gamma(x)$ is the Gamma function (see Special Functions)

The F-distribution is the ratio of two random variables with chi-squared distribution. The F-distribution is used in ANOVA for two random variables and their mean square ratio.
