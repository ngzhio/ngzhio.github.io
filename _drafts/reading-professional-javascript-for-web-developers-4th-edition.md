---
title: "Reading \"Professional JavaScript for Web Developers, 4th Edition\""
categories: [Notes, Programming]
tags: [javascript, programming language, web]
---

*Professional JavaScript for Web Developers* was originally written by [Nicholas C. Zakas](https://humanwhocodes.com/), but the author of the [4th Edition](https://www.wiley.com/en/Professional+JavaScript+for+Web+Developers,+4th+Edition-p-9781119366447) (2018) was changed to [Matt Frisbie](https://twitter.com/mattfriz).

![front cover](https://media.wiley.com/product_data/coverImage300/45/11193664/1119366445.jpg){: .align-right width="20%" }

## Chapter 1. What Is JavaScript?

JavaScript contains three parts:

- [ECMAScript](https://www.ecma-international.org/publications/standards/Ecma-262.htm), which is defined in ECMA-262 and provides the core functionality.
- The [Document Object Model (DOM)](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model), which provides methods and interfaces for working with the content of a web page.
- The [Browser Object Model (BOM)](https://en.wikipedia.org/wiki/Browser_Object_Model), which provides methods and interfaces for interacting with the browser.

## Chapter 2. JavaScript in HTML

As long as `async` and `defer` attributes are not used, all `<script>` elements are interpreted in the order in which they occur on the page.

`async` indicates that the script should begin downloading immediately but should not prevent other actions on the page such as downloading resources or waiting for othe scripts to load. It's valid only for external script files.

`defer` indicates that the *execution* of the script can safely be deferred until after the document's content has been parsed and displayed. It's valid only for external script files.

For nondeferred scripts, the browser must complete the interpretation of the code inside a `<script>` element before it can continue to render the rest of the page. For this reason, `<script>` elements are often placed after the main content of the page and just before the closing `</body>` tag.

## Chapter 3. Language Basics

### Strict Mode

ES 5 (2009) introduced the concept of *strict mode*. Strict mode is a different parsing and execution model for JavaScript, where some of the erratic behavior of ES 3 (1999) is addressed and errors are thrown for unsafe activities.

To enable strict mode for an entire script, include the following at the top:

```javascript
"use strict";
```

To enable strict mode just for a function, include it at the top of the function body.

### Variables

We use `var`, `let` or `const` to declare variables.

The `var` statement has a feature called *declaration hoisting*, where the interpreter pulls all variable declarations to the top of its scope. For example,

```javascript
function foo() {
    console.log(age);
    var age = 26;
}
foo(); // undefined
```

The above code may be equivalently interpreted as

```javascript
function foo() {
    var age;
    console.log(age);
    age = 26;
}
foo(); // undefined
```

`let` operates in nearly the same way as `var`, but with some important differences:

- `let` is block scoped, but `var` is function scoped.

    ```javascript
    if (true) {
        var age = 26;
        console.log(age); // 26
    }
    console.log(age);     // 26
    ```

    ```javascript
    if (true) {
        let age = 26;
        console.log(age); // 26
    }
    console.log(age);     // ReferenceError: age is not defined
    ```

- `let` does not allow for any redundant declarations within a block scope.

    ```javascript
    var age;
    var age; // OK
    ```

    ```javascript
    let age;
    let age; // SyntaxError: Identifier 'age' has already been declared
    ```

- `let` has the [*"temporal dead zone"*](https://stackoverflow.com/questions/33198849/what-is-the-temporal-dead-zone).

    ```javascript
    function foo() {
        console.log(age); // ReferenceError: Cannot access 'age' before initialization
        let age = 26;
    }
    foo();
    ```

    It seems that the `let` declaration isn't hoisted, but the truth is that it's hoisted. The interpreter marks the segment from the declaration to the initialization as the "temporal dead zone", in where any attempt to access the variable will throw a reference error.

    An evidence of hoisting:

    ```javascript
    let age = 25;
    function foo() {
        console.log(age); // ReferenceError: Cannot access 'age' before initialization
        let age = 26;
    }
    foo(); // undefined
    ```

    If the second `age` isn't hoisted, the `console.log` should print the first `age`, i.e. `25`. However, it still throws a reference error, that means the second `age` has been hoisted at the top of the function body of `foo`.

Maybe we don't need to remember all of these technical details. We just need to remember that **prefer to use `let` than `var`**. `let` makes code safer.

`const` behaves identically to that of `let` but with one important difference: It must be initialized with a value, and that value cannot be modified.

### Basic Data Types

### The `Object` Data Type

### Operators

### Functions
