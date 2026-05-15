+++
title = "Development on android"
date = "2010-02-23T18:14:00Z"
slug = "development-on-android"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2010/02/development-on-android.html"
bloggerID = "1948276915746663846"
tags = ["Online Dictionary", "Python", "Android"]
[cover]
  image = "/images/blogger/1948276915746663846/1988442594_283751c7d0.jpg"
+++

[![PB124730](/images/blogger/1948276915746663846/1988442594_283751c7d0.jpg)](http://www.flickr.com/photos/plateau/1988442594/ "PB124730 by plateaukao, on Flickr")  
Annecy.France  
  
看了點文件，想說就來寫寫東西吧，從最簡單的開始。  

之前在國外時，為了學法文，幫onlinedic寫了個Vocabulary Review的小程式在Windows Mobile上。讓自己可以用當時帶出去的dopod818加減看一下查過的單字。現在，當時的code已經都不見了，所以想說在android上也寫一個好了。反正onlinedic的export機制都還是okay的。

  

在寫程式時，也可以順便練習到android上的一些基本觀念，比方說：如何透過intent來叫起另一個activity；如果在叫起別的activity時，帶想要的參數給它；透過xml的UI建置方式，畫面橫轉正轉的處理；UI元件的動作指派；目錄結構的讀取，文字檔的讀取；簡單的webview應用；activity暫存狀態的記錄；功能權限的開啟；androidManifest.xml的基本設定；eclipse開發環境的熟悉等。

  

真的寫下去了，明明是個很簡單的程式，但也弄了一天多才寫好，花了許多時間在小細節上。如果不把除錯、追臭蟲方式弄熟，接下來的日子應該會很痛苦吧。

  
= = =  

如果有空的話，乾脆一不做二不休，把onlinedict也搬到android，這樣子就不用每次都要裝一堆字典了。在網路上找到open source，可以讀取stardict字典檔的程式，有空再研究吧。先記下link:

<http://code.google.com/p/toolkits/wiki/YAStarDict>  
  
另外，沒想到有人替eblib包了個python wrapper！！  

當初在onlinedict裡亂寫的鄨腳command line程式，應該可以用這個wrapper把它換掉吧，省下暫存文字檔輸入輸出的廢工。

也是…改天有空再試吧。  
Link: <http://code.google.com/p/pyeb/>
