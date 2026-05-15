+++
title = "Installing LInux in BlueAngel"
date = "2005-12-20T13:47:00Z"
slug = "installing-linux-in-blueangel"
canonicalURL = "https://plateautip.blogspot.com/2005/12/installing-linux-in-blueangel.html"
bloggerID = "113508791048279724"
+++

If you just want to install linux on your BlueAngel, the only website you have to visit is [Handhelds.org](http://handhelds.org/moin/moin.cgi/BlueAngel). By following the instructions you will have an Embedded Linux ready in a SD card within half hour, including downloading kernel image and gpe image. Well except one strange problem that I encountered: if I try to partition the SD card into two primary partitions: one in fat16 and the other in ext3, BlueAngel can not find the SD card. Only after I partitioned it into one logical partition (fat16) and the other primary partition(ext3) did it work normally.  
  
It's pretty exciting when the system boots up in Linux. I played around for a while and started wondering if I can build an application on it (that would be much more interesting than just putting a fixed system inside). The processor of BlueAngel is ARM CPU, so programs have to be compiled by arm compiler or ... so-called cross compiler on other systems, for example, x86-based linux.  
  
The default GUI environment built for BlueAngel is GPE, so that's the start point that I look for a cross compiler. And with luck, I found it [here](http://handhelds.org/moin/moin.cgi/GpeCrossCompilation). Just download [gpe-sdk-20050210.tar.bz2](http://handhelds.org/%7Eflorian/sdk/gpe-sdk-20050210.tar.bz2), and extract it as root under the root directory, you will have the cross-compiler environment and all the gpe related libraries.  
  
Now, you can write a program for gpe, compile it, use scp to copy it into BlueAngel and run. That's it. Isn't it simple? :)
