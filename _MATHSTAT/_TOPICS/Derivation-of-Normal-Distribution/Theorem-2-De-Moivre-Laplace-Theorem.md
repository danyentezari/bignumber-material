# Theorem 2: De Moivre-Laplace Theorem

<!-- pdf-page-width: wide -->

Theorem. Let

$$
\begin{align*}
X_n
&\sim
\operatorname{Bin}(n,p),
\qquad
0<p<1,
\qquad
q=1-p.
\tag*{\just{Fix a non-degenerate binomial distribution}}
\end{align*}
$$

Then, for fixed real numbers $a<b$,

$$
\begin{align*}
P\left(
a
\leq
\frac{X_n-np}{\sqrt{npq}}
\leq
b
\right)
&\longrightarrow
\int_a^b
\frac{1}{\sqrt{2\pi}}
e^{-z^2/2}
\,dz
\tag*{\just{De Moivre-Laplace limit theorem}}
\end{align*}
$$

as $n\rightarrow\infty$.

Proof.
