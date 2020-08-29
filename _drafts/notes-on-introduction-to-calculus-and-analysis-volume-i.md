---
title: "Notes on \"Introduction to Calculus and Analysis, Volume I\""
categories: [Notes]
tags: [calculus, analysis]
math: true
---

*Introduction to Calculus and Analysis, Volume I* by [Richard Courant](https://en.wikipedia.org/wiki/Richard_Courant) and [Fritz John](https://en.wikipedia.org/wiki/Fritz_John) was first published in 1965.

## Table of Contents <!-- omit in toc -->

- [1 Introduction](#1-introduction)
  - [1.1 The Continuum of Numbers](#11-the-continuum-of-numbers)
    - [b. Real Numbers and Nested Intervals](#b-real-numbers-and-nested-intervals)
    - [e. Inequalities](#e-inequalities)
  - [1.2 The Concept of Function](#12-the-concept-of-function)
    - [d. Continuity](#d-continuity)
  - [1.7 Discussion of the Concept of Limit](#17-discussion-of-the-concept-of-limit)
    - [a. Definition of Convergence and Divergence](#a-definition-of-convergence-and-divergence)
    - [b. Rational Operations with Limits](#b-rational-operations-with-limits)

## 1 Introduction

### 1.1 The Continuum of Numbers

#### b. Real Numbers and Nested Intervals

Although there are some points on a line that can't be represented as rational numbers, we always can use an interval \\\(I=[a,b]\\\) with rational endpoints to capture an irrational point \\\(x\\\). The length of the interval \\\(\|I\|=b-a\\\) is the error. We can improve the accuracy by narrowing the length of the interval while still keep the target irrational point inside the interval. The essence of the axiom of the continuum is just a statement that promises us can infinitely run this process.

**The axiom of the continuum**: If \\\(I_1, I_2, \cdots, I_n\\\) form a nested sequence of intervals with rational endpoints, there is a point \\\(x\\\) contained in all \\\(I_n\\\).

#### e. Inequalities

*The triangle inequality*:

\\\[
\|\alpha - \beta\| \leq \|\alpha - \gamma\| + \|\gamma - \beta\|
\\\]

To prove it, we just need to apply a basic inequality: \\\(\|a+b\|\leq\|a\|+\|b\|\\\); Let \\\(a=\alpha-\gamma\\\) and \\\(b=\gamma-\beta\\\).

The geometrical interpretation of the triangle inequality is that the direct distance from \\\(\alpha\\\) to \\\(\beta\\\) is less than or equal to the sum of the distances via a third point \\\(\gamma\\\).

*The Cauchy-Schwarz inequality*:

\\\[
(\sum_{i=1}^{n}a_i b_i)^2 \leq (\sum_{i=1}^{n}a_i^2)(\sum_{i=1}^{n}b_i^2)
\\\]

To prove it, we observe that for any real \\\(t\\\), we have

\\\[
\sum_{i=1}^{n}(a_i + tb_i)^2 \geq 0  
\\\]

Expand the left side, we have

\\\[
A + 2Bt + Ct^2 \geq 0
\\\]

where \\\(A=\sum_{i=1}^{n}a_i^2\\\), \\\(B=\sum_{i=1}^{n}a_i b_i\\\), and \\\(C=\sum_{i=1}^{n}b_i^2\\\). Since this inequality holds for any real \\\(t\\\), then according to the [discriminant](https://en.wikipedia.org/wiki/Discriminant) of the quadratic polynomial, we have

\\\[
B^2 \leq AC
\\\]

This is the Cauchy-Schwarz inequality. \\\(\blacksquare\\\)

In the special case \\\(n = 2\\\), we can choose \\\(a_1 = \sqrt{x}\\\), \\\(a_2 = \sqrt{y}\\\), \\\(b_1 = \sqrt{y}\\\), and \\\(b_2 = \sqrt{x}\\\), then we have

\\\[
\sqrt{xy} \leq \frac{x+y}{2}
\\\]

This inequality says that the geometric mean of \\\(x\\\) and \\\(y\\\) never exceeds their arithmetic mean.

### 1.2 The Concept of Function

#### d. Continuity

**The definition of continuity**: The function \\\(f(x)\\\) is continuous at a point \\\(x_0\\\) of its domain if for every positive \\\(\epsilon\\\) we can find a positive \\\(\delta\\\) such that

\\\[
\|f(x) - f(x_0)\| < \epsilon
\\\]

for all values \\\(x\\\) in the domain of \\\(f\\\) for which \\\(\|x-x_0\|<\delta\\\).

This definition is not very intuitive. In fact, this definition stipulates that a function at a certain point is continuous if it does not "break" near that point. If the function \\\(f\\\) breaks at \\\(x_0\\\), there is a positive number \\\(M\\\), no matter how close \\\(x\\\) is to \\\(x_0\\\), the distance between \\\(f(x)\\\) and \\\(f(x_0)\\\) will be greater than or equal to \\\(M\\\). The definition of a continuous function is just the negative proposition of this sentence.

The largest value of \\\(\delta\\\) is called *the modulus of continuity*, which expresses the information about the sensitivity of \\\(f\\\) to changes in \\\(x\\\). Normally, \\\(\delta\\\) is a function of \\\(\epsilon\\\) and \\\(x_0\\\). We call \\\(f\\\) *uniformly continuous* in an interval if we can find a modulus of continuity that only depend on \\\(\epsilon\\\), i.e. \\\(\delta=\delta(\epsilon)\\\).

A uniformly continuous function is called [*Lipschitz-continuous*](https://en.wikipedia.org/wiki/Lipschitz_continuity) if its modulus of continuity is propotional to \\\(\epsilon\\\). In other words, \\\(f(x)\\\) satisfies

\\\[
\|f(x_1)-f(x_2)\| \leq L\|x_1 - x_2\|
\\\]

for all \\\(x_1, x_2\\\) in the interval with a fixed \\\(L\\\). Clearly, \\\(\delta(\epsilon)=\epsilon/L\\\). Lipschitz-continuity means that the *different quotient* for any two distinct points in the interval never exceeds a fixed finite value \\\(L\\\).

A more general class of uniformly continuous functions is called [*Hölder-continuous*](https://en.wikipedia.org/wiki/H%C3%B6lder_condition). The condition is

\\\[
\|f(x_1)-f(x_2)\| \leq L\|x_1 - x_2\|^{\alpha}
\\\]

Summary: Conditions from weaker to stronger: Continuous -> uniformly continuous -> Hölder-continuous -> Lipschitz-continuous.

Example: Consider \\\(f(x)=x^2\\\) and \\\(g(x)=\sqrt{x}\\\). For \\\(\|x-x_0\|<\delta\\\), we have

\\\[
\begin{align}
\|x^2-x_0^2\| = \|(x-x_0)(x+x_0)\| &\leq \|x-x_0\|\|x+x_0\| = \|x-x_0\|\|x-x_0+2x_0\| \\\\\\
                                   &\leq \|x-x_0\|(\|x-x_0\|+\|2x_0\|) \\\\\\
                                   &< \delta(\delta + 2\|x_0\|) = \epsilon
\end{align}
\\\]

if we take \\\(\delta = \sqrt{x_0^2 + \epsilon} - \|x_0\|\\\). So that \\\(f(x)\\\) is continuous.

For \\\(g(x)\\\), we have

\\\[
\|\sqrt{x}-\sqrt{x_0}\| \leq \|\sqrt{x}+\sqrt{x_0}\|
\\\]

By multiplying \\\(\|\sqrt{x}-\sqrt{x_0}\|\\\) we get

\\\[
\|\sqrt{x}-\sqrt{x_0}\| \leq \sqrt{\|x-x_0\|} < \epsilon
\\\]

if we take \\\(\delta=\epsilon^2\\\). So that \\\(g(x)\\\) is continuous, even uniformly continuous since that \\\(\delta\\\) doesn't depend on \\\(x_0\\\).

\\\(f(x)\\\) is not uniformly continuous. Suppose it is, then for \\\(\|x_1 - x_2\|<\delta\\\), we have \\\(\|x_1^2 - x_2^2\|<\epsilon\\\). Let \\\(x_1 = x_2 + \delta / 2\\\), then we have \\\(\|\delta x_2 + \delta^2 / 4\|<\epsilon\\\), but this is not always true since \\\(\delta\\\) only depends on \\\(\epsilon\\\) and we can let \\\(x_2\\\) be large enough.

\\\(g(x)\\\) is also Hölder-continuous since that \\\(\|\sqrt{x_1}-\sqrt{x_2}\| \leq \|x_1-x_2\|^{\frac{1}{2}}\\\). But \\\(g(x)\\\) is not Lipschitz-continuous since that

\\\[
\frac{\|g(x)-g(0)\|}{\|x-0\|} = \frac{1}{\sqrt{x}}
\\\]

it can be infinitely large when \\\(x\\\) tends to 0.

### 1.7 Discussion of the Concept of Limit

#### a. Definition of Convergence and Divergence

**The definition of the limit of an infinite sequence**: For any positive value \\\(\epsilon\\\), if there exist an integer \\\(N=N(\epsilon)\\\) such that for all \\\(n > N\\\) we always have \\\(\|a_n - l\|<\epsilon\\\), then we call \\\(l\\\) is the limit of \\\(a_n\\\):

\\\[
\lim_{n\rightarrow\infty}a_n = l  
\\\]

#### b. Rational Operations with Limits
