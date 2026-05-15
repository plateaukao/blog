+++
title = "Adding macros in Android Studio (Intellij) -- take Adding Javadoc comment for example"
date = "2013-06-07T08:30:00.001Z"
slug = "adding-macros-in-android-studio-intellij-take-adding-javadoc-comment-for-example"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/06/adding-macros-in-android-studio.html"
bloggerID = "1748540228898903991"
tags = ["Computer", "Android"]
[cover]
  image = "/images/blogger/1748540228898903991/2044875142_0f8379e836_o.jpg"
+++

[![](/images/blogger/1748540228898903991/2044875142_0f8379e836_o.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibpzsflGiBPNnQQ2NpLxoGr1vtuh3Rzn8oXb_9yPCTX4mnyAFiu5EXvhs54-F1PYsB_9LrzWXCVbNnB677Dqkd4Yhzwp141q-u8YFrigT6Eef8hwerigdH0FAp_mvMoRcdlV5FEQeXfTE/s1600/2044875142_0f8379e836_o.jpg)
(Geneve.Swiss)
Climbing is pleasant, but it leads you to better views.  
  

Some shortcuts can be integrated into ideaVIM, but some are more complicated and need other tricks to make it more handy. One of the technique is to use macros. As Mac's Automator, you can ask Intellij or Android Studio to record your actions, and make it available as a keyboard shortcut.

For example, if you want to add javadoc comment to a funtion, you need to move to the first line of a certain function, and type in **/\*\***. After pressing **Enter**, it will generate javadoc template for that specific function. Though it's already very convenient, it still takes time if you're not quite familiar with how to move the cursor to the first line of the function.

So, to add javadoc comment from anywhere in codes, you can record a macro to move to the first line of the func, and type /\*\* , and Enter for you. Here's the actions:

1. Start recording a a macro in ***Edit - Macros - Start Macro Recording***  
   1. Press Down
   2. Press Ctrl + Up
   3. Press ⌘ + Left
   4. Write /\*\*
   5. Press Enter
2. Stop the macro recording in ***Edit - Macros - Stop Macro Recording***
3. Give it a cool name

And then you can add a keyboard shortcut for this macro in Keymapping in Preferences.

REF:

<http://tobiassodergren.blogspot.tw/2012/05/adding-javadoc-to-method-in-intellij.html>
