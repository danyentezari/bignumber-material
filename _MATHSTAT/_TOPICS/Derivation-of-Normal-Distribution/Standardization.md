# Standardization

<!-- pdf-page-width: wide -->

$$
\begin{align*}
z
&=
\frac{k-np}{\sqrt{npq}}
\tag*{\just{Define}}
\\[0.45em]
z
&=
\frac{k-\mu}{\sigma}
\tag*{\just{Then}}
\\[0.45em]
\Delta k
&=
1
\tag*{\just{Because $k$ changes in integer increments,}}
\\[0.45em]
\Delta z
&=
\frac{1}{\sqrt{npq}}
\tag*{\just{Therefore, the corresponding increment in $z$ is}}
\\[0.45em]
P(X_n=k)
&\approx
\frac{1}{\sqrt{2\pi}}
e^{-z^2/2}
\Delta z
\tag*{\just{The binomial probability can therefore be written}}
\\[0.45em]
a
&\leq
\frac{X_n-np}{\sqrt{npq}}
\leq
b
\tag*{\just{For an interval}}
\\[0.45em]
P
\left(
a
\leq
\frac{X_n-np}{\sqrt{npq}}
\leq
b
\right)
&\approx
\sum
\frac{1}{\sqrt{2\pi}}
e^{-z_i^2/2}
\Delta z
\tag*{\just{the probability is a sum of these terms:}}
\\[0.45em]
n
&\rightarrow\infty
\tag*{\just{As}}
\\[0.45em]
\Delta z
&\rightarrow0
\tag*{\just{we have}}
\\[0.45em]
\boxed{
P
\left(
a
\leq
\frac{X_n-np}{\sqrt{npq}}
\leq
b
\right)
\rightarrow
\int_a^b
\frac{1}{\sqrt{2\pi}}
e^{-z^2/2}
\,dz
}
\tag*{\just{The sum becomes a Riemann integral:}}
\end{align*}
$$

This is the de Moivre-Laplace limit theorem.
