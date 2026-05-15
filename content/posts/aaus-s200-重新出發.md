+++
title = "Aaus S200 重新出發"
date = "2008-03-18T01:22:00Z"
slug = "aaus-s200-重新出發"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/03/aaus-s200.html"
bloggerID = "297425765100028266"
tags = ["Linux", "Olympus E510"]
[cover]
  image = "http://farm3.static.flickr.com/2156/2250832299_bc97f1e6e5.jpg"
+++

[![P2080714](http://farm3.static.flickr.com/2156/2250832299_bc97f1e6e5.jpg)](http://www.flickr.com/photos/plateau/2250832299/ "P2080714 by plateaukao, on Flickr")  
(Olympus E510 Geneve.Art)  
  
在前往日內瓦的路上，看到某棟建築物有畫，覺得很特別。  
所以在公車上隨手拍了一張。  
後來進了市區就找不到這一幅畫了。  
  
\*\*\*\*  
  
之前提過我的jvc victor mp xp 5220不行動了。  
後來查過發現是自己新增256MB記憶體的問題，  
拿掉後，就可以正常開機。  
只是，僅存的128MB會讓它慢得嚇人。  
連我灌xubuntu都免不了聽著硬碟從頭到尾軋軋叫。  
  
目前PCMCIA 光碟機不在手邊，  
所以沒有辦法為它灌上更小的distribution，  
只能試著安裝一些比較不佔記憶體的軟體先撐著。  
參考了一下DSL套件的軟體列表，  
我安裝了：  
Dillo 看網頁的軟體  
Emelfm 兩欄的檔案總管  
xzgv 看圖軟體 （不過感覺上還是gqview關掉一些功能會比較不吃RAM)  
PCManfm PCMan寫的檔案總管，開啟速度快，而且支援mount外接設備的功能。  
我試了一下我的USB cle，發現它找得到，卻無法正常掛載上。  
上網找了一下解決的方法，只要利用apt-get安裝一下pmount就行了。  
pmount似乎是個讓一般使用者也可以mount的軟體。果然一裝就行^ ^  
  
之前一直死守xfce的環境就是因為它可以自動抓到外接設備，自動mount，  
現在pcmanfm可以幫我做到這件事，  
我就可以順理成章地改用icewm。  
畢竟它比較不佔體積，而且可以手動改的設定也比較多。  
  
另外一點之前使用s200時一直困擾著我的問題是：  
在xubuntu中的無線網路設定介面很爛，  
使用者得自行輸入ssid等資訊。  
如果我是到外頭抓無線網路，我怎麼知道有什麼ssid可以用呢？  
早先試過命令列的iwlist scanning，無奈不曉得為什麼它不能正常運作。  
所以我總是只能碰運氣，連上了，就用；連不上，也就沒輒了。  
  
今天，也順便在網路上找到了好東西。  
在某個論壇中看到，  
可以裝上ubuntu中的network-manager和它的applet，  
不過，這樣子可能會裝上不少ubuntu中的套件。  
另一個方式是，安裝wifi-radar。  
這個軟體的介面就很簡單明暸：  
可以掃出目前的無線網路，只要點選就可以輕易的在不同的ap間切換。  
下次，再帶s200出去我就不用怕上不了免費的網路了。
