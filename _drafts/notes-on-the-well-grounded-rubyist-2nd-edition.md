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
    - [1.2 Anatomy of the Ruby installation](#12-anatomy-of-the-ruby-installation)
    - [1.3 Ruby extensions and programming libraries](#13-ruby-extensions-and-programming-libraries)
      - [1.3.1 Loading external files and extensions](#131-loading-external-files-and-extensions)
      - [1.3.2 “Load”-ing a file in the default load path](#132-load-ing-a-file-in-the-default-load-path)
      - [1.3.3 “Require”-ing a feature](#133-require-ing-a-feature)
  - [Chapter 2. Objects, methods, and local variables](#chapter-2-objects-methods-and-local-variables)

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

Ruby sees all data structures as *objects*. Every object is capable of understanding a certain set of *messages*. Each message that an object understands corresponds directly to a *method* -- a named, executable routine whose execution the object has the ability to trigger.

*Classes* define clusters of behavior or functionality, and every object is an instance of exactly one class. But the author said that **the concept of class is less important than the concept of object**. Because objects in Ruby have the ability of adopting methods that their class didn’t give them. This is one of the most **central defining principles** of the design of Ruby as a language.

#### 1.2 Anatomy of the Ruby installation

Ruby can tell us where its installation files are located. First, we need to preload a package called `rbconfig`, which is an interface to a lot of compiled-in configuration information about the Ruby installation:

```shell
irb --simple-prompt -rrbconfig
```

Now we can access `RbConfig::CONFIG` (a *constant* referring to the *hash* where Ruby keeps its configuration knowledge) to get the configuration information.

| Term | Directory contents |
|:---- |:------------------ |
| `rubylibdir` | Ruby standard library |
| `bindir` | Ruby command-line tools |
| `archdir` | Architecture-specific extensions and libraries (compiled, binary files) |
| `sitedir` | Your own or third-party extensions and libraries (written in Ruby) |
| `vendordir` | Third-party extensions and libraries (written in Ruby) |
| `sitelibdir` | Your own Ruby language extensions (written in Ruby) |
| `sitearchdir` | Your own Ruby language extensions (written in C) |

For example,

```ruby
>> RbConfig::CONFIG["bindir"]
=> "/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/bin"
>> RbConfig::CONFIG["rubylibdir"]
=> "/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0"
>> RbConfig::CONFIG["archdir"]
=> "/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/universal-darwin19"
>> RbConfig::CONFIG["sitedir"]
=> "/Library/Ruby/Site"
>> RbConfig::CONFIG["vendordir"]
=> "/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/vendor_ruby"
>> RbConfig::CONFIG["sitelibdir"]
=> "/Library/Ruby/Site/2.6.0"
>> RbConfig::CONFIG["sitearchdir"]
=> "/Library/Ruby/Site/2.6.0/universal-darwin19"
```

#### 1.3 Ruby extensions and programming libraries

##### 1.3.1 Loading external files and extensions

Use the `load` method to load external files and extensions.

##### 1.3.2 “Load”-ing a file in the default load path

We can see the list of load paths by print a global variable named `$:` (a stupid name).

##### 1.3.3 “Require”-ing a feature

One major difference between `load` and `require` is that `require`, if called more than once with the same arguments, doesn’t reload files it’s already loaded.

### Chapter 2. Objects, methods, and local variables
