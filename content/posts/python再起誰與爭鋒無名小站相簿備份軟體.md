+++
title = "Python再起，誰與爭鋒：無名小站相簿備份軟體"
date = "2009-06-14T07:00:00Z"
slug = "python再起誰與爭鋒無名小站相簿備份軟體"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/06/python.html"
bloggerID = "1655055064661711195"
tags = ["Computer", "Python"]
+++

[![PB124784 (by plateaukao)](/images/blogger/1655055064661711195/1986083479_db8cba5fbb.jpg "PB124784 (by plateaukao)")](http://www.flickr.com/photos/plateau/1986083479/ "PB124784 (by plateaukao)")  
Autumn.Annecy  
  

這篇雖然是電腦文，不過因為國外連進來的，可能對這篇也不會感興趣，所以破例用中文寫囉。無名小站前陣子因為取消一些服務，搞得民怨四起(好像不是一直都這樣？)，鬧得很多人都要出走。要搬家的話，問題就來了：經年累月留下來的文章和照片，要怎樣搬到其他部落格去呢？關於文章、留言的部分，各家部落格其實都有提出類似的服務，可以讓使用者無痛搬家；但是對於相簿這塊，目前網路上找得到的軟體大都是專門設計來下載正妹照片用的，對於相簿中的標題和詳細描述，都沒有另外處理。也就是說，你搬得了照片，搬不了照片的字。

  

所以，昨晚我研究了一下網路上關於無名小站相簿原始檔格式的說明和網頁間的關連，寫了一小支程式可以把單一個相簿的相片抓下來，並且把照片和文字同時放進一個html檔。這麼一來，至少自己可以有一份相片和說明在一起的備份，就算不行匯到別的部落格去，也可以在自己的電腦上看爽的。等哪天有哪個部落格支援匯入照片和文字說明時，要再匯入也不會是件難事。

  
接下來是在寫這支python script時，需要注意的一些問題，和特別查到的資詢：  
1. URL request時的Referer：無名小站從以前就一直被人垢病相簿不行外連，因為在抓圖時，它會檢查這個request是從哪發來的。為了要順利抓到照片，在程式裡必須塞一個假的，可以通過它檢查的網址給它。如此一來，就不行用單純的urllib完成，而得改用urllib2才行。  

```
def GetURLContent(u):  
   req=urllib2.Request(url=u)  
   #req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6) Gecko/20040113')  
   req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.9.0.11) Gecko/2009060215')  
   req.add_header('Referer','http://www.wretch.cc')  
   return urllib2.urlopen(req)
```

  
如上，先在request中加上Referer的header就可以了。  
  

2. 在網頁的原始碼中，主要有三個tag是我們要抓的：DisplayTitle, DisplayImage, DisplayDesc；然後還有一個id="next"要抓。DisplayTitle是使用者設定的照片標題；DisplayImage該行有照片的真正路徑；DisplayDesc就是使用者可以寫得落落長的照片描述；id="next"則是用來檢查還有沒有下一張圖片，有的話，程式得要一路再抓下去，直到沒有下一張。

  
3. 抓的時候，記得要設一下sleep，不然抓太頻繁好像會被擋掉。所以每抓一張就加個sleep(10)或sleep(20)讓它休息一下。  
  
4. 原本有打算把描述和標題塞到jpeg的exif裡頭的，可是編碼問題一直搞不定，所以算了。因為加了，一般的image viewer也看不到。  
  
5. 用urllib2抓下image後，可以用read()讀出image的內容；存檔時記得開檔要用"wb"的flag，這樣子存出來的照片才能看。  
  
6. 沒了。就這麼簡單。真想不通我怎麼搞了那麼久才寫好。  
  
下載 DOWNLOAD:  
<http://daniel.kao.googlepages.com/WretchGrabPhoto.py>  
  
使用方式：  
0. 先在電腦上裝好[Python](http://www.python.org/download/)。  
1. 把WretchGrabPhoto.py下載下來，放在隨便一個目錄  
2. 用cmd開啟一個Dos視窗，進到該目錄，然後執行下面這行 (python執行檔的位置要看你灌的是哪一版而定)  
c:\Python24\python.exe WretchGrabPhoto.py "the\_url\_to\_the\_first\_photo\_in\_the\_album" html\_to\_be\_saved.html  
3. 等它執行完，用IE或Firefox開啟你自己設定的html檔就行了  
  
參考：  
[Read & Write JPEG COM and EXIF metadata [jpeg] [python] [image] [metadata] [exif]](http://snippets.dzone.com/posts/show/1021)  
[fetidcascade.com - Python Exif Utilities](http://www.fetidcascade.com/pyexif.html)  
[Team Programming Dragon．編程龍 » Blog Archive » 用 wget 抓無名單一相簿](http://graphics.csie.ntu.edu.tw/%7Ejonathan/tpd/2008/08/wget-for-wretch/)  
[下載無名Blog文章裡的圖片 | 無為閣](http://hychen.wuweig.org/?p=89)  

### [破解*無名小站*下載相簿照片作者: *井民全*前言](http://www.google.com.tw/url?sa=t&source=web&ct=res&cd=1&url=http%3A%2F%2Fdebut.cis.nctu.edu.tw%2F%7Eching%2FCourse%2FAdvancedC%2B%2BCourse%2F__Page%2FAdvanced_PChome%2F01%2520Wreth%2FPhotograph%2520Album%2520Download.pdf&ei=SZ40SvHtO6bs6gPBq4zHDw&usg=AFQjCNGwT0AWd4Myo0YtFZd_0175KHTQ-w&sig2=WytvbBwbNMeqqWwVnf7CFw)
