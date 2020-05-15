---
title: "Notes on \"Learning Python, 5th Edition\""
categories: [Notes, Computer]
tags: [python, programming language]
---

[*Learning Python*, 5th Edition](http://shop.oreilly.com/product/0636920028154.do) (2013) by [Mark Lutz](https://learning-python.com/) is a comprehensive, in-depth (1600+ pages) introduction to the core Python language. The author has another book -- [*Programming Python*](http://shop.oreilly.com/product/9780596158118.do) -- to teach how to apply Python.

![front cover](https://covers.oreillystatic.com/images/0636920028154/cat.gif){: .align-right width="20%" }

## Part I. Getting Started

### Chapter 1. A Python Q&A Session

#### Why Do People Use Python?

- Software quality
  - Readability
  - Coherence
  - OOP
  - Functional programming
- Developer productivity
  - Interpreted
  - Dynamically typed
- Program portability
- Support libraries
- Component integration
- Enjoyment

#### OK, but What’s the Downside?

Python's *execution speed* may not always be as fast as that of fully compiled and lower-level languages such as C and C++. The standard implementation of Python ([CPython](https://github.com/python/cpython)) compiles source code to an intermediate format known as *byte code* and then interpret the byte code. The [PyPy](https://www.pypy.org/) system can achieve a 10X to 100X speedup on some code by compiling further as the program runs.

### Chapter 2. How Python Runs Programs

#### Program Execution
