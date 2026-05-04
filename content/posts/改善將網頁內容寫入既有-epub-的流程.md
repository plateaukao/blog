+++
title = "改善將網頁內容寫入既有 epub 的流程"
date = "2022-01-09T16:16:15.710Z"
description = "目前 EinkBro 有提供儲存網頁成 epub 檔案的功能，這大概是少數(或是唯一)瀏覽器有提供的功能之一。不過，礙於 Android 每次升版對於檔案的存取方式都不斷在(亂無章法地)改進，到目前為止，最通用的開啟手機上檔案方式是：利用…"
slug = "改善將網頁內容寫入既有-epub-的流程"
canonicalURL = "https://medium.com/@danielkao/%E6%94%B9%E5%96%84%E5%B0%87%E7%B6%B2%E9%A0%81%E5%85%A7%E5%AE%B9%E5%AF%AB%E5%85%A5%E6%97%A2%E6%9C%89-epub-%E7%9A%84%E6%B5%81%E7%A8%8B-2bee7bfa09f1"
mediumID = "2bee7bfa09f1"
tags = ["EinkBro"]
[cover]
  image = "/images/2bee7bfa09f1/1_M9aQq7V5iFyfKIwTdGzzcw.png"
+++


目前 EinkBro 有提供儲存網頁成 epub 檔案的功能，這大概是少數(或是唯一)瀏覽器有提供的功能之一。不過，礙於 Android 每次升版對於檔案的存取方式都不斷在(亂無章法地)改進，到目前為止，最通用的開啟手機上檔案方式是：利用 Intent.ACTION\_CREATE\_DOCUMENT 叫起系統的 file expolorer default APP，從那很不好用的介面中選取想要的檔案，或新增一個檔案。

而 EinkBro 從一開始提供這功能時，就是採取了這方式。這作法在新增 epub 時，沒有什麼太大的問題，使用者只需要在對的目錄下輸入想要的檔案名稱就好， EinkBro 就會收到系統傳來的 content uri。

但如果使用者是想要將網頁儲存到既有的 epub 檔案中時，這方法就顯得很麻煩。開啟檔案選取時，有可能當下的目錄不是使用者想要的，也有可能當下的目錄有一堆 . 開頭的目錄或檔案，顯示在畫面最上方，必須要經過不斷捲動，或是在各個目錄間移動，才能找到想要的那個 epub 檔案。偶一為之還好；如果每天都有想要儲存的文章時，就會煩到想要放棄這功能，乾脆再另存一個新檔比較快。

### 解法的關鍵

我自己在使用了好長一段時間後，終於受不了了，想來看看有沒有辦法改善這個流程。昨天終於找到方法了。關鍵在於：在新建 epub 檔案時，那個 conten uri 的存取權限一般來說只可以使用到下次手機重開。一旦使用者重開手機，就只能再利用 file picker 選擇想要的檔案。這問題 Android 官方給出了解法：

<https://developer.android.com/training/data-storage/shared/documents-files#persist-permissions>

如果有想要拿到的 content uri，在未來不論何時都可以再次讀寫的話，可以加上下面的片段：

![](/images/2bee7bfa09f1/1_M9aQq7V5iFyfKIwTdGzzcw.png)

這麼一來，這個 uri 就可以保留在自己的 APP 中，之後利用它來讀取檔案的內容或是將新的資料寫入進去。

### EinkBro 中的實作說明

我把這段程式碼加在 openBook() 中，並且在 save epub 時，將這個檔案的 content uri 存到 sharedpreference 中 (是的，不是寫到資料庫，因為我懶得再開一個 table)。然後稍微調整了一下儲存 epub 的對話框，將原本的兩個選項(但都是開啟 file picker)：

1. Save to existing epub
2. New an epub

改為

1. Select Saved Epub
2. new Epub or from picker

選項 1 不再跳出系統難用的 file picker ，而是列出 EinkBro APP 曾經儲存過的 epub 檔案，讓使用者可以直接選擇！

雖然這只是一個很不起眼的流程小改善，但對於我的閱讀方式來說，卻有很大很大的幫助！也希望這個功能的改善，會讓大家更快速地儲存 epub 。

### 程式碼片段

#### 加入獲取權限的 commit

<https://github.com/plateaukao/browser/commit/3dca8703b72488cb33e2659e3aaafa7fd2292dca>

#### 將 epub 檔案的 uri 存入 sharedpreference，並呈現為列表

<https://github.com/plateaukao/browser/commit/73e227a6be807b7fd0a3cfe0d5cbc271f5812c26>

### 示範影片
