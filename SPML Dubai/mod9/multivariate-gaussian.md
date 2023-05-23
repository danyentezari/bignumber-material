## Gaussian

$$p(y | \mu, \sigma^2) = \dfrac{1}{\sigma \sqrt{2 \pi}} \exp \Big[ \dfrac{1}{2 \sigma^2} (y-\mu)^2 \Big ]$$

or

$$p(y | \mu, \sigma^2) \sim N(\mu, \sigma^2) $$

<br/>

Note:
- $p(y | \mu, \sigma^2)$ is maximized when $y = \mu$.

<br/>

### Multivariate Gaussian


$$ p(\mathbf{x}) = \dfrac{1}{ (2\pi)^{D/2} \: |\mathbf{\Sigma}|^{1/2} } \exp \Big[ -\dfrac{1}{2} (x-\mathbf{\mu})^{T} \: \Sigma^{-1}  (x-\mathbf{\mu}) \Big]$$

or

$$ p(\mathbf{x}) = \displaystyle \prod_{d=1}^{D} \dfrac{1}{(2\pi)^{1/2}} \exp \Big[ -\dfrac{1}{2} (x_{d}-\mu_{d})^2 \Big ]$$


Where
- $\mathbf{x}$ is the vector of features $[ x_1, ..., x_D ]$
- $D$ is the size of $\mathbf{x}$
- $|\mathbf{\mu}| = |\mathbf{x}|$

