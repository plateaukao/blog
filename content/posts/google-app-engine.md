+++
title = "Google App engine"
date = "2009-06-21T14:59:00Z"
slug = "google-app-engine"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/06/google-app-engine.html"
bloggerID = "5731819982353001912"
tags = ["Computer", "onlineDic", "Linux"]
+++

[![p7135683.jpg (by plateaukao)](/images/blogger/5731819982353001912/509462679_85de055413.jpg "p7135683.jpg (by plateaukao)")](http://www.flickr.com/photos/plateau/509462679/ "p7135683.jpg (by plateaukao)")  
Biei.Japan  
  

I forgot how I bumped into this site Google App engine. I saw there's a small youtube video at the right-hand side. Out of curiosity, I clicked on the video and gave it a gimplse. Wow, it's written in Python. That made me more interested in how it works. Within hours, I wrote my first google app based on its simple sample provided in the Google App Engine SDK. Hey, but it's already good enough to compete with my onlinedic!! The speed is amazing comparing to my desktop client. Instead of completing my first workable (and useful) android app, I ported my onlinedic to google apps. Well, I just changed the I/O part of my original python scripts. As for the html post-processing part, I did not change them at all.

  

Now, I have French-English dictionary, Yahoo Chinese-English dictionary, and French Conjugator ready on the internet! I can always have these basic function set as long as I have internet access.

  
Here are some notes about what obstacles I encountered while writing this small app.  
  
1. use python 2.5 instead of python 2.6  
If you are using python version other than 2.5, it'd better that you install python2.5 too.  
It will prevent you from bumping into a out-of-nowhere debugging error.  
(I spent some time on finding this out on my ubuntu 9.0)  
  
2. There's new\_project\_temple folder in the SDK root directory. That's where you can start with.  
  
3. Do not use urllib from python library. Use urlfetch from google.appengine.api instead.  
  
4. You can only upload/update your files to google app server, but you CANNOT download these files from the server!!  
So, remeber to back up your files and use version control systems by yourself.  
  
  
LINK:  
[http://onlinedict.appspot.com](http://onlinedict.appspot.com/)  
  
  
REF:  
<http://code.google.com/intl/zh-TW/appengine/>
