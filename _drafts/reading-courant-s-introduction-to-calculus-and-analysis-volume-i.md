---
title: "Reading Courant's \"Introduction to Calculus and Analysis, Volume I\""
categories: [Notes]
tags: [calculus, analysis, mathematics]
math: true
---

*Introduction to Calculus and Analysis*, Volume I by [Richard Courant](https://en.wikipedia.org/wiki/Richard_Courant) and [Fritz John](https://en.wikipedia.org/wiki/Fritz_John) was first published in 1965. The version I read is the [1998 edition](https://www.springer.com/gp/book/9783540650584) published by Springer.

![front cover](https://images.springer.com/sgw/books/medium/9783540650584.jpg){: .align-right width="20%" }

## Chapter 1. Introduction

### The Continuum of Numbers

The *continuum of numbers* is an extension of *natural numbers* for measuring continuous quantities.

*Rational numbers* are *infinite* and *dense*, but they are **not enough** to measure continuous quantities. For example, the diagonal length of a square with edge length of 1 could not be represented by a rational number. Suppose it could, let's denote the diagonal length by a rational number \\\(p/q\\\), where both \\\(p\\\) and \\\(q\\\) are natural numbers, and they have no common divisor. According to [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem), whe have \\\(p^2 = 2q^2\\\), so \\\(p\\\) is an even number, we may denote it as \\\(p = 2r\\\), then we have \\\(q^2 = 2r^2\\\), so \\\(q\\\) is also an even number. This result is constracted with our assumption.

Even without careful construction of the theory of continuum of numbers, we can think of the points on a line as the basic elements of the continuum. We can select a point as the zero point, and select another point as the unit point, then we can correspond every rational number into a point on the line. Of course, we already knew that *not every point on the line has a corresponding rational number*.

However, we can use an interval with rational points (\\\(I = [a,b]\\\)) to capture an irrational point \\\(i\\\), i.e. \\\(a < i < b\\\). The interval \\\(I\\\) is called an approximation of \\\(i\\\), and the length of it \\\(\|I\| = b - a\\\) is called the error of approximation. We can improve our approximation by narrowing the interval but without losing the target irrational point. Then we get a sequence of nested intervals \\\(I_1 \supset I_2 \supset \dots \supset I_n\\\). Our intuition of continuous tell us that even the length of the interval tends to zero, we could still capture the irrational point. We need to explicitely state it as an *axiom of continuity*:

*If \\\(I_1, I_2, I_3, \dots\\\) form a nested sequence of intervals with rational endpoints, there is a point \\\(x\\\) (rational or irrational) contained in all \\\(I_n\\\).*

### Some Useful Inequalities
