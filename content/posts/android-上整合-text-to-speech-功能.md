+++
title = "Android 上整合 Text to Speech 功能"
date = "2022-11-21T13:06:43.565Z"
description = "EinkBro 做為一個瀏覽器，很多開發的功能都是圍繞著內容呈現的調整。今天，要來介紹 9.14.0 新加入的特別功能：語音閱讀網頁內文。"
slug = "android-上整合-text-to-speech-功能"
canonicalURL = "https://medium.com/@danielkao/android-%E4%B8%8A%E6%95%B4%E5%90%88-text-to-speech-%E5%8A%9F%E8%83%BD-d5f50eb920ac"
mediumID = "d5f50eb920ac"
tags = ["EinkBro"]
+++

![](/images/d5f50eb920ac/1_6kubw9JkK-gY-FQNL7fWzQ.png)

EinkBro 做為一個瀏覽器，很多開發的功能都是圍繞著內容呈現的調整。今天，要來介紹 9.14.0 新加入的特別功能：語音閱讀網頁內文。

在 Android 上，Text to Speech 功能早在 API level 4 就開始支援，不過，好像很少有瀏覽器有支援這功能。畢竟，大部分人使用瀏覽器都是想要用眼睛去看內容，而網頁的篇幅通常也不會太長。

[TextToSpeech | Android Developers](https://developer.android.com/reference/android/speech/tts/TextToSpeech)

在電子書閱讀器上使用 EinkBro 的使用者，很多時候是想要用它來看網路小說，在這種情況下，如果 EinkBro 可以提供語音閱讀的功能的話，在使用方式上就更加地多元。

### 實作

#### 包裝 TextToSpeech 儿件

系統內建的 `TextToSpeech` 元件提供了大部分語音閱讀需要的函式。首先，新增一個 `TtsManager` class，將 `TextToSpeech` 相關的操作都寫在裡面。

在 28, 30 行，可以看到兩種不同的啟動語音閱讀的型態：一個是 QUEUE\_ADD，一個是 QUEUE\_FLUSH。前者是把文字片段加到語音閱讀的 queue 當中，而 QUEUE\_FLUSH 表示，當呼叫後，就開始播放 queue 中的內容。

另外，還有一點值得注意的是：25 行的 `TextToSpeech.getMaxSpeechInputLength()` 是每段語音的最大長度。超出這長度的文字，會造成 tts 不唸這段文字。為了要繞過這問題，這裡使用了 kotlin collection 的 `chunked` 將一大段文字切分成允許範圍內的多個片段。

![](/images/d5f50eb920ac/1_AyGtHCtgwGMEcoEg4tfc9Q.png)

#### 修改 EinkBroApplication

再來，因為 TextToSpeech 的實作是系統提供的，所以整個 App 共用一個實體就好，不需要在每個 Activity 中都生成一個。

因此我們在 `EinkBroApplication.kt` 中建立起一個 TtsManager 實體，並且定義好當 `onTerminate()` 被呼叫時，要把它回收掉。不然，這個元件會在系統背後持續播放，直到你重開手機或是等到它把內容全部讀完。

![](/images/d5f50eb920ac/1_pnd205FF32unh2W8cqy9LA.png)

#### 主要的使用邏輯

EinkBro 大部分的操作邏輯都在 BrowserActivity 中，這次也不例外。雖然這寫法很糟糕，不過，如果要重構成一堆 ViewModel，也是個大工程。這是題外話了，讓我們回到主題：

之前實作翻譯功能時，已經有個函式 `NinjaWebView.getRawText()` 能夠取得當前網頁中的純文字內容。在 1777 行，我們將這個函式拿到的內容餵入 `TtsManager.readText()` 。因為 `getRawText()` 是非同步的，所以要用 lifecycleScope 包裝起來。

1852 行的 `toggleTtsRead()` 則是藉由 `TtsManager.isSpeaking()` 判斷是不是正在語音閱讀中：如果是的話，這時的動作應該是要停止播放。

![](/images/d5f50eb920ac/1_zWcSQxuBXesmtUAP02ejmQ.png)

#### 語音設定

Android 語音閱讀有一些調整的彈性，包括更換不同語音引擎 (不同語言有可能存在更專業的語音引擎，可以透過 Google Play Store 下載)，切換發音的語言，調整發音的速度和發音的語調。有些引擎還支援同個語言裡有多個不同特性的語音。

有鑑於大部分的調整都能在系統的設定中做改變，針對這部分我只實作了兩件是：

- 調整語音閱讀的語速
- 將使用者快速帶到系統的語音閱讀設定中

前者很單純，只要使用者設定好想要的語速後，透過 `TtsManager.setSpeechRate` 就可以了。

![](/images/d5f50eb920ac/1_DTdHDYYWlo9PFdVwpY-thw.png)

後者則是建立一個 `Intent` 來達成。

![](/images/d5f50eb920ac/1_bjiNOS5ZEnZpxAFkCp5urA.png)

### 後話

目前的實作還很陽春，但對於單篇網頁的閱讀來說，已經綽綽有餘。以後有機會的話，想要擴充這功能，讓它可以在閱讀文章時，加入其他文章的內容到 queueu 中。這樣子就可以一直邊看邊聽了。

### 相關連結

[Comparing v9.13.0...v9.14.0 · plateaukao/einkbro](https://github.com/plateaukao/einkbro/compare/v9.13.0...v9.14.0)
