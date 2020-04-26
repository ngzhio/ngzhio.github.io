---
title: "Notes on \"What Is Mathematics?, 2nd Edition\""
categories: [Notes]
tags: [mathematics]
math: true
---

Here are some notes I took on [*What Is Mathematics?: An Elementary Approach to Ideas and Methods*, 2nd Edition](https://www.amazon.com/dp/B000SEKHFG) (1996) by [Richard Courant](https://en.wikipedia.org/wiki/Richard_Courant) and [Herbert Robbins](https://en.wikipedia.org/wiki/Herbert_Robbins). This book was first published in 1941. The second edition was published in 1996 with an additional chapter on recent progress in mathematics, written by [Ian Stewart](https://en.wikipedia.org/wiki/Ian_Stewart_(mathematician)).

![front cover](https://img3.doubanio.com/view/subject/s/public/s4321023.jpg){: .align-right width="20%" }

## Chapter I. The Natural Numbers

### Introduction

> Fortunately, the mathematician as such need not be concerned with the philosophical nature of the transition from collections of concrete objects to the abstract number concept. We shall therefore accept the natural numbers as given, together with the two fundamental operations, addition and multiplication, by which they may be combined.

### &sect;2. The Infinitude of the Number System. Mathematical Induction

#### 1. The Principle of Mathematical Induction

> Let us suppose that we wish to esthblish a whole infinite sequence of mathematical propositions
>
> \\\[
> A_1, A_2, A_3, \dots
> \\\]
>
> which together constitute the general proposition \\\(A\\\). Suppose that a) by some mathematical argument it is shown that if \\\(r\\\) is any integer and if the assertion \\\(A_r\\\) is known to be true then the truth of the assertion \\\(A_{r+1}\\\) will follow, and that b) the first proposition \\\(A_1\\\) is known to be true. Then all the propositions of the sequence must be true, and \\\(A\\\) is proved.

Mathematical induction can only be used to check the truth of propositions, but it cannot be used to find the proposition.

#### 2. The Arithmetical Progression

\\\[
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
\\\]

#### 3. The Geometrical Progression

\\\[
\sum_{i=0}^{n} q^{i} = \frac{1 - q^{n+1}}{1 - q}
\\\]

\\\[
\sum_{i=1}^{n} q^{i} = q\frac{1 - q^{n}}{1 - q}
\\\]

#### 4. The Sum of the First n Squares

\\\[
\sum_{i=1}^{n} i^{2} = \frac{n(n+1)(2n+1)}{6}
\\\]

\\\[
\sum_{i=1}^{n} i^{3} = (\frac{n(n+1)}{2})^2
\\\]

#### 5. An Important Inequality

\\\[
(1+p)^n \geq 1 + np, (p > -1)
\\\]

Proof: Suppose it is true for \\\(n\\\), then for \\\(n+1\\\),

\\\[
\begin{align}
(1+p)^{n+1} &= (1+p)^n (1 + p) \\\\\\
 &\geq (1 + np)(1 + p) \\\\\\
 &= 1 + np + p + np^2 \\\\\\
 &\geq 1 + (n+1)p
\end{align}
\\\]

When \\\(n = 1\\\), the equality is hold. According to mathematical induction, we have proved this inequality. \\\(\blacksquare\\\)

#### 6. The Binomial Theorem

\\\[
(a+b)^n = \sum_{i=0}^{n} C_i^n a^{n-i}b^{i}
\\\]

where \\\(C_{i}^n\\\) is the n-th row and the i-th column of [Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle). It obeys the following formulas:

\\\[
C_{i}^n = C_{i-1}^{n-1} + C_{i}^{n-1}, C_{0}^{n} = 1, C_{n}^{n} = 1
\\\]

Proof: Suppose it is true for \\\(n\\\), then for \\\(n+1\\\),

\\\[
\begin{align}
(a+b)^{n+1} &= (\sum_{i=0}^{n} C_i^n a^{n-i}b^{i}) (a + b) \\\\\\
 &= \sum_{i=0}^{n} C_i^n a^{n+1-i}b^{i} + \sum_{i=0}^{n} C_i^n a^{n-i}b^{i+1} \\\\\\
\end{align}
\\\]

The first term can be split as \\\(C_{0}^{n} a^{n+1} + \sum_{i=1}^{n} C_i^n a^{n+1-i}b^{i}\\\), and by \\\(C_{0}^{n} = C_{0}^{n+1}\\\), we can represent the first term as

\\\[
C_{0}^{n+1} a^{n+1} + \sum_{i=1}^{n} C_i^n a^{n+1-i}b^{i}
\\\]

The second term can be split as \\\(\sum_{i=0}^{n-1} C_{i}^n a^{n-i}b^{i+1} + C_{n}^{n}b^{n+1}\\\), and by \\\(C_{n}^{n} = C_{n+1}^{n+1}\\\), we can represent the second term as

\\\[
\sum_{i=0}^{n-1} C_{i}^n a^{n-i}b^{i+1} + C_{n+1}^{n+1}b^{n+1}
\\\]

The iteration is starting at the index 0, we may slightly adjust the iteration to let it start at the index 1, then the second term can be written as

\\\[
\sum_{i=1}^{n} C_{i-1}^n a^{n+1-i}b^{i} + C_{n+1}^{n+1}b^{n+1}
\\\]

Now we add these terms again,

\\\[
\begin{align}
(a+b)^{n+1} &= C_{0}^{n+1} a^{n+1} + \sum_{i=1}^{n} C_i^n a^{n+1-i}b^{i} + \sum_{i=1}^{n} C_{i-1}^n a^{n+1-i}b^{i} + C_{n+1}^{n+1}b^{n+1} \\\\\\
 &= C_{0}^{n+1} a^{n+1} + \sum_{i=1}^{n} (C_i^n + C_{i-1}^n) a^{n+1-i}b^{i} + C_{n+1}^{n+1}b^{n+1} \\\\\\
 &= C_{0}^{n+1} a^{n+1} + \sum_{i=1}^{n} C_i^{n+1} a^{n+1-i}b^{i} + C_{n+1}^{n+1}b^{n+1} \\\\\\
 &= \sum_{i=0}^{n+1} C_i^{n+1} a^{n+1-i}b^{i}
\end{align}
\\\]

Last check, when \\\(n=1\\\), this equality is obviously hold. So we have proved this equality. \\\(\blacksquare\\\)

\\\[
C_{i}^{n} = \frac{n!}{i!(n-i)!}
\\\]

Proof: Suppose it is true for \\\(n\\\), then for \\\(n+1\\\),

\\\[
\begin{align}
C_{i}^{n+1} &= C_{i}^{n} + C_{i-1}^{n} \\\\\\
 &= \frac{n!}{i!(n-i)!} + \frac{n!}{(i-1)!(n-(i-1))!} \\\\\\
 &= \frac{n! \cdot (n+1-i)}{i!(n+1-i)!} + \frac{i \cdot n!}{i!(n+1-i))!} \\\\\\
 &= \frac{(n+1)!}{i!(n+1-i)!} \\\\\\
\end{align}
\\\]

When \\\(n=1\\\), this equality is obviously hold. So we have proved this equality. \\\(\blacksquare\\\)

Exercises: Prove by mathematical induction:
