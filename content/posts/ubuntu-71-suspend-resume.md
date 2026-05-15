+++
title = "Ubuntu 7.1 Suspend / Resume"
date = "2008-05-16T20:15:00Z"
slug = "ubuntu-71-suspend-resume"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/05/ubuntu-71-suspend-resume.html"
bloggerID = "1124811954332874597"
tags = ["Linux", "Computer"]
[cover]
  image = "/images/blogger/1124811954332874597/2472434319_28700fae23.jpg"
+++

[![P5015257](/images/blogger/1124811954332874597/2472434319_28700fae23.jpg)](http://www.flickr.com/photos/plateau/2472434319/ "P5015257 by plateaukao, on Flickr")  
(Olympus E510 Avignon, France)  
  
亞維儂的教宗宮殿外，有街頭藝人在表演。老實說，她的joggling不是玩得很好。  
  
\*\*\*\*  
  
1.  
 sudo apt-get install uswsusp  
  
2.  
edit /etc/uswsusp.conf (use /dev/disk instead of UUID)  
resume device = /dev/disk/by-uuid/6d77e24a-79d3-425c-bac6-f875a3f35855  
splash = y  
compress = y  
early writeout = y  
#image size = 2.26133e+09  
RSA key file = /etc/uswsusp.key  
shutdown method = platform  
  
3.  
go to /etc/grub, edit menu.lst (make sure resume is there)  
  
 title Ubuntu 7.10, kernel 2.6.22-14-generic  
root (hd0,1)  
kernel /boot/vmlinuz-2.6.22-14-generic root=UUID=25d8c849-34b1-4009-81e1-d313a20844d7 resume=UUID=6d77e24a-79d3-425c-bac6-f875a3f35855 ro quiet splash  
initrd /boot/initrd.img-2.6.22-14-generic  
quiet  
  
4.  
Make sure the swap drive UUID is correct in this file /etc/initramfs-tools/conf.d/resume  
  
5.  
 sudo update-initramfs -u  
  
6.  
now, you can try:  
 sudo /sbin/s2disk  
  
REF:  
[ubuntuforums.org](http://ubuntuforums.org/showthread.php?t=745393&highlight=trying+t+resume+from)
