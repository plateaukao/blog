+++
title = "好用的id3tag轉換工具"
date = "2006-03-29T05:28:00Z"
slug = "好用的id3tag轉換工具"
canonicalURL = "https://plateautip.blogspot.com/2006/03/id3tag.html"
bloggerID = "114361038298933260"
+++

在linux下的mp3 player大部分都是把id3tag當成unicode來讀，但是大部分mp3的id3tag似乎都是用big5或是大陸編碼在存的，所以老是會看到一堆亂碼。  
  
剛剛找了一下，看有沒有現成的工具可以把id3tag轉成unicode，好讓linux下的mp3 player可以順利地顯示資訊。果然，有需求的東西，就會有人寫出來。  
  
找到一個工具叫做[Unicode Rewriter](http://unicoderewriter.sourceforge.net/)，是個用java寫成的小工具，不過，它運做得很好，把我大部分的id3tag都成功地轉對了。  
  
用法也很簡單，安裝好後，只要在開啟的GUI畫面中，先設定要搜尋mp3的目錄，和原始mp3中id3tag的編碼，就可以讓它乖乖地幫你轉啦。
