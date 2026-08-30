# Stirling's Approximation

<!-- pdf-page-width: wide -->

$$
\begin{align*}
a_n
&=
\frac{n!e^n}{n^{n+1/2}}
\tag*{\just{Define the sequence}}
\\[0.6em]
\log a_n
&=
\log(n!)+n-\left(n+\frac12\right)\log n
\tag*{\just{Take logarithms}}
\\[0.6em]
\log\frac{a_{n+1}}{a_n}
&=
1-\left(n+\frac12\right)
\log\left(1+\frac1n\right)
\tag*{\just{Compare consecutive terms}}
\\[0.6em]
\log(1+t)
&=
t-\frac{t^2}{2}+\frac{t^3}{3}-\cdots
\tag*{\just{Use the logarithmic series}}
\\[0.6em]
t
&=
\frac1n
\tag*{\just{Substitute}}
\\[0.6em]
\log\frac{a_{n+1}}{a_n}
&=
-\frac{1}{12n^2}
+
O\left(\frac1{n^3}\right)
\tag*{\just{Expand and simplify}}
\\[0.6em]
a_n
&\to C
\tag*{\just{The sequence converges}}
\\[0.6em]
n!
&\sim
C\,n^{n+1/2}e^{-n}
\tag*{\just{Solve for $n!$}}
\\[0.6em]
\binom{2n}{n}
&=
\frac{(2n)!}{(n!)^2}
\tag*{\just{Apply the approximation}}
\\[0.6em]
&\sim
\frac{\sqrt2}{C}\frac{4^n}{\sqrt n}
\tag*{\just{Substitute and simplify}}
\\[0.6em]
\binom{2n}{n}
&\sim
\frac{4^n}{\sqrt{\pi n}}
\tag*{\just{From the Wallis result}}
\\[0.6em]
\frac{\sqrt2}{C}
&=
\frac1{\sqrt\pi}
\tag*{\just{Equate the two asymptotic forms}}
\\[0.6em]
C
&=
\sqrt{2\pi}
\tag*{\just{Solve for the constant}}
\\[0.6em]
n!
&\sim
\sqrt{2\pi n}
\left(\frac ne\right)^n
\tag*{\just{Stirling's approximation}}
\end{align*}
$$