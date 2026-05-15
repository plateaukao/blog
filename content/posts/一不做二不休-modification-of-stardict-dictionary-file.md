+++
title = "一不做二不休 modification of stardict dictionary file"
date = "2008-05-17T20:43:00Z"
slug = "一不做二不休-modification-of-stardict-dictionary-file"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/05/modification-of-stardict-dictionary.html"
bloggerID = "2583551067247184670"
tags = ["onlineDic"]
+++

[![p7135667 (by plateaukao)](/images/blogger/2583551067247184670/431946618_2ec77df921.jpg "p7135667 (by plateaukao)")](http://www.flickr.com/photos/plateau/431946618/ "p7135667 (by plateaukao)")  
(Biie, Hokkaide)  
  
一直很討厭在查單字時還要輸入法語的音符，雖然之前找到的輸入方式已經很簡單了，但是如果能夠只輸入一般英文字母就能查詢的話，不是很輕鬆嗎？  
  
要在某些地方偷懶，就要在其他地方付出。  
  
於是，我把Larousse的字典export出來，重新生出了新的字典，裡頭包含了單純字母組成的單字，然後在解釋部分，利用=>來指到原始的單字。另外在stardict.py裡頭，加上識別=>的程式碼。這麼一來，以後就可以只輸入字母查詢啦！  
  
原本Babylon格式的字典檔，也可以支援syncronym，不過我怎麼樣也試不成功，所以只好用自己爛爛的workaround。Anyways, it works now~~
