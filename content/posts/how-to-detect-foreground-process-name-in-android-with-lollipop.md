+++
title = "How to detect foreground process name in Android with Lollipop"
date = "2015-09-27T04:10:00Z"
slug = "how-to-detect-foreground-process-name-in-android-with-lollipop"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2015/09/how-to-detect-foreground-process-name.html"
bloggerID = "8280208682070887822"
tags = ["Programming", "Android"]
[cover]
  image = "/images/blogger/8280208682070887822/373538371_70f1fe9eeb_o.jpg"
+++

[![](/images/blogger/8280208682070887822/373538371_70f1fe9eeb_o.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiE7rekh_acf6kdfks1EOpt7yQ50k-xVE8KFuquLVQgkmgGY2N5fEAHT-kdlU6VWnkciKck4dtmcYJrmBX4ZvK_O1QqO_voyZlvujNF1FNFhfeQxedMyDrH0e5QNzj6GT9J6UoLOjg-Pc/s1600/373538371_70f1fe9eeb_o.jpg)

(Katwijk.Holland)
  
  
Android 一直改版，原本可以用的功能，因為安全性，因為有的 app 會亂搞，所以把許多流程和功能不是改得變複雜，就是直接拿掉了。  
  
原本一個很單純的抓取前景正在執行的程式名稱的功能，也變得愈來愈複雜。之前只需要抓一下getRunningTasks() 就可以找到想要的結果，但是現在得要為 application 加上新的 permission PACKAGE\_USAGE\_STATS，然後還要要求使用者進到 Settings > Security > User Apps with access to usage data , 勾選該 application 後才可以。  
  
這種小功能還需要使用者大費周章的做一堆事，實在是很麻煩。  
  
下面的程式碼，是透過 user stats去取得這資料。另外，如果使用者還沒有在 Settings 中勾選 app 的話，出來的 runningTask 會是空的，這時應該要用程式碼中最下面的 startActivity 去把設定的畫面叫起來，叫使用者打勾。使用者不打勾，你還是抓不到資料的。
