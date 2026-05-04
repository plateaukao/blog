+++
title = "從 Android WebView 中取得點選連結的文字"
date = "2022-06-05T13:28:04.927Z"
description = "在用 WebView 開發瀏覽器時，一個很常見的功能是：長按連結時，會跳出 ContextMenu Dialog，提供針對這個連結的一些功能。大部分的瀏覽器都會包含像是開新分頁，在背景開啟分頁，分享連結網址等等的選項。"
slug = "從-android-webview-中取得點選連結的文字"
canonicalURL = "https://medium.com/@danielkao/%E5%BE%9E-android-webview-%E4%B8%AD%E5%8F%96%E5%BE%97%E9%BB%9E%E9%81%B8%E9%80%A3%E7%B5%90%E7%9A%84%E6%96%87%E5%AD%97-a965cd64365e"
mediumID = "a965cd64365e"
[cover]
  image = "/images/a965cd64365e/1_zjJy4xe6yBZo2TnYjbripQ.png"
+++


在用 WebView 開發瀏覽器時，一個很常見的功能是：長按連結時，會跳出 ContextMenu Dialog，提供針對這個連結的一些功能。大部分的瀏覽器都會包含像是開新分頁，在背景開啟分頁，分享連結網址等等的選項。

有些時候，除了連結外，如果也能夠取得被點選的連結的字串那就更好了。因為使用者的本意可能是想要看到的字串，而不是它真正的連。

在經過一番尋找後，找到了一個特別的用法，在此記錄下來。

[https://developer.android.com/reference/android/webkit/WebView#requestFocusNodeHref(android.os.Message)](https://developer.android.com/reference/android/webkit/WebView#requestFocusNodeHref%28android.os.Message%29)

WebView 有個函式叫 requestFocusNodeHref(), 它會回傳下面三個值：

- url: anchor 的 href 值
- src: 圖片 src d 值
- title: anchor 的字串

其中的 title 就是我想要取得的資料。requestFocusNodeHref() 的使用方式有點間接。下面列出我在 EinkBro 中的實作：

![](/images/a965cd64365e/1_zjJy4xe6yBZo2TnYjbripQ.png)

1 行寫到，必須建立一個 Message 物件，並餵給它 target，然後，它會在 handleMessage 的 callback 函式中，傳回我們要的資料。拿到後，再去做後續的處理。因為我只需要 anchor 的文字，所以我只拿取了 title 而已。

順利拿到字串後，接下來不論是想要 copy 這個字串，或是將連結建立成新的書籤，都能更方便地進行了。

### 相關連結

[fix: when new tab is not loading in background, need to get the title... ·…](https://github.com/plateaukao/browser/commit/bf293128e53f9bb221eae5301530da9e6be1584b)
