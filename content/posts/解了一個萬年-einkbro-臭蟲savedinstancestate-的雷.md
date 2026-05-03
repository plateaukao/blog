+++
title = "解了一個萬年 EinkBro 臭蟲：savedInstanceState 的雷"
date = "2022-11-02T13:38:55.935Z"
description = "最近下載 EinkBro 的使用者多了一點。早期不太去理它的臭蟲，也因此發生得愈來愈頻繁。今天終於花了點時間找出原因，並且解決了它。"
slug = "解了一個萬年-einkbro-臭蟲savedinstancestate-的雷"
canonicalURL = "https://medium.com/@danielkao/%E8%A7%A3%E4%BA%86%E4%B8%80%E5%80%8B%E8%90%AC%E5%B9%B4-einkbro-%E8%87%AD%E8%9F%B2-1b04a685008e"
mediumID = "1b04a685008e"
+++

![](/images/1b04a685008e/1_hvjSHf7-P99X9xE5OS2JZA.png)

![](/images/1b04a685008e/1_mT0JMjHvGeKA2PVein15JA.png)

最近下載 EinkBro 的使用者多了一點。早期不太去理它的臭蟲，也因此發生得愈來愈頻繁。今天終於花了點時間找出原因，並且解決了它。

![](/images/1b04a685008e/1_UFzWODVkbdwuhgYrfFEb8Q.png)

從 App 版本和 Android OS 版本看來，這是個非特定設備下就會觸發到的問題。之前一直沒理它的原因是，雖然 Google Play Console 上有 Crash 的 callstack (如下圖)，但是有寫跟沒寫差不多，因為沒有真的寫出行數，只能在 `BrowserActivity::onCreate()` 裡自己找線索。

![](/images/1b04a685008e/1_qe2DygyJQ5vcE0LNCH6n4g.png)

從這一大串訊息中，可以大概看出：在進到 `onCreate()` 後，會進到 Android 系統的 `FragmentManager`，它想要執行 `restoreSaveState()`，藉此呼叫 `instantiate()` 函式，然後就壞了。

在經過一番搜尋後，最終的原因是因為：雖然 `BrowserActivity` 中我沒有建立什麼特別的 `Fragment` 來顯示畫面，但是很多對話框我是利用 `DialogFragment` 來完成的。而這些客製的 DialogFragment 都在建構函式中必須要代入一些參數或功能函式。

![](/images/1b04a685008e/1__2sEoTBMWb9LxcVa0NKv5g.png)

在官方文件中指出：如果想要繼承 `Fragment` 的話，應該要保留空的建構函式，然後把需要的參數利用 `Bundle` 一一塞入 `Fragment` 中。這樣子才可以確保在某些情況下 `Fragment` 被重新建立時，這些參數能夠再從 Bundle 中取回。

目前因為已經實作了好多個 `DialogFragment`，我懶得改動這一部分。另一個可行的替代解法是：當 Android 系統想要回復 `BrowserActivity` 時，它會傳入 `savedInstanceState` 這個 `Bundle`。正常操作的方式是，在 `onCreate()` 的第一行執行：

```
super.onCreate(savedInstanceState)
```

而這一行正是造成 crash 的原因。`savedInstanceState` 的內容會指示 Android 系統幫忙把之前的 `Fragment` 再嘗試著建立出來。所以，要讓它不 crash 的話，就是假裝沒這回事，直接塞 `null` 給它。

![](/images/1b04a685008e/1_I6pDse9dtXcKXHwsJkbUcQ.png)

這麼一來，就能避掉 crash 的產生囉。

### 後話

或許有人會問，那之前的狀態怎麼辦？

就，隨它去囉。對於 `Dialog` 性質的 `Fragment`，通常在離開 `Activity` 後再回來 `Activity`，把這些 `Dialog` 自動關掉也是比較合理。

等過一兩週後，再來這裡更新一下新的 crash rate。

### 相關連結

- [修正臭蟲的 commit](https://github.com/plateaukao/einkbro/commit/fb07dbbe5131af6fa27bdb3b41ae35c61a9f9ac5)
- [網路上找到的參考資料](https://github.com/ncapdevi/FragNav/issues/238#issuecomment-761125925)
