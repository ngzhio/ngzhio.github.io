---
title: "Annotations on \"CLR via C#, 4th Edition\""
categories: [Notes]
tags: [csharp, dotnet, programming language, computer science]
---

[*CLR via C#*, 4th Edition](https://www.amazon.com/dp/0735667454) by [Jeffrey Richter](https://twitter.com/jeffrichter), published in 2012.

![front cover](https://images-na.ssl-images-amazon.com/images/I/41NxW1LMwKL._SX403_BO1,204,203,200_.jpg){: .align-right width="20%" }

I had built a [playground](https://github.com/ngzhio/clr-via-csharp-4e) for this book.

## Introduction

> As I invested more and more of my time into it, however, I realized that it was much bigger. In a way, it is its own operating system. It has its own memory manager, its own security system, its own file loader, its own error handling mechanism, its own application isolation boundaries ([AppDomains](https://docs.microsoft.com/en-us/dotnet/framework/app-domains/application-domains)), its own threading models, and more.

### Who This Book Is For

> The purpose of this book is to explain how to develop applications and reusable classes for the .NET Framework. Specifically, this means that I intend to explain how the CLR works and the facilities that it offers. I’ll also discuss various parts of the [Framework Class Library (FCL)](https://www.geeksforgeeks.org/net-framework-class-library-fcl/).

> The book addresses Microsoft Visual Studio 2012, .NET Framework 4.5, and version 5.0 of the C# programming language.

But I'll use the latest versions while I read this book: [Visual Studio 2019 for Mac](https://docs.microsoft.com/en-us/visualstudio/releasenotes/vs2019-mac-relnotes), [.NET Core 3.1](https://dotnet.microsoft.com/download/dotnet-core/3.1), and [C# 8.0](https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-8).

## Part I. CLR Basics

### Chapter 1. The CLR's Execution Model

#### Compiling Source Code into Managed Modules

> A managed module is a standard 32-bit Windows [portable executable](https://en.wikipedia.org/wiki/Portable_Executable) (PE32) file or a standard 64-bit Windows portable executable (PE32+) file that requires the CLR to execute.

#### Combining Managed Modules into Assemblies

1. An assembly is a logical grouping of one or more modules or resource files.
2. An assembly is the smallest unit of reuse, security, and versioning.

#### Loading the Common Language Runtime

Checking whether the .Net Core is installed in our system is easy -- just call `dotnet` on the command line. Running `dotnet --info`, it will display the .NET Core information, such as

```shell
$ dotnet --info
.NET Core SDK (reflecting any global.json):
 Version:   3.1.200
 Commit:    c5123d973b

Runtime Environment:
 OS Name:     Mac OS X
 OS Version:  10.14
 OS Platform: Darwin
 RID:         osx.10.14-x64
 Base Path:   /usr/local/share/dotnet/sdk/3.1.200/

Host (useful for support):
  Version: 3.1.2
  Commit:  916b5cba26

.NET Core SDKs installed:
  2.2.401 [/usr/local/share/dotnet/sdk]
  3.1.200 [/usr/local/share/dotnet/sdk]

.NET Core runtimes installed:
  Microsoft.AspNetCore.All 2.2.6 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.All]
  Microsoft.AspNetCore.App 2.2.6 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.AspNetCore.App 3.1.2 [/usr/local/share/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.NETCore.App 2.2.6 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]
  Microsoft.NETCore.App 3.1.2 [/usr/local/share/dotnet/shared/Microsoft.NETCore.App]

To install additional .NET Core runtimes or SDKs:
  https://aka.ms/dotnet-download
```

### Chapter 2. Building, Packaging, Deploying, and Administering Applications and Types
