+++
title = "Unofficial Plurk API in Python : A Plurk client in wxpython - Plurkao"
date = "2009-06-14T22:58:00Z"
slug = "unofficial-plurk-api-in-python-a-plurk-client-in-wxpython-plurkao"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/06/unofficial-plurk-api-in-python-plurk.html"
bloggerID = "6395848871394136414"
tags = ["Computer", "Python"]
+++

[![PB124783 (by plateaukao)](/images/blogger/6395848871394136414/1986061121_1bfac55e7b.jpg "PB124783 (by plateaukao)")](http://www.flickr.com/photos/plateau/1986061121/ "PB124783 (by plateaukao)")  
Des feuilles.Annecy  
  

Originally, I wanna study how to write a small plug-in for Windows Live Messenger, so that every time a plurk alert comes, I can easily input the plurk id and username to reply the message. However, it turns out it's a hard work to do and there's no high-level wrappers for this task (please refer to [CodeProject: Windows Live Messenger Plug-in Development Bible. Free source code and programming help](http://www.codeproject.com/KB/macros/wlmplugin.aspx)). Moreover, I don't even have Visual Studio installed on my home computers. How can I compile my codes without a compiler.

  

After searching for a while, I gave up the idea of tweaking with Windows Live Messenger. Instead, I turned to search for plurk clients for desktop. Still, in vain. What I can only find is some air clients that use plurk mobile link internally, which I can already find a firefox extension for it. That interface is not intuitive enough for me. I need something more user friendly and not so error-prone as msn plurk alerts.

  

Well, the unofficial Plurk API in Python is what I found so far. On its website, the demo only shows how to display user's karma value and how to list your plurks. Hm.... it's not so attractive isn't it? But!!! indeed, the module does more than these two simple not so useful demonstrations!! You can send plurks, respond to existing plurks, get plurk permemant links, and etc. That's powerful enough to let me write my own plurk client. Yeah. You bet. I am gonna write one for myself if I have enough time.

  

Currently, there's only one API to get plurks which is called getPlurks( ). This API will get plurks no matter they are already read or not. I did a little modification now so that it can let you choose if you only want to list unread messages only.

  
Update (20090617)  
I wrote a small app with this python library. Currently it can merely work. The speed is slow, but it works somehow.  
  
And~~ the screenshots!  
  
1. Login UI: well, that's almost you need to login your account  
[![plurkao_login (by plateaukao)](/images/blogger/6395848871394136414/3633530820_1042da7eae_o.png "plurkao_login (by plateaukao)")](http://www.flickr.com/photos/plateau/3633530820/ "plurkao_login (by plateaukao)")  
  

2. Main Window: you can click on RealAll or UnRead to see the plurks. Send button allows you to post a new plurk. There's no auto update mechanism so far; you have to manually click on them when you want to see updates. And...the data fetch is done in the same thread so the UI will be a bit lagged when the button is pressed.

[![plurkao_plurks (by plateaukao)](/images/blogger/6395848871394136414/3633530864_3ddd91ffb4_o.png "plurkao_plurks (by plateaukao)")](http://www.flickr.com/photos/plateau/3633530864/ "plurkao_plurks (by plateaukao)")  
  
[![plurkao_plurks2 (by plateaukao)](/images/blogger/6395848871394136414/3633530940_7db25b1e1c_o.png "plurkao_plurks2 (by plateaukao)")](http://www.flickr.com/photos/plateau/3633530940/ "plurkao_plurks2 (by plateaukao)")  
  

3. Response Window:You can click on Inside to open up a new window which shows you the responses of the plurk. Refresh button will refresh the plurk for you (cause there's no auto update now); and the Send button will post a response to this plurk.

[![plurk_responses (by plateaukao)](/images/blogger/6395848871394136414/3632718867_e3002dca6c_o.png "plurk_responses (by plateaukao)")](http://www.flickr.com/photos/plateau/3632718867/ "plurk_responses (by plateaukao)")  
  
The UI is done by wxpython, so you have to install wxpython on your system if you want to test this program. And thanks for python's portability, I think it can run well under Linux too.  
  
DOWNLOAD:  
<http://daniel.kao.googlepages.com/plurkao.zip>  
  
REF:  
[David - The Unofficial Plurk API in Python](http://dblume.livejournal.com/109600.html)  
[Boa Constructor Download](http://boa-constructor.sourceforge.net/Download.html)  
<http://plurkapi.com/http/methods>

2010/02/17 補充：

既然有官方版的plurk api了，照例隨便玩玩看：

<http://netherlandsdaniel.blogspot.com/2010/02/plurkmonitor.html>
