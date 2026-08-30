# Wallis Product

<!-- pdf-page-width: wide -->

$$
\begin{align*}
W_m
&=
\int_0^{\pi/2}\sin^m x\,dx
\tag*{\just{Define the Wallis integral}}
\\[0.6em]
W_m
&=
\frac{m-1}{m}W_{m-2}
\tag*{\just{Integration by parts}}
\\[0.6em]
W_0
&=
\frac{\pi}{2}
\tag*{\just{Initial even value}}
\\[0.6em]
W_1
&=
1
\tag*{\just{Initial odd value}}
\\[0.6em]
W_{2n}
&=
\frac{1\cdot3\cdot5\cdots(2n-1)}
{2\cdot4\cdot6\cdots(2n)}
\frac{\pi}{2}
\tag*{\just{Apply the recurrence to even powers}}
\\[0.6em]
W_{2n+1}
&=
\frac{2\cdot4\cdot6\cdots(2n)}
{3\cdot5\cdot7\cdots(2n+1)}
\tag*{\just{Apply the recurrence to odd powers}}
\\[0.6em]
\frac{\pi}{2}
&=
\prod_{n=1}^{\infty}
\frac{(2n)^2}{(2n-1)(2n+1)}
\tag*{\just{Wallis product}}
\\[0.6em]
W_{2n}
&=
\frac{\pi}{2}
\frac{\binom{2n}{n}}{4^n}
\tag*{\just{Rewrite the even integral}}
\\[0.6em]
W_{2n+1}
&=
\frac{4^n}
{(2n+1)\binom{2n}{n}}
\tag*{\just{Rewrite the odd integral}}
\\[0.6em]
W_{2n+1}
&<
W_{2n}
<
W_{2n-1}
\tag*{\just{Compare consecutive integrals}}
\\[0.6em]
\frac{W_{2n-1}}{W_{2n+1}}
&=
\frac{2n+1}{2n}
\to1
\tag*{\just{Take the limit}}
\\[0.6em]
\frac{W_{2n}}{W_{2n+1}}
&\to1
\tag*{\just{Apply the squeeze theorem}}
\\[0.6em]
\frac{\pi}{2}(2n+1)
\frac{\binom{2n}{n}^2}{16^n}
&\to1
\tag*{\just{Substitute the explicit forms}}
\\[0.6em]
\binom{2n}{n}
&\sim
\frac{4^n}{\sqrt{\pi n}}
\tag*{\just{Central binomial coefficient asymptotic}}
\end{align*}
$$