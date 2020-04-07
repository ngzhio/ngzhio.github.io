---
title: "Notes on \"Pro Git, 2nd Edition\""
categories: [Notes, Reading, Computer]
tags: [git]
---

[*Pro Git*, 2nd Edition](https://git-scm.com/book/en/v2) (2014) by [Scott Chacon](https://twitter.com/chacon) and [Ben Straub](https://twitter.com/benstraub) is the book suggested by [the Git official website](https://git-scm.com/), so we may call it the "Git Bible". It's available online and free to read.

![front cover](https://git-scm.com/images/progit2.png){: .align-right width="25%" }

## Chapter 10. Git Internals

> Git is fundamentally a content-addressable filesystem with a VCS user interface written on top of it.

### 10.1 Plumbing and Porcelain

> When you run `git init` in a new or existing directory, Git creates the `.git` directory, which is where almost everything that Git stores and manipulates is located.

The `.git` directory contains four core parts:

- `HEAD`, a file points to the branch you currently have checked out.
- (yet to be created) `index`, a file where Git stores your staging area information.
- `objects`, a directory stores all the content for your database.
- `refs`, a directory stores pointers into commit objects in that data (branches, tags, remotes and more).

### 10.2 Git Objects

Git is a content-addressable filesystem, that means the core of Git is a simple key-value data store. What this means is that you can insert any kind of content into a Git repository, for which Git will hand you back a unique key you can use later to retrieve that content.

The command [`git hash-object`](https://git-scm.com/docs/git-hash-object) computes checksums for contents we feed into Git. For example,

```shell
$ echo 'test content' | git hash-object -w --stdin
d670460b4b4aece5915caf5c68d12f560a9fe3e4
```

`-w` tells Git also store the object into the database (`.git/objects/`); `--stdin` tells Git read data from the standard input. This object type is called *blob*.

The command [`git cat-file`](https://git-scm.com/docs/git-cat-file) can let us retrieve the content back through the key:

```shell
$ git cat-file -p d670460b4b4aece5915caf5c68d12f560a9fe3e4
test content
```

We can also feed the content from a file:

```shell
$ echo 'version 1' > test.txt
$ git hash-object -w test.txt
83baae61804e65cc73a7201a7252750c76066a30
$ echo 'version 2' > test.txt
$ git hash-object -w test.txt
1f7a7a472abf3dd9643fd615f6da379c4acb3e3a
```

#### Tree Objects

*Tree* objects in Git correspondes to UNIX directory entries. A single tree object contains one or more entries, each of which is the SHA-1 hash of a blob or subtree with its associated mode, type, and filename.

Git normally creates a tree by taking the state of `index`. So, to create a tree object, we have to first update `index`. We use [`git update-index`](https://git-scm.com/docs/git-update-index) to update `index`, for example,

```shell
$ git update-index --add --cacheinfo 100644 \
  83baae61804e65cc73a7201a7252750c76066a30 test.txt
```

`100644` means it's a *normal file*; Other options are `100755`, which means it’s an *executable file*; and `120000`, which specifies a *symbolic link*.

`83baae61804e65cc73a7201a7252750c76066a30` is the key of the blob `version 1`, that means `test.txt` is the entry of the blob.

Now we can write the tree by running [`git write-tree`](https://git-scm.com/docs/git-write-tree):

```shell
$ git write-tree
d8329fc1cc938780ffdd9f94e0d364e0ea74f579
```

Let's see the tree object:

```shell
$ git cat-file -p d8329fc1cc938780ffdd9f94e0d364e0ea74f579
100644 blob 83baae61804e65cc73a7201a7252750c76066a30      test.txt
```
