+++
title = "The long way to port my onlinedic on Android platform"
date = "2009-06-10T17:06:00Z"
slug = "the-long-way-to-port-my-onlinedic-on-android-platform"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/06/long-way-to-port-my-onlinedic-on.html"
bloggerID = "4504508365512682395"
tags = ["Food", "Android"]
+++

[![P5045763 (by plateaukao)](/images/blogger/4504508365512682395/2483722738_297a56f4b8.jpg "P5045763 (by plateaukao)")](http://www.flickr.com/photos/plateau/2483722738/ "P5045763 (by plateaukao)")  
Cannes.France  
  
坎城除了大家比較熟悉的海邊的星光大道外，  
其實在車站的另一個方向有個舊城區。  
  
跟海邊的人潮比起來，  
這兒顯得寧靜許多（不過沒有上空美女就是了。  
看著清一色的橘紅色屋頂和遠方的山水，晒著不會太炙熱的陽光，  
這兒真的很適合度假。  
難怪在Bienvenue chez les Chi'tis裡的那個老婆，那麼想要搬到法國南部；  
而在南法，特地搬來這兒住的英國人也是屬一屬二多的。  
  
\*\*\*\*  
  
After glancing through the basic documents of Android SDK, I still have a lot of work to do before porting my onlinedic to this platform:  
  
1. Find the UI components that I need:  
1.1 EditControl  
1.2 Button (for start searching)  
1.3 HTML viewer  
2. How to create and use its menu  
3. Find the component to open http requests  
4. Find the component to post-process the received html file  
  
  
As for item 1, it's not so difficult because the UI components I need are few.  
Except for the 1.3 HTML viewer, I spent some time to make it work.  
  
First of all, the component to display html content on android is  
android.webkit.WebView  
You can create this component in the resource and find it by id in the java source code.  
  
Secondly, you need to add a permission line in the Manifest xml file in order to have the access to load URLs.  
<uses-permission android:name="android.permission.INTERNET" />  
  
Since I will only use this component to display the processed results of the html, I don't have to study too much about what actions it supports.  
  
As for 2, 3, and 4, I will update later once I know how to accomplish them.  
  
voila, here's the result of today's work:  
  
[![IMAG0427 (by plateaukao)](/images/blogger/4504508365512682395/3613651717_0c69df5d5d_m.jpg "IMAG0427 (by plateaukao)")](http://www.flickr.com/photos/plateau/3613651717/ "IMAG0427 (by plateaukao)")  
  
\*\*\*\*  
  
好久沒到韓風饌吃東西了。  
久久吃一次也是不錯的。  
新拿到的傢伙太大隻了。  
拍起照來手會不穩。  
不過，看電子書應該很過癮吧。  
  
[![IMAG0319 (by plateaukao)](/images/blogger/4504508365512682395/3614193872_a9be25accf_m.jpg "IMAG0319 (by plateaukao)")](http://www.flickr.com/photos/plateau/3614193872/ "IMAG0319 (by plateaukao)")
