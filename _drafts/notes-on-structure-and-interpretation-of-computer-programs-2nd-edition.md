---
title: "Notes on \"Structure and Interpretation of Computer Programs, 2nd Edition\""
categories: [Notes]
tags: [programming, lisp, scheme, programming language, computer science]
---

[*Structure and Interpretation of Computer Programs*, 2nd Edition](https://mitpress.mit.edu/sites/default/files/sicp/index.html) by [Harold Abelson](http://groups.csail.mit.edu/mac/users/hal/hal.html) and [Gerald Jay Sussman](http://groups.csail.mit.edu/mac/users/gjs/gjs.html) with Julie Sussman, published in 1996.

![front cover](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/cover.jpg){: .align-right width="20%" }

## Chapter 1. Building Abstractions with Procedures

The relationships between computational processes, data, programs and people:

> We are about to study the idea of a *computational process*. Computational processes are abstract beings that inhabit computers. As they evolve, processes manipulate other abstract things called *data*. The evolution of a process is directed by a pattern of rules called a *program*. People create programs to direct processes.

Why to use Lisp as the language to discuss programming?

> The most significant of these features is the fact that Lisp descriptions of processes, called *procedures*, can themselves be represented and manipulated as Lisp data. The importance of this is that there are powerful program-design techniques that rely on the ability to blur the traditional distinction between "passive" data and "active" processes.

I used [ChezScheme](https://github.com/cisco/ChezScheme) as my interpreter when I was walking through this book.

### 1.1 The Elements of Programming

Every powerful language has three mechanisms:

- *Primitive expressions*, which represent the simplest entities the language is concerned with.
- *Means of combination*, by which compound elements are built from simpler ones.
- *Means of abstraction*, by which compound elements can be named and manipulated as units.

#### 1.1.1 Expressions

What are *expressions*? An expression is something you can feed into the interpreter; the Interpreter would evaluate it and print its value. This loop is called *read-eval-print*.

Scheme provides some primitive expressions like *numbers*. Scheme also provide some *primitive procedures* such as `+`, `-`, `*`, `/` to let users to form compound expressions based on primitive expressions, for example,

```scheme
> (+ 1 2)
3
```

This compound expression is called a *combination*. The leftmost expression in the combination is called *operator*, and other expressions are called *operands*. Yes, an operator is also an expression, if you feed an operator into the interpreter, it will give you some value, for example,

```scheme
> +
#<procedure +>
```

Primitive procedures are the means of combination provided to us by Scheme.

Combinations can be nested:

```scheme
> (+ (* 3 5) (- 10 6))
19
```

#### 1.1.2 Naming and the Environment
