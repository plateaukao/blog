+++
title = "升級 EinkBro 的廣告阻擋機制"
date = "2024-11-06T13:59:44.924Z"
description = "新版的 EinkBro 在經過一番努力後，即將支援 EasyList 格式的廣告清單，除了阻擋一般廣告外，還可以隱藏其區塊，甚至是去除一些常見的 tracking 機制。"
slug = "升級-einkbro-的廣告阻擋機制"
canonicalURL = "https://medium.com/@danielkao/%E5%8D%87%E7%B4%9A-einkbro-%E7%9A%84%E5%BB%A3%E5%91%8A%E9%98%BB%E6%93%8B%E6%A9%9F%E5%88%B6-5f3756c4b3af"
mediumID = "5f3756c4b3af"
+++

![](/images/5f3756c4b3af/1_X6JIDNNT32UJOH8Hn2mfdA.png)

新版的 EinkBro 在經過一番努力後，即將支援 EasyList 格式的廣告清單，除了阻擋一般廣告外，還可以隱藏其區塊，甚至是去除一些常見的 tracking 機制。

---

原先 EinkBro 的廣告阻擋機制比較陽春，採用的方式是定期抓取 `<https://github.com/StevenBlack/hosts>` 上的 adblock 清單，在載入網頁時，會檢查每個 WebResourceRequest 的連結是不是來自於這份清單中的項目；是的話就傳送一個 dummy response 給 WebView，讓它既不會去浪費頻寬抓廣告，也不會在畫面上呈現出來。

一直以來這方式都還做得不錯，能擋掉大部分我原先看得到的廣告。不過，總還是有些小缺憾，像是廣告雖然看不見了，但通常它還是會在畫面上留下一塊空白，造成需要多捲動一些才能跳過廣告版面。

為了讓廣告阻擋的效果能更好，勢必得要導入更好的機制，讓這個機制能夠適度地去調整網頁的內容，把不必要的元素移除或隱藏。

---

### 找尋合適的方案(現成的作法)

在找了一陣子後，覺得 <https://github.com/Edsuns/AdblockAndroid> 這個 repository 還蠻完整的，實作了 [EasyList](https://easylist.to/) 和 [Adguard](https://adguard.com/kb/zh-TW/general/ad-filtering/adguard-filters/) 的過濾方式；程式碼大部分採用 c++ 開發的，理論上在執行的速度會比 Java/Kotlin 的版本還有效率；而且原始的實作是從開源的 brave 程式碼來的，應該在穩定度上也會不錯(吧？)。

這專案最後的 commit 是在 2021 年 8 月，已經三年多沒更新了。不過，我還是試著把它調整一下，讓它再度能在現在的開發環境以及各種最新的函式庫下運作。相關的調整可以看這支 commit:

[make it buildable on newer libraries · plateaukao/AdblockAndroid@2d819ae](https://github.com/plateaukao/AdblockAndroid/commit/2d819aed055e77d3538d00016a1ff7a359251a25)

### 與 EinkBro 整合

能將別人的 example app 成功編譯和執行是一回事，要能整合到自己的專案中，又是另一回事啦。

底下這第一支整合的 PR，一次塞進來了 19225 行的程式碼(主要為兩個函式庫 ad-filter 和 adblock-client。後者大多是 c++ 實作)，程式碼大部分是我已經看不大懂的 c++ filter implementation。雖然它看似能動，能正常運作，但還是抖抖的。

整合進來後，發現 app size 從原先的 4.2 MB 一下子跳到了 5.4 MB。再怎麼調整 makefile 也無事於補，怎樣就是要多出 1.2 MB 。

[feat: make sure new adblock works · plateaukao/einkbro@93fcc7b](https://github.com/plateaukao/einkbro/commit/93fcc7bb4b64102c96607b0c4328216784939e08)

#### 重構重構再重構

ad-filter 和 adblock-client 中還在使用早期的 LiveData，這必須換成 StateFlow 才行；為了要可以增修 adblock 列表，原先範例中的 Setting 介面，也得再重刻一個 Compose 版本的。

為了重寫這塊，花了我不少時間，才成功地把 LiveData 整個拔掉。

[refactor: remove livedata variables · plateaukao/einkbro@77972bc](https://github.com/plateaukao/einkbro/commit/77972bce98c705d6e3b93cf3d62e5c91e48d80e7)

光拿掉 LiveData 還不夠。原先有些資料 class 的 member variables 是可以變動的。這在 StatFlow 中會造成是否需要更新時，會有誤判的情況發生。以致於有的時候 adblock filter 下載後下載時間不會更新，或是刪除時畫面上的項目還留著。

最終，在將 Filter class 改成 Immutable 後才解決了 Compose UI 更新的問題。(請看下面 commit)

[refactor: make Filter immutable, whenever it's changed, create new one · plateaukao/einkbro@6725cb7](https://github.com/plateaukao/einkbro/commit/6725cb73c424ba71e2834d00de55a1a96112d622)

#### 多個 binary 版本的 release

只要 Android app 一使用上 jni，就得考慮到要怎麼編譯最終 apk 版本：一個比較簡單但吃容量的方式是，把所有 CPU model 會用到的 native library 都塞進 apk，這麼一來不管什麼裝置都能安裝並正常運作；另一個方式則是追求較小的 apk size，針對不同 CPU 架構編譯出不同的 binary。需要哪個版本就自己找到對應的版本安裝。

由於這項由一個 apk 變成多個 apk 的改變，延伸出來的是：原先在設定畫面中的版本更新按鈕都失效了。在程式碼裡我把它改成較多人會用的 cpu 版本 app-arm64-v8a-release.apk 。

#### 後續收尾

目前 adblock 的白名單是失效的，這得等之後有空再補做。再來是還得花更多時間了解一下這包函式庫大概的架構長怎樣，之後才會有能力去做點修正或改善。
