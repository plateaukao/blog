+++
title = "How to find and turn on USB debugging mode in Android 4.2 and higher"
date = "2013-03-26T17:52:00Z"
slug = "how-to-find-and-turn-on-usb-debugging-mode-in-android-42-and-higher"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/03/how-to-find-and-turn-on-usb-debugging.html"
bloggerID = "2166939870867757991"
tags = ["Android"]
[cover]
  image = "/images/blogger/2166939870867757991/8582406602_2006f62370_b.jpg"
+++

[![](/images/blogger/2166939870867757991/8582406602_2006f62370_b.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQUQoysfpC0gcjBYUGXMkXuNYOAmZkh5kjpxUrbBvNPa2Pq-BynPaH2ebm5Y41tp2hpuDMCKrDeHtGtywdTElRPusPPw6gIZaG2dcRM7LxRsiMQzYccmURUalWnlywEcc11fN6xC2iutw/s1600/8582406602_2006f62370_b.jpg)

(Paris.France)  
Tranquille dans la ville de belle Paris.  
  
\*\*\*\*  

While trying a certain app recently released by a company that I had interviewed with, it crashed every time I triggered it. I wanna get the logs for them to do further investigation. Howevever, I couldn't find the developer option in my Galaxy Nexus with android 4.2.2. Not sure why; I did some search on the internet. Seemd that google thought it's not so useful for normal users so they just hide it from settings app by default. If this feature is required by developers or someone boring enough, just like me, they can always find the solution on the internet: You can enable/disable it whenever you desire by going to “Settings”
-> “Developer Options” -> “Debugging” ->” USB debugging”.

  
Voila, I can successfully get logs by using adb logcat now.  
  
REF:  
<http://dottech.org/87439/how-to-unlock-usb-debugging-mode-on-android-4-2-jelly-bean-and-higher-guide/>
