---
title: "Notes on \"What Is Mathematics?: 2nd Edition\""
categories: [Notes]
tags: [mathematics]
math: true
---

[*What Is Mathematics?*](https://en.wikipedia.org/wiki/What_Is_Mathematics%3F) by [Richard Courant](https://en.wikipedia.org/wiki/Richard_Courant) and [Herbert Robbins](https://en.wikipedia.org/wiki/Herbert_Robbins) is an introduction to mathematics, intended both for the mathematics student and for the general public. It was first published in 1941; A second edition was published in 1996 with an additional chapter on recent progress in mathematics, written by [Ian Stewart](https://en.wikipedia.org/wiki/Ian_Stewart_(mathematician)).

![front cover](https://upload.wikimedia.org/wikipedia/en/e/ed/What_Is_Mathematics.jpg){: .align-right width="25%" }

## Table of Contents <!-- omit in toc -->

- [Supplement to Chapter I: The Theory of Numbers](#supplement-to-chapter-i-the-theory-of-numbers)
  - [&sect;1. The Prime Numbers](#1-the-prime-numbers)
    - [1. Fundamental Facts](#1-fundamental-facts)
    - [2. The Distribution of the Primes](#2-the-distribution-of-the-primes)
      - [a. Formulas Producing Primes](#a-formulas-producing-primes)
      - [b. Primes in Arithmetical Progressions](#b-primes-in-arithmetical-progressions)
      - [c. The Prime Number Theorem](#c-the-prime-number-theorem)
  - [&sect;2. Congruences](#2-congruences)

## Supplement to Chapter I: The Theory of Numbers

### &sect;1. The Prime Numbers

#### 1. Fundamental Facts

Euclid's proof of the infinitude of the class of primes: Suppose the numbers of primes is finite, then we can list them as \\\(p_1, p_2, \cdots, p_n\\\). Then we form an integer \\\(A = p_1 p_2 \cdots p_n + 1\\\). Obviously, each prime in \\\(p_1, p_2, \cdots, p_n\\\) divides \\\(A\\\) with a remainder 1, so either \\\(A\\\) is a prime larger than \\\(p_n\\\), or there is a prime factor of \\\(A\\\) larger than \\\(A\\\). \\\(\blacksquare\\\)

**Fundamental theorem of arithmetic**: *Every integer greater than 1 can be factored into a product of primes in only one way*.

#### 2. The Distribution of the Primes

##### a. Formulas Producing Primes

Fermat made a famous conjecture that all numbers of the form \\\(F(n) = 2^{2^n} + 1\\\) are primes. But he was wrong. In 1732, Euler found that \\\(F(5)=641\times6700417\\\). Are all Fermat numbers \\\(F(n)\\\) for \\\(n > 4\\\) are composite?

##### b. Primes in Arithmetical Progressions

Lejeune Dirichlet (1805-1859) had proved that *in each progression \\\(a + nd\\\), where \\\(a\\\) and \\\(d\\\) have no common factors, there are infinitely many primes*.

Dirichlet's proof is very difficult, but we can extend Euclid's method to prove some special cases.

1. \\\(4n+3\\\)

    First, we can observe that all odd numbers are either of the form \\\(4n+1\\\) or \\\(4n+3\\\), and the product of two numbers of the form \\\(4n+1\\\) is still of that form:

    \\\[
    (4n+1)(4m+1)=4(n+m+4nm) + 1
    \\\]

    Now suppose that there are finite many primes of the form \\\(4n+3\\\), and we denote them as \\\(p_1, p_2, \cdots, p_n\\\). Let's consider

    \\\[
    N = 4(p_1 p_2 \cdots p_n) - 1 = 4(p_1 p_2 \cdots p_n - 1) + 3
    \\\]

    \\\(N\\\) is also of the form \\\(4n+3\\\). \\\(N\\\) may be decomposed into a product of primes, none of which can be \\\(p_1, p_2, \cdots, p_n\\\), since each of them divides \\\(N\\\) with a remainder \\\(-1\\\). So all prime factors of \\\(N\\\) are of the form \\\(4n+1\\\), but according to our observation, \\\(N\\\) should be also of the form \\\(4n+1\\\), that's contradict to our assumption. \\\(\blacksquare\\\)

2. \\\(6n+5\\\)

    The proof is similar. First, we can observe that all odd numbers are either of the form \\\(6n+1\\\) or \\\(6n+5\\\), and

    \\\[
    (6n+1)(6m+1)=6(n+m+6nm) + 1
    \\\]

    Then form a number

    \\\[
    N = 6(p_1 p_2 \cdots p_n) - 1 = 6(p_1 p_2 \cdots p_n - 1) + 5 \blacksquare
    \\\]

The similar logic of proof can't be applied to other cases again; For example, \\\(8n+7\\\), since all odd numbers can be of four forms \\\(8n+1\\\), \\\(8n+3\\\), \\\(8n+5\\\), and \\\(8n+7\\\).

##### c. The Prime Number Theorem

If we denote the number of primes not greater than \\\(n\\\) as \\\(A_n\\\), the *prime number theorem* says that

\\\[
\lim_{n\rightarrow \infty} \frac{A_n / n}{1 / \log n} = 1
\\\]

Gauss made this conjecture first. It builds a connection between two mathematical concepts (primes and the natural logarithm) that seem so unrelated.

### &sect;2. Congruences
