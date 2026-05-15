+++
title = "Optimize the battery usage in Ubuntu 9.04 on Asus eeepc 1000HE"
date = "2009-10-03T08:36:00Z"
slug = "optimize-the-battery-usage-in-ubuntu-904-on-asus-eeepc-1000he"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/10/optimize-battery-usage-in-ubuntu-904-on.html"
bloggerID = "14234448488943763"
tags = ["Linux"]
[cover]
  image = "/images/blogger/14234448488943763/2591007974_0c8b7be043.jpg"
+++

[![P6180097](/images/blogger/14234448488943763/2591007974_0c8b7be043.jpg)](http://www.flickr.com/photos/plateau/2591007974/ "P6180097 by plateaukao, on Flickr")  
Annecy.France  
  

Yesterday, I brought my eeepc to office. I wanna try link it to my big screen LCD and see how it works. If possible, I want to control my office notebook under ubuntu remotely. In this way, I can control the computer in the way I want it, and still, being able to access all the necessary apps in windows.

  

However, out of no reasons, when changing the xorg settings to adapt the LCD resolution, my compiz 3D effects are all gone. A bit panicked, I gave up this idea and back to my original work style.

  

In addition, I also found that the battery strength is much less than what I observed in windows xp. Even turning CPU to powersave mode, the indicator shows 4 hour usage at most. This is a big shock for me. The long battery usage of this model is the very reason I bought it. If this is broken in ubuntu, then I may need to consider going back to windows xp platform.

  

Fortunately, the problem is much easier to solve than I think. Thanks for the enormous eeepc users, the power usage under ubuntu is being improved continuously. And the patch/tool on the internet is already very stable. This problem can be solved by simply installing several packages. One thing to notice though, the battery monitor in ubuntu is not quite accurate. Don't trust it. Install powertop to get a better measurement and some hints are also available to tell you how to improve the battery usage.

  
Two packages I used for this problem:  
eeepc-acpi-utilities  
eeepc-tray  
<http://sourceforge.net/projects/eeepc-acpi-util/>  
[Introduction](http://www.fewt.com/2009/08/eee-pc-acpi-utilities-11-series.html)  
  
  
I also found another package that can help you to quickly toggle H/W modules (wifi, bluetoo, webcam, etc).  
[eee-control](http://greg.geekmind.org/eee-control/)  
  
Now, it's time surfing~~
