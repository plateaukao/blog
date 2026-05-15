+++
title = "tweaking with Asus S200"
date = "2008-03-24T23:18:00Z"
slug = "tweaking-with-asus-s200"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/03/tweaking-with-asus-s200.html"
bloggerID = "3796098759075839895"
tags = ["Linux", "Computer"]
[cover]
  image = "/images/blogger/3796098759075839895/2349739236_5fbdfddf48_o.jpg"
+++

[![P2252737](/images/blogger/3796098759075839895/2349739236_5fbdfddf48_o.jpg)](http://www.flickr.com/photos/plateau/2349739236/ "P2252737 by plateaukao, on Flickr")  
(Italie.Venice)  
  
Searched some information on the internet to better utilize the 128 RAM on my s200.  
Firstly, I turned off GDM service.  
Instead, startx is executed (with icewm window manager) from command line,  
everytime I turn on my s200.  
It's said that GDM consumes quite some memory usage.  
Secondly, I commented unnecessary ttys.  
In general, one tty is enough for me.  
Nevetheless, I kept two, just in case.  
  
For improving the startup time, I turned off usplash too,  
by modifying menu.list of grub service.  
  
Now life's getting better with s200.  
  
However, once firefox is launched, the hdd keeps making noise all the time.  
only 128MB..... still a pain in the xxx.
