---
title: "Reading \"Professional C# 7 and .NET Core 2.0\""
categories: [Notes]
tags: [csharp, dotnet, programming language, computer science]
---

[*Professional C# 7 and .NET Core 2.0*](https://www.wiley.com/en-us/Professional+C%23+7+and+NET+Core+2+0-p-9781119449270) by [Christian Nagel](https://csharp.christiannagel.com/) was published in 2018.

![front cover](https://media.wiley.com/product_data/coverImage300/78/11194492/1119449278.jpg){: .align-right width="20%" }

I made a [playground](https://github.com/ngzhio/pro-csharp7) for this book.

## Part I. The C# Language

### Chapter 1. .NET Applications and Tools

#### .NET Core CLI

- Creating a console application named `HelloWorld`.

    ```shell
    dotnet new console --output HelloWorld
    ```

- Building the application.

    ```shell
    dotnet build
    ```

    It will generate a file named `HelloWorld.dll` in the path `bin/Debug/[target-framework]/`.

    We can also build a release version:

    ```shell
    dotnet build --configuration release
    ```

- Running the application.

    ```shell
    dotnet run
    ```

    However, in the production system, we don't use `dotnet run`. Instead, we use `dotnet` with the name of the library:

    ```shell
    dotnet bin/release/netcoreapp3.1/HelloWorld.dll
    ```

- Publishing the application.

    ```shell
    dotnet publish -f netcoreapp3.1 -c release
    ```

    The published package would be in the path `bin/Release/netcoreapp3.1/publish/`.

    The application can deliver the runtime with it, just add the following code into the project file:

    ```xml
    <PropertyGroup>
        <RuntimeIdentifiers>
            win10-x64;ubuntu-x64;osx.10.11-x64;
        </RuntimeIdentifiers>
    </PropertyGroup>
    ```

    Then run

    ```shell
    dotnet publish -c Release -r win10-x64
    dotnet publish -c Release -r osx.10.11-x64
    dotnet publish -c Release -r ubuntu-x64
    ```

### Chapter 2. Core C\#

#### Predefined Types

Values types include integers, floating-points, booleans, and characters.

{% include image.html name="integer-types.png" %}
{% include image.html name="floating-point-types.png" %}
{% include image.html name="decimal-type.png" %}

The `decimal` type is a high-precision floating-point type. It's suitable for financial calculations. But it's weird to name it "decimal", after all, all computers are based on binary systems.

{% include image.html name="boolean-type.png" %}
{% include image.html name="char-type.png" %}

Reference types include objects and strings.

{% include image.html name="reference-types.png" %}

#### Control Flows
