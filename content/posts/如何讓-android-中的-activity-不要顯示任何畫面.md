+++
title = "如何讓 Android 中的 Activity 不要顯示任何畫面"
date = "2014-06-22T03:08:00Z"
slug = "如何讓-android-中的-activity-不要顯示任何畫面"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2014/06/android-activity.html"
bloggerID = "3191908606506004196"
tags = ["programming", "Android"]
[cover]
  image = "http://3.bp.blogspot.com/-899VDUUPPQU/U6ZG46PQq8I/AAAAAAAA9YQ/XLkOcTeJ7h4/s1600/P6210357.JPG"
+++

[![](http://3.bp.blogspot.com/-899VDUUPPQU/U6ZG46PQq8I/AAAAAAAA9YQ/XLkOcTeJ7h4/s1600/P6210357.JPG)](http://3.bp.blogspot.com/-899VDUUPPQU/U6ZG46PQq8I/AAAAAAAA9YQ/XLkOcTeJ7h4/s1600/P6210357.JPG)

(ShinShan.Dream Lake.Taipei)  
  
北部難得可以找到人少一點的景點。  
之前來路跑竟然沒有看到。  
  
\*\*\*\*\*  
最近又在寫小 app，但總是在畫面上卡關，一直無法很順利的進行。  
今天早上起床，順手又改了幾個自己在使用上覺得不夠方便的地方，  
然後，就是這麼自然地，在網路上逛到了如何解決自己試了很久都沒成功的功能。  
  
根據 app 的需求，我在 AndroidManifest.xml 中透過 intent filter來接收某些事件。當事件發生時，被叫起的 Activity 其實並不需要顯示畫面，我只是要將事件再傳給 Servic，讓 Service 把事情處理掉。但是卻老是卡在 Activity 或多或少會秀一下白畫面，或黑畫面，或是閃一下，才會乖乖的不見。即使在 onCreate() 中呼叫了 finish()也解決不了這個問題。  
  
今天在網路上找到的解法，很簡單。只需要設定一個 theme 就好了。雖然這方法自己也試過，但應該是少了些什麼其他的設定吧。好吧，答案就是：  
  
            android:theme="@android:style/Theme.NoDisplay"  
  
REF:  
<http://stackoverflow.com/questions/4551868/how-to-completely-get-rid-of-an-activitys-gui-avoid-a-black-screen>
