# Corollary 5: Variance

<!-- pdf-page-width: wide -->

Corollary. If

$$
\begin{align*}
X
&\sim
N(\mu,\sigma^2),
\tag*{\just{Assume a general normal random variable}}
\end{align*}
$$

then

$$
\begin{align*}
\operatorname{Var}(X)
&=
\sigma^2.
\tag*{\just{Variance of the normal distribution}}
\end{align*}
$$

Proof.

$$
\begin{align*}
\operatorname{Var}(Z)
&=
E[Z^2]
\tag*{\just{$E[Z]=0$}}
\\[0.45em]
E[Z^2]
&=
\frac{1}{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
z^2e^{-z^2/2}\,dz
\tag*{\just{Write the second moment}}
\\[0.45em]
u
&=
z
\\
dv
&=
z e^{-z^2/2}\,dz
\tag*{\just{Choose terms for integration by parts}}
\\[0.45em]
du
&=
dz
\\
v
&=
-e^{-z^2/2}
\tag*{\just{Differentiate and integrate the chosen terms}}
\\[0.45em]
\int_{-\infty}^{\infty}
z^2e^{-z^2/2}\,dz
&=
\left[
-z e^{-z^2/2}
\right]_{-\infty}^{\infty}
+
\int_{-\infty}^{\infty}
e^{-z^2/2}\,dz
\tag*{\just{Apply integration by parts}}
\\[0.45em]
&=
\sqrt{2\pi}
\tag*{\just{The boundary term vanishes and Lemma 1 evaluates the integral}}
\\[0.45em]
E[Z^2]
&=
1
\tag*{\just{Divide by $\sqrt{2\pi}$}}
\\[0.45em]
\operatorname{Var}(Z)
&=
1
\tag*{\just{Standard normal variance}}
\\[0.45em]
X
&=
\mu+\sigma Z
\tag*{\just{Use Definition 3}}
\\[0.45em]
\operatorname{Var}(X)
&=
\sigma^2
\operatorname{Var}(Z)
\tag*{\just{Variance is invariant under translation and quadratic under scaling}}
\\[0.45em]
&=
\sigma^2
\tag*{\just{Substitute $\operatorname{Var}(Z)=1$}}
\\[0.45em]
\boxed{
\operatorname{Var}(X)
=
\sigma^2
}
&&
\tag*{\just{Variance of the general normal distribution}}
\end{align*}
$$

$\square$
