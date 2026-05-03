+++
title = "改善 EinkBro 的工具列設定畫面"
date = "2024-11-06T13:10:02.789Z"
description = "為了要可以塞入更多的功能按鈕，而又同時可以輕鬆的設定工具列，我改寫了工具列設定畫面。"
slug = "改善-einkbro-的工具列設定畫面"
canonicalURL = "https://medium.com/@danielkao/%E6%94%B9%E5%96%84-einkbro-%E7%9A%84%E5%B7%A5%E5%85%B7%E5%88%97%E8%A8%AD%E5%AE%9A%E7%95%AB%E9%9D%A2-2b70a3a25e57"
mediumID = "2b70a3a25e57"
tags = ["EinkBro"]
+++

為了要可以塞入更多的功能按鈕，而又同時可以輕鬆的設定工具列，我改寫了工具列設定畫面。

修改前和修改後的差異如下。

![](/images/2b70a3a25e57/0_R0ivP7OPKxP5M7zJ.png)

![](/images/2b70a3a25e57/1_MNwdpCSYeMnkyEdHY0T7eQ.png)
*修改前 vs 修改後*

在導入 Jetpack Compose 後，做這樣子的調整就容易多了，不需要再寫一堆無謂的 layout xml 檔案。右邊新的設定畫面，不再使用 Dialog 的方式來呈現，而是新建了一個 ToolbarConfigActivity，全畫面顯示，一方面是為了日後再加入更多的功能，以及設定；另一方面，在下方可以完整地顯示一個工具列預覽區，想調整成怎麼樣，在下面可以即時移動按鈕，不再需要望著一個直式的列表，在腦中想像成果會長成怎樣。

下面的預覽還包含了選擇空白空間按鈕後的效果(虛線區域)，會盡量吃掉工具列上剩餘的空間，讓按鈕往兩側靠的排列成為可能。

實作上沒有什麼特別的地方：下方的工具列預覽是參照目前 Compose 寫成的 Toolbar.kt，新增一個 ReorderableToolbar ，讓使用者可以長按按鈕以調整位置；以及特別將空間按鈕畫上虛線，方便標示。

而上方可供選擇的功能按鈕 GridView，就只是把原先的 listview 換成 GridView 而已，沒有什麼特別需要調解的。

---

目前在新的畫面下，已經陸續加入了”反轉顏色”，”分享連結”，”儲存epub”等功能。之後，應該會再把其他的功能也都加進來吧。到時候懶得再多按一下把功能選單叫起來的人有福啦~

### 相關連結

主要的實作在這支 commit ，和後續的幾支修改 commit 中。

[ui: re-write toolbar configuration UI · plateaukao/einkbro@77f78f0](https://github.com/plateaukao/einkbro/commit/77f78f0cd4ae91b29f56103a800b439141ccef9f)
