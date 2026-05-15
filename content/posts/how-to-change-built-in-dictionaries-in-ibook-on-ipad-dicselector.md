+++
title = "How to change built-in dictionaries in iBook on iPad -- DicSelector"
date = "2010-06-17T17:34:00Z"
slug = "how-to-change-built-in-dictionaries-in-ibook-on-ipad-dicselector"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2010/06/how-to-change-built-in-dictionaries-in.html"
bloggerID = "6297506096574085021"
tags = ["iPad"]
[cover]
  image = "/images/blogger/6297506096574085021/371850216_07f7f56925.jpg"
+++

[![img_2706.jpg](/images/blogger/6297506096574085021/371850216_07f7f56925.jpg)](http://www.flickr.com/photos/plateau/371850216/ "img_2706.jpg by plateaukao, on Flickr")  
Frankfurt.Germany  
  

By default, iBook only supports English to English dictionary. It's a great feature just like the one in Kindle devices. However, the English definition is not always clear enough for foreigners; and sometimes the ebook content is in other languages, for example in Japanese. In these scenarios, the built-in dictionary may not be that handy.

After searching on the internet, to my surprise,  I found that actually iBook did put more than one

dictionary on iPad. By checking folders with App iFile, you will see several dictionaries:

/Library/Dictionaries/Apple Dictionary.dictionary  
/Library/Dictionaries/New Oxford American Dictionary.dictionary  
/Library/Dictionaries/Oxford American's Thesaurus.dictionary  
/Library/Dictionaries/Shogakukan Daijisen.dictionary  
/Library/Dictionaries/Shogakukan Progressive English-Japanese Japanese-English Dictionary.dictionary  
/Library/Dictionaries/Shogakukan Ruigo Reikai Jiten.dictionary

  
Apparently, there are English-Japanese and Japanese dictionaries inside. We just need a way to set other dictionaries as the default dictionary. [A good blog post in Japanese](http://moyashi.air-nifty.com/hitori/2010/06/ipaddicselector.html) describes in detail how to do this for us already. The quick way to do so is to manipulate the file:  
  
/var/mobile/Applications/iBooks/iBooks.app/Japanese.lproj/DefaultDictionaries.plist  
  
By changing the dictionary order in the file, you can have access to other dics. Still, it's tedious to change the file every time I want to use another dic. Well, seems that someone have the same feelings as I do!!! A utility is created to make our lives easier -- DicSelector!!  
  
DicSelector can be installed by adding a package source in Cydia. Yeah, you got it. You need to Jail-break. You won't regret it! Here's the steps to add the source:  
  
1. Launch Cydia and switch to "Manage" tab  
2. Tap on Sources  
3. Press Edit on the right up corner, and then press "Add" on the left up corner  
4. input this url: http://homepage3.nifty.com/moyashi/cydia/  
5. Now, wait until Cydia update the sources  
6. Search "DicSelector" and install it.  
7. Go back to "Settings" app, you will see DicSelector now under Extensions at the left panel list  
8. Tap on it and choose your favorite dictionary!!!  
9. Change your default language to Japanese  
10. Launch iBook and enjoy your dictionary  
  
= = = = = = =  
Updates (2010/07/22)  
With iBooks 1.1 or 1.1.1, DicSelector no longer works. Instead, you can modify the following file:  
/var/mobile/Applications/xxxx/iBooks.app/BKDictionaryManager\_LanguageToOrder.plist  
All you have to do is change the order of the dictionaries in "en" or in "ja".  
In this way, the Japanese English dictionary can also be used to look up words in pure English epub files.  
  
= = = = =  
  
別以為iPad上的iBook因為免錢送你用，所以就只寒酸地送你一套英英的新牛津美國字典。其實，iBook裡頭還偷放了日文辭典 -- 大辭泉、小學館Progressive英和、和英中辭典、還有日文的類語例解辭典。對於苦於英英翻譯的人，又略懂日文的人，如果可以有辦法把這些"隱藏"的字典功能打開，那不就太棒了，馬上可以省下買日文字典的錢。  
  
廢話不多說，這就來教你怎樣切換 iBook 隱藏的字典。首先呢，如果你不想JB的話，可以自己手動想辦法改下面這個檔案，把你想要的字典改到最前面。  
  
/var/mobile/Applications/iBooks/iBooks.app/Japanese.lproj/DefaultDictionaries.plist  
裡頭的內容大概長成這樣：  
  
<key>DCSDefaultActiveDictionaries</key>  
<array>  
　<string>/Library/Dictionaries/New Oxford American Dictionary.dictionary</string>  
　<string>/Library/Dictionaries/Oxford American Writer's Thesaurus.dictionary</string>  
　<string>/Library/Dictionaries/Apple Dictionary.dictionary</string>  
</array>  
  
  
  
如果你跟我一樣懶的話，可以先把iPad JB一下，然後依照下面的步驟輕鬆切換字典：  
  
1. 開啟 Cydia 並切換到 "Manage" 這個Tab  
2. 按一下 Sources  
3. 按一下右上角的 Edit，再按一下左上角的 Add  
4. 輸入 http://homepage3.nifty.com/moyashi/cydia/  
5. 然後，讓Cydia更新一下它的套件庫  
6. 在Cydia中搜尋 DicSelector 這支小程式，並安裝它  
7. 好啦！請回到 iPad 的"設定"，你會發現左邊的Panel，Extensions下面多了一個DicSelector  
8. 點一下它，你就可以開始設定你想要的字典了  
9. 記得把你的語系切換到日文。目前這支程式好像只有去改日文語系時iBook的預設字典設定  
10. 進到 iBook，開始享用吧!  
  
沒圖沒真相，來一張圖吧：  
[![ ](/images/blogger/6297506096574085021/4709066993_f18ec93aa0.jpg)](http://www.flickr.com/photos/plateau/4709066993/ "  by plateaukao, on Flickr")  
  
ps. 感謝下面這些網址share info的日本人。  
  
REF:  
<http://moyashi.air-nifty.com/hitori/2010/06/ipaddicselector.html>  
<http://hondamarlboro.blog112.fc2.com/blog-entry-68.html>  
<http://moyashi.air-nifty.com/hitori/2008/08/iphoneeiisoftba_1145.html>
