+++
title = "improvement of &quot;Random Flickr Photos&quot; in C#"
date = "2008-06-16T20:56:00Z"
slug = "improvement-of-quotrandom-flickr-photosquot-in-c"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/06/improvement-of-flickr-photos-in-c.html"
bloggerID = "1654866620253748405"
tags = ["Computer", "Python", "Canon S30"]
[cover]
  image = "/images/blogger/1654866620253748405/373351560_410afe3bd0.jpg"
+++

[![img_4028](/images/blogger/1654866620253748405/373351560_410afe3bd0.jpg)](http://www.flickr.com/photos/plateau/373351560/ "img_4028 by plateaukao, on Flickr")  
Canon S30  
2004.04.15  
Keukenhof tuin  
  
荷蘭的庫肯霍夫花園，除了有各式各樣的鬱金香外，  
其實還有許多特別的花可以欣賞。  
  
\*\*\*\*  
  
Added features:  

1. modified the output html codes so that the title and the taken date of the photo will be shown when mouse is hovered over the photo.

2. moved interactions with flickr service into a thread so that it won't hang the whole application

3. every time the photo search is done, display the html results correspondingly, so that it won't take too long to show the results

  

A new class is created to do the time-consuming job. webbrowser is passed to it as a reference, so that it can set up DocumentText when it wants. To use pass by reference feature in C#, a "**ref**" keyword should be added in the function declaration and when being used.  
  
\*\*\*\*  
  
The launch look-up in the web browser function in onlinedic is broken for a while. Since I don't use this feature often, I did not care about it. The other day, I found that there's a good module in emesene just for the purpose as I want! It's called desktop.py. emesene uses it to determine the current system and choose the right web browser for you. With this module, what I need to do is nothing but copy the desktop.py and call a method!  
  
 `import desktop  
desktop.open('url_name')`
