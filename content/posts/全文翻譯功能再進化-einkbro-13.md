+++
title = "全文翻譯功能再進化 — EinkBro (13)"
date = "2021-08-25T15:20:36.184Z"
description = "之前在 EinkBro 全文翻譯的作法是：為了要避免丟進翻譯網頁的文字內容充滿太多非本文的部分，會在事前先利用 Reader mode 將網頁內容淨化，然後再把 Reader mode…"
slug = "全文翻譯功能再進化-einkbro-13"
canonicalURL = "https://medium.com/@danielkao/%E5%85%A8%E6%96%87%E7%BF%BB%E8%AD%AF%E5%8A%9F%E8%83%BD%E5%86%8D%E9%80%B2%E5%8C%96-einkbro-13-802683a34e4a"
mediumID = "802683a34e4a"
tags = ["EinkBro"]
[cover]
  image = "/images/802683a34e4a/1_5XOoKB-hq0-hWSr6TyqfxA.png"
+++


之前在 EinkBro 全文翻譯的作法是：為了要避免丟進翻譯網頁的文字內容充滿太多非本文的部分，會在事前先利用 Reader mode 將網頁內容淨化，然後再把 Reader mode 的內文餵到翻譯網頁中。這樣子雖然可以解決畫面過於淩亂的問題，但畢竟網頁的格式被簡化了，不見得是使用者想要的觀看方式。

前幾天發現，原來目前 EinkBro 支援的 Google Translate 以及 Naver Papago 兩種全文翻譯網站，除了可以餵字串給它們之外，也可以直接餵網址給它們；這麼一來它們就會輸出一個格式一模一樣的網頁，只是文字內容都被翻譯成設定的語言。

這功能真的太棒了！我原本還一直想要找出 Chrome App 是怎麼實作全文翻譯的，想從那個方面下手，把相關的功能實作搬到 EinkBro 中。現在就不用那麼麻煩了，直接利用現在的翻譯網頁來設定參數操作就可以。

在前一篇全文翻譯的文章中有提到大概的步驟是：

1. 在畫面中開啟另外一個 WebView，讓它佔有畫面的一半。
2. 將網頁轉為 Reader mode，並從中抽出文字的部分。
3. 將文字部分做 pagination，根據目前的頁數餵進全文翻譯的網站，讓它幫忙翻譯出設定的語言。

[打造 E-ink 專用的瀏覽器 (X) — 支援全文翻譯對照](https://medium.com/einkbro/%E6%89%93%E9%80%A0-e-ink-%E5%B0%88%E7%94%A8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-x-%E6%94%AF%E6%8F%B4%E5%85%A8%E6%96%87%E7%BF%BB%E8%AD%AF%E5%B0%8D%E7%85%A7-9fd49e769b63)

關於步驟 1，由於有實作了 TwoPanelLayout ，在設定上更為簡便；步驟 2 和 3 在這次功能的實作上就可以直接跳過，只要將當下網頁的 url 當成參數帶入全文翻譯的網站就行。

以 Google Translate 網頁來說，它的網址支援下面幾種參數設定：

```
sl (source language)  
tl (target language)  
text (text content to be translated)  
// 新發現的參數  
u (web url to be translated)
```

所以，在舊有的實作上，只要省去原本的 text 參數，改為代入 u 的參數，就可以得到跟原始網頁長得一樣的翻譯結果，而且不用再額外考慮單純翻譯文字內容時，會有字數超過限制的問題，整份網頁都會被翻譯到。

如此一來，在對照閱讀上就更加方便。

### 網頁翻譯的結果畫面

![](/images/802683a34e4a/1_5XOoKB-hq0-hWSr6TyqfxA.png)
