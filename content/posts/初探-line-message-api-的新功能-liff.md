+++
title = "初探 LINE Message API 的新功能 LIFF"
date = "2018-06-07T17:52:13.338Z"
description = "LIFF 全名是 LINE Front-end Framework，一個可以在 LINE app 內運作的 web app 平台，可以在對話視窗中，不需要另外加入 bot 就直接使用，比 bot…"
slug = "初探-line-message-api-的新功能-liff"
canonicalURL = "https://medium.com/@danielkao/%E5%88%9D%E6%8E%A2-line-message-api-%E7%9A%84%E6%96%B0%E5%8A%9F%E8%83%BD-liff-51d5e7ff1a6a"
mediumID = "51d5e7ff1a6a"
+++

![](/images/51d5e7ff1a6a/1_L9UaB0W_2OaGhF71UX60EA.jpeg)
*小烏來*

LIFF 全名是 **LINE Front-end Framework**，一個可以在 LINE app 內運作的 web app 平台，可以在對話視窗中，不需要另外加入 bot 就直接使用，比 bot 更加方便﹙雖然目前還是有些限制，後面會提到﹚。但由於它才剛推出沒多久，沒有太多官方以外的線上資源，只能參考下面的日文文章，再加上自己摸索。

昨天 (6/6) 在日本 LINE Engineering blog 看到了一篇在介紹 LIFF 實作範例的文章 (<https://engineering.linecorp.com/ja/blog/detail/299>)，之前剛好有申請了一個 channel，想說也來照著實作來看。

簡單來說要建立一個 LIFF web app ，需要下面幾個步驟：

1. 建立一個具有 Message API 權限的 LINE channel。
2. 取得 channel 的 token，用它來註冊 LIFF web app 取得一組 LIFF app id。
3. 參考官方 Github 的範例，開始寫 code。

關於第一點，在這裡就不詳述了，有了 channel 之後，channel token 可以從 [https://developers.line.me/console/channel/your\_channel\_id/basic/](https://developers.line.me/console/channel/1488346112/basic/) 中的 **Messaging settings** 中取得，然後執行以下的指命，拿到 LIFF app id。

```
curl -XPOST \  
-H "Authorization: Bearer YOUR_CHANNEL_TOKEN" \  
-H "Content-Type: application/json" \  
-d '{  
    "view": {  
        "type": "LIFF_SIZE",  
        "url": "URL_OF_YOUR_APPLICATION"  
    }  
}' \  
https://api.line.me/liff/v1/apps
```

**YOUR\_CHANNEL\_TOKEN** 剛剛取得的 channel token。

[**LIFF\_SIZE**](https://developers.line.me/en/docs/liff/reference/#view-object)這個 web app 可以有三種大小，分別是 compact (佔畫面 50%)，tall (80%), full (100%)。

**URL\_OF\_YOUR\_APPLICATION** web app 實際的網址。

一切順利的話，上面的指令很快會回傳一個 registration id 給你

```
{"liffId":"1234567890-XXXXXXXX"}
```

有了上面的 id，就可以在一般的 LINE 聊天視窗中輸入下面的連結，點下去就會開啟 LIFF 的畫面。

`line://app/1234567890-XXXXXXXX`

接下來，就可以照著上面的日文網誌一步步建立起 web app，或是直接 clone 文章最下面的官方範例，馬上可以看到 LIFF 所有支援的功能。

下面就是改良版 painting 的 LIFF web app 畫面。

![](/images/51d5e7ff1a6a/1_GMVSV0qdslS4fNt2_XpDtQ.png)
*size 為 tall 的畫面大小*

我用的 LIFF\_SIZE 是 tall，讓 web app 跳出時畫面夠大，又不致於蓋住整個聊天視窗。再經過一翻改良後，可以如下圖，輸出透明的字跡到聊天視窗中。比起呆板地輸入文字，用手寫的是不是更有誠意呢？

![](/images/51d5e7ff1a6a/1_hZT8X62jQOI0JZJSS2jkVw.jpeg)
*左：手寫內容，點擊 Share；右：內容會被送出到對話視窗中。*

在文章一開始有提到，儘管 LIFF 可以在聊天室窗中直接使用，不需要事先加入 bot，但有個缺點是它一定要透過 url 被啟動。也就是說，在一個對話視窗中如果要啟動 LIFF，就得先把 LIFF 的 url 輸入，然後再去點擊它才行。隨著聊天視窗中的對話訊息不斷增加，原先輸入的 LIFF url，可能會被推擠到很上方。這時，可以透過 LINE 前一陣子推出的公告置頂功能來快速定位到 LIFF url，方便再次啟動。

### 踩雷

手寫功能雖然很新奇，但如果每次想要輸入一樣的內容，都得再寫一次，那就不有趣了。所以我打算在原先的功能裡，增加可以顯示之前寫過的畫面。已經寫過的字，只要用選的就好，不用再重新寫一次，等於是有了自己的手寫圖庫。

最初的想法是在最下方的按鈕列加上一個 List 按鈕，只要點擊它就會進到另一個網頁，拿著 LIFF javascript library 給我的 userId 去把這個使用者事前寫過的圖片都撈出來。所以我在 List 按鈕被點擊時，呼叫了下面的 javascript，進到另一個實作好的網頁。

```
location.href = './list';
```

實際測試，畫面是切過去了沒錯，但跟 LIFF 相關的參數卻都抓不到，函式也呼叫不了。LIFF API 中有個 [openWindow()](https://developers.line.me/en/docs/liff/reference/#liff-openwindow) 的函式，試了也一樣不行。看來 LIFF 被啟動時，就只能在當下使用 LIFF 相關的功能，一旦換了連結，即使是同一個 domain 下的 url，也無法再使用 LIFF 的 library。

由於 LIFF javascript library 只有在 LINE 裡被啟動時才有作用，每次要測試時，一定要先把 server 上的程式碼更新好，然後進入 LINE 中實際操作看效果。如果有什麼功能不如預期般運作，不能用 Chrome debugger tool 來除錯，實在是很痛苦。只能不斷地 try and error。

無奈之下，只好改變作法。點擊 List 按鈕後 ，把用來手寫的 canvas element 隱藏住，然後直接在按鈕列下面顯示之前手寫過的圖片。

![](/images/51d5e7ff1a6a/1_uyBKHK_fI7hQ0wjeGpgTjg.png)

畫面很陽春，不過想要的功能完成了，可以很快速地從之前的圖片中點選一張，送出圖片。如果使用者是個很會畫圖的人，用了這個 LIFF web app，不用上架 LINE stickers 也可以很快地就產生出一組自己專屬的貼圖。

### 結論

LIFF 可以讓開發者很快地實作出與使用者互動的 web app，從使用者端得到 input 後，把處理完的結果馬上顯示到當下的聊天視窗中。未來應該陸陸續續會有各種有趣的小應用出現。

目前開發除錯不是很方便，如果能針對開發環境提供 LIFF dummy js library，讓開發者在沒有 LINE 的情況下，也可以很方便地測試 web app 功能，相信會有更多人願意開發相關的應用。

### 補充

在某些朋友的 iPhone 上無法正常運作，後來調查之後，發現有些版本的 mobile safari 會對以下的 javascript 報錯：說程式中宣告了跟 global 一樣的canvas 變數會造成 shadow effetct，造成網頁無法再正常運作。後來把變數名稱改成 canvasElement 之後，朋友的 iPhone 就可以使用了。

![](/images/51d5e7ff1a6a/1_sefv1tdjVGMzmre1XZCeyg.png)

參考連結：

1. [官方開發文件](https://developers.line.me/en/docs/liff/registering-liff-apps/)
2. [官方範例](https://github.com/line/line-liff-starter)
3. [Signature Pad](https://github.com/szimek/signature_pad)

### 延伸閱讀

[pylineliff](https://medium.com/@danielkao/pylineliff-37479d1814d8)
