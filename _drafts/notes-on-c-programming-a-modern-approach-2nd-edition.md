---
title: "Notes on \"C Programming: A Modern Approach, 2nd Edition\""
categories: [Notes, Programming]
tags: [c, programming language]
---

The first edition of [*C Programming: A Modern Approach*](http://knking.com/books/c/) by [K. N. King](http://knking.com/) was published in 1996, and the second edition was published in 2008, which covered [C99](https://en.wikipedia.org/wiki/C99). The author said that his *modern approach* includes these ways:

![front cover](https://images-na.ssl-images-amazon.com/images/I/41+bFKtFHjL._SX258_BO1,204,203,200_.jpg){: .align-right width="20%" }

- **Put C in perspective**. Instead of treating C as the only programming language, the author treated it as one of many programming languages. He discussed what kind of applications C is best suited for.
- **Emphasize standard versions of C**. The author didn't pay too much attention to C versions before C89, such as K&R C.
- **Debunk myths**. The author didn't hesitate to debunk some of the myths of C or challenge some beliefs that have long been part of the C folklore, for example, the belief that pointer arithmetic is always faster than array subscripting. He re-examined the old conventions of C, keeping the ones that are still helpful.
- **Emphasize software engineering**. The author emphasized how to use C to cope with issues that arise during programming-in-the-large.
- **Postpone C's low-level features**.
- **De-emphasize "manual optimization"**.

## Chapter 1. Introducing C

### 1.1 History of C

#### Origins

The old story: In 1969, [Thompson](https://en.wikipedia.org/wiki/Ken_Thompson) wrote [UNIX](https://en.wikipedia.org/wiki/Unix) in assembly language on [DEC PDP-7](https://en.wikipedia.org/wiki/PDP-7), but a program written in assembly language was hard to maintain, so he decided to develop a new high-level language B, which was based on [BCPL](https://en.wikipedia.org/wiki/BCPL). In 1970, Thompson rewrote UNIX in B. In 1971, it became apparent that B was not well-suited to the [PDP-11](https://en.wikipedia.org/wiki/PDP-11), so [Ritchie](https://en.wikipedia.org/wiki/Dennis_Ritchie) developed an extended version of B, which was finally called C. In 1973, C was stable enough, and UNIX was rewritten in C.

#### Standardization

In 1978, [Kernighan](https://www.cs.princeton.edu/~bwk/) and Ritchie wrote a book *The C Programming Language*. In the absence of an official standard for C, this book served as a bible and de facto standard for C programmers.

By the 1980s, C had expanded beyond the UNIX world, and that caused some problems. K&R was fuzzy about some language features, so compilers often treated them differently. Also, K&R failed to make a clear distinction between which features belong to C and which were part of UNIX. Besides, C continued to change after K&R was published -- new features were added and some old features were removed. These problems shouted the appearance of a standard for C.

In 1989, a standard was formally approved by [ANSI](https://www.ansi.org/) as X3.159-1989, which is referred to as C89. In 1990, this standard was approved by [ISO](https://www.iso.org/home.html) as ISO/IEC 9899:1990, which is referred to as C90. In 1999, some significant changes were added to C with the publication of a new standard ISO/IEC 9899:1999, which was referred to as C99.

As the latest version of this book was published in 2008, it had no opportunity to introduce the recent evolution of C: a major upgrade [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)) and a bug-fixed upgrade [C18](https://en.wikipedia.org/wiki/C18_(C_standard_revision)).

### 1.2 Strengths and Weaknesses of C

Both strengths and weaknesses of C stem from its original use (writing operating systems and other systems software) and its underlying philosophy:

- **C is a low-level language**.
- **C is a small language**.
- **C is a permissive language**.

## Chapter 2. C Fundamentals
