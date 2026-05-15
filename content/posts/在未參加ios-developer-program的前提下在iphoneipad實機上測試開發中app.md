+++
title = "在未參加iOS developer program的前提下，在iPhone/iPad實機上測試開發中app"
date = "2013-02-20T17:05:00.002Z"
slug = "在未參加ios-developer-program的前提下在iphoneipad實機上測試開發中app"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/02/ios-developer-programiphoneipadapp.html"
bloggerID = "8686974382411629765"
tags = ["iOS", "Programming"]
[cover]
  image = "/images/blogger/8686974382411629765/5427758925_c8ff86cf54_b.jpg"
+++

[![](/images/blogger/8686974382411629765/5427758925_c8ff86cf54_b.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfEJiGEAyGQHuz8DlVIokJQa2JvVMLo404-Rucgn4c8LcfktrQ57pHR8m9rf0Rya8_fpV2837GnCuEnNjwg_mupyGtl72sksPwA7ST3DA0KlPN9GoOGn_zv7CAoNnszqAdfUbhUBC-ttc/s1600/5427758925_c8ff86cf54_b.jpg)

(Taipei.Taiwan)  
  
該做的正事不認真，寫程式倒是花了不少時間。  
今天總算有了點進展，先是把addTags的功能搞定，  
再來是加上了Favorites的頁面，可以顯示自己加過特定tags的照片。  
  
有了這些自己想要的功能之後，光是在emulator上測試，  
就開始覺得不大過癮，想找辦法把程式放到iPhone上玩。  
為了要把app deploy到手機上開發測試，  
一般來說，得要加入US$99/year的developer program才可以。  
加入了這個program之後，除了可以在真機上測試，  
還可以發佈app到AppStore上去。  
不過，目前我還沒有這樣的需求也沒有這打算，  
因此實在是很不想花這筆錢。  
而且，也不確定自己之後是不是還有時間研究iOS...  
  
由於我的手機已經JB了，想說總會有辦法藉此到達我的目的吧。  
果不其然，網路上從很早以前就有很多教學在講怎麼設定和patch xcode。  
但是…全都好複雜呀：  
又要加certificate，又是改plist，還要加入scripts。  
只要其中哪個步驟沒弄好，應該就不行了吧。  
  
好在，找到有人直接提供了懶人包的程式，  
只要輕鬆按幾個按鈕就可以把所有的patch給搞定。  
步驟如下：  
1. 下載JailCoder，在Mac上執行它  
2. 根據畫面最上方的Guide button操作，把certificate先搞定  
3. 按左下方的patch xcode  
4. 再按右下方的patch project，選擇自己想要deploy的project  
5. 替自己的iOS device裝上AppSync (前提是要先JB)  
    AppSync的source repo path下面有，  
    把它加到Cydia的軟件源中，再尋找AppSync這支app就可以了  
  
REF:  
[JailCoder](http://oneiros.altervista.org/jailcoder/guide.php?lang=en-US)  
AppSync Installaion Source:  
<http://cydia.myrepospace.com/Bl00dra1n>
