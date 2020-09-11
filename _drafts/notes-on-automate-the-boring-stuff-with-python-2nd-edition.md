---
title: "Notes on \"Automate the Boring Stuff with Python, 2nd Edition\""
categories: [Notes]
tags: [python, programming language]
---

Here are some notes I took on [Al Sweigart](https://alsweigart.com/)'s [*Automate the Boring Stuff with Python*, 2nd Edition](https://automatetheboringstuff.com/) (2019).

## Table of Contents <!-- omit in toc -->

- [Part I. Python Programming Basics](#part-i-python-programming-basics)
  - [Chapter 3. Functions](#chapter-3-functions)
    - [The `global` Statement](#the-global-statement)
  - [Chapter 4. Lists](#chapter-4-lists)

## Part I. Python Programming Basics

### Chapter 3. Functions

#### The `global` Statement

Creating a variable in Python is very simple. It doesn't need any keyword or type specifier, just assigning a value to a name:

```python
message = 'hello'
```

But the cons is that you are unable to modify a global variable inside a local scope, for example,

```python
message = 'hi'

def modify():
    message = 'hello' # The interpreter would understand this statement as
                      # creating a new local variable.

modify()
print(message) # hi
```

So Python provides the `global` statement to resolve this problem:

```python
message = 'hi'

def modify():
    global message
    message = 'hello'

modify()
print(message) # hello
```

Python uses such a concise syntax to define variables is very beneficial -- it can make us write less code. Generally, in functions, we use local variables more frequently than global ones, and Python does not require us to use keywords such as `let` or `var` every time we define local variables. We only need to add a `global` statement when we need to modify global variables.

### Chapter 4. Lists
