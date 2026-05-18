0 pdf of normal distribution
1 De Moivre - Laplace theorem
2 binomial theorem
3 Stirling approximation
4 Wallis product
4 gaussian integral
5 "bell curve" $e^{-x^2}$
5 iterated integral (or double integral)
6 line integral
6 change of variables
6 double integral in polar coordinates
7 polar coordinates
7 polar rectangles
7 area of sector of circle
8 jacobian
9 vector differentiation
1
### Tree

<br/>

### Definition


---
9[] vector differentiation
> 

---
8[7, pp.2] jacobian
> $Area = \displaystyle\int \displaystyle\int_{P} 1 \: dxdy$

> where
> - $P$ is a parallelogram

<br/>

> We find the area of $P$ using the determinant function (see also Theorem 3.1 [7])
>
> Let $\mathbf{w}_1, \mathbf{w}_2$ represent the sides of $P$
> 
> $\mathbf{w}_1 = [2,1]$
> $\mathbf{w}_2 = [-1,1]$
>

> Then, let $\mathbf{M}_A$ be matrix containing $\mathbf{w}_1$ and $\mathbf{w}_3$
>
> $\mathbf{M}_A = \begin{bmatrix} 2 & 1 \\ -1 & 1 \end{bmatrix}$

>
> The determinant would give the area of P (see Theorem 3.1 [7])
>
> | $\mathbf{M}_A | = \det(\mathbf{M}_A) = (2 \times 1) - (1 \times -1) = 3$
>
> $[x,y] = u\mathbf{w}_1 + v\mathbf{w}_2 + [1,1] = u[2,1] + v[-1,1] + [1,1]$
>
> $x = 2u + 1v + 1$
> $y = 1u + 1v + 1$

>
> $(x,y)$ vertices correspond to $(u,v)$ as follows:
>
> | $(x,y)$ | $(u,v)$ |
> |-|-|
> | $(1,0)$ | $(0,0)$ |
> | $(0,2)$ | $(0,1)$ |
> | $(3,2)$ | $(1,0)$ |
> | $(2,3)$ | $(1,1)$ |
>
> Then the parallelogram is mapped to a unit square by converting to the $(u,v)$ coordinate system.

>
>  $\displaystyle\int \displaystyle\int_{S} 1 \: du \: dv $ $=$ area of $S = 1$
>

> **Theorem 3.1**
> See [3, pp. 155]

<br/>

---
7[6, pp. 430] polar coordinates
> $J = \dfrac{\partial (x,y)}{\partial(u,v)} = \begin{bmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\\\ \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{bmatrix}= \dfrac{\partial x}{\partial u}\dfrac{\partial y}{\partial v} - \dfrac{\partial x}{\partial v}\dfrac{\partial y}{\partial u}$
>
<br/>

---
7[12, pp. 1063 - 1064] polar rectangles
> <br/>
>
> $\Delta A_i = \dfrac{1}{2}r_{i}^2 \Delta \theta - \dfrac{1}{2}r_{i-1}^2 \Delta \theta$ <br/>
> $\qquad = \dfrac{1}{2} \Big(r_{i}^2 - r_{i-1}^2 \Big) \Delta \theta$ <br/>
> $\qquad = \dfrac{1}{2} \Big(r_{i} + r_{i-1} \Big) \Big(r_{i} - r_{i-1} \Big) \Delta \theta $ <br/>
> $\qquad = r_{i}^{*} \: \Delta r \: \Delta \theta$
>
> <br/>

<br/>


---
7[9, pp. 709][10] area of sector of circle
> <br/>
>
> $A = \dfrac{1}{2} r^2 \theta$
> <br/>
> Proof:  <br/> 
> where
> - $r$ is the radius of a circle
> - $r^2$ is the diameter of the circle
> - $ \theta $ is angle representing sector of circle
> - $\dfrac{\theta}{2\pi}$ is fraction of area of circle 
> <br/>
>
> Area of sector of circle, $A$, is given by <br/>
>
> $A = \Big( \dfrac{\theta}{2\pi} \Big) \pi r^2$ <br/>
> 
> For a circle sector, we will have a $\theta < 2\pi$ and, therefore, $\Big( \dfrac{\theta}{2\pi} \Big) < 1$  <br/>
>
> Simplifying, 
> <br/>
> $A = \Big( \dfrac{\theta}{2\pi} \Big) \pi r^2 \qquad$ (1) <br/>
> $\qquad = \Big( \dfrac{\theta}{2} \Big) r^2 \qquad $ (2) (cancelling $\pi$) <br/>
> $\qquad = \Big( \dfrac{1}{2} \theta \Big) r^2 \qquad$ (3) (reexpressing (2)) <br/>
> $\qquad = \dfrac{1}{2} r^2 \theta \qquad$ (moving $\theta$ outside) 
> <br/>


---
6[6, pp. 431][9, pp. 1052] double integrals in polar coordinates
> $ \displaystyle \int_{R} f(x,y) \displaystyle \int dx dy = \displaystyle \int_{R^*} \displaystyle \int f(r \cos(\theta), r \sin(\theta)) \: rdrd\theta  $

<br/><br/>

> <br/>
>
> $ \displaystyle \int_{R}  \displaystyle \int f(x,y) \: dA = \displaystyle \int_{\alpha}^{\beta} \displaystyle \int_{a}^{b} f(r \cos(\theta), r \sin(\theta)) \: r \: dr \: d\theta$
>
> <br/>where
> - $A = \displaystyle \int_{a}^{b} \dfrac{1}{2} r^2 \: d \theta$

<br/>

6[8, pp. 182] change of variables
> <br/>
>
> **Indefinite integral**
> <br/>
> $\displaystyle \int f(g(x))g'(x) \: dx = \displaystyle \int f(u) \: du \qquad$ (1)
> <br/>
> 
> where
> - $u = g(x)$
> <br/>
>
> Explanation:
> - $\dfrac{du}{dx} = g'(x) \qquad$ (derivative of $u$)
> <br/>
> - $du = g'(x)dx \qquad$ (multiplying both sides by $dx$)
> <br/>
> - In (1), in the left hand side, substitute $g(x)$ with $u$ and $g'(x)dx$ with $d(u)$
> <br/><br/>

> <br/>
>
> **Definite integral**
> <br/>
> By Fundamental Theorem of Calculus II. See Indefinite Integral.
> <br/>
> $\displaystyle \int_{a}^{b} f(g(x))g'(x) \: dx $ <br/>
> $ \qquad = \displaystyle\int_{g(a)}^{g(b)}f(u) \: du$ <br/>
> $ \qquad = F(u) \Big ]_{g(a)}^{g(b)}$ <br/>
> $ \qquad = F(g(b)) - F(g(a))$
> <br/>
> where
> - $u = g(x) $
> <br/>
> 

---
6[9, pp.1115] line integral
> $\displaystyle \int_{C} f(x,y) \: ds = \underset{n\rightarrow\infty}{\lim} \displaystyle\sum\limits_{i=1}^{n} f(x_i^*, y_i^*) \Delta_{s_i}$
> <br/>where
> - $(x_i^*, y_i^*)$ is a sample point (i.e, point in subinterval)
> - $C$ is a smooth curve
> - $\Delta_{s_i}$ is length of subarc
> <br/>

--- 
5[3] iterated integral (or double integral)
> The iterated integral (or double integral) is analogous to partial differentiation, where the transform is applied with respect to one variable while other variables are made constant.

> $ \displaystyle\int \displaystyle\int_{R} f(x,y)dxdy $
>
> $ = \displaystyle\int_{a}^{b} \displaystyle\int_{g_1(x)}^{g_2(x)} f(x,y) dxdy$
>
> $ = \displaystyle\int_{a}^{b} \Big[ \displaystyle\int_{g_1(x)}^{g_2(x)} f(x,y) dx \Big] dy$

<br/>


--- 
5[] "bell curve" $e^{-x^2}$
> The function $e^{-x^2}$ that produced the bell curve

<br/>

---
4[5, 2, 4] gaussian integral
> Integration of $e^{-x^2}$
>
> $ \displaystyle\int_{-\infty}^{+\infty} e^{-x^2} dx = \sqrt{\pi}$ 

> <br/> Proof: <br/>
> $ \displaystyle\int_{-\infty}^{+\infty} e^{-x^2} dx \qquad (1) $<br/>
> For algebraic proof, we re-express $(1)$ as the combination of two one-dimensional Gaussian distributions <br/>
> $ \qquad\qquad = \sqrt{\Big(\displaystyle\int_{-\infty}^{+\infty} e^{-x^2} dx\Big) \Big(\displaystyle\int_{-\infty}^{+\infty} e^{-x^2} dx}\Big) $ <br/>
> Replace $x$ with $y$ in first term<br/>
> $ \qquad\qquad = \sqrt{\Big(\displaystyle\int_{-\infty}^{+\infty} e^{-y^2} dy\Big) \Big(\displaystyle\int_{-\infty}^{+\infty} e^{-x^2} dx}\Big) \qquad (2) $ <br/>
> Dany to explain $(2)$ to $(3)$ <br/>
> $ \qquad\qquad = \sqrt{\displaystyle\int_{-\infty}^{+\infty} \displaystyle\int_{-\infty}^{+\infty} e^{-(y^2+x^2)} dy} \qquad (3)$ <br/> <br/> 
>
> Switching to polar coordinates by switching $x+y$ with $r$ <br/><br/>
> $\displaystyle \int_{-\infty}^{+\infty} e^{-x^2} \: dx = \sqrt{  \displaystyle \int_{0}^{2\pi} \displaystyle \int_{0}^{\infty} e^{-r^2} \: r \: dr \: d\theta}$ <br/>
> Using Integrated Integral theorem, evaluate inner integral <br/>
> $\qquad = \sqrt{ \displaystyle \int_{0}^{2\pi}  \Big [ -\dfrac{1}{2} e^{-r^2} \Big ]_{0}^{\infty} \:d\theta }$ <br/>
> $\qquad =  \sqrt{ \displaystyle \int_{0}^{2\pi} \Big(  -\dfrac{1}{2} e^{-\infty^2} - \Big( -\dfrac{1}{2} e^{-0^2}\Big) \Big) \:d\theta }$ <br/>


>
> Here, the expression within the paranthesis simplifies to $\dfrac{1}{2}$ because of the following:
> 
> **Term 1** 
>
> We have
> 
> $e^{-\infty^2} = e^{-\infty} \rightarrow 0$
>
> Therefore,
> 
> $ -\dfrac{1}{2} e^{-\infty^2} = -\dfrac{1}{2}0 = 0$
>
> <br/>
>
> **Term 2**
>
> We have 
> 
> $e^{0^2} = e^{0} = 1$
>
> Therefore,
> 
> $ - \Big( -\dfrac{1}{2} e^{-0^2} \Big) = \dfrac{1}{2} e^{-0^2} = \dfrac{1}{2}$
> <br/>
>

> $\qquad = \sqrt{ \displaystyle \int_{0}^{2\pi} \dfrac{1}{2} \:d\theta} $ <br/>
> $\qquad = \sqrt{ \quad \dfrac{1}{2} \Big ]_{0}^{2\pi} \quad } $ <br/>
> $\qquad = \sqrt{ \dfrac{1}{2} 2\pi - \dfrac{1}{2}0 }$ <br/>
> $\qquad = \sqrt{ \pi }$
>
> <br/>

<br/>

---
4[2] wallis product
> $???$

<br/>

---
3[2] Stirling's approximation

> $ n! \approx \Big(\dfrac{n}{e}\Big)^n \sqrt{2 \pi n} $

Also, since terms on both sides are approximates (almost equal)

> $ \underset{n \rightarrow \infty}{\lim}  \dfrac{n!}{ \Big(\dfrac{n}{e}\Big)^n \sqrt{2 \pi n} } = 1 $


<br/>

---
1[1] de Moivre - Laplace theorem

> $ \dbinom{n}{x} p^{x}q^{n-x} \approx =\dfrac{1}{\sqrt{2 \pi n p q}} \exp\Big[ - \dfrac{(x-np)^2}{2npq} \Big]$

where

> - $p+q = 1$
> - $p,q>0$

<br/>

---
0[1] pdf of normal distribution
> $f(x; \mu, \sigma) = \dfrac{1}{\sqrt{2 \pi \sigma^2}} \exp\Big[ -\dfrac{1}{2} \Big(\dfrac{x-\mu}{\sigma} \Big)^2 \Big]$

where
> - $-\infty < x < \infty$


References:
1. https://www.scirp.org/journal/paperinformation.aspx?paperid=100627
2. https://kconrad.math.uconn.edu/blurbs/analysis/stirling.pdf
3. https://www.ucl.ac.uk/~ucahjva/itera.pdf
4. https://kconrad.math.uconn.edu/blurbs/analysis/gaussianintegral.pdf
5. https://mathworld.wolfram.com/GaussianIntegral.html
6. E. Kreyszig..., Advanced Engineering Mathematics
7. https://booksite.elsevier.com/andrilli/elementary/content/jacobian.pdf
8. Schaum's...Caclulus,...
9. J. Stewart..., Calculus...8th
10. http://faculty.up.edu/wootton/calc2/section10.4.pdf
11. https://www.math.stonybrook.edu/~ndang/mat126-fall20/sec_7.4.pdf
12. J. Stewart..., Calculus...9th
13. https://people.maths.bris.ac.uk/~mb13434/Stirling_DeMoivre_Laplace.pdflllkl
14. https://healy.econ.ohio-state.edu/kcb/Ma103/Notes/Stirling.pdf