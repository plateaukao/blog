+++
title = "開啟 LINE LIFF v2 的無限潛力 — liff.shareTargetPicker()"
date = "2020-09-28T16:34:29.057Z"
description = "從 LINE LIFF 開放使用以來，一直不斷有在更新 API。去年底 v2 正式上線，然後在今年三月多官方開式有文件介紹怎麼使用新的 API — shreTargetPicker()。關於基本的 LIFF App 設定，可以參考本文最下面列的參考資料，在這邊就不多說了。"
slug = "開啟-line-liff-v2-的無限潛力-liffsharetargetpicker"
canonicalURL = "https://medium.com/@danielkao/%E9%96%8B%E5%95%9F-line-liff-v2-%E7%9A%84%E7%84%A1%E9%99%90%E6%BD%9B%E5%8A%9B-liff-sharetargetpicker-24b47b0b4252"
mediumID = "24b47b0b4252"
+++

### 開啟 LINE LIFF v2 的無限潛力 — liff.shareTargetPicker

從 LINE LIFF 開放使用以來，一直不斷有在更新 API。去年底 v2 正式上線，然後在今年三月多官方開式有文件介紹怎麼使用新的 API — shareTargetPicker。關於基本的 LIFF App 設定，可以參考本文最下面列的參考資料，在這邊就不多說了。

#### 今天要來談談強大的 shareTargetPicker API 的應用。

大家都知道，現在如果從其他 App 分享連結到 LINE app 中的話，通常是以純文字的方式呈現在聊天室中。雖然 LINE app 已經有做了簡單的 Url Meta Data fetcher，將連結內的主題和內文和圖片抓回來顯示，但是介面實在是很過時，而且遇到有些網站喜歡把中文字放到網址中，然後分享到 LINE 裡時，又會經過 UrlEncoding，造成一大串完全不知道在寫什麼的網址時，看到那麼一大段不可讀的 url 字串，實在是令人很無言。

既然分享這些連結的重點是網頁裡頭的內容，為什麼在 LINE 聊天室中針對分享的連結，在呈現時不是以內容為主體，而是把一般人看不懂的連結文字顯示出來呢？

![](/images/24b47b0b4252/1_zjy4NEztsBMtIMPoSl_Gqw.png)

這個想法在我腦中存在了很久，直到有一天我突然想到，這不是可以透過 LINE LIFF 的 shareTargetPicker() API 來解決嗎？

---

### 架構

作法大致如下：

![](/images/24b47b0b4252/1_8d0u4g08Wv2XcMbRIV32_Q.png)
*第一步，建立 LIFF App 和 LIFF API Server*

#### 第一步

建立一個可以輸入 url 的 LIFF App，在按下 Get Preview 按鈕時，它會去問 LIFF API server 關於這個 url 相關的 meta data。等到拿到資料後再呼叫 shareTargetPicker API，讓使用者可以選擇把資料分享到哪個聊天室。這時，我們可以把拿到的 meta data (title, description, image)用好看的 flex message 包裝起來，在該聊天室中呈現。效果大概如下：

![](/images/24b47b0b4252/1_74yJL892LauRdbyGR1lqOg.gif)

由於我的 LIFF API Server 是用 python 的 flask framework 寫的，在取得 meta data時，是透過 opengrapher 這個 package 完成的：

![](/images/24b47b0b4252/1_W_QnXJgGAQc3L3hZemtOwg.png)
*parse url meta data*

利用 liff 送出 flex message 的方式如下面程式碼：在52行的 `previewUrlInfo()` 會將取回的 meta data 存到 global variables；然後 143 行會拿現有的 flex message template與 global variables 組在一起，送出訊息。

其他程式碼是基本的 liff 操作，可以參考文章最下方附的連結說明。

[View gist](https://gist.github.com/plateaukao/fa85c20bae6d30f954e2ad799ec872b8)

當 LIFF App 上線後，就可以透過它送出漂亮的 Flex Message，而不再是醜醜的純文字連結。但是這時仍然有一個很大的問題：每次要分享連結前，都要特地找到 LIFF App 的連結，在 LINE App 中將它打開；把連結貼上，取得相關資料，再選擇要送往的聊天室。這過程中包含的步驟太多了，不會有人想要這麼做分享的。

所以，需要再加上第二步。

#### 第二步

![](/images/24b47b0b4252/1_EyQfNNHejn1GmoZpoMDOAg.png)
*第二步，整合負責處理大部分流程的 native App*

建立一個 Android App (或 iOS App，但我還沒空寫 iOS App)，這裡稱它為 LINE Share，讓它負責：

1. 從其他 App 那兒取得 url ；
2. 把 LINE App 叫起來，並自動開啟 LIFF App；
3. 將取得的 url 貼進 LIFF App，讓 LIFF App 自動去抓取 meta data，抓到自動開啟share target picker 的 UI。

第一點很容易，是 native app 很普通的應用。在 Android 下，只要在 AndroidManifest.xml 中的 Activity 區段加入以下的 intent-share 設定，

![](/images/24b47b0b4252/1_FJffnKlo1Lts6ndfCt7ahQ.png)

第二點則是在 Activity 的實作中去處理來自 `ACTION_SEND` 的 `Intent` 就可以了。

[View gist](https://gist.github.com/plateaukao/4e21546deee955833ec4eba2288c0757)

讓我們來看一下從其他 App 中分享的整個流程：

![](/images/24b47b0b4252/1_8F71PmCtkRo_WJmvHMVttA.gif)
*LINE Share App Demo*

到這邊，整個應用就已經蠻完整的了。但是，你以為到這邊就結束了嗎？其實在 Android 平台還能加入更方便的使用方式。

#### 更上一層樓的第三步

有些時候，並不是每個 App 都會提供系統介面的分享畫面，舉一個例子來說，下面這張圖是 LINE Today 文章的分享方式：

![](/images/24b47b0b4252/1_E3N0K56P9hesbY4kmCuztg.png)
*LINE App 中的 LINE Today 新聞文章畫面*

它只提供了客製化的 LINE 分享， Facebook 分享， Keep 儲存，和複製網址四個選項。前三者都是單純的分享文字連結。如果要透過第二步寫好的 LINE Share App的話，勢必得要選複製網址，然後再回到 Home，開啟 LINE Share App，貼上 url，進行分享。這樣子的流程還是很麻煩。

因此，我們可以利用 Android 提供的 Quick Tile Setting來解決這問題。Quick Tile Setting 是在 Android 7.0 開始推出的功能，讓 App可以在通知欄中加入自己 App 相關的 Tile，讓使用者可以快速開關一些功能，或是叫起常用的畫面，詳細說明可以參考下面這篇文章：

[Quick Settings Tiles](https://medium.com/androiddevelopers/quick-settings-tiles-e3c22daf93a8)

我們先在 LINE Share App 的 AndroidManifest.xml 中加入所需的 Service 設定

![](/images/24b47b0b4252/1_KEx0rpnptmCOkFLcoywU1A.png)

然後建立 LiffSharetileService 這個 class ，加上在被點擊時想要處理的方式(叫起 LINE Share App 的畫面)

[View gist](https://gist.github.com/plateaukao/da4bfa4bb97457d9e13e1737ab33ba3c)

當 LINE Share App 被喚醒時，它必須去查看是否現在在 Clipboard 中有資料，有的話(表示剛剛使用者複製了某些資料)，就直接接回第二步，處理資料的邏輯。要檢查 ClipBoard 是否有資料，可以在 `Activity` 的 `onWindowFocusChanged` 函式中實作

[View gist](https://gist.github.com/plateaukao/a519855748f4360d13e03594c7cf7703)

完成 Quick Tile 的實作後，就可以從通知欄的設定中，把這個新增的 Tile 拉到比較前面的位置，方便之後使用。讓我們再來看一次有 Quick Tile的操作方式。

![](/images/24b47b0b4252/1_zGz8treCl6dCcYvJAupnqA.gif)

---

還有沒有可以改進的地方呢？當然有啊。其實我最想解決的是下面這個情況：每次分享 Facebook 的連結時，因為現在 Facebook 很機車，一定要登入它才能讓你抓到連結相關的 meta data。如果把下面的連結貼到一個未登入的瀏覽器中，它只會顯示要你登入的畫面。

這問題有沒有解呢？如果你想要分享的 Facebook 連結的瀏覽權限是地球的話(所有人都可以看)，那其實有辦法抓到相關的 meta data的。

![](/images/24b47b0b4252/1__riQY_lKV2JjL7r6hO5MwA.png)

原本以為必須要透過 Facebook API 或 SDK 才可以拿到相關資料，但查了一輪之後，發現似乎串了 Facebook API 也無法拿到文章的 meta data。但網路找了一輪之後，終於在某個地方找到解決方式。目前 <https://mobile.facebook.com/> 可以在沒有登入的情況下看到所有人可見的 facebook 文章。於是，只要把任何 facebook 的 url 的 host 換成 `mobile.facebook.com`，就可以順利地抓到所需的文章 meta data。

[View gist](https://gist.github.com/plateaukao/f8c3392e9f87f76f9a3de0d59b8a0c7b)

在一開始介紹到的 `previewUrlInfo` 中，先判斷 url 的 host 是不是來自於 facebook，如果是的話，先把它換成 `mobile.facebook.com`，再去抓資料，就可以抓到了。效果如下：

![](/images/24b47b0b4252/1_zLtyytwXuYiegrrY-nmhPg.gif)

以上，是 liff.shareTargetPicker 的小小應用。透過少少的程式碼實作，即可有效提升資訊分享的效果。

希望在未來可以看到更多關於 liff.shareTargetPicker 的有趣應用。

### **網站連結**

#### 可以在網站登入 LINE 帳號，直接 Share Flex Message 的網站

(Heroku 很脆弱，請大家不要打掛它)

使用方式：

1. 先點 Login，登入 LINE 之後，
2. 貼上想分享的連結，按下 Get Preview
3. 如果下面有正常出現 title, description 和縮圖的話 (有時會抓不到，要看網址)，再按下 Open ShareTargetPicker 按鈕。
4. 選個聊天室，送出訊息。

[Share Url Content Message](https://message-preview-liff.herokuapp.com/)

#### LINE Share App 原始碼

[plateaukao/liff\_url\_share\_app](https://github.com/plateaukao/liff_url_share_app)

### 參考資料

以下是一些官方文件可以參考基本的設定和使用方式：

[LIFF v2 新增支援外部瀏覽器與二維條碼掃描器等功能 - LINE ENGINEERING](https://engineering.linecorp.com/zh-hant/blog/liff-our-latest-product-for-third-party-developers-ch/)

[Share Target Picker 已經公開，透過 LIFF 來分享訊息將更加的便利 - LINE ENGINEERING](https://engineering.linecorp.com/zh-hant/blog/liff-share-target-picker/)

[在 Vue3 中引入 LIFF 的 ShareTargetPicker 分享 FlexMessage 訊息給 LINE 好友 - LINE ENGINEERING](https://engineering.linecorp.com/zh-hant/blog/how-to-use-liff-in-vue3/)

另外關於 LIFF v1 的介紹，也可以看一下我很久以前寫的一篇文章：

[初探 LINE Message API 的新功能 LIFF](https://medium.com/@danielkao/%E5%88%9D%E6%8E%A2-line-message-api-%E7%9A%84%E6%96%B0%E5%8A%9F%E8%83%BD-liff-51d5e7ff1a6a)
