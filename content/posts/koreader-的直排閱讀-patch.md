+++
title = "Koreader 的直排閱讀 patch"
date = "2024-04-21T14:03:07.802Z"
description = "從 Koreader 的開發網站上，有另一位神人寫了個小修正(lua script)，可以在當書籍的 typography 設為日文時，將畫面(文字的部分)轉成 90 度。"
slug = "koreader-的直排閱讀-patch"
canonicalURL = "https://medium.com/@danielkao/koreader-%E7%9A%84%E7%9B%B4%E6%8E%92%E9%96%B1%E8%AE%80-patch-8fcf1f366269"
mediumID = "8fcf1f366269"
tags = ["電子書閱讀器"]
+++

從 Koreader 的開發網站上，有另一位神人寫了個小修正(lua script)，可以在當書籍的 typography 設為日文時，將畫面(文字的部分)轉成 90 度。

這樣子有什麼好處呢？

前幾週我有分享一個方式可以讓使用者點擊畫面某個區域時，可以同時把字型換成 轉成 90 度的特殊字型，再順便將系統畫面也轉 90 度，藉此達成一個很克難的直排閱讀。雖然這樣子就可以直排閱讀了，但是當你想要做些其他調整時，就會發現 menu 變成在畫面的左右邊，很難操作(見圖二)。

而這個 script 則是可以讓只有套了轉 90 度的文字的顯示區再轉 90 度而已 (有點繞口)，其他的 app 介面都還是正常的(選單，對話框，進度列都還是在上下方，見圖一)！

#### 套用方式

神人的說明在: <https://github.com/koreader/koreader/issues/11469#issuecomment-1969338188>

1. 簡單的操作方式是 1. 先下載這個連結到手機上 <https://github.com/koreader/koreader/files/14436601/2-cre-rotate-japanese-book.lua.txt>

2. 把它放到 /koreader/patches 下 (可能要把 .txt 的副檔名拿掉)

3. 然後開啟書籍後，自己先將字型換成 偽直排字型，再將書籍的 typography 設成日文 (目前 script 裡是寫死 ja，如果你主要看的是中文書的話，可能要換成中文 locale)

#### 同場加映

另一個神人在同個討論串裡，提到他寫了個 python script 可以快速地將字型轉成 偽直排字型，不用再開啟 fontforge 去操作那難用的 UI 了 (但不確定是不是它只針對日文有作用而已，我還沒拿來試中文)。有興趣的人可以研究一下他的 script 寫法 (要使用到 fontforge 的 python extension) 。

在 MacOS 上的話，要先安裝 fontforge，然後執行下面的指令。(直接用 python 跑會找不到 fontforge module，所以，必須用 fontforge 中提供的 FFPython 來執行)

```
/Applications/FontForge.app/Contents/MacOS/FFPython main.py input.ttf ouput.ttf
```

轉換偽直排字型的小工具: <https://github.com/MyK00L/tategakifont?tab=readme-ov-file>
