---
title: "Notes on \"Computer Science: An Overview, 12th Edition\""
categories: [Notes]
tags: [computer science]
---

J. Glenn Brookshear's *Computer Science: An Overview* is a textbook intended for use in the Introduction to Computer Science course. It takes a breadth-first approach. The first version was published in 1985. The version I read is the [12th edition (Global Edition, 2014)](https://www.amazon.com/dp/B00XN4D0BQ); the second author, [Dennis Brylow](https://www.cs.mu.edu/~brylow/), shared the copyright of this book since the 11th edition.

![front cover](https://m.media-amazon.com/images/I/51LM1-F57vL.jpg){: .align-right width="25%" }

This book divides into 13 chapters:

- [Chapter 0. Introduction](#chapter-0-introduction)
- [Chapter 1. Data Storage](#chapter-1-data-storage)
- Chapter 2. Data Manipulation
- Chapter 3. Operating Systems
- Chapter 4. Networking and the Internet
- Chapter 5. Algorithms
- Chapter 6. Programming Languages
- Chapter 7. Software Engineering
- Chapter 8. Data Abstractions
- Chapter 9. Database Systems
- Chapter 10. Computer Graphics
- Chapter 11. Artificial Intelligence
- Chapter 12. Theory of Computation

## Chapter 0. Introduction

## Chapter 1. Data Storage

### 1.1 Bits and Their Storage

#### Gates and Flip­Flops

> A device that produces the output of a Boolean operation when given the operation’s input values is called a **gate**.

> A flip-flop is a fundamental unit of computer memory. It is a circuit that produces an output value of 0 or 1, which remains constant until a pulse (a temporary change to a 1 that returns to 0) from another circuit causes it to shift to the other value. In other words, the output can be set to “remember” a zero or a one under control of external stimuli.

Here are two kinds of implementations of the flip-flop:

{% include image.html name="flip-flop-a.png" caption="An implementation of the flip-flop (A)" width="50%" %}
{% include image.html name="flip-flop-b.png" caption="An implementation of the flip-flop (B)" width="50%" %}

### 1.2 Main Memory

#### Memory Organization

> A computer’s main memory is organized in manageable units called **cells**, with a typical cell size being eight bits.

> Because a computer’s main memory is organized as individual, addressable cells, the cells can be accessed independently as required. To reflect the ability to access cells in any order, a computer’s main memory is often called **random access memory (RAM)**.

> Although we have introduced flip-flops as a means of storing bits, the RAM in most modern computers is constructed using analogous, but more complex technologies that provide greater miniaturization and faster response time. Many of these technologies store bits as tiny electric charges that dissipate quickly. Thus these devices require additional circuitry, known as a refresh circuit, that repeatedly replenishes the charges many times a second. In recognition of this volatility, computer memory constructed from such technology is often called **dynamic memory**, leading to the term **DRAM** (pronounced “DEE–ram”) meaning Dynamic RAM. Or, at times the term **SDRAM** (pronounced “ES-DEE-ram”), meaning Synchronous DRAM, is used in reference to DRAM that applies additional techniques to decrease the time needed to retrieve the contents from its memory cells.

### 1.3 Mass Storage
