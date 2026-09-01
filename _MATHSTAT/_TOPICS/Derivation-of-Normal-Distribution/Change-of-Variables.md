# Change of Variables

<!-- pdf-page-width: wide -->

\defaultwidthpar{For a one-dimensional integral,}

$$
\begin{align*}
u
&=
g(x)
\tag*{\just{Define a new variable}}
\\[0.45em]
\frac{du}{dx}
&=
g'(x)
\tag*{\just{Differentiate with respect to $x$}}
\\[0.45em]
du
&=
g'(x)\,dx
\tag*{\just{Express the differential}}
\\[0.45em]
\int
f(g(x))g'(x)\,dx
&=
\int
f(u)\,du
\tag*{\just{Substitute $u=g(x)$}}
\\[0.45em]
\int_a^b
f(g(x))g'(x)\,dx
&=
\int_{g(a)}^{g(b)}
f(u)\,du
\tag*{\just{Transform the limits for a definite integral}}
\end{align*}
$$

\defaultwidthpar{The same principle extends to several variables, except that changes in area or volume must also be accounted for.}
