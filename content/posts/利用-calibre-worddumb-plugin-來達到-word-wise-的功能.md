+++
title = "利用 Calibre + WordDumb plugin 來達到 Word Wise 的功能"
date = "2022-06-11T15:45:43.514Z"
description = "大綱"
slug = "利用-calibre-worddumb-plugin-來達到-word-wise-的功能"
canonicalURL = "https://medium.com/@danielkao/%E5%88%A9%E7%94%A8-calibre-worddumb-plugin-%E4%BE%86%E9%81%94%E5%88%B0-word-wise-%E7%9A%84%E5%8A%9F%E8%83%BD-6c21d93ccae0"
mediumID = "6c21d93ccae0"
tags = ["電子書閱讀器"]
+++

### 大綱

- Word Wise 和 X-Ray 是什麼
- 替代方案介紹
- 安裝方式
- 如何使用
- 範例畫面
- 其他設備上的效果

### Word Wise 和 X-Ray 是什麼

在亞馬遜官網有介紹：X-Ray 功能讓你在閱讀時可以很方便地知道人物、地點和事件。如果一本書很厚，人物錯綜複雜，或是看書的前後時間拉很長，常常會忘記誰是誰。這時， X-Ray 可以讓你很方便地回想起書中目前提到的人物是誰。Word-Wise 則是當你在閱讀其他語言的書籍時，把一些較難的單字直接在書籍中用小字標上簡單的說明。讓你不用一直要手動再去翻字典也能看得懂內容。

[Kindle Features: Search, X-Ray, Wikipedia and Dictionary Lookup, Instant Translations](https://www.amazon.com/b?ie=UTF8&node=17717476011)

![](/images/6c21d93ccae0/0_EOA12nxOnzg6uYEZ.png)
*from WordDumb github*

### 替代方案介紹

Word Wise 和 X-Ray 只限於在亞馬遜購買的書，在 Kindle 上能使用而已。如果是在其他書城，或是沒版權的書，就無法享用到這麼方便的功能。不過，方法是人想出來的。有好心人推出了類似的功能 — WordDumb，而且開放原始碼在 Github 上。這是由 Facebook 粉絲團裡的網友推薦的。今天我安裝，試了一下，感覺還不錯，所以打算來詳細介紹怎麼安裝和使用。看得懂英文的，可以直接參考下面的連結就行。

[GitHub - xxyzz/WordDumb: A calibre plugin that generates Kindle Word Wise and X-Ray files for KFX…](https://github.com/xxyzz/WordDumb)

### 安裝方式

1. 這功能是依附在 Calibre 上的。Calibre 是個跨平台的電子書管理兼閱讀軟體。功能超級強大，只是介面個人覺得不是很好看。但是，用久了也就會習慣的。Calibre 的安裝方式網路上很多，基本上就是去官網抓安裝檔下來，點個幾下就行。

[calibre - Download calibre](https://calibre-ebook.com/download)

2. (非必需，如果你 KFX 格式的書籍再裝就行了) 到 mobileread 網站下載 KFX Input 的 plugin。安裝的方式是：進到 Calibre 軟體中，進到它的設定畫面，選擇 plugins，然後選 Load plugin from file，把下載下來的 KFX Input.zip 指給它。

[[Conversion Plugin] KFX Input - MobileRead Forums](https://www.mobileread.com/forums/showthread.php?t=291290)

![](/images/6c21d93ccae0/1_aDswBcLoPjTXaxj4wv4isA.png)

#### 3. 再來就是這篇文章的重頭戲：安裝 WordDumb plugin

請看影片，可以直接從 Clibre 中安裝。

<https://user-images.githubusercontent.com/21101839/124686751-39f3aa00-df06-11eb-9b07-8c8f98544683.mov>

簡單的說明如下，最後，重新開啟一下 Clibre 就可以來使用啦！

![](/images/6c21d93ccae0/1_d1XoP_kM07fjtXXK9ONkaw.png)

---

### 使用方式

全部安裝好以後，在 Calibre 的上方工具列會有個紅色海星。只要選幾本書，再點它，就會開始運作。第一次使用時，可能要好幾分鐘才會完成，因為第一次需要去抓一堆函式庫回來安裝。不過都是自動地，不用擔心，過一陣子就可以看到右下方的 Jobs 完成。

![](/images/6c21d93ccae0/1_kd-JCmTmqCGcRTR88KKhiA.png)

執行完成後，請進到書籍所在的目錄 (點畫面中的 Path: Click to open)，可以看到多了一份 xxxxx\_x\_ray.epub 檔案。檔案大小可能會大很多，因為其中還包含了許多圖片。

點紅色海星右邊的下拉選單可以看到很多選項，大家可以自己摸索一下。

![](/images/6c21d93ccae0/1_iBrKr78Ws2nkfhMlBRfikA.png)

### 範例畫面

先來看看原本書籍在 Kindle 中的樣子，就是很平淡的樣子，沒有任何額外的資訊。

![](/images/6c21d93ccae0/1_X13o-i2tLOv1Ka7O9nTvCQ.jpeg)

再來看看在經過處理後的檔案 (有 Word Wise 和 X-Ray了)

![](/images/6c21d93ccae0/1_LH7aUV9gQwIkovMxi9RPiA.jpeg)

再點選單中的 X-Ray 來看看，人物，術語和相關圖片都整理地好好的。

![](/images/6c21d93ccae0/1_hzHJemhK3qmCg1nUqwJfKg.jpeg)

### 在其他設備上看的效果

同樣的輸出檔，試了在 Huawei Matepad Paper 和文石的 NeoReader，Koreader，還有靜讀天下軟體中閱讀。**目前只有靜讀天下 (Moon Reader) 可以正常顯示所有的 X-Ray 相關解釋。**而 Word Wise 則是看不到。

![](/images/6c21d93ccae0/1_E4zRq_tmTlDQmyEtghXtxw.jpeg)
*大部分的人名和專有名詞都會是藍色的*

![](/images/6c21d93ccae0/1_tnPVoK0e7lWst5w71z__Kg.jpeg)
*Big Island 的說明，可以往下捲動，還有附地圖！*

![](/images/6c21d93ccae0/1_fB9aK7TthFuPJ-tNiRv0bw.jpeg)
*本書主角的說明*

### 後話

還蠻有趣的 plugin，讓書籍的參考資料能在開始閱讀前都先塞到書籍中。之後應該找幾本書來看看是不是有很大的幫助。
