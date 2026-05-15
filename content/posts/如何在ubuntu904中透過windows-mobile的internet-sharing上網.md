+++
title = "如何在ubuntu9.04中透過windows mobile的internet sharing上網"
date = "2009-09-23T15:45:00Z"
slug = "如何在ubuntu904中透過windows-mobile的internet-sharing上網"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/09/ubuntu904windows-mobileinternet-sharing.html"
bloggerID = "8142229182696200508"
tags = ["Linux"]
[cover]
  image = "/images/blogger/8142229182696200508/3937354149_215b17b2ea.jpg"
+++

[![R8075831.JPG](/images/blogger/8142229182696200508/3937354149_215b17b2ea.jpg)](http://www.flickr.com/photos/plateau/3937354149/ "R8075831.JPG by plateaukao, on Flickr")  
Taipei.Taiwan  
  
城市中盛開的花。   
  
\*\*\*\*  

在asus epc 1000HE上使用ubuntu9.04的感覺，真是愉快得不得了。明明windows xp已經夠輕量了，應該run起來要很smooth才對，但總覺得1000HE跑起來比我三年前的notebook還要不順。最近不知道是中毒了還是怎樣，常常會發生系統快要死當的情形：一會兒檔案總管沒動作，一會兒firefox罷工，連微軟自家的IE也常常沒有回應。原本打算要灌windows 7來玩玩看的，無奈免費下載的期間早就過了，我也懶得再去找現成的iso檔回來試。

  

ubuntu9.04出來時，聽說它的開機速度有下過一番苦功，一直沒有機會好好試一下。所以，我變節了，直接把系統換成ubuntu9.04。六百多MB的光碟映像檔，不用半個小時就抓完了。安裝的時候很順，除了那個硬碟分割的軟體很鳥，每新增或刪除一個磁區，它都要重新在那兒轉上半天，有點惱人。

  

灌完系統後，有線網路直接可以運作（這從很早期的ubuntu開始，就已經支援得很好了），第一件事便是把我常用的中文輸入法－－無蝦米－－灌起來。由於之前都是在用linux系統，我早就在我的gmail裡準備了一套字庫檔和輸入法圖案。下載下來後，先裝了scim-tables-zh，讓我可以在scim setup中載入我自己的字庫檔。就這樣，無蝦米回來了。

  

最近還申請了3G上網吃到飽的方案。週末有時會把電腦和手機一起帶出去，在坐捷運時使用。這下問題來了。在Windows下，只要直接把手機接上電腦，然後選擇internet sharing就可以開始用網路。在ubuntu下，就沒這麼直覺了。一開始我看到在NetworkManager下有Mobile BroadBand的選項還以為在這邊做些設定就可以一切搞定，但是後來發現事情並沒有想像中那麼簡單（雖然也沒有多難啦）。

  
1．首先請把subversion裝起來，因為要利用它來抓一個package  
$ sudo apt-get install subversion  
2．利用svn抓usb-rndis-lite的原始碼  
$ svn co http://synce.svn.sourceforge.net/svnroot/synce/trunk/usb-rndis-lite  
cd usb-rndis-lite/  
3．更改原始碼  
$ vi rndis\_host.c  
  
在第524行，可以找到下面這段程式碼  

```
if (tmp <>hard_mtu) {  
dev_err(&intf->dev,  
"dev can't take %u byte packets (max %u)\n",  
dev->hard_mtu, tmp);  
goto fail;  
}
```

請把它改成下面這樣：  
  

```
if (tmp <>hard_mtu) {  
dev_err(&intf->dev,  
"dev can't take %u byte packets (max %u)\n",  
dev->hard_mtu, tmp);  
retval = -EINVAL;  
/* goto fail;*/  
}
```

  
  
  
4．編譯程式並安裝之  
$ make  
$ sudo ./clean.sh  
$ sudo make install  
  
5．把手機連上電腦，並且在手機上選擇Internet sharing的選項  
  
6．讓它可以抓到dhcp傳來的ip address  
$ sudo dhclient  
  
Okay啦！  
  
\*\*\*  
  
在epc 1000HE上，要讓它支援3D的超炫畫面也很簡單，只要到system->preferences->appearence下，Visual effects選擇Extra就行了。更多詳細的設定可以透過安裝某些package來達成。網路上有很多文件了，我就不再這兒多說了。
