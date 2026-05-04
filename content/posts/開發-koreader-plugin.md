+++
title = "開發 Koreader Plugin"
date = "2023-07-23T10:21:55.529Z"
description = "Koreader 是個跨設備的閱讀 App，提供強大的閱讀功能以及相當多的客製化彈性。除了內建的許多功能外，它也提供開發者可以透過撰寫 lua script，擴充新功能或是修改原先的行為。這篇文章將會說明怎麼開發一個簡單的 koreader…"
slug = "開發-koreader-plugin"
canonicalURL = "https://medium.com/@danielkao/%E9%96%8B%E7%99%BC-koreader-plugin-fda80c51b098"
mediumID = "fda80c51b098"
tags = ["電子書閱讀器"]
[cover]
  image = "/images/fda80c51b098/1_Izm8TnmZ0Q70iPWRedbwow.png"
+++


Koreader 是個跨設備的閱讀 App，提供強大的閱讀功能以及相當多的客製化彈性。除了內建的許多功能外，它也提供開發者可以透過撰寫 lua script，擴充新功能或是修改原先的行為。這篇文章將會說明怎麼開發一個簡單的 koreader plugin，讓使用者在呼叫辭典時，可以連結到 EinkBro 做搜尋。

#### 大綱

- koplugin 基本架構
- lua 教學
- askeinkbro.koplugin 功能
- 參考 Koreader 現有架構並實作
- 怎麼把 plugin 安裝到 Koreader 中和 Debug

### koplugin 基本架構

關於 koplugin 的開發範例，可以參考官方 github.com 中最簡易的 [hello.koplugin](https://github.com/koreader/koreader/tree/master/plugins/hello.koplugin)。

![](/images/fda80c51b098/1_Izm8TnmZ0Q70iPWRedbwow.png)

每個 plugin 目錄中至少會有兩個檔案：`_meta.lua` 和 `main.lua`。

- `_meta.lua`: 定義該 plugin 名稱，和一個簡單的功能描述。
- `main.lua`: 真正的實作所在。如果要寫的內容太多，也可以把實作寫到其他的 lua 檔案中，然後再利用 `require()` 的方式，將其引入到主要邏輯開發中。

#### \_meta.lua

下面是 `hello.koplugin` `_meta.lua` 的實作內容。

```
local _ = require("gettext")  
return {  
    name = "hello",  
    fullname = _("Hello"),  
    description = _([[This is a debugging plugin.]]),  
}
```

這邊利用了 `local _ = require(“gettext”)` 把用來處理多國語系的模組引入。如果你的模組沒有做其他語言的翻譯的話，不特別引入 gettext 也是可以的。

大部分 plugin 的 `_meta.lua` 也都是這麼簡潔。下面再來看個例子，keepalive.koplugin ：

```
local _ = require("gettext")  
return {  
    name = "keepalive",  
    fullname = _("Keep alive"),  
    description = _([[Keeps the device awake to prevent automatic Wi-Fi disconnects.]]),  
}
```

#### main.lua

這個檔案會是主要的實作區域，內容可以簡單分成四部分：

- 引用現有模組的宣告
- 建立並初始化 plugin 物件
- 各種需要用到的函式，或是覆寫既有函式的實作
- 回傳初始化的 plugin

以 hello.koplugin 來說，對應如下。在建立 hello plugin 時，它是繼承 `WidgetContainer` 而來的物件。`Hello:init()` 是每個 plugin 都會實作，用來把需要啟動或做連結的邏輯都放在這兒。

![](/images/fda80c51b098/1_yNWRcdUdtL3Mq6ZpxlnrAA.png)

### lua 教學

lua 的語法很容易，這邊不做詳細的介紹，只是給一下相關的官方教學連結。以筆者在開發 plugin 時的經驗來說，我完全沒有閱讀下面的連結，全是參考現有 plugin 的作法，就足以開發出想要的功能。

[Programming in Lua (first edition)](https://www.lua.org/pil/contents.html)

簡而言之，如果不是太複雜的 plugin 的話，應該參考現有的實作會比較快。如果想要開發規模比較大的功能，可能投入點時間閱讀一下 lua 文件會比較有效率。

### askeinkbro.koplugin

看完 hello world 版的 koplugin 後，接著要講自己開發的 plugin 就容易多了。會開發這個 plugin 是因為有使用者在問，是不是能在使用 koreader 閱讀時，比較快速地把選取的文字帶到 EinkBro 中做查詢。

在沒有這個 plugin 之前，使用者必須要在選取文字後，點選”分享文字”，再從系統的 action picker 中點選 EinkBro App 才能進到 EinkBro 中。如果有 plugin 的話，這個操作可以節省至少一個步驟(從系統清單中選擇 EinkBro)，甚至有機會做到選完單字後，直接帶到 EinkBro 的搜尋結果畫面去。

#### \_meta.lua ([link](https://github.com/einkbro/askeinkbro/blob/main/_meta.lua))

先來看看這個 plugin 的定義內容。雖然我也照抄了 gettext 的引入，但其實使用者不管用什麼語系，都只會看到 AskEinBro 就是了。目前版本很快地已經來到了 0.4.1，因為過程中修正了不少臭蟲。

```
local _ = require("gettext")  
return {
```

#### main.lua ([link](https://github.com/einkbro/askeinkbro/blob/main/main.lua))

主要的實作如下。有了上面的架構後，再來看 askeinkbro.koplugin 就清楚多了。這裡繼承的 UI 模組是 InputContainer。至於為什麼，其實我也還沒去細究，這是沿用 AskChatGPT (請見下面參考連結) 的實作而來的。

在初始化的函式 (53 ~ 88 行) 中，包含了三個重點，分別是：

- 15, 39 行：將 plugin 加入在選取單字後，能直接查詢的字典選單中
- 67 行：在字典結果畫面中，增加 Query EinkBro 的按鈕
- 54 行：在選取文字的清單中，增加 Query EinkBro 的按鈕

這幾個功能實作會在後面展開來講解。

![](/images/fda80c51b098/1_ov1fSO286U_s6intG_DorQ.png)

#### 選取單字後直接查詢 EinkBro

對於查詢頻繁的使用者來說，點完單字就直接跳到特定字典(或是 EinkBro)會是最方便的行為。這在原本的 Koreader 中就有支援，只差沒有把 EinkBro 列進去。所以這裡實作的重點是，把 EinkBro 加到字典清單中；並且在當它被選取後，能夠呼叫正確的方式，把 EinkBro 叫起來。

讓我們先來看看原先在 [Koreader 裡的實作](https://github.com/koreader/koreader/blob/d350418367ddf39d752d05e0587e562d7d4af2c4/frontend/device/android/device.lua#L50)。它在 `koreader/frontend/device/android/device.lua` 中定義了一個列表 `external`，其中包含了許多字典 App 的名稱和對應的 package name，以及適用的 `action` (aard2, search, send, quickdic, text, etc)。如果想讓 EinkBro 也出現在列表中，就必須要覆寫這個列表 (後來想想，好像不用覆寫，只要抓出 `external.dicts` ，幫它加上一條新的資訊就好吧？) 。

![](/images/fda80c51b098/1_j-yzPWzSfI5Fm-n7YGfmZw.png)

以下是修改後的版本。

- 28 行是新加入的資訊，定義了 EinkBro 的名稱，package name，以及想要的 `action` 為 `text`。
- 35 行將它定為 `getExternalDictLookupList`。這函式將會在下面使用到。
- 39 行的 `doExternalDictLookup()` 是真正用來叫起 EinkBro App 的實作。這裡用到了內建的 `android.dictLookup()` 函式。

![](/images/fda80c51b098/1_Xmz_LCwd1dvWm0DAOgWXOg.png)

有了這些準備後，接下來是在 `AskGPT:init()` 中，把一切串起來。下面可以看到：

- 64 行把原先系統的 `Device.getExternalDictLookupList` 換成我的版本
- 65 行把原先系統的 `Device.doExternalDictLookup` 實作換成我的函式

這樣子的操作基本上說明了大部分 koreader 的 plugin 可以怎麼實作：

- 在可以攔截列表生成的函式中，加入自己想要新增的功能選項
- 將系統原先的功能函式置換成自己想要的行為

![](/images/fda80c51b098/1_cjPqz3ux_aybEycN7G5iig.png)

#### 圖例

下面就是關於快速查詢字典的相關畫面結果。

![](/images/fda80c51b098/1_Uucxq30M8FUmn4NNVSHCOQ.png)

![](/images/fda80c51b098/1_R_ViCCwnJwvO81F5oZ-xWA.png)

#### 在字典結果畫面新增 Query EinkBro 按鈕

在用一般字典查詢完單字後，有的時候可能找不到結果，或是內容不是自己想要的，這時可能會想要再延伸去 EinkBro 上看看。所以，使用者會希望在字典結果頁上也能有個快速前往 EinkBro 的方式。

在經過一番尋找後，發現在這功能是實作在 `koreader/frontend/ui/widget/dictquicklookup.lua` 中。看來這是個常常有被修改需求的元件，所以它在它的 `init()` 實作中，多了下面的邏輯：看看有沒有其他人定義了 `tweak_buttons_func`，如果有的話，就呼叫一下，讓其他元件可以透過這方式來調整原先的 `buttons` 列表。

```
    if self.tweak_buttons_func then  
        self:tweak_buttons_func(buttons)  
    end
```

有了這樣的認知後，我們再回過頭來看一下 askeinkbro plugin 中的 `init()` 函式吧：

- 66行：先把原先的 `tweak_buttons_func` 保留下來，因為我們的目的是要加按鈕，而不是要把別人的客製化內容都覆蓋掉
- 68 行：在做其他事之前，先呼叫一下別人的實作
- 69 ~ 75 行：加上一個 boolean flag，確保不會在多次呼叫下，一直加入一樣的按鈕
- 76 ~ 86 行：做了點判斷後，利用 `table` 在 `buttons` 中加入按鈕；而 `callback` 是被點擊後要執行的實作。這邊一樣是利用了 `android.dictLookup()` 函式。83 行則是要記得把這個對話框關閉。不然從 EinkBro App 回來時，這個對話框還會在畫面上。

![](/images/fda80c51b098/1_4Xs6I1UhTmutPk8V-BYIlQ.png)

圖例

來看看完成後的畫面吧。

![](/images/fda80c51b098/1_ysQqegjzzVUf69SdbmjVag.png)

#### 在選取文字的清單中新增 Query EinkBro的按鈕 ([link](https://github.com/koreader/koreader/blob/d350418367ddf39d752d05e0587e562d7d4af2c4/frontend/apps/reader/modules/readerhighlight.lua#L159))

在看完前兩個功能的實作後，第三個功能就是重覆一樣的動作而已。首先，找到文字選取後的新增功能清單定義在 `koreader/frontend/apps/reader/modules/readerhighlight.lua` 。下面可以看到類似我想要做的事：在 Highlight 對話框中新增一個項目。而這裡的 `readerhighlight` 其實會被生成到 `self.ui.highlight` 上。

![](/images/fda80c51b098/1_L8M6MLFGI5RHCP5Y5PZXDA.png)

所以，在 `AskGPT:init()` 中就依樣畫葫蘆，放進一個 Query EinkBro 的按鈕。實作跟上面的兩個功能大同小異。

![](/images/fda80c51b098/1_p4d-VA6KDK4vON3akO6sfg.png)

圖例

完成啦，來看看長出 Query EinkBro 的畫面。

![](/images/fda80c51b098/1_szQ8w2Ltaw3Op5NFIlNYkg.png)

### 如何安裝 plugin 和 Debug

#### 安裝 plugin

目前剛成開發的 askeinkbro plugin 都會壓成 zip 檔案，放在 github 上。<https://github.com/einkbro/askeinkbro/releases>

要安裝到設備的 Koreader 的話，需要先把 zip 下載到設備上解壓縮，並把目錄名稱重新命名為 askeinkbro.koplugin，再移動到 `koreader/plugins` 下面。

#### 如何 Debug

不確定有沒有更好的方式，不過，目前筆者的作法是在修改完 `main.lua` 喔，利用 Android Studio 中的 File Explorer 把它移到 `askeinkbro.koplugin` 目錄下，覆蓋掉舊的檔案，再重新啟動 Koreader。

如果寫的 lua script 有問題的話，在 Android Sutdio 的 logcat 畫面中會有相關的除錯訊息。通常這些訊息都寫得很清楚，能夠很正確地跟你說問題出在哪。

如果對於 lua 語法不熟，或是看不懂出錯在哪的話，通常問一下 ChatGPT 可以得到不錯的回答。畢竟，lua 已經存在很久了，koreader 也是；所以 ChatGPT 有足夠的知識回答 koreader plugin 開發上遇到的問題。

### 相關連結

- AskEinkBro koreader plugin: <https://github.com/einkbro/askeinkbro>
- AskGPT: <https://github.com/drewbaumann/AskGPT>
