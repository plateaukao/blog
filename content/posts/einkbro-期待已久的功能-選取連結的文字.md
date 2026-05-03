+++
title = "EinkBro 期待已久的功能 — 選取連結的文字！"
date = "2023-11-03T14:53:52.343Z"
description = "期待了很久，一直不知道怎麼實作的功能終於做出來了！在 Android WebView中，一般來說，只可以長按非連結的文字，選取文字進行複製或其他的動作。如果想要選取連結上的文字的話，必須要用些小技巧才能達成。"
slug = "einkbro-期待已久的功能-選取連結的文字"
canonicalURL = "https://medium.com/@danielkao/einkbro-%E6%9C%9F%E5%BE%85%E5%B7%B2%E4%B9%85%E7%9A%84%E5%8A%9F%E8%83%BD-%E9%81%B8%E5%8F%96%E9%80%A3%E7%B5%90%E7%9A%84%E6%96%87%E5%AD%97-9408285898cc"
mediumID = "9408285898cc"
tags = ["EinkBro"]
+++

期待了很久，一直不知道怎麼實作的功能終於做出來了！在 Android WebView中，一般來說，只可以長按非連結的文字，選取文字進行複製或其他的動作。如果想要選取**連結上的文字**的話，必須要用些小技巧才能達成。

下面的 sequence diagram 說明了如何透過一系列的操作達到這效果。

![](/images/9408285898cc/0_AC6uCjUPJt42oZNP)

### 步驟

- 在網頁載入完成後，要塞一段程式去偵測文字選取範圍改變時的區域
- 當下達指令**要選取連結文字時**，要把點擊處的 **a node** 的 href 屬性拿掉
- 再模擬一次長按的行為 (`simulateLongClick()`)
- 等選取好連結字串後，再回復原先 a element 中的 href 屬性

#### 接著再改善

- 把原先的 ActionMode DialogFragment 變成是Compose 的 Dialog，讓它不會對 ActionMode selection anchor 的顯示造成影響
- 自行處理視窗超出畫面的問題
- 第一步中的 `udpateSelectionRection()` 會回傳 Selection Range 的 position，可以用來調整 Context Menu 的位置

[View gist](https://gist.github.com/plateaukao/e8b4cbf7ac6ba9060a402591b17a6081)

[View gist](https://gist.github.com/plateaukao/239297b3c2d7a502b5326032c2e3e566)

[View gist](https://gist.github.com/plateaukao/e81faa0797243aaf33bada07bee65824)

### 相關連結

[Release Release v10.16.0 · plateaukao/einkbro](https://github.com/plateaukao/einkbro/releases/tag/v10.16.0)
