+++
title = "EinkBro 分頁列表的小改進"
date = "2023-03-14T15:15:04.915Z"
description = "從 v9.7.0 開始，EinkBro 支援在畫面上固定顯示分頁的列表。如果開啟這功能的話，整個介面看起來會更像是傳統的瀏覽器；能夠在不同分頁間快速切換。很適合在一般的電子書閱讀器上開啟。"
slug = "einkbro-分頁列表的小改進"
canonicalURL = "https://medium.com/@danielkao/einkbro-%E5%88%86%E9%A0%81%E5%88%97%E8%A1%A8%E7%9A%84%E5%B0%8F%E6%94%B9%E9%80%B2-4cf300373947"
mediumID = "4cf300373947"
tags = ["EinkBro"]
+++

從 v9.7.0 開始，EinkBro 支援在畫面上固定顯示分頁的列表。如果開啟這功能的話，整個介面看起來會更像是傳統的瀏覽器；能夠在不同分頁間快速切換。很適合在一般的電子書閱讀器上開啟。

![](/images/4cf300373947/1_0HMuFbmd0-j4lYEqa77MjA.png)

這個功能完成後，就一直到了現在，覺得應該可以讓它再多發揮點功用。所以，我為它加入了：

1. 點擊目前已經是顯示中的分頁：將畫面跳至網頁內容最頂端。
2. 點擊目前已經是顯示中的分頁，而且也已經是在網頁內容最頂端的話：重新載入目前的網頁內容。

實作細節其實沒有什麼複雜的地方：原先在點擊當前分頁時，不會做任何動作；現在多了 if-else 判斷是否在內容頂端，是的話就重新載入網頁，不是的話就跳至內容最上方。

![](/images/4cf300373947/1_GCgGNUouUjSTnYH0MCGKqQ.png)

`isAtTop()` 是新增的判斷函式；剩下的函式都是現成的。

### 重構

功能實作雖然很快速和簡短，但是仔細看一下上面的程式碼：怎麼在 `showAlbum()` 中去根據 `WebView` 的狀態決定要移動內容位置還是重新載入畫面呢？這兩件事好像都跟 `showAlbum()` 沒有什麼關係啊？

其實這只是因為當分頁被點擊時，會來呼叫 `showAlbum()` 函式，所以最直覺的修改就是直接做在 `showAlbum()` 中。這樣子快雖快，但會有好幾個衍伸的問題：

1. 單純看 `showAlbum()` 的實作，會無法理解為什麼裡面會有這種邏輯；而且跟 show album 字面上的意義沒有直接的關係。
2. `showAlbum()` 還有被使用在其他場合。其他場合不見得會需要根據 `WebView` 的狀態做不同的反應。

所以，在思考後，又多發了一個 commit 來改寫已經可以用的程式碼。對於原先的 showAlbum 不做更動，然後針對分頁點擊時的第一個函式更名，讓它更符合函式實作的內容：

![](/images/4cf300373947/1_hl9hL77rS5FBFczsjID6dQ.png)

這邊的 `browserController` 是一個抽象的介面，姑且可以把它想成能用來操作 `WebView` 的中介；而 `Album` 則是用來表示分頁列表上每個分頁的物件。當分頁被點擊時，`Album.showOrJumpToTop()` 會被呼叫，依照 `browserController` 提供的狀態決定要做怎樣的行為。

這麼一來，就不會去改到原本的 `showAlbum()`。

### 相關連結

- [feat: click on tab will scroll top to and second time will refresh tab](https://github.com/plateaukao/einkbro/commit/3ea1351857491dbc96b364d3371190c144134601)
- [refactor: click on album behavior.](https://github.com/plateaukao/einkbro/commit/9a2e3625d10262c236b687215ac5025298d26340)
