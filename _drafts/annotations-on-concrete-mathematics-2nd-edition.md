---
title: "Annotations on \"Concrete Mathematics, 2nd Edition\""
categories: [Notes]
tags: [mathematics, computer science]
math: true
---

[*Concrete Mathematics*, 2nd Edition](https://en.wikipedia.org/wiki/Concrete_Mathematics) by [Ronald Graham](http://www.math.ucsd.edu/~fan/ron/), [Donald Knuth](https://www-cs-faculty.stanford.edu/~knuth/), and [Oren Patashnik](https://en.wikipedia.org/wiki/Oren_Patashnik), published in 1994.

![front cover](https://img3.doubanio.com/view/subject/s/public/s3224520.jpg){: .align-right width="20%" }

## Preface

> THIS BOOK IS BASED on a course of the same name that has been taught annually at Stanford University since 1970.

## Chapter 1. Recurrent Problems

### 1.1 The Tower of Hanoi

[Tower of Hanoi](https://www.mathsisfun.com/games/towerofhanoi.html) was invented by the French mathematician [Edouard Lucas](https://en.wikipedia.org/wiki/%C3%89douard_Lucas) in 1883. It can be described as that we are given \\\(n\\\) disks, initially stacked in decreasing size on one of three pegs; The objective is to transfer the entire tower to one of the other pegs, moving only one disk at a time and never moving a larger one onto a smaller.

How to solve it?

1. *Name and conquer*: Let's say that \\\(T_n\\\) is the minimum number of moves that will transfer \\\(n\\\) disks from one peg to another under Lucas's rules.
2. *Look at small cases*: \\\(T_0 = 0\\\), \\\(T_1 = 1\\\), \\\(T_2 = 3\\\)...
3. *Try to think big*: We first transfer the \\\(n − 1\\\) smallest to a different peg (requiring \\\(T_{n−1}\\\) moves), then move the largest (requiring one move), and finally transfer the \\\(T_{n−1}\\\) smallest back onto the largest (requiring another \\\(T_{n−1}\\\) moves).

So we have

\\\[
T_n = 2T_{n-1} + 1
\\\]

How to solve this equation?

First, slightly transform the form of this equation,

\\\[
T_n + 1 = 2(T_{n-1} + 1)
\\\]

Combining with \\\(T_0 = 0\\\), we have

\\\[
T_n = 2^n - 1
\\\]

### 1.2 Lines in the Plane
