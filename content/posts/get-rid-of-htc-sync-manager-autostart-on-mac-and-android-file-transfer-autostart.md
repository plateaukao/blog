+++
title = "Get Rid of HTC Sync Manager autostart on Mac, and Android File Transfer Autostart"
date = "2013-06-30T03:55:00Z"
slug = "get-rid-of-htc-sync-manager-autostart-on-mac-and-android-file-transfer-autostart"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/06/get-rid-of-htc-sync-manager-autostart.html"
bloggerID = "8739144520567435915"
[cover]
  image = "/images/blogger/8739144520567435915/1668067771_173f6fc4fb_b.jpg"
+++

[![](/images/blogger/8739144520567435915/1668067771_173f6fc4fb_b.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiL5ZOAIyF4bSa9vrrk70tSU6MHz8dS7Txdgzq9_DaPnbaKfx4fHSwVzP5l2cO7Mk9W601fV3X0-Hb5y1iJfF-9vfo60vo9fIXM_QDKvEfCQS5GJlx5PjLYGOGsgOloxOaPTUTSIF3RogE/s1024/1668067771_173f6fc4fb_b.jpg)

(Geneve.Swiss)  
  
Tired of seeing autostart finder popups every time I plugged in my new hTc one into my mac. Here's a way to disable it:  
1. Identify UUID:  
   by using "diskutil info /Volumes/HTC\ Sync\ Manager  
   you can get its volume UUID  
2. sudo vifs  
    add a line as below:  

```
UUID=YOURVOLUMEUUID none hfs rw,noauto
```

  
= = = = =  
As for disabling Android File Transfer app, you just need to rename file names of the so called Agent app:  
1. /Users/user\_name/Library/Application Support/Google/Android File Transfer  
2. /Applications/Android File Transfer.app/Contents/Resources  
  
REF:  
<http://blog.softwareispoetry.com/2013/05/disable-htc-syc-manager-autostarting.html>
