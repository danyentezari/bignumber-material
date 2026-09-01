# Standardization

<!-- pdf-page-width: wide -->

$$
\begin{align*}
z
&=
\frac{k-np}{\sqrt{npq}}
\tag*{\just{Standardize the displacement from the mean}}
\\[0.45em]
&=
\frac{k-\mu}{\sigma}
\tag*{\just{Substitute the binomial mean and standard deviation}}
\\[0.45em]
\Delta k
&=
1
\tag*{\just{$k$ changes in integer increments}}
\\[0.45em]
\Delta z
&=
\frac{1}{\sqrt{npq}}
\tag*{\just{Find the corresponding increment in standardized coordinates}}
\\[0.45em]
P(X_n=k)
&\approx
\frac{1}{\sqrt{2\pi}}
e^{-z^2/2}
\Delta z
\tag*{\just{Write each binomial mass as a Riemann-sum term}}
\\[0.45em]
a
&\leq
\frac{X_n-np}{\sqrt{npq}}
\leq
b
\tag*{\just{Consider a fixed standardized interval}}
\\[0.45em]
P\left(
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
\tag*{\just{Sum the binomial probabilities over the interval}}
\\[0.45em]
n
&\longrightarrow
\infty
\\
\Delta z
&\longrightarrow
0
\tag*{\just{The standardized lattice becomes arbitrarily fine}}
\\[0.45em]
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
\tag*{\just{The Riemann sum converges to the Gaussian integral}}
\end{align*}
$$

\defaultwidthpar{This proves the De Moivre-Laplace theorem.}

$\square$
