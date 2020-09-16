---
title: "解决中国境内在某些网络环境下无法访问 github.io 的问题"
date: 2020-09-03 01:01:04 +0800
last_modified_at: 2020-09-16 18:33:27 +0800
lang: zh-Hans
categories: [Notes, Tech]
tags: [github, github-pages, internet, dns]
---

[GitHub Pages](https://pages.github.com/) 是 [GitHub](https://github.com/) 提供的一个网页寄存服务，于 2008 年推出。它可以用于存放静态网页，包括博客、项目文档，甚至整本书。它的默认域名是 `github.io`。然而大约从今年 6 月份开始，`github.io` 这个域名在**中国境内的某些网络环境下**就无法访问了。经检查，是因为某些 DNS 服务器将这个域名解析到了 `127.0.0.1` 这个 IP 地址；具备一定计算机知识的人都知道，这个 IP 地址表示“此计算机”，所以我们访问 `github.io` 就变成了访问自己的计算机，结果当然是无法打开挂在 GitHub Pages 上的网站。

目前尚不知这是事故还是有意为之。似乎不是 [GFW](https://zh.wikipedia.org/wiki/%E9%98%B2%E7%81%AB%E9%95%B7%E5%9F%8E) 的所作所为，因为这种手段太低级了，低级到我们不需要“翻墙”就能解决这个问题。思路也很简单：既然某些 DNS 服务器错误解析了 `github.io`，那我们**换个新的 DNS 服务器**就行了；换成国外的。这里推荐 [Google Public DNS](https://developers.google.com/speed/public-dns) `8.8.8.8`，还有 [OpenDNS](https://www.opendns.com/) `208.67.222.222`。

下面展示如何在 iPhone 上修改 DNS 服务器。

- 1）进入**设置->无线局域网**界面，点击**连接的 WiFi**。
  
  {% include image.html src="assets/img/posts/jie-jue-zhong-guo-jing-nei-zai-mou-xie-wang-luo-huan-jing-xia-wu-fa-fang-wen-github-io-de-wen-ti/471599064709_.pic-min.jpg" width="40%" %}

- 2）点击**配置 DNS**。

  {% include image.html src="assets/img/posts/jie-jue-zhong-guo-jing-nei-zai-mou-xie-wang-luo-huan-jing-xia-wu-fa-fang-wen-github-io-de-wen-ti/461599064709_.pic-min.jpg" width="40%" %}

- 3）改**自动**为**手动**。
  
  {% include image.html src="assets/img/posts/jie-jue-zhong-guo-jing-nei-zai-mou-xie-wang-luo-huan-jing-xia-wu-fa-fang-wen-github-io-de-wen-ti/451599064709_.pic-min.jpg" width="40%" %}

- 4）删掉旧的 DNS 服务器地址，换成新的。

  {% include image.html src="assets/img/posts/jie-jue-zhong-guo-jing-nei-zai-mou-xie-wang-luo-huan-jing-xia-wu-fa-fang-wen-github-io-de-wen-ti/441599064708_.pic-min.jpg" width="40%" %}
