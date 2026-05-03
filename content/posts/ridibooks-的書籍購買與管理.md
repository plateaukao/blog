+++
title = "RIDIBooks 的書籍購買與管理"
date = "2023-05-11T13:20:14.553Z"
description = "本文記錄了怎麼在 Ridibooks 上購買韓文書籍，以及事後的書籍管理方式。"
slug = "ridibooks-的書籍購買與管理"
canonicalURL = "https://medium.com/@danielkao/ridobooks-%E7%9A%84%E6%9B%B8%E7%B1%8D%E8%B3%BC%E8%B2%B7%E8%88%87%E7%AE%A1%E7%90%86-388d197e5fc2"
mediumID = "388d197e5fc2"
tags = ["韓語學習筆記"]
+++

本文記錄了怎麼在 Ridibooks 上購買韓文書籍，以及事後的書籍管理方式。

---

學習韓文，在差不多到達一定程度後，會開始找更多的資料來廣泛閱讀。除了線上的各種媒體外，也可以找自己有興趣的書籍來看。這幾年韓國也有不少好看的小說進到台灣的市場來。由於翻譯需要時間，所以，如果想要看第一手的韓文小說，或是想要讀市面上暢銷書的韓文原版的話，通常得要到韓國的線上書城才買得到。

### 線上購買書籍

這篇文章要介紹的是怎麼從 [RIDIBOOKS](https://ridibooks.com/ebook/recommendation) 上買書。首先，當然是先申請個帳號囉。登入後，先選一本自己想要購買的書籍，然後點擊右下方的購買。

![](/images/388d197e5fc2/1_xHiXCXhkVdIiThdW1c4tjw.png)

點下後，會出現付費的選擇畫面，這時，要選擇最下面的海外發行信用卡的選項。

![](/images/388d197e5fc2/1_9VmjjeV_I6yCLg3fRnIsbA.png)

再來，就是填入信用卡相關的訊息，就購買完成囉。

---

### 下載已購買的書籍

要將書籍下載到電腦上，必須要先安裝它在桌上型電腦的軟體。連結可以在官網畫面下方取得。紅色框框的部分寫的是 [Viewer Download](https://ridibooks.com/support/app/download)。

![](/images/388d197e5fc2/1_Z71WwlJpT1SzYDpU0FbB3g.png)

因為我使用的是 Mac Studio，所以我選擇了 Mac OS 的版本安裝。

![](/images/388d197e5fc2/1_0Nwesn6OzViK43jv3kbCnA.png)

安裝完後，一樣可以用自己建立好的帳號登入。該軟體無法截圖，所以我是用手機拍攝的。它會列出你已經購買好的書籍，這時，可以點擊下載，將它們都先下載到本機上，但，切記，不要點開來看。

![](/images/388d197e5fc2/1_TvT_1oNhcckC_ru_Ab27XQ.png)

這時，可以點擊右上方的設定按鈕，它會列出下載的書籍會放在哪個目錄下。以我自己來說，書籍都是放在下面這個路徑：

> ~/Library/Application Support/Ridibooks/library/plateaukao/…

![](/images/388d197e5fc2/1_wUXo3358vcf7R8oGvlScrw.png)

這時，雖然書籍都下載下來了，但無法直接用一般的閱讀 App 開啟，因為都有受到 DRM 的保護。以下是一些主要書商使用的 DRM 格式：

> - Amazon Kindle : Amazon’s own DRM

> - Kakao Page : Teruten MediaShell

> - Kyobo eBook : **Fasoo.com**

> - crema : **MarkAny**

> - Ridibooks : **MarkAny** (Android) / **Fasoo.com** (PC)

### 後續處理 — 轉成雙語書籍

在經過一些處理後，已經可以在一般的 App 中閱讀這些書籍。但是，畢竟全都是韓文的內容，就算大概看得懂，閱讀的速度還是會相當地慢。

隨著時代的進步，目前已經可以使用 AI 來幫忙做翻譯這件很費時費力的事了。一本好幾萬字的外文書，只要花幾個小時讓 AI 來處理一下，在平均花不到一美元的情況下，就能完成。

我使用的是 github 上的 [bilingual\_book\_maker](https://github.com/yihong0618/bilingual_book_maker) 這個 repository。目前已經翻過三、四本書，品質都足夠好，可以拿來做一般的閱讀用。偶爾遇到不知所云，前言不對後語的情形時，再回過頭來看一下原文就可以了。

![](/images/388d197e5fc2/1_GfY42Bp40y-i0VgGZmaRoA.png)

---

### 結語

這年頭，想要學好一個語言，沒有學習管道不再是一個藉口。網路上還有各式各樣的工具和內容可以嘗試，總是會找到適合自己的學習方法。
