---
title: "InjectFix 爬坑笔记"
date: 2020-04-20 16:30:15 +0800
modified_date: 2020-04-28 00:24:44 +0800
lang: zh-Hans
categories: [Notes, Programming]
tags: [csharp, game, unity, hot-fix, injectfix]
---

[InjectFix](https://github.com/Tencent/InjectFix) 是腾讯开源的一个适用于 Unity 游戏线上 bug 修复的工具。

## 编译

在 Mac 平台上运行 `Source/VSProj/build_for_unity.sh` 进行编译。

这个脚本写得非常不灵活，你需要自己去修改这个脚本中的某些配置，如 Unity 程序路径 `UNITY_HOME`，还有编译器的路径 `GMCS`。`gmcs` 是一种 Mono C# 编译器的名字，在 Unity 2017 中，这个编译器位于 `$UNITY_HOME/Contents/Mono/bin/gmcs`；Mono 从 2.11 版本开始提供了一个新的统一编译器 `mcs`，在 Unity 2019 中，这个编译器位于 `$UNITY_HOME/Contents/MonoBleedingEdge/bin/mcs`。

编译得到一个库 `IFix.Core.dll` 和一个可执行工具程序 `IFix.exe`。需要把这两个文件拷贝到你自己的工程之中。

## 操作步骤

使用 InjectFix 修复线上代码包含两个步骤：

1. 每次发包时需要在 Unity 编辑器中点击菜单 InjectFix -> Inject 进行注入。
2. 发现线上版本存在 bug 之后，进入线上版本对应的代码库，修改需要修复的方法，并且给这个方法打上 `[Patch]` 标签。在 Unity 编辑器中点击菜单 InjectFix -> Fix；它会将打上 `[Patch]` 标签的方法编译为特殊格式的指令集，并将其放入到两份补丁 `Assembly-CSharp.patch.bytes` 和 `Assembly-CSharp-firstpass.patch.bytes` 之中。然后就可以将这两份补丁发布到资源服务器上供客户端下载了。

执行 Fix 的时候可能会遇到报错：

    Error: the new assembly must not be inject, please reimport the project!

这表明该工程已经注入过了，你需要删除 `Library` 文件夹，然后重新用 Unity 编辑器打开工程，再执行 Fix 步骤。

## 原理

InjectFix 实现 bug 修复主要靠这两部分：虚拟机负责新逻辑的解析执行；注入代码负责把调用重定向到虚拟机。

### 虚拟机

接入 InjectFix 时，应该在游戏开始后加载补丁：

```c#
var patch = Resources.Load<TextAsset>("Assembly-CSharp.patch");
if (patch != null)
{
    PatchManager.Load(new MemoryStream(patch.bytes));
}

patch = Resources.Load<TextAsset>("Assembly-CSharp-firstpass.patch");
if (patch != null)
{
    PatchManager.Load(new MemoryStream(patch.bytes));
}
```

`PatchManager.Load` 会创建一个虚拟机（`VirtualMachine`），并把加载的补丁代码传递给它。`VirtualMachine.Execute` 负责执行补丁代码中的指令，它的主流程如下：

```c#
public Value* Execute(Instruction* pc, Value* argumentBase)
{
    while (true)
    {
        switch (pc->Code)
        {
            case Code.Ldarg:
                // ...
                break;
            case Code.Call:
                // ...
                break;
            case Code.Newobj:
                // ...
                break;
            // ...
        }
    }
}
```

`pc` 指向某条指令，`argumentBase` 指向第一个参数。`switch` 根据不同的指令码做不同的运算。

关键的问题是：怎样将原来代码中某个方法的调用重定向到这个 `Execute` 之中，以执行新的逻辑呢？

## 参考

- [《腾讯正式开源面向 Unity 项目的 Bug 修复神器 InjectFix》](https://www.oschina.net/news/109803/injectfix-opensource)
