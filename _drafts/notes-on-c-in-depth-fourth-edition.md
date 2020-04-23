---
title: "Notes on \"C# in Depth, Fourth Edition\""
categories: [Notes]
tags: [csharp, dotnet, programming language, computer science]
---

Here are some notes I took on [*C# in Depth*, Fourth Edition](https://www.manning.com/books/c-sharp-in-depth-fourth-edition) (2019) by [Jon Skeet](https://codeblog.jonskeet.uk/).

![front cover](https://images.manning.com/720/960/resize/book/9/319e4bc-7503-43cd-a4a2-f53fa410ebc0/Skeet-4ED-HI.png){: .align-right width="20%" }

## Part 1. C# in context

### Chapter 1. Survival of the sharpest

#### 1.1 An evolving language

##### 1.1.1 A helpful type system at large and small scales

At large scale:

- C# 2
  - [*Generics*](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/), that make code more concrete.
  - [*Nullable value types*](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types), that allow the absence of information to be expressed effectively without resorting to magic values such as `–1` for a collection index or `DateTime.MinValue` for a date.
- C# 7
  - [`readonly struct`](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/struct#readonly-struct), that lets users can specify immutable `struct`.
- C# 8
  - [*Nullable reference types*](https://docs.microsoft.com/en-us/dotnet/csharp/nullable-references), that enable users to declare a reference may be `null`.

At small scale:

- C# 3
  - [*Anonymous types*](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/anonymous-types) and [*implicitly typed local variables*](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/implicitly-typed-local-variables) (`var`), they can reduce the *verbosity* of code.
- C# 7
  - [*Tuples*](https://docs.microsoft.com/en-us/dotnet/csharp/tuples). Tuples can replace anonymous types in some cases but certainly not all.
- C# 8
  - [*Record types*](https://github.com/dotnet/csharplang/blob/master/proposals/records.md).

##### 1.1.2 Ever more concise code
