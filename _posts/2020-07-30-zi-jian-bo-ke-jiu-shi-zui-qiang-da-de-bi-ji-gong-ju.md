---
title: "自建博客就是最强大的笔记工具"
date: 2020-07-30 22:39:17 +0800
lang: zh-Hans
categories: [Essays]
tags: [blog, note-taking]
---

听说最近的 [Notion](https://www.notion.so/) 很火。据其官网宣称，Notion 是一款融合了笔记、任务、维基等功能的“多合一”笔记工具。“嗯，又冒出了一款笔记工具！”——当我第一次听到 Notion 时，我是这么想它的。[Evernote](https://evernote.com/)、[Leanote](https://leanote.com/)、[OneNote](https://www.onenote.com)、[Boostnote](https://boostnote.io/)……我们折腾过的笔记 App 还算少吗？为什么我们还需要一款新的笔记 App？为什么我们需要这些笔记 App？至少我不需要，因为我有自建博客。

让我们思考一些“灵魂拷问“：

1. 谁拥有数据？这些 App 以什么格式存储数据？万一维护这些 App 的公司倒闭了怎么办？我们的数据会卖给谁？我们还能解析这些数据吗？
2. 在编辑笔记的过程中遇到数据丢失怎么办？至少我在使用这些笔记 App 的过程中不止一次遇到过这种情况；这可能是 bug，可能会在未来的版本中被修复，但我可没有耐心等待。
3. 这些 App 支持我需要的功能吗？比如写代码、数学公式。

[纯文本](https://en.wikipedia.org/wiki/Plain_text)可以解决以上所有问题：

1. 纯文本不依赖于任何特定商业公司所制定的任何格式，随便用诸如 [Vim](https://www.vim.org/)、[Emacs](https://www.gnu.org/software/emacs/)、[VSCode](https://code.visualstudio.com/) 等一些文本编辑器即可打开、阅读、编辑。我相信，即使一百年后，这些纯文本依然可以被轻松解析。另外，纯文本就存储在我们的电脑硬盘中，所以可以确保是我们拥有这些数据，而不是任何商业公司。
2. 我们可以用例如 [Git](https://git-scm.com/) 这样的版本控制系统管理纯文本的修改记录，几乎不必担心数据的丢失；而且，使用 Git，我们可以将文本回退到之前的任意一次修改版本——据我所知，还没有哪一款笔记 App 拥有如此强大的功能。
3. 我们可以在纯文本中使用一些简单的标记语法——例如 [Markdown](https://daringfireball.net/projects/markdown/)——实现特定的语义。我们也可以在纯文本中潜入 [LaTex](https://www.latex-project.org/) 写作数学公式。

关于纯文本的强大威力，CM Smith 的博文 [*Why Geeks Love Plain Text (And Why You Should Too)*](https://www.lifehack.org/articles/technology/why-geeks-love-plain-text-and-why-you-should-too.html) 有更详细的介绍。

用纯文本写笔记，仅仅是构建笔记系统的第一步；将一份份纯文本文件零散地放置在我们的电脑中是不够的；我们还需要将纯文本转换为更便于我们阅读的形式。有许多静态网页生成器——例如 [Jekyll](https://jekyllrb.com/)、[Hugo](https://gohugo.io/)——可以轻松将纯文本转化为网页。它们支持的 categories 和 tags 功能可以将我们的笔记灵活地归类。最后，我们可以将我们的笔记发布到自建博客上，让所有人阅读、评论和指正我们的笔记。
