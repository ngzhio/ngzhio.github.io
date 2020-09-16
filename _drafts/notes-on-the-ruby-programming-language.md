---
title: "Notes on \"The Ruby Programming Language\""
categories: [Notes, Computer]
tags: [ruby, programming language]
---

Here are some notes I took on [David Flanagan](https://davidflanagan.com/) and [Yukihiro Matsumoto](https://github.com/matz)'s [*The Ruby Programming Language: Everything You Need to Know*](https://www.amazon.com/dp/0596516177) (2008).

The source code can be found [here](https://github.com/ngzhio/trpl).

## Table of Contents <!-- omit in toc -->

- [Chapter 1. Introduction](#chapter-1-introduction)
  - [1.1 A Tour of Ruby](#11-a-tour-of-ruby)
    - [1.1.1 Ruby Is Object-Oriented](#111-ruby-is-object-oriented)
    - [1.1.2 Blocks and Iterators](#112-blocks-and-iterators)
    - [1.1.3 Expressions and Operators in Ruby](#113-expressions-and-operators-in-ruby)
    - [1.1.5 Assignment](#115-assignment)
    - [1.1.7 Regexp and Range](#117-regexp-and-range)
    - [1.1.9 Ruby Surprises](#119-ruby-surprises)
- [Chapter 2. The Structure and Execution of Ruby Programs](#chapter-2-the-structure-and-execution-of-ruby-programs)

## Chapter 1. Introduction

A nice summary of what programming language Ruby is:

> Ruby is a dynamic programming language with a complex but expressive grammar and a core class library with a rich and powerful API. Ruby draws inspiration from Lisp, Smalltalk, and Perl, but uses a grammar that is easy for C and JavaTM programmers to learn. Ruby is a pure object-oriented language, but it is also suitable for procedural and functional programming styles. It includes powerful metaprogramming capabilities and can be used to create domain-specific languages or DSLs.

### 1.1 A Tour of Ruby

#### 1.1.1 Ruby Is Object-Oriented

Ruby is a *completely* object-oriented language, that means, every value in Ruby is an object, i.e. it has methods. For example,

```ruby
>> 0.class
=> Integer
>> 0.0.class
=> Float
>> ''.class
=> String
>> true.class
=> TrueClass
>> false.class
=> FalseClass
>> nil.class
=> NilClass
```

> In Ruby, parentheses are usually optional and they are commonly omitted, especially when the method being invoked takes no arguments. The fact that the parentheses are omitted in the method invocations here makes them look like references to named fields or named variables of the object. This is intentional, but the fact is, Ruby is very strict about encapsulation of its objects; there is no access to the internal state of an object from outside the object.

Do omitting parentheses make the code more readable?

#### 1.1.2 Blocks and Iterators

Iterators are a special kind of method. We can associate an invocation of an iterator with a block to implement a looping. For example,

```ruby
>> 3.times { print "Ruby! " }
Ruby! Ruby! Ruby! => 3
>> 1.upto(9) { |x| print x }
123456789=> 1
```

This feature is notable, but not unique. Blocks in here behave very similarly to λ-functions, both Python and JavaScript support it, just syntaxes are different.

#### 1.1.3 Expressions and Operators in Ruby

Ruby’s syntax is expression-oriented. Every statement is an expression.

#### 1.1.5 Assignment

Ruby supports parallel assignments:

```ruby
x, y = 1, 2
x, y = y, x         # Swap the value of two variables
x, y, z = [1, 2 ,3] # Array elements automatically assigned to variables

def polar(x, y)
    theta = Math.atan2(y, x)
    r = Math.hypot(x, y)
    [r, theta]
end

distance, angle = polar(2, 2)
```

What if we delete the brackets `[]` in the last statement of `polar`? It would report a syntax error:

    syntax error, unexpected '\n', expecting '='

#### 1.1.7 Regexp and Range

> A `Regexp` (regular expression) object describes a textual pattern and has methods for determining whether a given string matches that pattern or not. And a `Range` represents the values (usually integers) between two endpoints.

```ruby
/[Rr]uby/ # Matches "Ruby" or "ruby"
/\d{5}/   # Matches 5 consecutive digits
1..3      # All x where 1 <= x <= 3
1...3     # All x where 1 <= x < 3
```

> `Regexp` and `Range` objects define the normal `==` operator for testing equality. In addition, they also define the `===` operator for testing matching and membership. Ruby’s `case` statement (like the `switch` statement of C or Java) matches its expression against each of the possible cases using `===,` so this operator is often called the *case equality operator*.

#### 1.1.9 Ruby Surprises

Ruby’s strings are mutable. So be careful that if you include a string literal within a loop, it evaluates to a new object on each iteration of the loop.

> Conditional expressions often evaluate to `true` or `false`, but this is not required. The value of `nil` is treated the same as `false`, and *any other value is the same as* `true`. This is likely to surprise C programmers who expect `0` to work like `false`, and JavaScript programmers who expect the empty string `""` to be the same as `false`.

## Chapter 2. The Structure and Execution of Ruby Programs
