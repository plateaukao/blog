+++
title = "讓 KOReader 再次偉大"
date = "2025-02-15T17:34:42.197Z"
description = "這篇文章將分享在 KOReader 中怎麼修改 epub 中的 css style，讓閱讀體驗可以有更多樣的應用場景。"
slug = "讓-koreader-再次偉大"
canonicalURL = "https://medium.com/@danielkao/%E8%AE%93-koreader-%E5%86%8D%E6%AC%A1%E5%81%89%E5%A4%A7-051daa010ef0"
mediumID = "051daa010ef0"
tags = ["電子書閱讀器"]
+++

> 這篇文章將分享在 KOReader 中怎麼修改 epub 中的 css style，讓閱讀體驗可以有更多樣的應用場景。

其實 KOReader 一次都很強大，只是我又再次感受到它的可調整性，想要來跟大家分享一下。這次是認真的研究了一下在文件的設定中，可以指定使用者自行加入的 css 樣式表，用來調整 epub 電子書的呈現方式。

會研究這個功能的原因是：之前自己曾寫了一個小 script，可以把 iTHome 的鐵人賽參賽系列文章轉換成電子書；而這些電子書因為原本網頁的設計，背景並不是全白的，而是帶點淡淡顏色的灰色。

這背景色在電腦上看，不會有什麼不舒服的地方；但在電子書閱讀器上就會很明顯地讓畫面背景和文字的對比不夠高。在 KOReader 又因為是整頁背景色，在切換頁面時，都會重繪整個畫面。

為了解決這問題，一個最根治的方式是：把我已經轉換好的每本 iTHome 鐵人賽主題電子書檔案中的每個 html 的背景，再強制設定為透明的。這方式曠日費時。

另一個方式則是亡羊補牢，只需要在 KOReader 中針對這些電子書將其背景設定為透明即可。稍微研究了一下，要讓畫面背景變為透明的話，可以用下面的 css 設定

```
body { background-color: transparent !important; }
```

將它寫入一個 transparent\_background.css，再放到 koreader 目錄下的 styletweaks 目錄即可。它會出現在 KOReader 文件設定 > 樣式表調整 > 使用者樣式表調整中。

—

同樣地，想到之前曾經開發了製作雙語字幕電子書的 calibre plugin，製作了許多影集的字幕書，如果想要將其中的中文(第二個語言)翻譯部分給隱藏的話，也可以為它建立一個 css 檔案，並放入以下的 css:

```
div[class="sub"] {display: none !important;}
```

隱藏的話，會造成整份文件的位置改變，效果其實不是很好。另一個嘗試是：把第二個字幕語言的文字顏色改為透明的。如此一來，保留了第二字幕所佔的空間，只是字都看不到了。這麼一來，整份文件的相對位置就不會因此而改變。

```
body { background-color: transparent !important; }
```

加入到使用者樣式表後，還可以長按這些項目，點擊加入功能列表中。這麼一來，在設定手勢時，就可以將部分手勢指定為這些 css style change 的開關，省下需要層層進入選單的麻煩。
