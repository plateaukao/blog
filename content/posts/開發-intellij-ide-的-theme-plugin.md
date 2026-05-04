+++
title = "開發 IntelliJ IDE 的 theme plugin"
date = "2022-08-12T16:14:50.678Z"
description = "使用文石的電子紙螢幕 Mira 差不多要一年了，平常拿來看網路上的文章外，還很常拿它來開發 side projects。不過，在使用 Android Studio 時，一直是很克難地使用系統內建的 IntelliJ Light…"
slug = "開發-intellij-ide-的-theme-plugin"
canonicalURL = "https://medium.com/@danielkao/%E9%96%8B%E7%99%BC-intellij-ide-%E7%9A%84-theme-plugin-91e06f5b1fcd"
mediumID = "91e06f5b1fcd"
tags = ["電子書閱讀器"]
[cover]
  image = "/images/91e06f5b1fcd/1_GE3Pm7UIVERQ2dvdJlFIGw.png"
+++


使用文石的電子紙螢幕 Mira 差不多要一年了，平常拿來看網路上的文章外，還很常拿它來開發 side projects。不過，在使用 Android Studio 時，一直是很克難地使用系統內建的 IntelliJ Light 主題。雖然不會整個畫面一片黑，但是大面積的淺色背景依然不夠黑白分明，使用一段時間後，還是要不定時地手動刷新畫面。所以，今天花了點時間，寫了一個 Eink 螢幕專用的 theme，在這邊也順便記錄一下開發的方式。

### 前置作業

[Setting Up a Development Environment | IntelliJ Platform Plugin SDK](https://plugins.jetbrains.com/docs/intellij/setting-up-environment.html)

其實，照著官方網上教學，一步步做就可以了。不過，因為官網都是寫英文，所以我還是稍微講一下我開發的過程。雖然我主要想裝 theme 的 IDE 是 Android Studio，但因為它跟 IntelliJ 系出同門，所以要開發 theme plugin 的話，需要先安裝 IntelliJ CE。這到下面官網抓來裝一下就行。

[Download IntelliJ IDEA: The Capable & Ergonomic Java IDE by JetBrains](https://www.jetbrains.com/idea/download/#section=mac)

安裝好後，到設定的 Plugins 中，把 Plugin DevKit 也安裝進來。

### 新增一個 Plugin 專案

[Creating a Plugin Project | IntelliJ Platform Plugin SDK](https://plugins.jetbrains.com/docs/intellij/creating-plugin-project.html)

從 IntelliJ CE 中，新增一個 IDE Plugin 的專案。

![](/images/91e06f5b1fcd/1_GE3Pm7UIVERQ2dvdJlFIGw.png)

完成後，專案的目錄結構會長得跟下面類似。resources 目錄下會有大部分的檔案：META-INF 中的 plugin.xml 會定義 themeProvider，這裡會指定你的 plugin id，還有 theme 的名稱；而 theme 目錄中的 einktheme.theme.json 則是用來設定各種 UI 元件在不同狀態時，所需要呈現出來的顏色。

除了設定 IDE 整個介面的顏色外，如果也想要一併調整文字編輯器 (Code Editor) 中的套色，也可以如下圖中的第 17 行，指定另一個 xml 檔來修改相關的顏色設定。

這邊的 Eink.xml 是我參考 [Eink Color Scheme](https://plugins.jetbrains.com/plugin/17106-eink-color-scheme) 這個套件來的，它也有把 source code 放在 [github](https://github.com/leizhag/eink-color-scheme) 上。

![](/images/91e06f5b1fcd/1_pQbuNbjef2p-CDhP3MO6fw.png)

![](/images/91e06f5b1fcd/0_GsRJdDjKkH13KEHo.png)
*官網的目錄說明*

基本上，這樣子就可以先把 theme plugin 編譯出來套用看看了。

### 如何編譯和套用自製的 Plugin

在 Build 選單中，有個 Prepare Plugin Module xxxxxx For Development 的選項，點擊後，就會在 resources 目錄中產生一個 jar 檔。

![](/images/91e06f5b1fcd/1_XIInE3daoEmACbSLTirIxQ.png)

這時，可以進到設定的 Plugin 畫面，選擇 Install Plugin from Disk，然後選擇剛剛產生好的 jar 檔。安裝完後，再重開 IDE，就可以套用自製的 theme 了。

![](/images/91e06f5b1fcd/1_ocrLSNSEABQdbPRFm7RULQ.png)

### 調整 UI 元件的顏色

以下是最基本的設定檔內容，裡面都是 key-value 的 pair。

![](/images/91e06f5b1fcd/1_45ZnfVnMXn2RwgZEiAYk6Q.png)

下面的官網文章有介紹幾個基本元件的設定方式，包括 icons, ui, 等等。因為可以設定的值實在是太多了，文章中的建議竟然是要開發者利用 IDE 的 code completion 來找想要設定的屬性。這方式也太原始了吧，我怎麼知道我想設定的元件可能是叫什麼名字呢？後來，在設定時，有些時候我還是到網路上直接搜尋比較快知道該元件的名稱。

[Customizing UI Themes - Icons and UI Controls | IntelliJ Platform Plugin SDK](https://plugins.jetbrains.com/docs/intellij/themes-customize.html#custom-icon-palette-colors)

除了不是很好用的 code completion 外，在文章的最後面有提到可以利用另一個介面 Laf Defaults 來查找元件名稱，和目前元件的顏色。名字不見得能確定叫什麼，但看了它們的顏色，應該就比較能確認是不是自己想要修改的元件。

Laf Defaults 可以在選單 Tools | Internal Actions | UI Laf Defaults 開啟。但是…預設 Internal Actions 是看不到的，得先用下列方式打開：

- 打開 Help | Edit Custom Properties
- 在裡頭輸入 `idea.is.internal=true` ，然後重開 IDE

### Laf Defaults

在 Laf Defaults 視窗中，因為可以看到每個屬性的目前顏色，在搜尋上比較方便，比方說我打關鍵字 background，就可以看到還有多少背景沒有被我改成白色，再看看名稱決定是不是要做修改。

![](/images/91e06f5b1fcd/1_I4Sw_g3drYTxz1_S6EAQYg.png)

### 調整後的內容

其實修改的地方不多，主要是畫面大區塊的淺灰色都能改成白色，整個的感覺就會好很多。其他細部的修改，就等以後有發現再慢慢調整。

![](/images/91e06f5b1fcd/1_ifQxlZDfYEnNygq_JwQQAg.png)

### 畫面比較

![](/images/91e06f5b1fcd/1_6iRHey7Sb4jl2LSpoJg5xA.jpeg)

![](/images/91e06f5b1fcd/1_FgS2o9hdsLXKGeRKfOaB7w.jpeg)
*左圖：修改前，右圖：修改後*

### 相關連結

第一版 plugin

[Release Release v1.0.0 · plateaukao/intellij\_eink\_theme](https://github.com/plateaukao/intellij_eink_theme/releases/tag/v1.0.0)

Eink Color Theme

[GitHub - leizhag/eink-color-scheme: A color scheme for JetBrains IDEs on eink displays based on…](https://github.com/leizhag/eink-color-scheme)
