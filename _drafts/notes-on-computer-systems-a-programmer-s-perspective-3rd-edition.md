---
title: "Notes on \"Computer Systems: A Programmer's Perspective, 3rd Edition\""
categories: [Notes, Programming]
tags: [computer system]
math: true
---

[*Computer Systems: A Programmer's Perspective*, 3rd Edition](http://csapp.cs.cmu.edu/) (2015) by [Randal E. Bryant](http://www.cs.cmu.edu/~bryant) and [David R. O'Hallaron](http://www.cs.cmu.edu/~droh) is a book that stems from the introductory computer systems course the authors developed at Carnegie Mellon University, starting in the Fall of 1998.

![front cover](http://csapp.cs.cmu.edu/3e/images/csapp3e-cover.jpg){: .align-right width="20%" }
![front cover](https://images-na.ssl-images-amazon.com/images/I/51pqLWAcyFL._SX384_BO1,204,203,200_.jpg){: .align-right width="20%" }

The presentation is based on the following principles, which aim to help the students become better programmers and to help prepare them for upper-level systems courses:

- Students should be introduced to computer systems from the perspective of a programmer, rather from the more traditional perspective of a system implementer.
- Students should get a view of the complete system, comprising the hardware, operating system, compiler, and network.
- Students learn best by developing and evaluating real programs that run on real machines.

What is the perspective of a programmer? Most books on systems -- computer architecture, compilers, operating systems, and networking -- are written as if the reader were going to design and implement such a system. That's the "builder's perspective". To learn how they affect the behavior and performance of their programs -- that's the "programmer's perspective".

## Chapter 1. A Tour of Computer Systems

### 1.3 It Pays to Understand How Compilation Systems Work

Why do programmers need to understand how compilation systems work?

- *Optimizing program performance*. For example,
  - Is a `switch` statement always more efficient than a sequence of `if-else` statements?
  - How much overhead is incurred by a function call?
  - Is a `while` loop more efficient than a `for` loop?
  - Are pointer references more efficient than array indexes?
  - Why does our loop run so much faster if we sum into a local variable instead of an argument that is passed by reference?
  - How can a function run faster when we simply rearrange the parentheses in an arithmetic expression?
- *Understanding link-time errors*. For example,
  - What does it mean when the linker reports that it cannot resolve a reference?
  - What is the difference between a static variable and a global variable?
  - What happens if you define two global variables in different C files with the same name?
  - What is the difference between a static library and a dynamic library?
  - Why does it matter what order we list libraries on the command line?
  - Scariest of all, why do some linker-related errors not appear until run time?
- *Avoiding security holes*.

### 1.4 Processors Read and Interpret Instructions Stored in Memory

#### 1.4.1 Hardware Organization of a System

{% include image.html name="hardware-organization.png" caption="Hardware organization of a aomputer system" width="50%" %}

##### Buses

*Buses* are typically designed to transfer fixed-size chunks of bytes known as *words*. The number of bytes in a word (the *word size*) is a fundamental system parameter that varies across systems.

##### I/O Devices

Each *I/O device* is connected to the I/O bus by either a *controller* or an *adapter*. Controllers are chip sets in the device itself or on the system’s main printed circuit board (often called the *motherboard*). An adapter is a card that plugs into a slot on the motherboard.

##### Main Memory

Physically, *main memory* consists of a collection of *dynamic random access memory* (DRAM) chips. Logically, memory is organized as a linear array of bytes, each with its own unique address (array index) starting at zero.

##### Processor

The *central processing unit* (CPU) is the engine that interprets (or executes) instructions stored in main memory. At its core is a word-size storage device (or register) called the *program counter* (PC). At any point in time, the PC points at (contains the address of) some machine-language instruction in main memory.

### 1.7 The Operating System Manages the Hardware

The operating system has two primary purposes:

1. To protect the hardware from misuse by runaway applications.
2. To provide applications with simple and uniform mechanisms for manipulating complicated and often wildly different low-level hardware devices.

The operating system achieves both goals via the fundamental abstractions: *processes*, *virtual memory*, and *files*.

{% include image.html name="fundamental-abstractions.png" caption="Abstractions provided by an operating system" width="50%" %}

#### 1.7.1 Processes

A *process* is the operating system’s abstraction for a running program. Multiple processes can run *concurrently* on the same system, and each process appears to have exclusive use of the hardware. By concurrently, we mean that the instructions of one process are interleaved with the instructions of another process. The operating system performs this interleaving with a mechanism known as *context switching*.

When the operating system decides to transfer control from the current process to some new process, it performs a *context switch* by saving the context -- information such as the current values of the PC, the register file, and the contents of main memory -- of the current process, restoring the context of the new process, and then passing control to the new process.

#### 1.7.2 Threads

A process may contains multiple execution units called *threads*, each running in the context of the process and sharing the same code and global data. It is easier to share data between multiple threads than between multiple processes, and threads are typically more efficient than processes.

#### 1.7.3 Virtual Memory

The virtual address space for Linux processes:

{% include image.html name="virtual-address-space.png" alt="The virtual address space for Linux processes" width="50%" %}

### 1.9 Important Themes

#### 1.9.1 Amdahl’s Law

The main idea of [*Amdahl’s law*](https://en.wikipedia.org/wiki/Amdahl%27s_law) is that when we speed up one part of a system, the effect on the overall system performance depends on both how significant this part was and how much it sped up. Consider a system in which executing some application requires time \\\(T_{old}\\\). Suppose some part of the system requires a fraction \\\(\alpha\\\) of this time, and that we improve its performance by a factor of \\\(k\\\). The overall execution time would thus be

\\\[
\begin{align}
T_{new} &= (1 - \alpha)T_{old} + (\alpha T_{old}) / k \\\\\\
 &= T_{old}(1 - \alpha + \alpha / k)
\end{align}
\\\]

From this, we can compute the speedup \\\(S = \frac{T_{old}}{T_{new}}\\\) as

\\\[
S = \frac{1}{1 - \alpha + \alpha / k}
\\\]

As an example, consider \\\(\alpha = 0.6\\\) and \\\(k = 3\\\), then we get a speedup \\\(S \approx 1.67\\\). As another example, consider \\\(k = \infty\\\), then we get \\\(S = \frac{1}{1-\alpha}\\\). **Even though we made a substantial improvement to a major part of the system, our net speedup was significantly less than the speedup for the one part.**

#### 1.9.2 Concurrency and Parallelism

##### Thread-Level Concurrency

> When we construct a system consisting of multiple processors all under the control of a single operating system kernel, we have a *multiprocessor system*. Such systems have been available for large-scale computing since the 1980s, but they have more recently become commonplace with the advent of *multi-core* processors and *hyperthreading*.

Multi-core processors have several CPUs (referred to as “cores”) integrated onto a single integrated-circuit chip.

Hyperthreading, is a technique that allows a single CPU to execute multiple flows of control. It involves having multiple copies of some of the CPU hardware, such as program counters and register files, while having only single copies of other parts of the hardware, such as the units that perform floating-point arithmetic.
