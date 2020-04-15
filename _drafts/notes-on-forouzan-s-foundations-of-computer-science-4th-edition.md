---
title: "Notes on Forouzan's \"Foundations of Computer Science, 4th Edition\""
categories: [Notes]
tags: [computer science]
---

[*Foundations of Computer Science*, 4th Edition](https://www.cengage.co.uk/books/9781473751040/) by [Behrouz Forouzan](https://en.wikipedia.org/wiki/Behrouz_A._Forouzan), published in 2018.

![front cover](https://www.cengage.com/covers/imageServlet?productISBN13=9781473751040&image_type=LRGFC&catalog=cengage){: .align-right width="20%" }

## Chapter 1. Introduction

### 1.1 Turing Model

The idea of a universal computational device was first described by [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) in [1936](http://140.177.205.52/prizes/tm23/images/Turing.pdf). He proposed that all computation could be performed by a special kind of a machine, now called a *Turing machine*. This machine could be described as a *programmable data processor*.

{% include image.html name="turing-machine.png" alt="Turing machine" width="50%" %}

### 1.2 Von Neumann Model

Around 1944–1945, [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann) proposed that, since program and data are logically the same, programs should also be stored in the memory of a computer. Computers built on the von Neumann model divide the computer hardware into four subsystems:

{% include image.html name="von-neumann-machine.png" alt="von Neumann machine" width="50%" %}

### 1.3 Computer Components

Computer hardware, data, and computer software.

### 1.4 History

- Mechanical machines (before 1930)
  - [Pascal's calculator](https://en.wikipedia.org/wiki/Pascal%27s_calculator) (Pascaline) invented by [Blaise Pascal](https://en.wikipedia.org/wiki/Blaise_Pascal) in the early 17th century, a mechanical calculator for addition and subtraction operations.
  - [The Leibniz Wheel](https://en.wikipedia.org/wiki/Leibniz_wheel) invented by [Gottfried Leibniz](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) in the late 17th century, a mechanical calculator that could do multiplication and division as well as addition and subtraction.
  - [The Jacquard loom](https://en.wikipedia.org/wiki/Jacquard_machine) invented by [Joseph-Marie Jacquard](https://en.wikipedia.org/wiki/Joseph_Marie_Jacquard) at the beginning of the 19th century. The loom used punched cards (like a stored program) to control the raising of the warp threads in the manufacture of textiles.
  - [The Difference Engine](https://en.wikipedia.org/wiki/Difference_engine) invented by [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) in 1823, which could do more than simple arithmetic operations -- it could solve polynomial equations, too.
  - [The Analytical Engine](https://en.wikipedia.org/wiki/Analytical_Engine) described by Charles Babbage in 1837. It had four components: a mill (corresponding to a modern ALU), a store (memory), an operator (control unit), and output (input/output).
  - In 1890, [Herman Hollerith](https://en.wikipedia.org/wiki/Herman_Hollerith), working at the US Census Bureau, designed and built a programmer machine that could automatically read, tally, and sort data stored on punched cards.
- Electronic computers (1930–1950)
  - The ABC invented by [John V. Atanasoff](https://en.wikipedia.org/wiki/John_Vincent_Atanasoff) and [Clifford Berry](https://en.wikipedia.org/wiki/Clifford_Berry) in 1939, which was the first special-purpose computer that encoded information electrically. It was specifically designed to solve a system of linear equations.
  - Z1 designed by [Konrad Zuse](https://en.wikipedia.org/wiki/Konrad_Zuse) in 1938, a general-purpose computer.
  - [Mark I](https://en.wikipedia.org/wiki/Harvard_Mark_I) in 1930s, a huge computer used both electrical and mechanical components.
  - [Colossus](https://en.wikipedia.org/wiki/Colossus_computer) invented by Alan Turing to break the German Enigma code.
  - [ENIAC](https://en.wikipedia.org/wiki/ENIAC) made by [John Mauchly](https://en.wikipedia.org/wiki/John_Mauchly) and [J. Presper Eckert](https://en.wikipedia.org/wiki/J._Presper_Eckert) in 1946, the first general-purpose, totally electronic computer.

Computer generations:

1. The first generation (roughly 1950–1959) is characterized by the emergence of commercial computers.
2. The second generation computers (roughly 1959–1965) used transistors instead of vacuum tubes.
3. The third generation (roughly 1965-1075) used *integrated circuit*.
4. The fourth generation (approximately 1975–1985) saw the appearance of microcomputers.
5. This open-ended generation started in 1985.

## Chapter 2. Number Systems
