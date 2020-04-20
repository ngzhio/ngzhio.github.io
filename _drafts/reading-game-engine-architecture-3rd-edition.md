---
title: "Reading \"Game Engine Architecture, 3rd Edition\""
categories: [Notes]
tags: [game, game engine, computer science]
---

[*Game Engine Architecture*](https://www.gameenginebook.com/) by [Jason Gregory](https://twitter.com/jqgregory) was first published in 2009. Now the latest 3rd edition was published in 2018.

![front cover](https://www.gameenginebook.com/img/cover_full_3.png){: .align-right width="20%" }

## Part I. Foundations

### Chapter 1. Introduction

#### What is a game

> In his excellent book, [*A Theory of Fun for Game Design*](https://www.theoryoffun.com/), [Raph Koster](https://www.raphkoster.com/) defines a game to be an interactive experience that provides the player with an increasingly challenging sequence of patterns which he or she learns and eventually masters.

Computer scientists' definition of games: *soft real-time interactive agent-based computer simulations*. A computer *simulation* is a mathematical model of the real or imagined world. An *agent-based* simulation is one in which a number of distinct entities known as “agents” interact. Most video games present their stories and respond to player input in real time, making them *real-time interactive* simulations. A *soft* real-time system is one in which missed deadlines are not catastrophic, for example, if the frame rate dies, the human player generally doesn’t.

#### What is a game engine
