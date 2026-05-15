+++
title = "Disable Photo Import in Ubuntu"
date = "2008-05-07T11:28:00Z"
slug = "disable-photo-import-in-ubuntu"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/05/disable-photo-import-in-ubuntu.html"
bloggerID = "420062382255909827"
tags = ["Computer", "Linux", "Olympus E510"]
[cover]
  image = "/images/blogger/420062382255909827/2472723803_047cdbb103.jpg"
+++

[![P5035504](/images/blogger/420062382255909827/2472723803_047cdbb103.jpg)](http://www.flickr.com/photos/plateau/2472723803/ "P5035504 by plateaukao, on Flickr")  
(Olympus E510 Marseille, France. Street)  
  
馬賽的道路有不少高低起伏的路段，還有很多單行道。在巷弄間開車應該很容易迷路吧。  
  
\*\*\*\*  
  
Every time I insert a SD card ( or CF card) into my Linux box, it shows up a "Photo Import" dialog to ask me if I want to import photos directly. However, I never used this function, so it turns out to be nothing more than an annoying notification.  
  
To my surprise, it's quite easy to turn it off (though you have to know how to do it). From the command-line, call gnome-volume-properties to set up attributes. One of the checkboxes is to allow you turn on/off this feature. Uncheck it, and it's done. No more un-necessary pop-ups. :)
