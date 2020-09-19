---
title: "Reading \"The Pattern On The Stone: The Simple Ideas That Make Computers Work\""
categories: [Notes, Tech]
tags: [computer]
---

[William Daniel Hillis](https://en.wikipedia.org/wiki/Danny_Hillis) (born September 25, 1956) is an American inventor, entrepreneur, and scientist, who pioneered parallel computers and their use in artificial intelligence. In 1998, he wrote a book [*The Pattern On The Stone: The Simple Ideas That Make Computers Work*](https://www.amazon.com/dp/046502596X) to explain concepts from computer science by using simple language, metaphor and analogy. It moves from *Boolean algebra* through topics such as *finite-state machines*, *programming languages*, *compilers and interpreters*, *information theory*, *parallel computing*, *cryptography*, *algorithms*, *heuristics*, *Turing machines*, *uncomutable functions*, and evolving technologies such as *quantum computing*, *neural networks*, *machine learning*, and *self-organizing systems*.

The author compares the computer to a stone (it is clever, after all, computer chips are made of silicon), and compares the program to a pattern of spells etched on the stone -- that's the source of the strange title of this book.

Computers are complex but also simple. Here are some principles that make computers easy to understand:

1. *Computers are built up in a hierarchy of parts, with each part repeated many times over*.

   So for understading a computer, we can analyze it into a hierarchy of parts, then try to understand each part first.

2. *The interactions among these parts are simple, well-defined, and usually one-directional*.

   So that the actions of the computer can be sorted neatly into causes and effects.

3. *Computers are not dependent so much on technology as on ideas*.

   This book is about ideas but not the technology.

## Table of Contents <!-- omit in toc -->

- [Notes on Each Chapter](#notes-on-each-chapter)
  - [Chapter 1. Nuts and Bolts](#chapter-1-nuts-and-bolts)
  - [Chapter 2. Universal Building Blocks](#chapter-2-universal-building-blocks)

## Notes on Each Chapter

### Chapter 1. Nuts and Bolts

The first book the author ever read on the subject of computation was [George Boole](https://en.wikipedia.org/wiki/George_Boole)'s [*An Investigation of the Laws of Thought*](https://en.wikipedia.org/wiki/The_Laws_of_Thought) -- What a high start point! In the book, Boole reduced the logic of human thoughts into mathematical operations that later called the *Boolean algebra*. In 1940, [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon) published his master's thesis [*A Symbolic Analysis of Relay Switching Circuits*](https://www.cs.virginia.edu/~evans/greatworks/shannon38.pdf). In the article, he showed that it was possible to build electrical circuits equivalent to expressions in Boolean algebra. In Shannon’s circuits, switches that were open or closed corresponded to logical variables of Boolean algebra that were true or false. Shannon demonstrated a way of converting any expression in Boolean algebra into an arrangement of switches. The circuit would establish a connection if the statement was true and break the connection if it was false. This reveals that **the circuit can perform human logical inferences**.

### Chapter 2. Universal Building Blocks
