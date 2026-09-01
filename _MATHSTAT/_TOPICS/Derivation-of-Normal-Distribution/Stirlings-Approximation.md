# Theorem 1: Stirling's Approximation

<!-- pdf-page-width: wide -->

Theorem. As $n\rightarrow\infty$,

$$
\begin{align*}
n!
&\sim
\sqrt{2\pi n}
\left(
\frac{n}{e}
\right)^n
\tag*{\just{Stirling's approximation}}
\end{align*}
$$

Proof.

$$
\begin{align*}
a_n
&=
\frac{n!e^n}{n^{n+1/2}}
\tag*{\just{Define a sequence containing the unknown constant}}
\\[0.45em]
\log a_n
&=
\log(n!)
+
n
-
\left(
n+\frac{1}{2}
\right)
\log n
\tag*{\just{Take logarithms}}
\\[0.45em]
\log\frac{a_{n+1}}{a_n}
&=
1
-
\left(
n+\frac{1}{2}
\right)
\log\left(
1+\frac{1}{n}
\right)
\tag*{\just{Compare consecutive terms}}
\\[0.45em]
\log(1+t)
&=
t-\frac{t^2}{2}
+\frac{t^3}{3}
-\cdots
\tag*{\just{Use the logarithmic series}}
\\[0.45em]
t
&=
\frac{1}{n}
\tag*{\just{Substitute}}
\\[0.45em]
\log\frac{a_{n+1}}{a_n}
&=
-\frac{1}{12n^2}
+
O\left(
\frac{1}{n^3}
\right)
\tag*{\just{Expand and simplify}}
\\[0.45em]
\sum_{n=1}^{\infty}
\frac{1}{n^2}
&<
\infty
\tag*{\just{The increments form an absolutely convergent tail}}
\\[0.45em]
a_n
&\longrightarrow
C
\qquad
(C>0)
\tag*{\just{Therefore the sequence converges}}
\\[0.45em]
n!
&\sim
C
n^{n+1/2}
e^{-n}
\tag*{\just{Solve for $n!$}}
\\[0.45em]
\binom{2n}{n}
&=
\frac{(2n)!}{(n!)^2}
\tag*{\just{Use the central binomial coefficient}}
\\[0.45em]
&\sim
\frac{
C(2n)^{2n+1/2}e^{-2n}
}{
C^2n^{2n+1}e^{-2n}
}
\tag*{\just{Apply the asymptotic to each factorial}}
\\[0.45em]
&\sim
\frac{\sqrt{2}}{C}
\frac{4^n}{\sqrt{n}}
\tag*{\just{Simplify}}
\\[0.45em]
\binom{2n}{n}
&\sim
\frac{4^n}{\sqrt{\pi n}}
\tag*{\just{Apply Lemma 2}}
\\[0.45em]
\frac{\sqrt{2}}{C}
&=
\frac{1}{\sqrt{\pi}}
\tag*{\just{Equate the two asymptotic forms}}
\\[0.45em]
C
&=
\sqrt{2\pi}
\tag*{\just{Solve for the constant}}
\\[0.45em]
\boxed{
n!
\sim
\sqrt{2\pi n}
\left(
\frac{n}{e}
\right)^n
}
&&
\tag*{\just{Stirling's approximation}}
\\[0.45em]
\boxed{
\lim_{n\to\infty}
\frac{
n!
}{
\sqrt{2\pi n}
\left(
\dfrac{n}{e}
\right)^n
}
=
1
}
&&
\tag*{\just{Equivalent limit statement}}
\end{align*}
$$

$\square$
