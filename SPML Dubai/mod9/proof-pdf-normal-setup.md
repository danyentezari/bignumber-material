### Binomial to Normal

<img src="https://d1whtlypfis84e.cloudfront.net/guides/wp-content/uploads/2018/09/03051417/11.jpg" />

<br/><br/>

**PDF of the Normal Distribution**

$f(x \mid \mu, \sigma^2) = \dfrac{1}{\sqrt{2\pi\sigma^2}} \exp \Big [ \dfrac{-(x - \mu)^2}{2\sigma^2} \Big ]$

<br/><br/>

**Theorem 1 [2]**

According to de Moivre’s Laplace limit theorem, the binomial distribution function can be approximated by

$\displaystyle{n \choose k} p^x q^{n-x} \approx \dfrac{1}{\sqrt{2 \pi n p q}} \exp \Big[ \dfrac{-(x-np^2)}{2npq}  \Big]$

where 

- $p,q $ are probabilities and $p+q= 1$ and $p,q>0$ <br/>
- $\displaystyle{n \choose k} = \dfrac{n!}{k!(n-k)!}$

<br/><br/>

**Theorem 2 [1]**

$P(\text{between } a \text{ and } b \text{ successes}) = \phi \Big( \dfrac{b-np}{\sqrt{np(1-p)}} \Big) - \phi \Big( \dfrac{a-np}{\sqrt{np(1-p)}} \Big)$

<br/>

where
- $\phi$ is the CDF of the Normal Distribution
- $np$ is the mean <br/><br/>
- $\sqrt{np(1-p)}$ is the standard deviation <br/><br/>
- $\dfrac{np}{\sqrt{np(1-p)}}$ is the standardization formula

<br/><br/>

**Theorem 3 [1]**

$\Phi(x) = \dfrac{1}{\sqrt{2\pi}} \displaystyle\int_{-\infty}^{x} \exp \Big[-\dfrac{t^2}{2} \Big] \: dt$

<br/>

Also, alternatively,

$\Phi(x) = \dfrac{1}{2} \left[ 1 + \text{erf}\left(\frac{x}{\sqrt{2}}\right) \right]$

where

- $\text{erf}(x) = \dfrac{2}{\sqrt{\pi}} \displaystyle \int_{0}^{x} e^{-t^2} \, dt$

<br/>


<br/>

**Derivation of Error Function [3]**


Given

$$\operatorname{erf}(x)=\dfrac{2}{\sqrt{\pi}} \displaystyle \int_0^x e^{-x^2} d x$$

<br/>

Let 

$$ I = \displaystyle \int_0^{\infty} e^{-x^2} \: dx $$

<br/>$

Then,
$$
\begin{aligned}
I^2 & =\int_0^{\infty} e^{-x^2} d x \int_0^{\infty} e^{-y^2} d y \\\\
& =\int_0^{\infty} \int_0^{\infty} e^{-\left(x^2+y^2\right)} d x d y \\\\
& =\int_0^{\frac{\pi}{2}} \int_0^{\infty} e^{-r^2} r d r \: d\theta
\end{aligned}
$$

<br/>

Now, as the inner integral doesn't depend on $\theta$, let $r^2=s$ (and so, $rdr=\dfrac{d s}{2}$) to get

$$
\begin{aligned}
I^2 & =\frac{\pi}{2} \int_0^{\infty} e^{-s} \frac{d s}{2} \\
& =\frac{\pi}{4}\left[-e^{-s}\right]_0^{\infty} \\
&= \frac{\pi}{4} (-e^{-\infty}) - (-e^{-0}) \\
& =\frac{\pi}{4}
\end{aligned}
$$

Therefore, we have that
$$
I=\sqrt{\frac{\pi}{4}}=\frac{\sqrt{\pi}}{2}
$$

<br/>

And 

$ \dfrac{2}{\sqrt{\pi}} \displaystyle \int_0^x e^{-x^2} d x $ <br/>

$ \dfrac{2}{\sqrt{\pi}} I $

$ \dfrac{2}{\sqrt{\pi}} \dfrac{\sqrt{\pi}}{2} = 1 $

<br/><br/>


**Changing Variables in Double Integral**

Given

$ x = r \cos(\theta) $ 
$ y = r \sin(\theta) $

<br/>

The double integral change of variables formula is 

$ \displaystyle\int_R f(x, y) \, dx \, dy = \displaystyle\int_D f(r \cos(\theta), r \sin(\theta)) \cdot r \, dr \, d\theta $

<br/>

Let \(f(x, y) = 1\). Then,

$ dy \, dx = \displaystyle\int_R 1 \, dx \, dy = \displaystyle\int_D 1 \cdot r \, dr \, d\theta $

<br/>

Now, we need to find the Jacobian determinant \(\left|\dfrac{\partial(x, y)}{\partial(r, \theta)}\right|\). The transformation matrix is:

$ J = \begin{bmatrix} \dfrac{\partial x}{\partial r} & \dfrac{\partial x}{\partial \theta} \\ \\  \dfrac{\partial y}{\partial r} & \dfrac{\partial y}{\partial \theta} \end{bmatrix} $

<br/>

Evaluating each partial derivative:

$ \dfrac{\partial x}{\partial r} = \cos(\theta) $

$ \dfrac{\partial x}{\partial \theta} = -r \sin(\theta) $

$ \dfrac{\partial y}{\partial r} = \sin(\theta) $

$ \dfrac{\partial y}{\partial \theta} = r \cos(\theta) $

<br/>

The Jacobian determinant is

$ \left|\dfrac{\partial(x, y)}{\partial(r, \theta)}\right| = \left|(\cos(\theta))(r \cos(\theta)) - (-r \sin(\theta))( \sin(\theta))\right| = r $

<br/>

Substituting this into the integral:

$ dy \, dx = \displaystyle \int_D 1 \cdot r \, dr \, d\theta $

<br/>

Thus

$ dy \, dx = \left|\dfrac{\partial(x, y)}{\partial(r, \theta)}\right| \, dr \, d\theta = r \, dr \, d\theta $


<br/><br/>

**Explanation for $dydx = r \: dr \: d\theta$**

In polar coordinates, we have,

$x = r \cos(\theta)$
$y = r \sin(\theta)$

<br/>

Given the two functions $x,y$ we apply partial differentiation with respect to $r$ and $\theta$

$\dfrac{\partial x}{\partial r} = \cos(\theta)$ 

$\dfrac{\partial x}{\partial \theta} = -r \sin(\theta)$

<br/> 

$\dfrac{\partial y}{\partial r} = \sin(\theta)$

$\dfrac{\partial y}{\partial \theta} = r \cos(\theta)$


<br/>

Then, changing variables in a double integral,

$ dy \, dx = \left|\dfrac{\partial(x, y)}{\partial(r, \theta)}\right| \, dr \, d\theta $

<br/>

Applying the determinant of the Jacobian matrix,

$ \left|\dfrac{\partial(x, y)}{\partial(r, \theta)}\right| = \left| (\cos(\theta))(r \cos(\theta)) - (-r \sin(\theta))(\sin(\theta)) \right| $

<br/>

Simplifying

$ \left| (\cos(\theta))(r \cos(\theta)) - (-r \sin(\theta))(\sin(\theta)) \right| $

<br/>

Expand the terms

$ \left| r \times (\cos^2(\theta) +  \sin^2(\theta)) \right| $

<br/>

Use the trigonometric identity \(\cos^2(\theta) + \sin^2(\theta) = 1\)


$ \left| r \cdot 1 \right| = |r| $

<br/>

Therefore

$ \left|\dfrac{\partial(x, y)}{\partial(r, \theta)}\right| = |r| $


$ dy \, dx = r \, dr \, d\theta $

<br/><br/>

**Explaining $\dfrac{\partial x}{\partial r} = \cos(\theta)$**


Given

$x = r \cos(\theta)$
$y = r \sin(\theta)$

<br/>

The partial derivative of $x$ is

$\dfrac{\partial x}{\partial r} = \dfrac{\partial}{\partial r} (r \cos(\theta))$

<br/>

Applying the product rule of differentiation (\(uv'\))

$\dfrac{\partial x}{\partial r} = \dfrac{\partial}{\partial r} x = \dfrac{\partial}{\partial r} (r \cos(\theta)) = \dfrac{\partial r}{\partial r} \cos(\theta) + \dfrac{\partial \cos(\theta)}{\partial r} r$

where
- $\dfrac{d}{dx}(uv) = \dfrac{dv}{dx} u + \dfrac{du}{dx} v$ is the product differentiation rule

- $u = r$  
- $v = \cos(\theta)$

<br/>

Then, we have

- $\dfrac{\partial r}{\partial r} = 1$ and <br/> <br/>

- $\dfrac{\partial \cos(\theta)}{\partial r} = 0$ (since \(\cos(\theta)\) is not a function of \(r\))

<br/>

Simplifying

$\dfrac{\partial x}{\partial r} = \cos(\theta) $


<br/><br/>

##### Reference(s)
1. https://www.math.utah.edu/~davar/math5010/summer2010/L7.pdf
2. https://www.scirp.org/journal/paperinformation.aspx?paperid=100627
3. https://math.stackexchange.com/questions/364112/how-to-prove-that-integration-of-exp-x2-is-error-function