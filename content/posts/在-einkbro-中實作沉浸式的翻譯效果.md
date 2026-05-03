+++
title = "在 EinkBro 中實作沉浸式的翻譯效果"
date = "2023-05-20T11:27:51.081Z"
description = "前不久有人推出了 Desktop 上瀏覽器的 Immersive Translation Plugin，可以在看外文網頁時，以段落的方式翻譯內容。這種方式對於正在學習語言或是想要雙語對照著看的用戶來說，真的是一大福音。"
slug = "在-einkbro-中實作沉浸式的翻譯效果"
canonicalURL = "https://medium.com/@danielkao/%E5%9C%A8-einkbro-%E4%B8%AD%E5%AF%A6%E4%BD%9C%E6%B2%89%E6%B5%B8%E5%BC%8F%E7%9A%84%E7%BF%BB%E8%AD%AF%E6%95%88%E6%9E%9C-4b5a146b4e69"
mediumID = "4b5a146b4e69"
tags = ["EinkBro"]
+++

前不久有人推出了 Desktop 上瀏覽器的 [Immersive Translation Plugin](https://youtu.be/0nIzWCseLVo)，可以在看外文網頁時，以段落的方式翻譯內容。這種方式對於正在學習語言或是想要雙語對照著看的用戶來說，真的是一大福音。

雖然它很好用，但是在手機上有支援的瀏覽器 App 並不多。在 iPhone 上，Safari App 的 Plugin 可以安裝；但是在 Android 平台上，只有少數幾個選擇 : kiwi browser，或是用起來怪怪的 xBrowser。

想當然爾，目前 EinkBro 並不支援這 plugin 。如果想要支援的話，得要先整合 GreaseMonkey 相關的 API set 才有機會；不然，就是要自己參考它的方式，在 EinkBro App 中自己實作類似的功能。

---

後來我選擇了後者，因為目前的架構下，自己實作會是比較單純的。

### 大綱

- 利用原有的 Reader Mode
- 解釋整個流程
- Google Translate 的兩種實作方式

### 利用原有的 Reader Mode

在兩年前曾經介紹過怎麼在 EinkBro 中實作 Reader Mode：在 Firefox 中的 `readerview` 模組以及 `readability.js` 的協助下，EinkBro 可以為大多數的網頁提供乾淨的閱讀內容。

[打造 E-ink 專用的瀏覽器: Part V](https://medium.com/einkbro/%E6%89%93%E9%80%A0-e-ink-%E5%B0%88%E7%94%A8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-v-769216ef6db6)

當畫面元素只剩下核心的內容元件後，要支援沉浸式翻譯就相對上容易許多，因為 Reader Mode 的實作已經先對亂七八糟的 html elements 做了一次過濾，只留下含有文字的 html elements。

### 流程解釋

#### 流程圖

![](/images/4b5a146b4e69/1_9CfK3Q5EnbRnb9c-OHF_iA.png)

```
 sequenceDiagram  
    autonumber
```

#### 步驟

1. 當使用者按下 Immersive Translate 按鈕時，會先跟 WebView 傳達該要進入 Reader Mode 了。
2. 這時，WebView 會將 Readability.js 載入，並且請它把 html 內容過濾過濾，取出當中屬於本文的文字內容。
3. 回傳本文的文字內容
4. 要進入閱讀模式的話，這一步就可以直接顯示本文的文字內容；但是因為我們想要的功能是沉浸式翻譯，所以要再把拿到的文字內容交給 Jsoup 函式庫處理處理。這裡的處理指的是：4.1 為每個文字元件加上一個 to-translate 的 class name，然後還順手在它們的 sibling 加上一個 <p> 元件, 做為翻譯結果的存放處。4.2 對這些文字元件加上 visibility 的 listener。當它們出現在畫面上時，才需要去翻譯該段文字。
5. 回傳完成的整包結果
6. 讓 WebView，把整包結果顯示出來。(這時，lisener 開始在運作)
7. 為了讓 WebView 中 web 的 visibility event 能夠傳回 Android native 的實作中，這裡建了一個 class JsWebInterface。
8. callback 回來時，會呼叫 JsWebInterface 中的 getTranslation()，裡頭會呼叫已經實作好的 translate repository 的函式，拿到翻譯後的文字。
9. 翻譯好的文字會透過 evaluateJavascript 再帶回 Web 中。

---

#### 相關程式碼

步驟 4 中的 Jsoup 處理方式如下。行 4 ~ 10 就是在加 tag 和補一個 <p> 的元件。行 15 則是加入 visibility listener 。

![](/images/4b5a146b4e69/1_uXH8HQWq9VoyPWzzSLDzzg.png)

下面是載入的 Javascript。行 8 建立了一個 IntersectionObserver，並在 31行為每個文字元件加上這個 observer。

行 12 判斷 entry 被顯示時，會在行 17 呼叫 bridge 的函式 getTranslation()，等結果回來時，行 1 的 myCallback 會被執行，將翻譯好的內容帶入之前建立好的 <p> 元件。

![](/images/4b5a146b4e69/1_vuxxxcbmX-X_n_XjkGb3fg.png)

接下來，我們來看看步驟 8 中的 getTranslation() 函式。下圖中的行 7 出現了 Semaphore！為什麼這邊要使用 semaphore 呢？因為通常在捲動畫面時，常常會讓多個段落一下子顯示在畫面上，如果讓他們一個接著一個去取得翻譯，整體的反應時間會比較久。所以，在這邊設定了 semaphore 4，希望段落翻譯可以盡量地同步進行。

行 16 呼叫了 Google Translate 的實作。當翻譯結果回傳時，會被存在 translatedString 中，在行 23 處再利用 webView.evaluateJavascript 將這結果送回 web 的 callback 中。

![](/images/4b5a146b4e69/1_bM30JOj3FR5HSXYyahCutg.png)

---

### Google Translate 的兩種實作方式

嚴格來說，應該是有三種方式：

1. 付費去申請 Google Translate API 的使用權，依使用量付費
2. 利用 http request 去呼叫 Google Translate 網頁，把取得的網頁內容做處理，取出其中翻譯的結果
3. 利用網路上其他人發現的方式，呼叫 Google Translate API

第一種方式請大家參考 Google 官網的介紹就好。

[Cloud Translation documentation | Google Cloud](https://cloud.google.com/translate/docs)

在 EinkBro 中，先是使用第二種方式，後來改成第三種。在這邊分別來說說實作的方式。

#### **採用 Google Translate 網頁**

- 行 25: 因為實作裡的 okhttpclient 是以 callback 的型式回傳結果，這裡使用的是 suspendCancellableCoroutine，它可以把 callback 的用法包裝成一般的 suspend function，方便呼叫的人使用。
- 行 26: 可以看到，這裡使用的是一般的網頁連結 https://translate.google.com。代入需要的參數後(最重要的是 q，它的值就是想翻譯的字串)
- 行 39: 將組好的 url 交給 okhttpclient 去處理
- 行 50: 取出 body 內容，交給 Jsoup 處理。Google Translate 網頁中，會把翻譯結果放在 `result-container` 的 html element 中。只要能從其中取出文字，就表示翻譯成功。

![](/images/4b5a146b4e69/1_DIRQHF_p57XnKvRiWpF4Xw.png)

#### 採用網路上找到的 Google Translate API

新的實作方式，除了改用 API 外，也移除了原先的 callback 實作，看起來更加簡潔。

- 行 70: 一樣要利用 HttpUrl 建立 url，但這次使用的是 translate.googleapis.com。然後這裡有個神奇的參數(client=gtx)，加上後就可以正常取得翻譯結果。
- 行 88: 換成 coroutine 的方式去打 API
- 行 93 ~ 98: 從 response 的 json 中，取出翻譯文字。這邊的實作有點醜，因為當時還沒有引入任何 json parsing 的函式庫。之後應該會再小小地改寫一下吧。

![](/images/4b5a146b4e69/1_xl0ee2x_bKts9NN_v0vacQ.png)

### 示範畫面

![](/images/4b5a146b4e69/1_7L2hB6RN7BlIMut1r3G6Wg.jpeg)

![](/images/4b5a146b4e69/1_pULaJvWGuekMvqmcrEpFeA.jpeg)

### 相關連結

開始支援的版本 v10.3.0

[Release Release v10.3.0 · plateaukao/einkbro](https://github.com/plateaukao/einkbro/releases/tag/v10.3.0)
