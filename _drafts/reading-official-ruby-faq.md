---
title: "Reading \"Official Ruby FAQ\""
categories: [Notes]
tags: [ruby, programming language, computer science]
---

[*Official Ruby FAQ*](https://www.ruby-lang.org/en/documentation/faq/) contains Frequently Asked Questions about Ruby with answers. It is based on [*The Ruby Language FAQ*](https://ruby-doc.org/docs/ruby-doc-bundle/FAQ/FAQ.html) originally compiled by [Shugo Maeda](https://twitter.com/shugomaeda) and translated into English by Kentaro Goto. I think it's a good starting point to learn Ruby.

I made a [playground](https://github.com/ngzhio/official-ruby-faq) for this tutorial.

## General questions

### What is Ruby

> Ruby is a simple and powerful object-oriented programming language, created by [Yukihiro Matsumoto](https://twitter.com/yukihiro_matz) (who goes by the handle “Matz” in this document and on the mailing lists).
>
> Like Perl, Ruby is good at text processing. Like Smalltalk, everything in Ruby is an object, and Ruby has blocks, iterators, meta-classes and other good stuff.
>
> You can use Ruby to write servers, experiment with prototypes, and for everyday programming tasks. As a fully-integrated object-oriented language, Ruby scales well.

How simple is Ruby? What makes Ruby being good at text processing? What does it mean that everything in Ruby is an object? What makes Ruby scales well?

### Why the name “Ruby”

> Influenced by Perl, Matz wanted to use a jewel name for his new language, so he named Ruby after a colleague’s [birthstone](https://en.wikipedia.org/wiki/Birthstone).
>
> Later, he realized that Ruby comes right after Perl in several situations. In birthstones, pearl is June, ruby is July. When measuring font sizes, pearl is 5pt, ruby is 5.5pt. He thought Ruby was a good name for a programming language newer (and hopefully better) than Perl.

:smile: Funny origin.

### What is the history of Ruby

> Well, Ruby was born on February 24, 1993. I was talking with my colleague about the possibility of an object-oriented scripting language. I knew Perl (Perl4, not Perl5), but I didn’t like it really, because it had the smell of a toy language (it still has). The object-oriented scripting language seemed very promising.
>
> I knew Python then. But I didn’t like it, because I didn’t think it was a true object-oriented language—OO features appeared to be an add-on to the language. As a language manic and OO fan for 15 years, I really wanted a genuine object-oriented, easy-to-use scripting language. I looked for, but couldn’t find one.
>
> So, I decided to make it. It took several months to make the interpreter run. I put into it the features I love to have in my language, such as iterators, exception handling, garbage collection.
>
> Then, I reorganized the features of Perl into a class library, and implemented them. I posted Ruby 0.95 to the Japanese domestic newsgroups in Dec. 1995.
>
> Since then, highly active [mailing lists](https://www.ruby-lang.org/en/community/mailing-lists/) have been established and web pages formed.
>
> -- [Matz, 1999](http://blade.nagaokaut.ac.jp/cgi-bin/scat.rb/ruby/ruby-talk/382)

Why did Matz say that Python was not a true object-oriented language? What did mean that Python's OO features appeared to be an add-on to the language?

If you have a strong passion for creating programming languages, then try it. It reminds me of the book [*Crafting Interpreters*](https://craftinginterpreters.com/) by [Bob Nystrom](http://journal.stuffwithstuff.com/).

### How can I annotate Ruby code with its results

> People commonly annotate Ruby code by showing the results of executing each statement as a comment attached to that statement.

For example,

```ruby
str = "Billy" + " Bob"           # => "Billy Bob"
str[0,1] + str[2,1] + str[-2,2]  # => "Blob"
```

> Gotoken’s `xmp` package, available from [http://www.ruby-lang.org/en/raa-list.rhtml?name=xmp](http://www.ruby-lang.org/en/raa-list.rhtml?name=xmp) is a utility that annotates Ruby source code this way.

That link is broken.

## How does Ruby stack up against…

In this section, [John Dell’Aquila](mailto://jbd@alum.mit.edu) (2000) compared Python with Ruby.

A difference in the aspect of philosophy between them is that they approach the solution of combining procedural and object-oriented programming from opposite directions.

Python is a hybrid language. It has functions for procedural and object-oriented programming. When a `def` statement is written outside any class, it is a function that you can directly call. When a `def` statement is written inside a class, it is a method; The first parameter of the method will be as the receiver, and it should be explicitly named as `self`.

Ruby is a pure OO language. It has only methods. A `def` statement can use a hidden name `self` to refer to the receiver. If a `def` statement is written outside any class, the `self` refers to the root object [`Object`](https://ruby-doc.org/core-2.7.1/Object.html). So when you directly invoke a function, you are calling a method of `Object`.

> Ruby’s OO purity provides a number features that Python lacks or is still working toward: a unified type/class hierarchy, metaclasses, the ability to subclass everything, and uniform method invocation (none of this `len()` is a function but `items()` is a method rubbish).

The benefit of having a root object `Object` is that you can treat anything as an `Object`. This gives you a unifying.

Python supports multiple inheritance, while Ruby only support single inheritance. So Ruby could avoid the [diamond problem](https://en.wikipedia.org/wiki/Multiple_inheritance) caused by multiple inheritance. But sometimes we want to share features or methods between classes outside the lines of single inheritance. Ruby provides *modules* for us to achieve this.

> In Ruby, we define something called a module, which is like a class, but with some restrictions: namely, you can't create an instance of a module, and a module can't inherit from a class. So in Ruby, if you define a module that has methods and plug that module into a class, then that class will have those methods, both signatures and implementations. If you then plug the same module into another class, there will be two classes that share the implementation. This gives much of the benefit of multiple inheritance, but without destroying the simple tree model of single inheritance.
>
> -- [Matz](https://www.artima.com/intv/tuesday.html#part2)

John Dell’Aquila also said that the Ruby collection classes and iterators are better:

> The Ruby collection classes and iterators are outstanding, much more powerful and elegant than the ad hoc solutions that Python is sprouting (lambdas and list comprehensions).

## Variables, constants, and arguments

### Does assignment generate a new copy of an object

Assignments in Ruby never generate a new copy of an object. An variable is a reference to an object. For example,

```ruby
a = "hello"
b = a
a.object_id == b.object_id  # => true
a[0] = "f"
b                           # => "fello"
```

Even for numbers,

```ruby
a = 42
b = a
a.object_id == b.object_id  # => true
```

## Iterators
