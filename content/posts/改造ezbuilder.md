+++
title = "改造EzBuilder"
date = "2008-05-08T22:52:00Z"
slug = "改造ezbuilder"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/05/ezbuilder.html"
bloggerID = "5333786204461389292"
tags = ["Computer", "Annecy Life", "Ricoh GRD"]
[cover]
  image = "/images/blogger/5333786204461389292/2475769322_6c040df8d8.jpg"
+++

[![R8071148](/images/blogger/5333786204461389292/2475769322_6c040df8d8.jpg)](http://www.flickr.com/photos/plateau/2475769322/ "R8071148 by plateaukao, on Flickr")  
(Ricoh GRD Nice, France)  
  
尼斯附近的小半島上，最長一條散步道，就長這樣。  
  
\*\*\*  
  
用EzBuilder來轉影音檔案到手持裝置上的效果很好。之前我都用它來轉些好東西到我的SONY Clie TH55上。  
  
最近在看法文電視時，常常會將影集或是電影錄下來，留著之後再重覆聽。不過我的電視棒附的PowerCinema能錄出來的檔案都超級大，一個多小時的節目至少都要錄上1GB到2GB。雖然我有帶外接硬碟來，但也不行這麼錄下去，所以有了轉檔的需求。  
  
首先使用的是Windows自附的Windows Encoder。不過這個Encoder只可以轉Windows自己的格式，再者介面複雜，雖然我不是不會用，但總覺得轉一個檔得要花好多步驟才可以完成，太累人了。所以我又再去研究了一下EzBuilder，發現它可以將檔案轉成rmvb檔(儘管慢到爆)。rmvb檔用來存這些影集再恰當也不過了，所以我開始了我的轉檔路程。  
  
EzBuilder的介面很簡單，是console模式的選單，只要選定profile，就可以開始進行轉檔。它會去一個MediaFile的目錄下找影音檔，轉好後會存到DoneFile目錄中。對於這一點我一直覺得很麻煩。通常錄好的影片我都會直接拷貝到外接硬碟去，以節省筆電的空間。然而當我要轉檔時，卻還得要把它再搬到筆電的硬碟上(MediaFile目錄中)，等到轉檔完成後，再特地從DoneFile目錄撈出轉好的檔案。  
  
久久做一次也就罷了，如果天天都要轉檔的話，就累人了。動輒2, 3 GB的檔案，光是移動就得花上不少時間，還增加不必要的硬碟讀取。所以今天上了EzBuilder的網站看了一下，發現它是Open Source的！！作者是用perl撰寫該程式，然後再將它轉成一般的執行檔。既然是一般的script檔，那我何不把它port成python，然後再隨我高興亂改一通呢？  
  
大一之後就再也沒碰過perl，不過這似乎不是個問題，反正script的寫法各家都大同小異。一邊看著EzBuilder的原始碼，一邊將它改成python的版本。裡面主要只有兩大部分，一個是UI的呈現(profile的選擇)，另一個是字幕的處理。第一個部分，我就照樣照句，轉成python；第二部分，則是直接跳過。反正我錄電視，不會有字幕檔的問題，所以先擱著不理。  
  
完成後，便針對礙眼的MediaFile做小變動。原先設計是所有在MediaFile目錄下的檔案會被做處理，我直接把它改成從console多個input，讓使用者可以輸入要轉檔的路徑和名稱。轉好的檔案也從原來的DoneFile目錄，改成輸出到原有檔案的目錄。  
  
這樣子看起來似乎沒有比較方便，不過，至少不用再手動把檔案拷貝到MediaFile中了。等哪天有心情，再把wxpython的drag and drop例子拿來套用，讓它支援多檔案拖拉的功能。  
  
Open Source萬歲 :)  
  
REF:  
[EzBuilder Official Site](http://abraxas.no-ip.org/%7Eabraxas/ezbuilder/)
