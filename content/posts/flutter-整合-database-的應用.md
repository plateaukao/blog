+++
title = "Flutter 整合 Database 的應用"
date = "2020-03-11T16:15:20.875Z"
description = "在學習韓文時，除了背單字的需求外，還希望可以有隨時可以查閱或複習的文法資料。找了一下 Android 平台上的相關 App，大部分都沒有太多內容，不然就是雖然有完整的內容，但操作上不是很符合我的需求，或是 UI 有點簡陋，讓人提不起學習的興趣，有的還會一直在畫面下方閃廣告。"
slug = "flutter-整合-database-的應用"
canonicalURL = "https://medium.com/@danielkao/flutter-%E6%95%B4%E5%90%88-database-%E7%9A%84%E6%87%89%E7%94%A8-b9024af88daa"
mediumID = "b9024af88daa"
tags = ["韓語學習筆記"]
[cover]
  image = "/images/b9024af88daa/1_aDegaTz8oRMp921bnG_d_w.jpeg"
+++


![](/images/b9024af88daa/1_aDegaTz8oRMp921bnG_d_w.jpeg)
*Taichung.Taiwan*

在學習韓文時，除了背單字的需求外，還希望可以有隨時可以查閱或複習的文法資料。找了一下 Android 平台上的相關 App，大部分都沒有太多內容，不然就是雖然有完整的內容，但操作上不是很符合我的需求，或是 UI 有點簡陋，讓人提不起學習的興趣，有的還會一直在畫面下方閃廣告。

#### 找資料庫

目前看到兩個資料比較完整 App 分別是下圖中的第一個和第三個 App。

![](/images/b9024af88daa/1_ig_XZCAZStA8PWjG1ES03Q.png)

想說，如果能夠利用它們 App 中的資料庫，自己透過 Flutter 來撰寫 UI 的話，不就兩全齊美了嗎。所以我先去 <https://apkpure.com/tw/> 下載了這兩個軟體的好幾個版本，然後用 <https://github.com/venshine/decompile-apk/releases> 把它們打開來看一下究竟資料是存在伺服器端，還是 App 裡頭的 database。

經過一番努力，有的 App 隱藏的比較好，找不到 App 中的資料；有的 App 在新版已經把資料上了雲端，但舊的版本倒還是把資料庫塞在 App 當中，讓我有機會大展身手，在它之上建立自己想要的 UI。

#### 分析資料庫

有了資料庫後，要先研究一下裡頭的 table 長怎麼樣，才可以決定要怎麼利用。在 Mac 上可以安裝 <https://sqlitebrowser.org/> 來開啟 sqlite 資料庫。該資料庫中的 table 都還蠻清楚的，而且也有稍微做了正規化，避免重複的訊息造成資料庫太大。

**grammar**: 文法本體，有名稱，難度級別，出現頻率等資料。

**grammar\_category**:類別，不同語言的翻譯，也放在了裡頭。

**grammar\_desc**: 文法說明，也是包含了不同語言的翻譯。

**grammar\_exam**: 跟文法相關的例句。如果在畫面中想要顯示例句的話，就需要來讀取這個 table 的資料。

![](/images/b9024af88daa/1_k3z2vqdsGqR_w1p2lcG-JQ.png)

### Flutter 整合既有的 sqlite database

有了基本了解後，就可以開始寫 Flutter啦。首先是在 pubspec.yaml 中加入 sqlitedb 和 path\_provider 的支援。

```
# sqlite support  
sqflite: 1.1.2  
path_provider: 1.5.1
```

需要 path\_provider 的原因是，我們得把 asset 中的 db 拷貝一份到 storage 中以後，才可以去讀取 db 。加好 package 後，下面是 db 相關的啟動程式碼，我想應該還蠻好懂的。isDBExisting() 是檢查放 db 的目錄是否存在，不存在的話，就建立它，然後看 db 檔案在不在； initDB() 則是確保 db 已經複製到應該存在的地方，然後 openDatabase()，等著之後的操作。

[View gist](https://gist.github.com/plateaukao/9d5e9536282e89301854ae9b9fd313fe)

db 中撈出來的資料會是 `List<Map>`，如果要直接拿來用在 UI 上，應該會很痛苦；所以我們先建立 data model，做一層轉換。資料庫中資訊很分散，但我們希望在建 data model 時還是都放在一起比較好。

[View gist](https://gist.github.com/plateaukao/b2d377de5337d8fa0abe72c500cfe108)

#### 抓資料

透過又臭又長的 SQL 語法，把上述的幾個 table join 一下，在 22 行呼叫 `_grammarDb.rawQuery()` 取出必要的資料，然後在 23 行轉換成上面剛定義好的 `GrammarItem` 清單。除了文法清單外，文法類別也是利用同樣的方式來取得。

[View gist](https://gist.github.com/plateaukao/8acd05dca010ad895c16182ec0487ece)

#### 畫 UI

資料部分完成，終於進入重頭戲，兜出自己想要的 UI 呈現方式。先把之前的單字本 App 翻出來，在主畫面中，加入下方 tabbar的功能。(如果不知道單字本的故事，可以在下面連結看到我的上一篇文章)。在 `Scaffold` 的 `bottomNavigationBar` 塞兩個 `BottomNavigationBarItem`，然後 body 的部分用 `IndexedStack` 放原先的 單字本 Page，以及接下來要實作的 `GrammarHomeWidget`。

[View gist](https://gist.github.com/plateaukao/3d12b98a1fb11ee6f0e4ccc67a1eda7a)

再來是把 db 中撈出來的文法類別先呈現出來。這對於 Fluter 來說，是蛋糕一塊，這裡就不多作說明，反正就是一個 ListView，幾行 code 可以完成的功能。點擊分類後，顯示該分類下的文法清單，也是幾行 code 的事。

![](/images/b9024af88daa/1_GpVQRNKNzmu1pCMSjYYLXg.png)

![](/images/b9024af88daa/1_eHpvwo_nOv2Oz8sxtB7Ryg.png)

#### 換主題

到這邊為止，其實都做得跟原本 App 差不多，而且一樣不好看。接下來才是發揮的地方。換主題先！Flutter 對於 Theme 有很容易的更換方式。不過我個人也是沒有什麼美感的，所以只好參考一下網路上看起來比較順眼的畫面來套一下。修改不多，定義了一個主要 Theme: `kBaseThemeData` ，把兩個主色換掉，然後在四處的 Widget 中套用。

[View gist](https://gist.github.com/plateaukao/f7eeac1d3f7f8192fe06751b2c4075c4)

這就是套完的結果，是不是頓時有質感多了呢？(至少比較不像是 flutter demo app 了)。

![](/images/b9024af88daa/1_PPpZV6RTRkueqMkQedqUGw.png)

![](/images/b9024af88daa/1_FXdOHTfX4mjzSAe4DgrwvA.png)

#### 增加功能

剛剛在講資料庫內容時有提到，它包含了每個文法的難易程度。對於還在幼幼班的我來說，如果能先只濾出初級的文法，應該會比較容易學習，所以我在 Scaffold Appbar 的 actions 中加了 level 的 popupMenu，讓它可以切換不同難度的文法。切換的方式很暴力，直接從 db 從新讀取，然後再重新 build ListView。

[View gist](https://gist.github.com/plateaukao/cda81f948542093c03c12125d8cf4cdc)

![](/images/b9024af88daa/1_PM6VndD8hWGoj10ycFtamw.png)

![](/images/b9024af88daa/1_sfYSsy22yyuZJfTkSb1wMw.png)

另外，對於文法詳細內容呈現時，我希望顯示的例句在一開始不要有英文說明。因為很直覺的會看到英文，那就失去了先自己猜意思的機會。所以我把它設計成要手動點擊例句再把英文翻譯顯示出來，然後隔幾秒後又會再消失(雖然好像沒有什麼必要)。

show/hide 的功能是透過 `Visibility` Widget，在 `ListTile` `onTap` event 來的時候去把 `_SentenceWidgetState` 中的 `isDisplayDefinition` 狀態改變，然後叫 Widget 再重新繪製。三秒後消失的功能則是利用 Timer。

[View gist](https://gist.github.com/plateaukao/46852e4a1b63d59a7928e9a445c94dc0)

![](/images/b9024af88daa/1_1eIJjO5uIdG8zg4--fn_9Q.png)

![](/images/b9024af88daa/1_zXJCoVLQqz_MlBmTg3_F3w.png)

#### 未來展望

目前功能只做到這樣。將來希望能自己擴充例句，畢竟，自己生活中遇到的例子會比較容易記得。針對文法的說明，也希望能自己再加入自己的(中文)見解，比較容易記憶的方式等資料。

### 前情提要

[用 Flutter + Google Sheets 建立單字本 App](https://medium.com/%E9%9F%93%E6%96%87%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98/%E7%94%A8-flutter-google-sheets-%E5%BB%BA%E7%AB%8B%E5%96%AE%E5%AD%97%E6%9C%AC-app-c51f198cfbf3)
