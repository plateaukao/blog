+++
title = "compilation of ebmodule succeeded!!"
date = "2008-05-26T00:31:00Z"
slug = "compilation-of-ebmodule-succeeded"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/05/compilation-of-ebmodule-succeeded.html"
bloggerID = "3598733203161694975"
tags = ["Annecy Life", "Linux", "Ricoh GRD", "Python"]
[cover]
  image = "/images/blogger/3598733203161694975/2518935133_9df74a407d.jpg"
+++

![](/images/blogger/3598733203161694975/2518935133_9df74a407d.jpg)  
(Ricoh GRD Morbihan Tour 2008, Annecy du 21 au 24 mai)  
  
一連好幾天，在Courrier和學校中間的大廣場有法國西北部旅遊推廣活動。除了很普通的旅遊簡介、講解和美食品嚐外；還有三十場的免費concert可以聽。這種好事法國人自然不會錯過。週六下午在臨時搭起的表演台前，坐滿也站滿了觀眾。有沒有發現？表演台看起來很像是台灣廟會搭的台子。  
  
\*\*\*\*  
  
[Last time](http://netherlandsdaniel.blogspot.com/2007/04/onlinedicepwing.html), I said that **ebmodule** is not compatible with current **eb library**, so I turned to modify the sample code of eb library and use a separate execution file for both linux and windows. Though it works smoothly for me, putting an extra program in the package is not what I really want it to be. Several days ago, I thought: since ebmodule couldn't work with **current** eb library, why not try using the old eb library with which it says it compiles.   
  
I downloaded eb library 0.3.1 from internet and compiled it. And then, I spent some time figuring out where to put eb headers / library in order to compile ebmodule module; and I modified ebmodule.c too because there're some errors about the static char arrays. Finally, the native python ebmodule module is GENERATED!! Well, what a success!! The README says it compiles with Python 1.5.2; however with Python 2.5, it can be compiled too.  
  
After some simple tests of the ebmodule, I am quite happy with it. From now on, I think I can provide more support for EPWING files (to start with, maybe I can put in "strict match", "prefix match", and "postfix"; and ... word list too).
