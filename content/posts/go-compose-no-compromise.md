+++
title = "Go Compose, No Compromise"
date = "2022-06-21T15:59:56.495Z"
description = "Android 的 Jetpack Compose 也推出好一段時間了，從前一兩年的 beta 版，再到去年的正式版，網路上的相關教學文章也愈來愈多，相關的函式庫也愈來愈成熟。是時候可以跳進這個坑了。"
slug = "go-compose-no-compromise"
canonicalURL = "https://medium.com/@danielkao/go-compose-no-compromise-135094f076e4"
mediumID = "135094f076e4"
+++

Android 的 Jetpack Compose 也推出好一段時間了，從前一兩年的 beta 版，再到去年的正式版，網路上的相關教學文章也愈來愈多，相關的函式庫也愈來愈成熟。是時候可以跳進這個坑了。

### EinkBro 現況分析

目前 EinkBro 真正有需要顯示自己的畫面的地方並不多，畫面上大部分的空間都留給了 `WebView`。在全螢幕的情況下，更是一點其他的 UI 元件都沒有。稍微歸納了一下還稱得上是 UI 的畫面如下：

#### 一堆對話框

- 點擊翻頁的設定
- 主要功能選單
- 工具列設定
- 書籤列表
- 字型設定
- 快速切換設定選單

…

#### 設定畫面

- 進入設定後的 `PreferenceScreen`，這算是 UI 的大宗，但大部分都只需要設定 preference xml，和在 fragment 中接一下 action 就可以搞定了

#### 工具列

- 畫面下方除了有很彈性的工具列外，還包含了網址輸入框以及網頁內搜尋的介面。工具列得要配合**工具列設定**還有 **Preference** 才能完美運作。

#### 開雙視窗的翻譯功能

- 網頁全文翻譯時，可以將畫面一分為二。主視窗依然可以利用工具列操控；副視窗則是會在畫面上有一條新增的工具列可以使用。這功能採用了自己客製出來的 `TwoPaneLayout` ，不僅可以上下分頁，還可以左右分頁，或是主副對調位置；更厲害的是，能透過畫面中的拉桿，調整兩個視窗的比例。

---

### 選擇逐步採用策略

說多不多，但說少，想要一次全部改成用 Compose 實作，也是不大可能，尤其是我對於 Jetpack Compose 的認知也還極其有限，修改起來應該要花不少工夫。

最終，**選定的策略是先從最單純，相依性不高的對話框開始改起**。對話框的邏輯通常不會太複雜，給定資料後，只管呈現出來，再把最終使用者選的項目，做的修改，再帶回給呼叫的人處理就可以了。不會有太多的狀態變化要管理。這麼一來可以讓我先不去接觸 state management 這一塊。

在這麼多對話框裡，再選出一個相對單純的應用來試刀：快速切換設定選單。畫面上只需要幾筆項目，每一筆項目有圖，有文字，還有個 `Checkbox`，點下去會呼叫對應的 `preference` 改變。

#### 快速切換設定選單

[第一支 commit 在此。](https://github.com/plateaukao/browser/commit/f103417ef9f44208a478e5662330ff3fad8280d1)

原本有打算直接使用 Jetpack Compose 的 `dialog` 來實作，或是利用原生的 Dialog，在裡頭塞一個 `ComposeView` 。但這兩個方式都失敗了。最後，退而求其次，改成實作 `DialogFragment`，並在 `DialogFragment` 中的 `Dialog` 放入所需的 `ComposeView`。

![](/images/135094f076e4/1_b74QsblMZn1eGfEqiA75Rg.png)
*FastToggleDialogFragment*

原生的程式碼就這樣而已，主要是設定一下 `Dialog` 的屬性，讓它不要畫 `Shadow`，而且可以放置在畫面上我想放的位置，然後，設定好 `ComposeView`。(第 39 行的 Column 可以忽略。我不知道那時候在想什麼。)

![](/images/135094f076e4/1_CBoQzLYm7lSW2NprfH_nGg.png)
*FastToggleItemList*

`FastToggleItemList` 就有點像是在刻 xml 的 layout，把一個個的項目所需的 resource 都指定到 `FastToggleItem` 中，最後還包含了一個 action，用來切換對應的 `SharedPreference` 值。

![](/images/135094f076e4/1_UxINoKmQN4LYlLFzF2enUg.png)
*FastToggleItem*

`FastToggleItem` 就很像一般的 Jetpack Compose 教學，利用 `Row` 將 `Checkbox`, `Icon`, 和 `Text` 放在一行上。這邊有用到 `remember` 來記錄 Compose 中的 `isChecked` 狀態。

![](/images/135094f076e4/1__bj428Z9dqXcNXg1-JDBZw.png)
*Screenshot of FastToggleItemList*

程式寫得差不多後，在 Android Studio 的 Preview 畫面也能即時看到畫面大概會長成怎麼樣。雖然沒有像 Flutter 的 hotreload 那麼快速，但也遠比要一直去調整 layout xml 來得好多了。

#### 功能選單

完成快速切換設定畫面後，再來處理的是充滿各種功能的選單畫面。

![](/images/135094f076e4/1_K4cI5qqxWonfQMLXqHrrFQ.png)
*MenuItems*

實作的[第一支 Commit 在這兒](https://github.com/plateaukao/browser/commit/9635b2b25ee6dcaa38abdb82df196df40b85b3b4)。

當初在用 xml 撰寫這個畫面時，一直覺得很厭世。每個功能都要先用 `LinearLayout` 包一張圖，一個字串，然後再塞到對應的 Horizontal `LinearLayout` 中。再加上每個元件都要設定寬高大小，整個 xml 常常要複製貼上一大段 code。

換成 Jetpack Compose 就好做多了。可以先利用 `Preview` 把單一 Item 的樣子寫好(如下)：

![](/images/135094f076e4/1_jd59-gn0qQbIwwMNoDf7OA.png)
*MenuItem screenshot*

實作如下。(其實看起來跟 FastToggleItem 長得差不多)

![](/images/135094f076e4/1_r24sJtGysOdrDRNhW2H5tA.png)
*MenuItem*

確定外觀沒錯後，就能再把外圈的 layout 構建出來。

![](/images/135094f076e4/1_N4Jxt51v80xDo7yadzVRMQ.png)
*MenuItems*

由於我不想要在 `DialogFragment` 中實作每個按鈕的動作，所以我在這裡定義了 `MenuItemType`，當某個按鈕被點擊時，我會將這資訊帶給呼叫的人，並告知這是哪種 Type，這麼一來，外面的人就知道可以怎麼處理這情形。

要讓程式看起來更乾淨的話，其實可以將 `MenuItem` title 和 icon resource id 都塞到 enum type 中，這樣子 `MenuItem` 就可以只塞 `MenuItemType` 就好。

#### 工具列設定畫面與主畫面的工具列

之前最想利用 Jetpack Compose 來改寫的，應該就是這兩個畫面吧。原本要新增一個新的工具列功能，必須要先在 `ToolbarAction` `enum` 中新增一個 type，然後去改主畫面的 xml layout，在工具列 layout 上新增一個按鍵；再來，還要工具列設定的實作中，確定新增的 type 有被列入。整個過程很煩索，要改好幾個地方。常常都是改了之後，發現還有地方忘了改而 crash，再事後補上。

![](/images/135094f076e4/1_Is9t3EAfUdIvvykkECKjLQ.png)

![](/images/135094f076e4/1_rVLa_XXKSxnXKh4izEvijA.png)
*工具列設定與工具列*

調整成 Jetpack Compose 後，就沒這問題了，因為都是用程式碼寫出來的介面，而 single source of truth 就是定義好的 `ToolbarAction` `enum` 和存在 sharedpreference 中的目前工具列狀態。

現在想要新增功能的話，只要在 `ToolbarAction` `enum` 中加一個新的項目，然後在主畫面的 `BrowserActivity` 中去實作該 `ToolbarAction` 被點擊時要做的事就行了。兩個畫面的 UI 實作完全不用再改動。

下面就是目前的主畫面工具列實作方式。在 18 行會 for loop 整個 `ToolbarAction` `enum` 去決定怎麼生成每個 `ToolbarIcon`。

![](/images/135094f076e4/1_Gp_OEX2KxnFaq7B1YzQDig.png)
*ComposedToolbar*

`ToolbarIcon` 提供了 `onClick` 和 `onLongClick` 兩種函式，並依據 `toolbarActionInfo` 決定當下的 icon resource id 為何。(因為有些按鈕有開和關的不同狀態，所以我把它包在 `ToolbarActionInfo` 中。)

![](/images/135094f076e4/1_n426XwNr_zAXI7CZZfDTOQ.png)
*ToolbarIcon*

**工具列設定畫面**有點類似**快速功能啟動設定畫面**，這裡就不細說了。

### 改造設定畫面第一層

Dialog 在摸熟後，逐漸可以比較快速地翻新成 Jetpack Compose 的實作。再來，要處理的是設定的畫面。原本設定的畫面如下，就很一般的 Preference 介面。雖然是設定，但其實第一層幾乎都是空的，負責將使用者帶往真正要設定值的下一頁去。

![](/images/135094f076e4/0_sbdnrI0y1erydPXF.png)
*舊的設定畫面*

以 EinkBro 的用戶來看，大部分使用者使用的會是電子書閱讀器，通常畫面會比手機大。如果一行只顯示一個項目的話，實在有點浪費畫面。所以，我打算把它改成是按鈕式的，而且是一行兩個元件的型式。

![](/images/135094f076e4/1_SO_yKbpw2xI-StJlkYN-AA.png)
*修改後的畫面*

這次[修改的 commit 在此](https://github.com/plateaukao/browser/commit/3ebc75c1b891a30d2549d8c7fca76c3ed79649fa)。

這次定義了 SettingItemType enum，並在裡頭加入了字串和圖案的 resource id。

![](/images/135094f076e4/1_OKrkGW6Yhwe-lW5fc8vS3g.png)
*SettingItemType*

比較不同的是，在實作 Setting item 時，加入了我想要的點擊效果：讓按鈕的邊框會加粗。這會比整個按鈕反白來得自然，又不會在電子紙上產生過多的殘影。

![](/images/135094f076e4/1_Nzrjb8cPmv85p-yepLv19Q.png)
*SettingItem*

第 60, 61 行的 interactionSource，和 51, 52 行的實作，就是讓 Composable 知道當下點擊狀態的方式。知道狀態後，在 59 行，可以依照狀態決定邊框的粗細。下圖就是點擊後的示意圖。如果有其他的 Compose 元件想要根據點擊狀態來做一些處理，都可以用這方式實作。

![](/images/135094f076e4/0___CFEmF9N0oLTm_W)

### 結語

在經過這些嘗試後，開始體會到 Compose 方便的地方。與其事前定義好 xml layout，然後事後拿出對應的 View 元件去設定屬性或調整畫面，不如畫面全部都利用程式碼產生，這麼一來各種邏輯寫法都可以套在產生 UI 這件事上，不再被 xml 給侷限住。

目前離全部轉換成 Jetpack Compose 還有很遠的一段路要走，但我已經跨出了最艱難的第一步了。:)

#### 補充一點

因為採用 Jetpack Compose，讓 EinkBro 的 apk size 大了 900 KB 左右。這對一般 app 來說，並不是很大的差別。但是對於一個原本只有 3.47 MB 的 EinkBro 來說，整個 App 就這麼因此大了快 1/3。這對我來說是個很痛的決定，不過，為了以後能更方便地調整 UI，也只能接受這結果。

對於 EinkBro Jetpack Compose Migration 有興趣的人，可以去看一下 9.0.0 和 9.1.0 之間的 commits。

![](/images/135094f076e4/1_IkweFDKzRtwzNJEmObVocg.png)

![](/images/135094f076e4/1_5Ha-f4f_IeGyJklaN-5xUA.png)

### 相關連結

[GitHub - plateaukao/browser: An Android web browser based on webview, which is specialized for…](https://github.com/plateaukao/browser)
