---
title: "Notes on \"Programming Ruby 1.9 & 2.0\""
categories: [Reading]
tags: [ruby, programming language]
---

[*Programming Ruby 1.9 & 2.0*](http://shop.oreilly.com/product/9781937785499.do) (2013) by [Andy Hunt](https://toolshed.com/), [Dave Thomas](http://pragdave.me/), and [Chad Fowler](http://chadfowler.com/) is the 4th edition of *Programming Ruby: The Pragmatic Programmer's Guide*. It is a tutorial and reference for versions 1.9 and 2.0 of the Ruby programming language.

![front cover](https://covers.oreillystatic.com/images/9781937785499/cat.gif){: .align-right width="20%" }

Ruby 1.9 was a significant departure from previous versions. There are major changes in string handling, the scoping of block variables, and the threading model. It has a new virtual machine.

Instead, Ruby 2.0 is a fairly minor incremental improvement on Ruby 1.9. The release of Ruby 2.0 was a celebration of the 20th anniversary of Ruby.

The current stable version is [2.7.1](https://www.ruby-lang.org/en/news/2020/03/31/ruby-2-7-1-released/) (Mar 2020).

## Part I. Facets of Ruby

### Chapter 1. Getting Started

#### 1.3 Running Ruby

We can invoke `ruby` to run the Ruby interpreter, or we can invoke `irb` to run the Ruby interpreter interactively. `ruby` is a binary file, and `irb` is a Ruby script.

### Chapter 2. Ruby.new

#### 2.1 Ruby Is an Object-Oriented Language

Object-oriented programming is a programming paradigm based on the concept of *objects*. An object contains data and behaviors (methods). An object calls another object to act behaviors by sending messages.

Ruby is a pure object-oriented language. That means everything in Ruby is an object. Simple as numbers, they are also objects -- they have methods:

```ruby
> 3.14.class
=> Float
> 3.14.object_id
=> 20536414300809466
```

#### 2.3 Arrays and Hashes
