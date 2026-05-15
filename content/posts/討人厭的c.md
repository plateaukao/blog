+++
title = "討人厭的C#"
date = "2009-01-11T16:56:00Z"
slug = "討人厭的c"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/01/c.html"
bloggerID = "7927525077702162668"
tags = ["Computer"]
[cover]
  image = "/images/blogger/7927525077702162668/365658742_8c6d4d1a1a.jpg"
+++

[![P6180111 (by plateaukao)](/images/blogger/7927525077702162668/2590215215_3252e94347.jpg "P6180111 (by plateaukao)")](http://flickr.com/photos/plateau/2590215215/ "P6180111 (by plateaukao)")  
Lac d'Annecy.France  
  
在安納西最後一個月坐上觀光船繞湖一週時拍的。  
  
[![DCP01031](/images/blogger/7927525077702162668/365658742_8c6d4d1a1a.jpg)](http://www.flickr.com/photos/plateau/365658742/ "DCP01031 by plateaukao, on Flickr")  
Taiwan  
  
盡國民應盡的義務時，拍的基隆嶼。   
  
\*\*\*\*  
  
上班時，為了讓自己在做一些事情時更有效率，或是減少copy paste的動作，  
特地寫了一個C#的小程式。  
一方面是為了熟悉這個語言（雖然到現在還是一點兒也不熟）；  
另一方面還是因為懶，懶得用C或C++撰寫。  
  
最近想把這工具拷貝到同事的電腦裡，讓他也可以用時，  
發現竟然執行時會有錯誤。  
一時之間我也不知道為什麼，也不行就耗在那兒。  
最後只好土法鍊鋼，還是用老方式，copy paste。  
  
之後就一直對這件事梗梗於懷。  
既然花時間寫了一個好用（至少我覺得好用）的東西，  
不能跟其他人分享實在是很可惜。  
  
所以這兩天特別再花了點時間，研究出到底是哪一次的更新所造成的問題。  
原來，是一個registry key啊～  
  
前不久有位同事寄了一篇好文章給大家，  
裡頭說明了如果在PC上的registry設定某一個鍵值，  
Windows Mobile Device在連上Activesync時就不會囉哩八唆，  
跳出對話視窗問你要不要這個那個的，  
它會直接以Guest的方式做連結。  
  
這對於在開發windows mobile程式有很大的幫助，  
因為我們通常一天要連activesync不下數十次。  
每次都要用滑鼠去取消建立partnership，累積下來的時間也是很可觀的。  
  
所以在知道這個訊息之後，我自然很高興的為我的小工具加上了這個功能，  
讓我可以很快的切換是不是要用Guest的方式連結我的Device。  
但是，在讀取registry key時，我用的API是OpenRegistryKey。  
當系統中不存在某個鍵時，OpenRegistryKey的回傳值是null。  
我卻沒有事先判斷回傳值，就直接去抓回傳值的Value。  
這樣的一個小疏忽，害我花了大半天的時間在trace問題所在。  
因為我的電腦上，已經建立了這個key，所以怎麼debug都不會失敗；  
而我手邊又沒有多餘的電腦，有灌好Visual Studio with C#，  
可以讓我做測試。  
  
終於在昨晚，我用家裡的電腦debug程式，才找到了因為registry key不存在的這個問題。  
寫程式，還是乖乖地在每個可能出錯的地方加上錯誤判斷才是正解啊。  
nullreferenceexception，希望以後不要再遇到你了。  
  
接下來，應該要試著把這支程式包個安裝檔。  
這樣子其他人比較會有想用的意願。
