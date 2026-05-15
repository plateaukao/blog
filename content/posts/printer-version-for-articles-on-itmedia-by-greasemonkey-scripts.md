+++
title = "Printer version for articles on ITMedia by Greasemonkey scripts"
date = "2008-07-31T18:31:00Z"
slug = "printer-version-for-articles-on-itmedia-by-greasemonkey-scripts"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/07/printer-version-for-articles-on-itmedia.html"
bloggerID = "1558949171391854233"
tags = ["Computer", "Annecy Life"]
[cover]
  image = "/images/blogger/1558949171391854233/2223799982_e43a999855.jpg"
+++

[![P1210756](/images/blogger/1558949171391854233/2223799982_e43a999855.jpg)](http://www.flickr.com/photos/plateau/2223799982/ "P1210756 by plateaukao, on Flickr")  
Olympus E300  
Annecy.France  
2008.01.21  
  
早晨八點多醒來，看到窗外的天空顏色不太一樣，  
隨手拿起床邊的相機拍了幾張。  
然後，  
滿意地再回到睡夢中  
  
\*\*\*\*  
  
Wrote a small javascript for GreaseMonkey so that I can access printable version directly from the website of ITMedia.  
  

```
if(/itmedia.co.jp\/[\D\d]*\//.test(href) && /html/.test(href) && !/print/.test(href))  
   window.location.href = window.location.href + '\?print'
```
