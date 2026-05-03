+++
title = "快上加快 — EinkBro (14)"
date = "2021-09-16T11:47:07.064Z"
description = "原以為這麼小的一個 App，不到 3MB (扣除擋廣告的資料檔)的實作，既沒有任何的 tracking 機制，也沒有去網路抓任何非網頁內容的資料回來，理論上網頁載入速度要快到不行才對。"
slug = "快上加快-einkbro-14"
canonicalURL = "https://medium.com/@danielkao/%E5%BF%AB%E4%B8%8A%E5%8A%A0%E5%BF%AB-einkbro-14-290ebc6f1d3d"
mediumID = "290ebc6f1d3d"
tags = ["EinkBro"]
+++

### 快上加快 — EinkBro (15)

原以為這麼小的一個 App，不到 3MB (扣除擋廣告的資料檔)的實作，既沒有任何的 tracking 機制，也沒有去網路抓任何非網頁內容的資料回來，理論上網頁載入速度要快到不行才對。

但這半年來使用時，總覺得在切換網頁時，那條進度條總是會卡在 10% 的地方一下下，才有繼續往下進行。一開始以為是因為要去找每個 url 的 dns 位址，所以慢了半拍。但是別的瀏覽器又沒有這樣子的毛病。

### 移除造成載入緩慢的邏輯

終於！在昨天晚上陰錯陽差的解其他問題時，讓我仔細看到了 `updateProgress()` 的實作。看完後差點沒吐血。當 `WebView` 在載入網頁時，會不斷回報目前的載入進度，這時，這個函式就是用來更新相關畫面的。但它除了更新畫面的進度條外，竟然還做了很多意想不到的事情。

![](/images/290ebc6f1d3d/1_xX4dqHeSDR48bYNos5EA6g.png)

除了 1108 行到 1114 行是在更新進度條的呈現，1114 行的 `updateAutoComplete()` 是去資料庫中撈取新的資料出來，以備使用者要手動輸入網址時，可以提供相關的資訊；`scrollChange()` 則是在設定 `WebView` 的 `ScrollListener`。而 `HelperUnit.initRendering()` 是在檢查要不要把畫面顏色整個做反轉。

`updateAutoComplete()` 這件事，完全不需要在這邊出現。只要等使用者點下網址列，想要開始輸入時再去做一次就好了(如果那時候覺得有需要)。它被放在這邊，每次載入網頁，都會被呼叫許多次，在資料庫中不斷地查重覆的資料出來。如果使用者記錄了很多書籤，和瀏覽記錄已經累積了好幾百筆幾千筆的話，這樣子每個呼叫都要花不少時間。

這也難怪我會覺得每次在載入網頁時，進度列總是會卡住一下，因為 `updateAutoComplete()` 正在瘋狂地跟資料庫索取資料。把它移走後，果然速度就有了很大幅度的提升！

至於 `scrollChange()`，這種只需要在 `WebView` 生成的時候，或是網頁完全載入的時候呼叫一次就好的函式，我也把它搬到網頁載入完成後的邏輯中。

最後的 `HelperUnit.initRendering()` ，我就整段拿掉了。因為我的 EinkBro 已經把這功能拿掉了。

最終的實作變成這樣：

![](/images/290ebc6f1d3d/1_Z6SBpghx2Ro_TYKa8kNzXg.png)

### 限制歷史記錄的容量

剛剛提到造成載入速度慢的其中一點是：在更新 `AutoCompleteTextView` 所需的資料時，會去從資料庫讀取書籤和歷史記錄。在原本的實作中，歷史記錄是無上限的。

也就是說，如果你使用了 EinkBro 半年的話，你的 App 中包含了你這半年來的所有瀏覽記錄，這將會造成每次在讀取資料庫時，時間會愈來愈長。

為了解決這問題，我在每次新增瀏覽記錄時，會去把 EinkBro 中超過 2 週的歷史記錄刪掉。透過這方式來限制瀏覽記錄的無限增長。

---

做了這些改善後，就再也不用等候慢慢的載入速度啦！

### 參考版本

[Release Version v8.16.1 · plateaukao/browser](https://github.com/plateaukao/browser/releases/tag/v8.16.1)
