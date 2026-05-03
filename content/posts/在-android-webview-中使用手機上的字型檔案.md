+++
title = "在 Android WebView 中使用手機上的字型檔案"
date = "2022-01-21T15:45:55.800Z"
description = "這個需求來自於每台手機或電子書閱讀器的預設字型都長得不太一樣，有的是用比較粗的黑體，有的是用我不太喜歡的細圓體；有些時候網頁還會套上自己想要的雲端字體。面對這麼多系統或網頁提供的字型，看久了總是會覺得膩，或是單純地只是想要用一套自己最喜歡的字型就好。"
slug = "在-android-webview-中使用手機上的字型檔案"
canonicalURL = "https://medium.com/@danielkao/%E5%9C%A8-android-webview-%E4%B8%AD%E4%BD%BF%E7%94%A8%E6%89%8B%E6%A9%9F%E4%B8%8A%E7%9A%84%E5%AD%97%E5%9E%8B%E6%AA%94%E6%A1%88-de9157906ee9"
mediumID = "de9157906ee9"
tags = ["電子書閱讀器"]
+++

這個需求來自於每台手機或電子書閱讀器的預設字型都長得不太一樣，有的是用比較粗的黑體，有的是用我不太喜歡的細圓體；有些時候網頁還會套上自己想要的雲端字體。面對這麼多系統或網頁提供的字型，看久了總是會覺得膩，或是單純地只是想要用一套自己最喜歡的字型就好。

很久以前就有試著解決這問題，無奈網上的解決方案都是繞著使用編譯到 apk 中 assets 目錄下的固定字型。這方式無法套用到使用者自行放到手機上的字型檔案；我也不想因此在 2.5 MB 的 APP 中，放入一個動輒 10 到 30 MB 的字型檔案，這樣有點太本末倒置了。

最近，又開始研究這個問題，終於讓我試出了一套可行的方式。雖然還不是很完美的方案，但在此記錄下來，希望以後有機會再把它變得更完美。

### 實作

步驟不多，簡單來說：要讓使用者先選擇一下字型檔，在 WebView 中注入 CSS style，自定義一個字型，把它的 src 指定到一個特別的 uri。當 WebView 在讀取這個 CSS font 時，會經過 `WebViewClient` 的 `shouldInterceptRequest` ，這時要把字型檔的 binary stream 餵進去。

下面就是詳細的步驟內容。

#### 步驟一：從系統中選擇想要的字型檔案

這步驟不難，只是因為要讓使用者選擇字型的話，還是要把這部分的 UI 邏輯先做好。我寫了一個 openFontFilePicker 的函式，叫起系統的 file picker。

![](/images/de9157906ee9/1_kHbSqlE6uZVFbyncCblxQQ.png)

當 Activity 或 Fragment 收到系統回傳的 intent 時，我會把它記錄到 SharedPreferences 中，並且利用第 71, 72 行，取得之後 APP 繼續能夠讀取這個檔案的權限。

![](/images/de9157906ee9/1_KBhGDRW4RAMNJySWZr5jgA.png)

塞在 SharedPreferences 的字型資料，寫了一個簡單的 class 儲存檔名和收到的 content uri。

![](/images/de9157906ee9/1_nOzlR3guaK-EGllFR9UCew.png)

![](/images/de9157906ee9/1_F8fzNkIxYOZbd42G8MU4fw.png)

#### 步驟二：注入 CSS Font 資訊到 WebView 中

注入的方式，網路上倒是有不少文件，而且其實都寫得大同小異。我定義了一段要注入的 script 如下：新增一個 `font-face`，它的 `font-family` 為 `customfont`，來源是隨便訂的 `url(‘mycustomfont’)`，然後把所有 `body` 的字型全換成我的 `customfont`。補充說明一下，在參考加入 Google Web fonts 時(<https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400&display=swap>)，看到 Google 字型設定設定中都會加入 `font-display: swap;` 後來發現，加入後畫面在更換字型時就不會再閃爍。更多的說明可以參見下方的 Controlling Font Performance with font-display。

![](/images/de9157906ee9/1_k7vYhl7REyG2hctjPEc5Aw.png)

[Controlling Font Performance with font-display | Web | Google Developers](https://developers.google.com/web/updates/2016/02/font-display#swap)

注入 CSS 的方式之前我也有包成一個函式了：

![](/images/de9157906ee9/1_L9HXl4Xusj5Rlp7J3mE8eA.png)

#### 步驟三：攔截 WebRequest，傳回字型資訊

利用 injectCSS，將 customFontCSS 注入後，接著要處理 intercept Web Request：在 WebViewClient 中覆寫 shouldInterceptRequest()。主要處理落在下圖的第 5行到 17 行：如果來的 request url 是事前定義好的 mycustomfont 的話，這就是 Web 要來找字型資訊的時機，10, 11 行透過 context.contentResolver 建立檔案串流，再生成一個 WebResourceResponse 回傳。

![](/images/de9157906ee9/1_MSzWyX_eOdJa0OPRIp0dMw.png)

基本上這樣子就可以正確地看到手機上的字型檔案有被載入，用來顯示網頁的內容。

#### 未來需要改進的地方

步驟三可以看到，每次網頁來要求字型資訊時，我都是建立新的 inputstream，回傳一個新的 WebResourceResponse。這邊我有嘗試著 re-use inputstream 或是 WebResourceResponse，但都還沒有成功。所以，也就只能先停在這兒。至少這已經是個可以運作的方案了。

另外一點是，很多網頁的字型都會在不同的 element 中另外設定。這種情況下，直接改 body 的字型會沒有作用，這也造成大部分網頁可以；但少部分的網頁還是會維持原來的字型。這問題稍微可以透過把網頁轉成 Reader mode 來解決，但畢竟不是一個很漂亮的作法。也是希望未來會有更完美的處理方式。

### 示範畫面

![](/images/de9157906ee9/1_MI9j_GDMXkZsroXXoHXsSA.jpeg)

![](/images/de9157906ee9/1_P1yhfVI3ayT3vf4jaA_EkA.jpeg)

![](/images/de9157906ee9/1_hPZ1Y2KTSI8yDkA4TApbqg.jpeg)

![](/images/de9157906ee9/1_irY8mmWpcxIY7q3dhK31Jw.jpeg)

### 程式碼連結

大部分的程式碼都在這個 commit 了，雖然後來還有些小修改。

[some what works now · plateaukao/browser@23acbaa](https://github.com/plateaukao/browser/commit/23acbaa50e34d084c32ae95fc8c1a8861801c89d)
