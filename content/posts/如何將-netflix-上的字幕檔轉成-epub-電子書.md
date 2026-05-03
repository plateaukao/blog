+++
title = "如何將 Netflix 上的字幕檔轉成 epub 電子書"
date = "2020-12-08T15:20:14.858Z"
description = "想要跟大家分享一下怎麼把 Netflix 上喜歡的影集或電影的字幕轉換成電子書。這個需求主要是來自於自己平常看影片一方面是休閒，另一方面希望同時也可以訓練自己的外語能力。"
slug = "如何將-netflix-上的字幕檔轉成-epub-電子書"
canonicalURL = "https://medium.com/@danielkao/%E5%A6%82%E4%BD%95%E5%B0%87-netflix-%E4%B8%8A%E7%9A%84%E5%AD%97%E5%B9%95%E6%AA%94%E8%BD%89%E6%88%90-epub-%E9%9B%BB%E5%AD%90%E6%9B%B8-bd2c78cb1694"
mediumID = "bd2c78cb1694"
+++

想要跟大家分享一下怎麼把 Netflix 上喜歡的影集或電影的字幕轉換成電子書。這個需求主要是來自於自己平常看影片一方面是休閒，另一方面希望同時也可以訓練自己的外語能力。

在 PC 上的瀏覽器可以裝 extension 擴充 Netflix 讓它支援雙語字幕，達到看影片時同時練習外語的目的，但有時看完影片後，想要再回味影片對白時，就會很希望能有一份影片中的對白。而且這份對白最好還是雙語對照的，省下自己事後再翻譯的時間。

[dannvix/NflxMultiSubs](https://github.com/dannvix/NflxMultiSubs)

### 步驟

以下是大概的步驟。後面會再針對每個步驟有詳細的說明：

#### 前置作業

1. 在瀏覽器 (Chrome) 中安裝 Tempermonkey
2. 在 Tempermonkey 中安裝Netflix subtitle downloader
3. 在 PC (or Mac) 上安裝 calibre (一個看電子書，建立電子書的軟體)

#### 手動作業

1. 在瀏覽器中透過 Netflix subtitle download 下載想要的影集的字幕 zip 檔案
2. 利用我寫的 python script 將影集字幕按照時間，集結成單一的文字檔
3. 將文字檔加入到 calibre 中，並設定相關參數，讓 calibre 幫忙產生 epub 檔案

---

### 前置作業

前置作業中需要的 extension 和軟體分別列在下面：

[Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en)

[Netflix - subtitle downloader](https://greasyfork.org/en/scripts/26654-netflix-subtitle-downloader)

[calibre - Download calibre](https://calibre-ebook.com/download)

---

### 手動作業

1. 在瀏覽器中透過 Netflix subtitle downloader 下載字幕。這一個步驟可以參考下面的連結。下載時，記得要選格式為 vtt，因為後面的處理是針對 vtt 格式進行的。

[Netflix 字幕下载](https://www.bilibili.com/read/cv3584236/)

2. 下載好 zip 檔案後，先把它解開來，可以看到目錄中包含所有影集的字幕。檔案名稱的組成：前面是片名，接著是第幾季，第幾集；再來會寫到語言。語言常見的是 en (英文)，zh-Hant (繁體中文), ja (日文), ko (韓文), fr (法文) 等等。如果是顧及聽障朋友的字幕的話(除了對白外，還包含畫面中聲音的描述)，會加上 [cc] 的結尾。cc 是 Closed Captioning 的縮寫。

![](/images/bd2c78cb1694/1_puxcy8fOYRjGhyR469N09A.png)
*例子*

然後也把我寫的 script 下載下來，記得要先安裝 python module webvtt-py 唷。

```
pip install webvtt-py  
或是  
pip install -r requirements.txt
```

[plateaukao/webvtt\_to\_html](https://github.com/plateaukao/webvtt_to_html)

在 Terminal 中執行下面的指令格式：

```
python convert.py lang_main lang_sub path_to_subtitles/*\[cc\].vtt > output.html
```

`lang_main` 和 `lang_sub` 要替換成你有下載的語言；還有 `path_to_subtitles`要換成真的目錄位置 。以上面的例子來說，我只下載了韓文和日文的字幕檔。我想要電子書中主要顯示韓文字幕，然後日文字幕充當成翻譯，以防有些句子看不懂。所以真的指令可以下：

```
python convert.py ko\[cc\] ja path_to_subtitles/*\[cc\].vtt > output.html
```

執行時間很快，應該不用幾秒就會處理完成，產生一個 output.html 。這時，可以把 html 檔案打開來看一下內容，是不是有正確產生所需的內容：

![](/images/bd2c78cb1694/1_b7zhWNSajipD4SyHqCuy0A.png)

從上圖可以看到，韓文部分都有被標上 `<h3>` 的 tag，日文則是標上一般的 `<p>`tag。這樣表示 python script 處理出來的檔案是正確的。

3. 開啟 calibre 軟體，把生成的 output.html 拉進 calibre 中，點選該檔案，按右鍵，然後選擇convert books -> convert individually。

![](/images/bd2c78cb1694/1_q8uVPOqTx-6jwaLz-MLB3A.png)

這時會跳出一個編輯的畫面，你可以在這修改電子書的名稱(Title)，作者(Author)等資訊。

![](/images/bd2c78cb1694/1_Xzt9W3u6KOblbYwUPiZKSw.png)

更改好之後，請點左側的 Table of Contents，因為我們想要為電子書建立目錄；不然一部影集少說都有十幾集，沒有目錄的話，很難在每一集中跳轉。

請在右側的 Level 1 TOC 填上 `//h:title` ，這樣子 calibre 才會在建立電子書時，將我在 html 中預先塞好的 title 位置當成每一集分段的地方加到目錄中。

![](/images/bd2c78cb1694/1_iyD2Ab1yO7WMnsZrpE5H1A.png)

設定完成後，就可以按右下角的 OK，讓 calibre 開始工作囉！

---

建立好 epub 電子書後，可以用 calibre 內建的 epub viewer 來觀看。在 Mac 上的話，可以用 Mac 提供的 iBooks 來觀看。 iBooks 中的效果大概如下：

![](/images/bd2c78cb1694/1_6Gss8twPCgN_hxNR0yEXDg.png)

![](/images/bd2c78cb1694/1_RITSuzbYUQ8I2Y-SU7F4Iw.png)

---

到這邊為止，已經達到了一開始的目的，可以順利地將字幕轉成電子書，透過不同的 epub reader 來閱讀。但仔細看一下，這樣子的排版似乎可讀性不是很高：韓文跟日文的字型大小都一樣；很難一眼看到主要想閱讀的主語言，有點賓客不分。

所以，我們其實可以再進一步地改善這個建立好的電子書。在 Calibre 中，在這本書上點右鍵，選擇 Edit Book。

![](/images/bd2c78cb1694/1_pncq6T7MeJovJvweKyss9g.png)

這時，會跳出一個編輯書籍的介面。請從左邊選擇 `stylesheet.css` ；這時中間會列出所有的 html element，以及它們現在的 style 設定。 `.calibre` 是第二語言的 style，而 `.calibre2` 則是主要語言的 style。所以如果我想要韓文字大一些的話，我可以透過 `font-size` 的參數調整，讓它變大。

畫面最右邊是書籍內容的即時預覽，你可以邊調整邊看是不是有符合需求。等確定後，再按 toolbar 上的 Save Icon 就行了

![](/images/bd2c78cb1694/1_ZzoBZWGMGTfyrnQsMeVYsA.png)

經過調整，可以看到韓文字變大了一些，同時日文部分也比較真的像是註釋的感覺。

![](/images/bd2c78cb1694/1_6uvcIDU8G7J0pHoyJG60fA.png)

---

目前整個流程還是充滿著手動的步驟，所以操作起來很煩瑣(雖然我做起來還是很快就是了)。希望之後有機會能寫成一個 plugin 加到 calibre 中，只要從 Netflix subtitle downloader 拿到 zip 檔後，就能全在 calibre 中處理。
