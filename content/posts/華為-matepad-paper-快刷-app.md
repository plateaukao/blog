+++
title = "華為 Matepad Paper 快刷 App"
date = "2024-04-17T13:31:30.129Z"
description = "我的 matepad paper 復活了！"
slug = "華為-matepad-paper-快刷-app"
canonicalURL = "https://medium.com/@danielkao/%E8%8F%AF%E7%82%BA-matepad-paper-%E5%BF%AB%E5%88%B7-app-0641e4ddda3b"
mediumID = "0641e4ddda3b"
tags = ["電子書閱讀器"]
[cover]
  image = "/images/0641e4ddda3b/1_4eaLRk1rPmxmiX-kG7OtjA.jpeg"
+++


### 我的 matepad paper 復活了！

2022 年上半年發布的華為 matepad paper，因為是第一代產品，所以在軟體穩定度和完整度上，一直被使用者詬病；但是，它的硬體堪稱是當時最強的也不為過，就算是放到現在，也比大多數的閱讀器要強很多。

下面圖中我稍微裝了一下 geek bench 6 來跑一下 cpu 的性能，在跟右邊的 BOOX Tab Ultra C 做比較時，比分硬是高了快一倍。

![](/images/0641e4ddda3b/1_4eaLRk1rPmxmiX-kG7OtjA.jpeg)

matepad paper 的硬體雖然很強，但是它為了追求無殘影的效果，只提供了使用者兩種刷新模式：普通模式和智慧模式。普通模式就是畫質最好的刷新方式，很適和在看靜態的內容；而智慧模式則是由系統幫你決定在什麼情況下，要不要用稍微快一點的刷新速度來處理畫面變化。

這個智慧模式的刷新速度跟文石的極速和快刷完全不行比，刷新速度相當慢，也因此，空有強大的 cpu 性能，在操作上總是會覺得它慢半拍。

### 曙光

不過，前幾天在網友的分享下，得知原來早在 2023 年初就有神人透過修改 app 的 package id (系統用來辨識 app 的 id) 欺騙系統，讓閱讀器以為當前的 app 是個影音播放 app，這時，matepad paper 就會進入”隱藏版”的刷新模式，達到類似一般文石系統的極速刷新模式。雖然這個模式下，殘影明顯地多了起來，但很多時候操作上的流暢性是勝於輕微的殘影的。

但是，這個作法的前提是要有辦法取得想要它刷新變快的 app 原始碼，自己重新修改過 package id 才行，沒辦法套用到一般從網路上抓到的 apk。

### 希望

這時，神人又找到了另一個作法，他去改了一個叫”屏幕濾鏡”的 app，這個 app 原先的作用是可以在畫面上蓋上一層膜，用來適度地調整畫面呈現的顏色，或是亮度。而這個機制剛好可以造成不管目前畫面上是哪個 app 在運作，都可以有快刷的效果。

不過，畢竟原先屏幕濾鏡不是要拿來做快刷的，所以在設定上很煩索。一般人要裝，在操作上也很麻煩；再者，這 app 中也多了一堆不需要的功能。

### 自己動手作

因此，在了解了它的運作方式後，我也自己寫了一個小程式專門來做這件事，讓操作的步驟變得簡單很多。而且，佔用的體積也從原本的 4MB 降到了 28 KB。(雖然這點不是很重要就是了)

結論是：目前 matepad paper 幾乎無敵啦，有好看的外表，有性能高的 CPU，還有隨時想快刷就快刷的作法，重量又輕(約360克而已，那些 400 多克的 10 吋機型請一邊排排站)。

附上程式(HWQuickRefresh)的連結，要使用的人，在安裝後執行它，會跳出需要允許 accessibility 的權限(因為要蓋在畫面上)。同意後，回到桌面，再切到”智慧模式”，大部分的 app 應該就是快刷模式。如果想臨時關掉，就切到一般模式；要整個關掉的話，就再點一次 HWQuickRefresh app，即可。

(ps. 如果執行時有遇到畫面全黑，可以從右上方下拉，進入 系統設定，再進入應用程式列表，把它反安裝就行)

### 連結

[Release 華為 Matepad Paper 快刷模式 v1.0 · plateaukao/AssistiveTouch](https://github.com/plateaukao/AssistiveTouch/releases/tag/mp1.0)
