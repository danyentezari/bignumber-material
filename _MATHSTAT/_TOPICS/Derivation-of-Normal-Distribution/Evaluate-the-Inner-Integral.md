# Evaluate the Inner Integral

<!-- pdf-page-width: wide -->

$$
\begin{align*}
u
&=
\frac{r^2}{2}
\tag*{\just{Let}}
\\[0.45em]
du
&=
r\,dr
\tag*{\just{Then}}
\\[0.45em]
\int_0^\infty
e^{-r^2/2}
r\,dr
&=
\int_0^\infty e^{-u}\,du
\tag*{\just{Thus,}}
\\[0.45em]
\int_0^\infty e^{-u}\,du
&=
\left[
-e^{-u}
\right]_0^\infty
=
1
\tag*{\just{Therefore,}}
\\[0.45em]
I^2
&=
\int_0^{2\pi}1\,d\theta
\tag*{\just{Hence,}}
\\[0.45em]
I^2
&=
2\pi
\tag*{\just{Therefore,}}
\\[0.45em]
I
&=
\sqrt{2\pi}
\tag*{\just{Since $I>0$,}}
\\[0.45em]
\boxed{
\int_{-\infty}^{\infty}
e^{-x^2/2}\,dx
=
\sqrt{2\pi}
}
\tag*{\just{Thus,}}
\\[0.45em]
\boxed{
\int_{-\infty}^{\infty}
e^{-x^2}\,dx
=
\sqrt{\pi}
}
\tag*{\just{and equivalently,}}
\end{align*}
$$
