---
title: "Notes on \"The Well-Grounded Rubyist, 2nd Edition\""
categories: [Notes]
tags: [ruby, programming language]
---

*The Well-Grounded Rubyist* by David A. Black is a book to introduce the Ruby programming language. The [second edition](https://www.manning.com/books/the-well-grounded-rubyist-second-edition) was published in 2014, which covers the Ruby version of 2.1.

![front cover](https://images-na.ssl-images-amazon.com/images/I/51qtp4NzjRL._SX397_BO1,204,203,200_.jpg){: .align-right width="25%" }

Source code: [ngzhio/rubyist2e](https://github.com/ngzhio/rubyist2e).

## Table of Contents <!-- omit in toc -->

- [Part 1. Ruby foundations](#part-1-ruby-foundations)
  - [Chapter 1. Bootstrapping your Ruby literacy](#chapter-1-bootstrapping-your-ruby-literacy)
    - [1.1 Basic Ruby language literacy](#11-basic-ruby-language-literacy)
      - [1.1.2 The variety of Ruby identifiers](#112-the-variety-of-ruby-identifiers)
      - [1.1.3 Method calls, messages, and Ruby objects](#113-method-calls-messages-and-ruby-objects)

## Part 1. Ruby foundations

### Chapter 1. Bootstrapping your Ruby literacy

> The chapter is based on a view of the whole Ruby landscape as being divided into three fundamental levels:
>
> - Core language: design principles, syntax, and semantics
> - Extensions and libraries that ship with Ruby, and the facilities for adding extensions of your own
> - Command-line tools that come with Ruby, with which you run the interpreter and some other important utilities

#### 1.1 Basic Ruby language literacy

##### 1.1.2 The variety of Ruby identifiers

- Variables
  - Local

    *Local variables* start with a lowercase letter or an underscore and consist of letters, underscores, and/or digits. The Ruby convention is to use underscores rather than camel case when composing local variable names from multiple words.

  - Instance

    *Instance variables* always start with a single at sign (`@`) and consist thereafter of the same character set as local variables.

  - Class

    *Class variables* follow the same rules as instance variables, except that they start with two at signs (`@@`).

  - Global

    *Global variables* always start with a dollar sign (`$`) and consist thereafter any character.

- Constants

    *Constants* begin with an uppercase letter.

- Keywords
- Method names

    *Method names* in Ruby follow the same rules and conventions as local variables, except that they can end with `?`, `!`, or `=`. This is intentional for blending methods and expressions.

##### 1.1.3 Method calls, messages, and Ruby objects
