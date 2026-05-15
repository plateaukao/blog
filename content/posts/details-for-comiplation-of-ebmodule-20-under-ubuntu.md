+++
title = "Details for comiplation of ebmodule-2.0 under ubuntu"
date = "2008-05-26T09:11:00Z"
slug = "details-for-comiplation-of-ebmodule-20-under-ubuntu"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/05/details-for-comiplation-of-ebmodule-20.html"
bloggerID = "1911249131889135482"
tags = ["Computer", "onlineDic", "Linux", "Ricoh GRD"]
[cover]
  image = "/images/blogger/1911249131889135482/2421215845_6324fb7a73.jpg"
+++

[![RIMG0368](/images/blogger/1911249131889135482/2421215845_6324fb7a73.jpg)](http://www.flickr.com/photos/plateau/2421215845/ "RIMG0368 by plateaukao, on Flickr")  
(Ricoh GRD Semnoz, Annecy, France)  
  
滑雪滑到一半遇上大雪，多少會讓人覺得很掃興。  
買的是一日券，少溜愈多虧愈多。  
看著屋外一字排開的滑雪用具和空蕩蕩的桌椅，  
還是快進到餐廳裡取暖吧。  
  
\*\*\*\*  
  
I need to write it down here to prevent that some day my no-so-working brains forget how I did it. Actually it's not so complicated. Here's the steps:  
  
1. download eb-3.1.tar.gz and compile it. You will find dynamic libraries under eb/.libs and zlib/.libs.  
2. download ebmodule-2.0. Modify setup.py and ebmodule.c  
2.1 change library path and include path to where you put eb libraries and eb headers.  
2.2 modify ebmodule.c. The "static char" is not well written. So gcc will complain about it. You have to modify all the "static char".  
2.3 compile! Voila. If everything goes fine, you can test your eblib.py or test.py.  
  
I uploaded a modified version of ebmodule-2.0 (compiled python lib included) to my googlepage. You can find everything you need in the file to start programming with ebmodule. Have fun!  
  
  
REF:  
[EB Library](http://www.sra.co.jp/people/m-kasahr/eb/)  
  
DOWNLOAD:  
[compiled ebmodule-2.0 module and modified source codes](http://daniel.kao.googlepages.com/ebmodule-2.0-modified.tgz)
