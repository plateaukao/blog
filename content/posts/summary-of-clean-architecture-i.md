+++
title = "Summary of Clean Architecture (I)"
date = "2019-07-25T02:26:34.709Z"
description = "Part I"
slug = "summary-of-clean-architecture-i"
canonicalURL = "https://medium.com/@danielkao/summary-of-clean-architecture-i-910d1ebdc60b"
mediumID = "910d1ebdc60b"
[cover]
  image = "/images/910d1ebdc60b/1_rnOWr47Ytu91MtOhw6qLFw.png"
+++


![](/images/910d1ebdc60b/1_rnOWr47Ytu91MtOhw6qLFw.png)
*上高地。日本*

[Clean Architecture: A Craftsman's Guide to Software Structure and Design, First Edition](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/)

### Part I

writing working codes is easy; to write codes that are easy to maintain and extend is *really hard*.

### Ch1 What is Design & Architecture

In this book, **design and architecture means the same thing**: it’s simply a continuum of decisions from the highest to the lowest levels.

> The goal of software architecture is to minimize the human resources required to build and maintain the required system.

Cost per line increased dramatically if code is a mess.

- Tortoise and the Hare racing game

Conclusion: *the only way to go fast, is to go well.*

### Ch2 A Tale of Two Values

Every software system provides two different values: **behavior & structure**.

![](/images/910d1ebdc60b/1_yElCT6PoH6APSTO-luEprQ.png)
*Eisenhower’s Matrix*

> I have two kinds of problems, the urgent and the important. The urgent are not important, and the important are never urgent.

**it is the responsibility of the software development team to assert the importance of architecture over the urgency of features.**

### Part II

### Ch3 **Paradigm Overview**

**Structured Programming**: discovered by Dijkstra. Use *if/then/else* instead of *goto*. Discipline on direct transfer of control.

**OO Programming**: Discipline on indirect transfer of control.

**Functional Programming**: A functional language has no assignment statement. Discipline upon assignment.

**Removed goto statements, function pointers, and assignment.**

### Ch4 Structured Programming

Böhm and Jacopini proved that all programs can be constructed from just three structures: **sequence, selection, and iteration**.

Structured programming allows modules to be recursively decomposed into provable units, which in turn means that modules can be functionally decomposed.

Dijkstra once said, “Testing shows the presence, not the absence, of bugs.”

### Ch5 OO Programming

What is OO? One answer to this question is “The combination of data and function.” Another common answer to this question is “A way to model the real world.” ??!!

Three magic words: ***encapsulation***, ***inheritance***, and ***polymorphism***.

**Encapsulation**: programming language C can have good encapsulation too, and C++ broke it.

**Inheritance**: programming language C can do it too.

**Polymorphism**: You guess? Yes, we can do it in C too. The problem with explicitly using pointers to functions to create polymorphic behavior is that pointers to functions are *dangerous*.

Dependency Inversion

Conclusion: OO is the ability, through **the use of polymorphism**, to gain **absolute control over every source code dependency** in the system. It allows the architect to create a plugin architecture, in which modules that contain high-level policies are independent of modules that contain low-level details.

### Ch6 Functional Programming

Variables in functional languages *do not vary*.

**Why would an architect be concerned with the mutability of variables?** The answer is absurdly simple: All race conditions, deadlock conditions, and concurrent update problems are due to mutable variables.

**Event sourcing** is a strategy wherein we store the transactions, but not the state. When state is required, we simply apply all the transactions from the beginning of time.

**CRUD** to **CR** only in ideal case. No modifications anymore.

### PART III DESIGN PRINCIPLES

SOLID principles are explained.

**SRP:** The Single Responsibility Principle

**OCP:** The Open-Closed Principle

**LSP:** The Liskov Substitution Principle

**ISP:** The Interface Segregation Principle

**DIP:** The Dependency Inversion Principle

### Ch7 SRP: Single Responsibility Principle

- least well understood principle due to naming

> A module should be responsible to one , and only one, actor

**cohesive** (凝聚力): Something that is cohesive consists of parts that [fit](https://www.collinsdictionary.com/dictionary/english/fit "Definition of fit") together [well](https://www.collinsdictionary.com/dictionary/english/well "Definition of well") and form a [united](https://www.collinsdictionary.com/dictionary/english/unite "Definition of united") [whole](https://www.collinsdictionary.com/dictionary/english/whole "Definition of whole").

Cohesion is the force that binds together the code responsible to a single actor.

[Cohesive definition and meaning | Collins English Dictionary](https://www.collinsdictionary.com/dictionary/english/cohesive)

**Case 1: Accidental Duplication**

![](/images/910d1ebdc60b/1_09bfbt13d8qgOorHT8gtyQ.png)
*Employee is a class*

Employee violates SRP because these three methods are responsible for different actors. It might affect each other, if one of the functions wants to have some changes.

![](/images/910d1ebdc60b/1_Ur6p6P_Ubtc1ULmDjmG4_w.png)

> The SRP says to *separate the code that different actors depend on*.

**Case 2: Modifications on the same class at the same time**

**Solution**

1. Separate the Data
2. Use facade pattern
3. Use separate classes as facade for lesser functions

### **Conclusion**

At level of components: Common Closure Principle

At architectural level, it becomes the Axis of Change responsible for the creation of Architectural Boundaries.
