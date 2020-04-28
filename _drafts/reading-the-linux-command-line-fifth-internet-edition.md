---
title: "Reading \"The Linux Command Line, Fifth Internet Edition\""
categories: [Notes, Programming]
tags: [linux, shell, command line, unix, operating system]
---

[*The Linux Command Line*](http://linuxcommand.org/tlcl.php) by [William Shotts](https://twitter.com/william_shotts) was first published in 2012. It can be read freely online, and the version I read is the 5th Internet edition.

![front cover](http://linuxcommand.org/images/lcl2_front_new.png){: .align-right width="20%" }

Linux means freedom.

> Freedom is the power to decide what your computer does, and the only way to have this freedom is to know what your computer is doing. Freedom is a computer that is without secrets, one where everything can be known if you care enough to find out.

For playing with Linux, we don't have to install it on our local computer. We can access a Linux system through a [Linux container](https://linuxcontainers.org/).

## Part 1. Learning the Shell

### Chapter 1. What Is the Shell?

A *shell* is a user interface for accessing the operating system. Operating system shells use either a *command-line interface* (CLI) or a *graphical user interface* (GUI). [`bash`](https://www.gnu.org/software/bash/) is a shell program shipped with almost all Linux distributions. The name "bash" is an acronym for "Bourne Again SHell", a reference to the fact `bash` is an enhanced replacement for `sh`, the original Unix shell program written by [Steve Bourne](https://en.wikipedia.org/wiki/Stephen_R._Bourne). When using a computer through a GUI, we normally interact with the shell through a program called *terminal emulator*.

    Termial -> Shell -> Operating System

#### Prompt

If the last character of the prompt is a pound sign (`#`) rather than a dollar sign (`$`), the terminal session has *superuser* privileges.

### Chapter 2. Navigation
