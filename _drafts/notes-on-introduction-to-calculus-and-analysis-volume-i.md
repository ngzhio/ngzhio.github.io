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

The largest value of \\\(\delta\\\) is called the modulus of continuity, which expresses the information about the sensitivity of \\\(f\\\) to changes in \\\(x\\\). Normally, \\\(\delta\\\) is a function of \\\(\epsilon\\\) and \\\(x_0\\\). We call \\\(f\\\) *uniformly continuous* in an interval if we can find a modulus of continuity that only depend on \\\(\epsilon\\\), i.e. \\\(\delta=\delta(\epsilon)\\\).
