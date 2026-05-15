+++
title = "pebble 初體驗"
date = "2014-08-07T16:57:00Z"
slug = "pebble-初體驗"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2014/08/pebble.html"
bloggerID = "2824160816506306488"
tags = ["Pebble"]
[cover]
  image = "/images/blogger/2824160816506306488/1986083479_ea2b59638b_o.jpg"
+++

[![](/images/blogger/2824160816506306488/1986083479_ea2b59638b_o.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-PY_tgYvV81fEpAHf7u9tA_wMa43u8cxzsdLSMBChKolENcJzWk_R7Bvm1irWhEf5qhs1eI7lkONQpWxRN_dh4Hta72WvkcxBLoUmVd8539ib44mQS8VigVnEB-DUoRjUMflIr7VMBrs/s1600/1986083479_ea2b59638b_o.jpg)

  
好像國內都沒有什麼相關的說明， Google 一找全是對岸或香港的文章。  
所以，如果有什麼心得的話，偶爾還是來留點記錄好了。  
  
單純手機跟 pebble 的連結應用，目前已經有不少了，  
畢竟， pebble 出來好像也有一陣子了。  
但是，在與 Mac 端的連結應用就沒那麼豐富，  
目前只找到 libpebble 比較完整，  
透過 python script 可以讓 Mac 經由藍芽連結到 pebble，  
進而發送訊息到手錶上，或是用手錶來控制 Mac 上的 Application。  
  
我抓的這版 libpebble 已經有處理 Keynote 和 iTunes，  
後來我又加上了比較常用的 Powerpoint 和 Spotify，  
方便我在床上的時候，可以隨時開關 Spotify 的播放。  
  
Mac Application  的操作其實是透過 Music app on pebble 的介面來完成的，  
所以能按的鍵不多。  
然後在 Mac 上要寫一寫 button 對應的 osascript 行為。  
換句話說，只要 osascript 做得到的，就可以讓 pebble 來驅動。  
  
目前就完成到這樣，還沒有想到什麼其他好玩的應用。
