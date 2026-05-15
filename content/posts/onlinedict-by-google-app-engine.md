+++
title = "onlinedict by google app engine"
date = "2010-03-04T23:47:00Z"
slug = "onlinedict-by-google-app-engine"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2010/03/onlinedict-by-google-app-engine.html"
bloggerID = "1742694637497403009"
tags = ["Python", "Online Dictionary"]
[cover]
  image = "/images/blogger/1742694637497403009/4405933201_fdbddd578f.jpg"
+++

[![PB173371](/images/blogger/1742694637497403009/4405933201_fdbddd578f.jpg)](http://www.flickr.com/photos/plateau/4405933201/ "PB173371 by plateaukao, on Flickr")  
Central Station.NYC.US  
  

I posted an [article](http://netherlandsdaniel.blogspot.com/2009/06/google-app-engine.html) about using Google App Engine in last June, and the experiment target is the onlinedict. Everything goes well and since onlinedict is originally written in python, the porting task is without any efforts.

  

However, there's one limitation of using Google App Engine: You can get your codes back from the server. You have to keep your codes somewhere. That's quite strange as a policy. I know it may be easier to control the whole system on google side, but as a user, it's troublesome ofr me because I am too lazy to my stuff in another source control website.

  

As a consequence, I lost my codes after re-installing OS on my nb for several times. Although my original work still runs well, it looks bad on all mobile devices. The words are too small to read. However, I don't have original codes anymore! no way to improve it at all!

  

Finally, I decided to rewrite it again,since this website should help me most on mobile devices. If the outlook on devices are bad, then it is somehow useless to me. Well, the first thing to do is study again how to apply the google app engine framework into my dictionaries. With the help of the tutorial, I quickly achieved what I have done last time: a working fr-en, ch-en dictionary, and, plus eijiro dictionary!

  

The most difficult part (not really difficult at all, I just don't know how to do) is to adopt some css style to make it look great on mobile devices. Well, I found a good refernce site: <http://building-iphone-apps.labs.oreilly.com/>. And, it's free!

  

Okay, after several hours of work, I am happy with my new dictionary now. The font size is good, the input control is at the right position, with some hints in the box. Three online dictionaries are available. It's time to go to sleep again~~

  

[![](/images/blogger/1742694637497403009/IMG_0475.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPhI6RCbwlfi5Y_pvRU52MGaw5u2GxVkH2k6Z295Kigz3NK1jnbawF4hTLn4chYRbkNB2DIJhyu2ZwD_ByODpTpcPhcnmQb7_0w19lnTwQiNrfAdt4eLpRniRy3AteQDqLxBV5fX8ItUs/s1600-h/IMG_0475.png)
