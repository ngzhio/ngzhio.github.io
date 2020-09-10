---
title: "Notes on \"Python Crash Course, 2nd Edition\""
categories: [Notes]
tags: [python, programming language]
---

Here are some notes I took on [Eric Matthes](https://ehmatthes.github.io/)' [*Python Crash Course*, 2nd Edition](https://nostarch.com/pythoncrashcourse2e) (2019).

## Table of Contents <!-- omit in toc -->

- [Part I. Basics](#part-i-basics)
  - [Chapter 2. Variables and Simple Data Types](#chapter-2-variables-and-simple-data-types)
    - [Variables](#variables)
    - [Strings](#strings)
  - [Chapter 3. Introducing Lists](#chapter-3-introducing-lists)
    - [Changing, Adding, and Removing Elements](#changing-adding-and-removing-elements)
    - [Organizing a List](#organizing-a-list)
  - [Chapter 4. Working with Lists](#chapter-4-working-with-lists)

## Part I. Basics

### Chapter 2. Variables and Simple Data Types

#### Variables

Creating a variable in Python is very simple. It doesn't need any keyword or type specifier, just assigning a value to a name:

```python
message = "Hello Python world!"
```

> Variables are often described as boxes you can store values in. This idea can be helpful the first few times you use a variable, but it isn’t an accurate way to describe how variables are represented internally in Python. It’s much better to think of variables as labels that you can assign to values. You can also say that a variable references a certain value.

It's better if the author can give some examples to explain the benefits of thinking variables as labels. Maybe he didn't want to make readers stuck in confusion too early.

#### Strings

The author introduced some methods of strings:

- Changing cases
  - [`title()`](https://docs.python.org/3/library/stdtypes.html#str.title)
  - [`upper()`](https://docs.python.org/3/library/stdtypes.html#str.upper)
  - [`lower()`](https://docs.python.org/3/library/stdtypes.html#str.lower)
- Stripping whitespaces
  - [`rstrip()`](https://docs.python.org/3/library/stdtypes.html#str.rstrip)
  - [`lstrip()`](https://docs.python.org/3/library/stdtypes.html#str.lstrip)
  - [`strip()`](https://docs.python.org/3/library/stdtypes.html#str.strip)

The algorithm used by `title()` defines a word as a group of consecutive letters. The implementation can be found in the [`_Py_bytes_title`](https://github.com/python/cpython/blob/a15e260b708a98edaba86a2aa663c3f6b2abc964/Objects/bytes_methods.c#L334) function in cpython.

### Chapter 3. Introducing Lists

#### Changing, Adding, and Removing Elements

Changing an element:

```python
names[2] = 'Alexander Huang'
```

Appending an element to the end of a list:

```python
names.append('Alexander Huang')
```

Inserting an element into a list:

```python
names.insert(2, 'Alexander Huang')
```

If we want to directly delete an element by its index, we can use `del`:

```python
del names[2]
```

If we want to remove an element from a list and then later use it, we can use the `pop()` method.

Removing the last element from a list:

```python
last_name = names.pop()
```

Removing an element at any position from a list:

```python
my_name = names.pop(2)
```

If we want to remove an element by its value, we can use the `remove()` method:

```python
names.remove('Alexander Huang')
```

**Note**: The `remove()` method deletes only the first occurrence of the value.

#### Organizing a List

Using the `sort()` *method* to permanently sort a list; Using the `sorted` *function* to get a sorted copy of the list.

### Chapter 4. Working with Lists
