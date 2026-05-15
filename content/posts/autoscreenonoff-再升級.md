+++
title = "AutoScreenOnOff 再升級"
date = "2014-07-22T15:00:00.001Z"
slug = "autoscreenonoff-再升級"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2014/07/autoscreenonoff.html"
bloggerID = "5027626825927423780"
tags = ["Computer", "Programming", "Android"]
[cover]
  image = "/images/blogger/5027626825927423780/5479178966_7069c28f5f_o.jpg"
+++

[![](/images/blogger/5027626825927423780/5479178966_7069c28f5f_o.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEil3UBhGHsgFo_2x5BBGgVhlNIGTrVc9zXdjYYTsavlC_K3tzjhakKbboVrJuWrIw56WrcOFEY4kMgz6OxJtHQpGlxGsndUzF5Iloo_oLw_gbR25LAXEnyqn0O8zf25P20SQpdDK9pUYNY/s1600/5479178966_7069c28f5f_o.jpg)

(Dansui.Taiwan)  
  
前幾天花了半天加入 app 黑名單的功能後，評價還不錯，至少止血了。今天趁著明天颱風要來早點回家，花了一個多小時，把一個單純的 screen off widget 給加了進去。  
  
花的時間比預料的快很多，因為本來在 notification 的互動中就已經有這個 intent 和處理邏輯在了，今天只是照著原本的 widget 再生一個出來，然後設定個 pendingIntent 給它，就收工了。  
  
另外，還隨手將 changelog 的輸出方式改了一下，改成每個版本都會是一個新的 string ，如果其他語言沒有翻譯的話，那自然會抓到預設英文的版本，省下我每次升級都要把同樣的字串貼到每個語系的changelog\_html中。
