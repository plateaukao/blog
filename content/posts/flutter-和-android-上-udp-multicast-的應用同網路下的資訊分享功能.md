+++
title = "Flutter 和 Android 上 UDP Multicast 的應用：同網路下的資訊分享功能"
date = "2022-05-19T16:07:15.766Z"
description = "用 Flutter 開發出來的 Sharik APP 是個可以安裝在多平台( Android, iOS, Windows, Mac, Linux) 上的軟體，可以在同個網路下快速地分享字串、檔案，甚至是 Android App 上已經安裝的軟體 apk。"
slug = "flutter-和-android-上-udp-multicast-的應用同網路下的資訊分享功能"
canonicalURL = "https://medium.com/@danielkao/flutter-%E5%92%8C-android-%E4%B8%8A-udp-multicast-%E7%9A%84%E6%87%89%E7%94%A8-%E5%90%8C%E7%B6%B2%E8%B7%AF%E4%B8%8B%E7%9A%84%E8%B3%87%E8%A8%8A%E5%88%86%E4%BA%AB%E5%8A%9F%E8%83%BD-751ea08c1921"
mediumID = "751ea08c1921"
[cover]
  image = "/images/751ea08c1921/1_ueMy4iBa8dn-Gu8fui5A-Q.png"
+++


用 Flutter 開發出來的 [Sharik APP](https://github.com/marchellodev/sharik) 是個可以安裝在多平台( Android, iOS, Windows, Mac, Linux) 上的軟體，可以在同個網路下快速地分享字串、檔案，甚至是 Android App 上已經安裝的軟體 apk。

![](/images/751ea08c1921/1_ueMy4iBa8dn-Gu8fui5A-Q.png)

它很有效地解決了在同個網路下多個設備間的訊息交換需求。因為是用 Flutter 開發的，所以我的 iMac, mac mini, Macbook pro，Android 手機們，Android 電子書閱讀器們，都能隨時開啟功能，將當下的網址、文件，甚至是在使用中的 APP apk 檔案，很方便地傳送到另一台設備去。

不過，Sharik APP 中的實作不是很有效率。**在發送端的設備**，它寫了一個簡易的 Web Server，可以處理 sharik.json 的 request，傳出設備的一些基本資訊，以及想要傳送的字串；而 base url path `/` 則是會回傳想要傳送的檔案或 apk。

**在接收端的設備**，為了找到同個網路下哪個 IP有開啟 Web Server 可以用來取得資料，它的作法是先查出自己的 IP 為何，然後產生所有 local subnet 的 IP 列表，對著這些 IP 一個一個去 ping ping 看，看有沒有 timeout，沒有的話就放到一個清單中。然後再針對這個清單的 IP 發出 http request，看能不能取得 sharik.json 。可以的話就表示對方有在分享資料，這時，就會把這些資料傳給 UI 去呈現，讓使用者可以確認後點擊，然後帶到瀏覽器去做下載的行為。

發送端沒有什麼太大的問題，但接收端的作法很暴力。上面描述的邏輯是塞在同一個函式中，用 Flutter 的 compute function 包住，每隔一兩秒就會再執行一次；在搜尋的過程中，一直重覆著同樣的 ping -> fetch sharik.json 。

![](/images/751ea08c1921/1_aSvguKIoaRLGByfBBIbT8w.jpeg)

![](/images/751ea08c1921/1_Xgn4Mf-8GEJ9uVWxF7FbFw.jpeg)
*原本的發送端與接受端實作*

### 調整 Sharik App 的作法

後來，在朋友的提示下，我把整個機制改成 UDP multicast 來實作：在發送端開始分享時，每隔一秒對同個網路發出 broadcast ，直接送出 sharik.json 的內容；在接收端的設備，也是註冊了同一個 multicast 網路，然後 listen ，等著看是否有訊息進來。如果有的話，就直接可以 parse 然後呈現在 UI 上。

這作法少了很多不必要的邏輯，重點是在接收資料時，比原先有時收得到有時收不到的效果好太多了。通常一按下接收，資料就進來了。

![](/images/751ea08c1921/1_HhCbRIqPbBzP7J-o3oA2TA.jpeg)

![](/images/751ea08c1921/1_SdNHq8Wdj24CJSLugR4FtQ.jpeg)
*修正後，導入 multicast 的實作方式*

以下是發送端的作法：

![](/images/751ea08c1921/1_v_pggkWRtAK0JcHrGA-AZw.png)
*Sharing Service*

55, 56 行是 bind 到一個 Socket 上，

57~64 行是後來多加的，可以用來知道遠端是誰接收了這資料。

67~70 行則是簡單地利用 Timer 定期透過 Socket 發送訊息出去。

接收端的實作也很單純：

![](/images/751ea08c1921/1_EbbRpgTgoGgV-nkU_pR1LA.png)
*Receiver Service*

41 ~ 43 行是 bind 到同個 Multicast 上。

45 ~ 64 行則是在收到 socket 傳來的 datagram 時，針對內容做些資料的處理。

50 ~ 54 行是在處理當 datagram 資料字串是 http 開頭時，這情況應該就是由 EinkBro 送來的，所以可以把內容當成是 url，直接叫 UI 呈現出來。

55 ~ 60 行就是收到 sharik.json 後的處理。

這邊之所以要特別針對 EinkBro 做處理的原因是：我也把這整套機制加到 EinkBro 中了！如果只是單純要傳網址，或是設備只想拿來當接收端的話，完全不需要再安裝 Sharik APP。只要打開 EinkBro，再點接收資料的按鈕就行了。

### EinkBro 的實作

下面就也來講講在 EinkBro APP 上的實作。主要可以分成兩部分來說，一個是 UI 的呈現，一個是底層網路的操作。

UI 部分，我先是做了兩個 Dialog (如下)：

![](/images/751ea08c1921/1_nCsy86hyIA04kDgZCJv1Ug.png)
*SendLinkDialog*

![](/images/751ea08c1921/1_I4pgeHNfg2JfmEQM6de5Ng.png)
*ReceiveDataDialog*

從 EinkBro APP 中，只能分享網址，所以它的分享畫面只是一個單純的對話框，中間有個轉不停的 progressbar 。想要接收資料時，也是先顯示一個對話框，一旦收到資料後，不論是收到字串，檔案，或是 apk，其實都是要透過**分享端**的 http server 來下載，這時，只要把 url 代入 EinkBro 中，就能很自然地串到下載的邏輯。

我們再來看看 ShareUtil 中的 幾個函式是如何實作的：

![](/images/751ea08c1921/1_j4Ui_Or_7eT1h3QbAAtlyQ.png)
*ShareUtil*

26, 25 行的 multicast IP還有 port 都是跟 Sharik APP 中使用一樣的值；這樣能確保兩者間能夠相通。

`startBroadcastingUrl()` 在 17 行建立好 multicast socket 後，每隔一秒會發出想要分享的網址。

![](/images/751ea08c1921/1_MOTB49-y4rtUuG2ItUR2VQ.png)
*startReceiving*

如果是接收端的 EinkBro，也是一樣會先生成 multicast socket，然後處理收到的 datagram 字串。`handleSharikScenario` 只是做做 json parsing 的邏輯，這裡就不特別說明了。

如此一來，兩台設備間的 EinkBro 就也可以很方便地傳送網址了。我大部分的網頁瀏覽都是在電子紙閱讀器上的 EinkBro 完成的，但有時看到一些 Youtube 網址的分享，或是有比較多圖片的網頁時，還是會想要用一般的手機來閱讀。這時，我就能很快地利用兩台設備的 EinkBro 交換網址，無縫繼續使用。

或許有人會說，為什麼不用 Chrome 或是 Firefox 這類瀏覽器，它們都可以登入帳號，然後你在哪台設備上做的事，也可以很快地在別台設備上看到。雖然它們可以滿足一部分類似的需求，但它們做不到傳檔案的需求，而且，它們的任何操作都是要經過 cloud 的。

目前在 Sharik APP 和 EinkBro 中，是完全沒有 tracking 的機制在的，沒有什麼行為資訊會被送到遙遠的遠端做分析。我自己用起來比較開心。

### **相關連結**

Forked 而且改過的 Sharik APP

[GitHub - plateaukao/sharik: Sharik is an open-source, cross-platform solution for sharing files via…](https://github.com/plateaukao/sharik)

已經發了 commit，但還沒發行最新版的 EinkBro repo

[GitHub - plateaukao/browser: An Android web browser based on webview, which is specialized for…](https://github.com/plateaukao/browser)

Sharik APP 調整實作的前後 Sequence Diagram

[Refactoring of Send Receive Mechanism · plateaukao/sharik Wiki](https://github.com/plateaukao/sharik/wiki/Refactoring-of-Send-Receive-Mechanism)
