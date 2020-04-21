---
title: "Reading \"Structure and Interpretation of Computer Programs, 2nd Edition\""
categories: [Notes]
tags: [programming, lisp, scheme, programming language, computer science]
---

[*Structure and Interpretation of Computer Programs*](https://mitpress.mit.edu/sites/default/files/sicp/index.html), 2nd Edition by [Harold Abelson](http://groups.csail.mit.edu/mac/users/hal/hal.html) and [Gerald Jay Sussman](http://groups.csail.mit.edu/mac/users/gjs/gjs.html) with Julie Sussman was published in 1996. It is a textbook for teaching fundamental principles of computer programming, including recursion, abstraction, modularity, and programming language design and implementation.

![front cover](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/cover.jpg){: .align-right width="20%" }

I use [ChezScheme](https://github.com/cisco/ChezScheme) as my interpreter while I walk through this book.

## Chapter 1. Building Abstractions with Procedures

### The Elements of Programming

> A powerful programming language is more than just a means for instructing a computer to perform tasks. The language also serves as a framework within which we organize our ideas about processes. Thus, when we describe a language, we should pay particular attention to the means that the language provides for combining simple ideas to form more complex ideas. Every powerful language has three mechanisms for accomplishing this:
>
> - **primitive expressions**, which represent the simplest entities the language is concerned with,
> - **means of combination**, by which compound elements are built from simpler ones, and
> - **means of abstraction**, by which compound elements can be named and manipulated as units.

#### Expressions

An *expression* is something we can feed into the interpreter that will evaluate its value and print the result. This loop is called [*read-eval-print*](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop).

One kind of *primitive expressions* provided by Scheme is the *numbers*.

Primitive expressions may be combined with an expression representing a *primitive procedure* (such as `+` or `*`) to form a *compound expression* that represents the application of the procedure to those numbers. For example,

```scheme
> (+ 42 39)
81
> (* 42 39)
1638
```

They are called *combinations*. The leftmost element in the list is called the *operator*, and the other elements are called *operands*. Operators are also expressions, we can feed them into the interpreter to check its value:

```scheme
> +
#<procedure +>
> *
#<procedure *>
```

Combinations can be nested:

```scheme
> (+ (* 3 5) (- 10 6))
19
```

#### Naming and the Environment
