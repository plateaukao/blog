+++
title = "Sound Juicer"
date = "2008-03-18T09:32:00Z"
slug = "sound-juicer"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/03/sound-juicer.html"
bloggerID = "4069472024941546942"
tags = ["Computer", "Linux", "Olympus E510"]
[cover]
  image = "/images/blogger/4069472024941546942/2255415652_22e22533b1.jpg"
+++

[![P2091362](/images/blogger/4069472024941546942/2255415652_22e22533b1.jpg)](http://www.flickr.com/photos/plateau/2255415652/ "P2091362 by plateaukao, on Flickr")  
(Olympus E510 Lyon)  
  
到里昂那麼多次，終於有一次是好天氣。  
  
\*\*\*\*  
  
借來的Business French就要到期了，可是看沒幾課。  
想說先把CD拷一拷好了。  
在ubuntu下有Sound Juicer可以幫忙rip光碟，  
但是，預設模式下只有flac和ogg，  
我的mp3 player並不支援這兩種格式，  
所以我把profile改成mp3，可是卻不行運作。  
  
後來發現，我得要先自己灌上gstreamer-lame這個coder才行。  
然後再自己改改現有的mp3 profile，  
讓我可以用小一點的容量來rip。  
（因為是內容都是講話，所以並不需要用到44100KHz和128kbps的高規格）
