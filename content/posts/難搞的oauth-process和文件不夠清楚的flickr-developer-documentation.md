+++
title = "難搞的oAuth Process和文件不夠清楚的flickr Developer Documentation"
date = "2013-02-20T08:01:00.001Z"
slug = "難搞的oauth-process和文件不夠清楚的flickr-developer-documentation"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/02/oauth-processflickr-developer.html"
bloggerID = "6270304994648693634"
tags = ["iOS", "programming"]
[cover]
  image = "/images/blogger/6270304994648693634/197084726_44e5127d95_o.jpg"
+++

[![](/images/blogger/6270304994648693634/197084726_44e5127d95_o.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUwDDiP6tXiXeCalEFbCDyHws-o51nXfHedo_05V1O_lorhaZ9aG8zCFHavd89UZcSlYhLVNBWbugPWnKY-367BgHs4cesl-y_4-MxLP2THz5kE89Fz_PpybAYTLsT0FPpiz0QAaAotgc/s1600/197084726_44e5127d95_o.jpg)

(JingMei Bridge.Taipei)  
  
試圖為抓下來的圖片加上一個tag，查了flickr api dev guide，對於這種request應該要使用post method才行。可是flickr上的api explorer還是用舊的token方式，而api說明頁又說得不清不楚，只說舊版的token要deprecated，要用新版的oAuth。卻沒說清楚oAuth的signature要怎麼生出來。  
  
後來又回頭看了幾次oAuth signature的生法，並且在我原本找來做oAuth認識的class中找到相關的code；這才把它們改了一下搬到我需要的logic中。  
  
結果發現用post method還是會有問題，可是我把整串request直接貼給browser竟然可以了！這是說如果用oAuth機制的話，不需要用post method也可以嗎？那我又何必大費周章的去改用NSURLConnection呢？再改回原本的[NSString URLWithString]]就好了。  
  
REF:  
[gitk documentation](http://lostechies.com/joshuaflanagan/2010/09/03/use-gitk-to-understand-git/)   
[oAuth 簡介](http://www.slideshare.net/Blaine/oauth-presentation)
