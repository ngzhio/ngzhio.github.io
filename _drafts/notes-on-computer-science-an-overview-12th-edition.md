---
title: "Notes on \"Computer Science An Overview, 12th Edition\""
categories: [Notes]
tags: [computer science]
---

Here are some notes I took on [*Computer Science An Overview*, 12th Edition (Global Edition, 2014)](https://www.amazon.com/dp/B00XN4D0BQ) by Glenn Brookshear and [Dennis Brylow](https://www.cs.mu.edu/~brylow/).

![front cover](https://img3.doubanio.com/view/subject/s/public/s28274280.jpg){: .align-right width="20%" }

## Chapter 1. Data Storage

### 1.1 Bits and Their Storage

#### Gates and Flip-Flops

> A device that produces the output of a Boolean operation when given the operation’s input values is called a **gate**.

{% include image.html name="flip-flop1.png" caption="A simple flip-flop circuit" width="30%" %}

At the normal state, both inputs are at zeros, and the output can be 0 or 1. When a *pulse* (a temporary change to a 1 that returns to 0) is sent to the upper input, the output will shift to 1 then state constant. When a pulse is sent to the lower input, the output will shift to 0 then state constant. So the value of a flip-flop circuit can be modified and remember. This property makes them to be building blocks of the computer memory.

A flip-flop circuit can be viewed as a black box. It has many implementations, for example,

{% include image.html name="flip-flop2.png" caption="Another simple flip-flop circuit" width="40%" %}

To compare this implementation with the first one, the former has a benefit: It only uses two kinds of gates.

> Although we have introduced flip-flops as a means of storing bits, the RAM in most modern computers is constructed using analogous, but more complex technologies that provide greater miniaturization and faster response time. Many of these technologies store bits as tiny electric charges that dissipate quickly. Thus these devices require additional circuitry, known as a refresh circuit, that repeatedly replenishes the charges many times a second. In recognition of this volatility, computer memory constructed from such technology is often called **dynamic memory**, leading to the term **DRAM** (pronounced “DEE–ram”) meaning Dynamic RAM. Or, at times the term **SDRAM** (pronounced “ES-DEE-ram”), meaning Synchronous DRAM, is used in reference to DRAM that applies additional techniques to decrease the time needed to retrieve the contents from its memory cells.

### 1.9 Data Compression
