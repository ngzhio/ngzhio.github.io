---
title: "Notes on \"What Is Mathematics?: 2nd Edition\""
categories: [Notes]
tags: [mathematics]
math: true
---

*[What Is Mathematics? An Elementary Approach to Ideas and Methods](https://en.wikipedia.org/wiki/What_Is_Mathematics%3F)* is a mathematics book written by [Richard Courant](https://en.wikipedia.org/wiki/Richard_Courant) and [Herbert Robbins](https://en.wikipedia.org/wiki/Herbert_Robbins), and was first published in 1941. A second edition was published in 1996 with an additional chapter on recent progress in mathematics, written by [Ian Stewart](https://en.wikipedia.org/wiki/Ian_Stewart_(mathematician)).

![front cover](https://upload.wikimedia.org/wikipedia/en/e/ed/What_Is_Mathematics.jpg){: .align-right width="25%" }

This book contains 9 chapters, and some supplement material is attached to the end of some chapters:

- [Chapter 1. The Natural Numbers](#chapter-1-the-natural-numbers)
- [Supplement to Chapter 1. The Theory of Numbers](#supplement-to-chapter-1-the-theory-of-numbers)
- [Chapter 2. The Number System of Mathematics](#supplement-to-chapter-1-the-theory-of-numbers)
- [Supplement to Chapter 2. The Algebra of Sets](#supplement-to-chapter-2-the-algebra-of-sets)
- [Chapter 3. Geometrical Constructions. The Algebra of Number Fields](#chapter-3-geometrical-constructions-the-algebra-of-number-fields)
- [Chapter 4. Projective Geometry. Axiomatics. Non-Euclidean Geometries](#chapter-4-projective-geometry-axiomatics-non-euclidean-geometries)
- [Chapter 5. Topology](#chapter-5-topology)
- [Chapter 6. Functions and Limits](#chapter-6-functions-and-limits)
- [Supplement to Chapter 6. More Examples on Limits and Continuity](#supplement-to-chapter-6-more-examples-on-limits-and-continuity)
- [Chapter 7. Maxima and Minima](#chapter-7-maxima-and-minima)
- [Chapter 8. The Calculus](#chapter-8-the-calculus)
- [Supplement to Chapter 8](#supplement-to-chapter-8)
- [Chapter 9. Recent Developments](#chapter-9-recent-developments)

## Chapter 1. The Natural Numbers

This chapter introduces some basic properties of the natural numbers, including arithmetics and the mathematical induction. Not very exciting for me.

## Supplement to Chapter 1. The Theory of Numbers

### &sect; 1. The Prime Numbers

#### 1. Fundamental Facts

Theorem: There are infinite many primes.

[Euclid](https://en.wikipedia.org/wiki/Euclid)'s proof: Suppose there are finite primes, then number them from 1 to n:

\\\[
p_1, p_2, \cdots, p_n
\\\]

Now consider

\\\[A = p_1 p_2 \cdots p_n + 1\\\]

Obviously, \\\(A\\\) divides by \\\(p_1, p_2, \cdots, p_n\\\) always leaves a remainder 1. So \\\(A\\\) is either a prime larger than \\\(p_n\\\) or a composite number which has a divisor larger than \\\(p_n\\\). This is contradictary to the assumption. \\\(\blacksquare\\\)

The fundamental theorem of arithmetic: *Every integer N greater than 1 can be factored into a product of primes in only one way*.

The book proved this theorem with a logic that is slightly more complicated, but the theorem is obvious: as long as the integer is continuously divided by primes from small to large, we will get a unique prime factorization. Of course, this cannot be regarded as a proof.

#### 2. The Distribution of the Primes

The algorithm of the ["sieve of Eratosthenes"](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes):

```python
def Eratosthenes(N):
    integers = list(range(N + 1))
    integers[0] = 0
    integers[1] = 0
    for i in range(2, math.ceil(math.sqrt(N))):
        if integers[i] != 0:
            for j in range(2, N):
                k = i * j
                if k > N:
                    break
                integers[k] = 0
    for i in range(2, N):
        if integers[i] != 0:
            sys.stdout.write("%d " % integers[i])
    print("\n")
```

##### a. Formulas Producing Primes

[Fermat](https://en.wikipedia.org/wiki/Pierre_de_Fermat) made a famous conjecture that all numbers of the form

\\\[F(n)=2^{2^{n}} + 1\\\]

are primes. He was wrong. In 1732, [Euler](https://en.wikipedia.org/wiki/Leonhard_Euler) discovered that \\\(F(5)=641 \times 6700417\\\), so it is not a prime. Later, more and more [Fermat numbers](https://en.wikipedia.org/wiki/Fermat_number) were found to be composite. Now, the more interested conjecture about Fermat numbers is that all Fermat numbers for \\\(n > 4\\\) are composite.

Some simple expressions to produce primes:

- \\\(n^2 - n + 41\\\) for \\\(1 \leq n \leq 40\\\)
- \\\(n^2 - 79n + 1601\\\) for \\\(1 \leq n \leq 79\\\)

##### b. Primes in Arithmetical Progressions

[Lejeune Dirichlet](https://en.wikipedia.org/wiki/Peter_Gustav_Lejeune_Dirichlet) (1805-1859) had proved a theorem by applying the most advanced tools of mathematical analysis then known: There are infinite primes in sequences of the form \\\(f(n) = a + nd\\\), where \\\(a\\\) and \\\(d\\\) have no common factors.

However, we can imitate Euclid's method to prove two special forms: \\\(4n + 3\\\) and \\\(6n + 5\\\).

1. \\\(4n + 3\\\)

    First, we observe that any prime greater than 2 is odd and hence is the form of \\\(4n + 1\\\) or \\\(4n + 3\\\). Furthermore, the product of two numbers of the form \\\(4n + 1\\\) is still that form,

    \\\[
        (4a+1)(4b+1) = 16ab + 4a + 4b + 1 = 4(4ab + a + b) + 1
    \\\]

    Now suppose there were finite primes \\\(p_1, p_2, \cdots, p_n\\\) of the form \\\(4n + 3\\\), then consider

    \\\[
        N = 4p_1 \cdots p_n - 1 = 4(p_1 \cdots p_n - 1) + 3
    \\\]

    \\\(N\\\) is also of the form \\\(4n + 3\\\). Since all \\\(p_1, \cdots, p_n\\\) divide N with a remainder \\\(-1\\\), either \\\(N\\\) is a prime, then it is contradictory to our assumption; Or there is a prime \\\(p\\\) greater than \\\(p_n\\\) which is a factor of \\\(N\\\). If \\\(p\\\) is of the form \\\(4n + 3\\\), it is also contradictory to our assumption; If \\\(p\\\) is of the form \\\(4n + 1\\\), then there is at least a prime factor of the form \\\(4n + 3\\\) greater than \\\(p_n\\\), since the product of two numbers of the form \\\(4n + 1\\\) is still that form, but it is also contradictory to our assumption. \\\(\blacksquare\\\)

2. \\\(6n + 5\\\)

    The proof is similar. First, we observe that any prime greater than 2 is odd and hence is the form of \\\(6n + 1\\\) or \\\(6n + 5\\\). Furthermore, the product of two numbers of the form \\\(6n + 1\\\) is still that form,

    \\\[
        (6a+1)(6b+1) = 36ab + 6a + 6b + 1 = 6(6ab + a + b) + 1
    \\\]

    Now suppose there were finite primes \\\(p_1, p_2, \cdots, p_n\\\) of the form \\\(6n + 5\\\), then consider

    \\\[
        N = 6p_1 \cdots p_n - 1 = 6(p_1 \cdots p_n - 1) + 5
    \\\]

    Either \\\(N\\\) is a prime, or it has a prime factor of the form \\\(6n + 5\\\) greater than \\\(p_n\\\). Both of these cases are contradictory to the assumption.

The same strategy can not be extended to the form \\\(8n + 7\\\), since odd primes can be of the form \\\(8n + 1\\\), \\\(8n + 3\\\), \\\(8n + 5\\\), or \\\(8n + 7\\\).

##### c. The Prime Number Theorem

Denote \\\(A_n\\\) as the numbers of primes not greater than \\\(n\\\). On the basis of empirical evidence [Gauss](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss) made the conjecture that the ratio \\\(A_n/n\\\) is "asymptotically equal" to \\\(1/\log n\\\), i.e.

\\\[
\lim_{n\rightarrow\infty} \frac{A_n/n}{1/\log n} = 1
\\\]

> That the average behavior of the prime number distribution can be described by the logarithmic function is a very remarkable discovery, for it is surprising that two mathematical concepts which seem so unrelated should be in fact so intimately connected.
>
> Although the statement of Gauss's conjecture is simple to understand, a rigorous mathematical proof was far beyond the powers of mathematical science in Gauss's time. To prove this theorem, concerned only with the most elementary concepts, it is necessary to employ the most powerful methods of modern mathematics. It took almost a hundred years before analysis was developed to the point where [Hadamard](https://en.wikipedia.org/wiki/Jacques_Hadamard) (1896) in Paris and [de la Vallée Poussin](https://en.wikipedia.org/wiki/Charles_Jean_de_la_Vall%C3%A9e_Poussin) (1896) in Louvain could give a complete proof of the prime number theorem. Simplifications and important modifications were given by [v. Mangoldt](https://en.wikipedia.org/wiki/Hans_Carl_Friedrich_von_Mangoldt) and [Landau](https://en.wikipedia.org/wiki/Edmund_Landau). Long before Hadamard, decisive pioneering work had been done by [Riemann](https://en.wikipedia.org/wiki/Bernhard_Riemann) (1826-1866) in a famous paper where the strategic lines for the attack were drawn. Recently, the American mathematician [Norbert Wiener](https://en.wikipedia.org/wiki/Norbert_Wiener) was able to modify the proof so as to avoid the use of complex numbers at an important step of the reasoning. But the proof of the prime number theorem is still no easy matter even for an advanced student.

##### d. Two Unsolved Problems Concerning Prime Numbers

[*Goldbach's conjecture*](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture) and the [*twin prime conjecture*](https://en.wikipedia.org/wiki/Twin_prime).

### &sect; 2. Congruences

#### 1. General Concepts

### &sect; 3. Pythagorean Numbers and Fermat's Last Theorem

### &sect; 4. The Euclidean Algorithm

## Chapter 2. The Number System of Mathematics

## Supplement to Chapter 2. The Algebra of Sets

## Chapter 3. Geometrical Constructions. The Algebra of Number Fields

## Chapter 4. Projective Geometry. Axiomatics. Non-Euclidean Geometries

## Chapter 5. Topology

## Chapter 6. Functions and Limits

## Supplement to Chapter 6. More Examples on Limits and Continuity

## Chapter 7. Maxima and Minima

## Chapter 8. The Calculus

## Supplement to Chapter 8

## Chapter 9. Recent Developments
