+++
title = "打造 E-ink 專用的瀏覽器 (VI) — 匯出 epub 檔案"
date = "2021-04-04T14:08:22.617Z"
description = "為電子書閱讀器而開發的瀏覽器，在繞了一大圈之後，終於又繞回了電子書本身。原本的實作就已經可以將網頁輸出成 pdf 檔案。不過，如果希望產生的檔案可以更有彈性地調整字型大小，或是在不同的設備上閱讀，轉成 epub…"
slug = "打造-e-ink-專用的瀏覽器-vi-匯出-epub-檔案"
canonicalURL = "https://medium.com/@danielkao/%E6%89%93%E9%80%A0-e-ink-%E5%B0%88%E7%94%A8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-vi-%E5%8C%AF%E5%87%BA-epub-%E6%AA%94%E6%A1%88-98ce6ef56d24"
mediumID = "98ce6ef56d24"
tags = ["EinkBro"]
[cover]
  image = "/images/98ce6ef56d24/1_oul9c2Q--bvoW3yG9PRucw.png"
+++


為電子書閱讀器而開發的瀏覽器，在繞了一大圈之後，終於又繞回了電子書本身。原本的實作就已經可以將網頁輸出成 pdf 檔案。不過，如果希望產生的檔案可以更有彈性地調整字型大小，或是在不同的設備上閱讀，轉成 epub 格式會是更好的選擇。但目前市面上的行動瀏覽器都沒有這樣子的設計，頂多提供輸出成 pdf，mhtml 等格式。

為了在 EinkBro 中加入這功能，當務之急是先找到一個可以在 Android 設備上新增、開啟和編輯 epub 的函式庫。找來找去，似乎選擇也不多，只有 Epublib 是個比較完整的方案。

[psiegman/epublib](https://github.com/psiegman/epublib)

Epublib 是個純 Java 的函式庫，不過也支援在 Android 系統中使用。雖然它已經很久沒有什麼更新了，但看起來功能應該還算符合我的需求。它並沒有把它的函式庫放在常用的 public repository 中；文件中是建議直接下載 jar 檔案，塞在 Android app 中。不過這和發布到 F-Droid 的規則有抵觸，所以我去 `mavenCentral` 找到了其他人幫忙上傳的版本。比最新版差了些 commit，但並不影響我需要的功能。

[Maven Central Repository Search](https://search.maven.org/artifact/com.positiondev.epublib/epublib-core)

### 實作內容

目前我在實作上，會先跳出系統的 document picker ，讓使用者建立一個新檔名，或是選擇一個已經存在的 epub 檔案，再把目前網頁的 innerHtml 內容取出，利用 Epublib 注入到 epub 檔案中，當成一個新的章節。

![](/images/98ce6ef56d24/1_oul9c2Q--bvoW3yG9PRucw.png)
*code snippet for saving epub file*

677 行的 getRawHtml() 利用注入 javasript 取得 raw html。拿到手的 raw html 還不行直接拿來用，因為它裡頭有些字元已經被轉換過了，需要加入

```
implementation 'org.apache.commons:commons-text:1.7'
```

![](/images/98ce6ef56d24/1_rqZpTnwnt5JZuZkaaajEIw.png)

然後呼叫 `StringEscapeUtils.unscapeJava()` ，還原成可用的字串。

#### 電子書名及章節名稱

`getBookName()` 和 `getChapterName()` 都會跳出 AlertDialog 讓使用者輸入字串。因為不想再用 callback 的方式，所以把它們都包成 suspendCoroutine，讓程式好讀一下。

以 `getChapterName()` 為例，在代入恰當的參數到 `TextInputDialog` 後，就可以得到想要的章節名稱。

![](/images/98ce6ef56d24/1_i3dQ3vJCDKwTjAqgPs1hDA.png)

而 `TextInputDialog` 只是很單純地實作了 `show()`，在使用者有任何互動後，把字串傳出。

![](/images/98ce6ef56d24/1_mYzxQOcZsEtRA1phYya-Ng.png)

#### **待改進的地方**

目前只能把純文字的資料存進 epub 檔案裡。希望在不久的將來，也可以把圖片存下來，讓產生的 epub 更有價值。

### 相關連結

#### 從 v8.6.0 開始支援匯出 epub 檔案

[EinkBro - Apps on Google Play](https://play.google.com/store/apps/details?id=info.plateaukao.einkbro)
