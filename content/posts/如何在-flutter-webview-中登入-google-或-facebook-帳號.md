+++
title = "如何在 Flutter WebView 中登入 Google 或 Facebook 帳號"
date = "2020-09-02T17:13:10.347Z"
description = "開發 Flutter  App 時，偶爾需要使用 WebView 提供一些既有的功能，或是短暫地開啟一個 App 內的 Web 畫面讓使用者在不離開 App 的情況下，能夠使用其他網站的內容。這時常常會遇到別人的 Web 服務需要先登入 Google 或 Facebook…"
slug = "如何在-flutter-webview-中登入-google-或-facebook-帳號"
canonicalURL = "https://medium.com/@danielkao/%E5%A6%82%E4%BD%95%E5%9C%A8-flutter-webview-%E4%B8%AD%E7%99%BB%E5%85%A5-google-%E6%88%96-facebook-%E5%B8%B3%E8%99%9F-cf5135af59df"
mediumID = "cf5135af59df"
+++

開發 Flutter App 時，偶爾需要使用 WebView 提供一些既有的功能，或是短暫地開啟一個 App 內的 Web 畫面讓使用者在不離開 App 的情況下，能夠使用其他網站的內容。這時常常會遇到別人的 Web 服務需要先登入 Google 或 Facebook 才能繼續使用。如果沒有為此修改一下 WebView 實作的話，通常是會登入失敗的。

### Android WebView 中的 User Agent String

在 Android 平台上，第一件要做的事是把 WebView 的 user agent 給改掉。Android WebView 預設的 user agent string 帶有 wv 的字樣，Google 在登入時會先檢查是不是一般的 browser；如果它在 user agent string 中發現 wv 字樣的話，就會顯示 403 錯誤，跟你說這不是一個合格的 browser，請你換其他的 browser 再試著登入看看。

解決這第一個問題很容易，只要把 WebView user agent string 中的 wv 字樣刪除就可以。

### New Window 問題

串接 Google / Facebook 登入時，Web Service常會利用 target = \_blank 或是 window.open 的方式將登入相關的邏輯用新的 Web Window 呈現。在 Desktop 或是手機上 browser 的運作方式會開啟一個新的 tab 來執行，等到登入完成後，會再回到原本的 Web 畫面，更新登入狀態。

Android 的 WebView 也有提供開啟新的 Web Window 的介面 `WebChromeClient.onCreateWindow()` ，如果開發者想要達到跟 browser 一樣的功能的話，可以自己實作這個函式。

[https://developer.android.com/reference/android/webkit/WebChromeClient#onCreateWindow(android.webkit.WebView,%20boolean,%20boolean,%20android.os.Message)](https://developer.android.com/reference/android/webkit/WebChromeClient#onCreateWindow%28android.webkit.WebView,%20boolean,%20boolean,%20android.os.Message%29)

在 Flutter 中要怎麼做呢？這邊以 flutter\_inappwebview 做例子。flutter\_inappwebview 在很早之前有打通了 native 層 `onCreatWindow` 的介面；但在測試之後，發現在最近的 v4.0.0 才真的能做到讓 Google / Facebook 登入的功能。

以 Android 來說，在建立 flutter\_inappwebview 的 InAppWebView 時，要先在 android 專屬的 `AndroidInAppWebViewOptions` 中設 `supportMultipleWindows` 為 `true` (第94行)；然後實作 `onCreateWindow` 。(第103行)

![](/images/cf5135af59df/1_xnRtbhmh3IIX8qd_sAIRbA.png)

`_onCreateWindow` 的實作則是再建立一個新的 `InAppWebView`，用來處理 target = \_blank 或是 window.open 裡帶來的 url。

![](/images/cf5135af59df/1_S050CTJES8tjGFf_a3-XlA.png)

**iOS 也需要更改 user agent String**

這裡，我們透過 `AlertDialog` 包裝 `InAppWebView`；新建立的 `InAppWebView` 要更改其 userAgent，不能包含 wv，針對 iOS 也要改一下，不然會遇到跟 Android 一樣 403 的問題。關於怎麼設定，可以參考下面的 stackoverflow 連結。

[Google Authentication - User agent gives error on WebView (Nylas api)](https://stackoverflow.com/a/50095100/1265915)

**關閉 New Window 視窗**

當新 WebView Window 完成登入後，會呼叫 `onCloseWindow` callback。這時是關閉 `AlertDialog` 的好時機，我們可以利用 `Navigator.pop(context);` 來關閉。

不過不知道為什麼，Facebook 登入的流程會被呼叫兩次 onCloseWindow，為了避免這件事，這裡用了一個變數 `_isWindowDisplayed` 來確保 `AlertDialog` 只會被關閉一次。

### Demo

![](/images/cf5135af59df/1_id22lDlY_xjQLogPUJftGQ.gif)

### 結語

如果能有個包裝得更高層的 WebView，把這些常見的問題都事先處理好，或是提供內建的處理方式，只需要設設 flag (像是 enableSocialNetworkLogin)就可以支援相關功能的話，那該有多好啊。

#### 範例程式碼連結

[plateaukao/flutter\_webview\_login\_demo](https://github.com/plateaukao/flutter_webview_login_demo)

[pichillilorenzo/flutter\_inappwebview](https://github.com/pichillilorenzo/flutter_inappwebview)

### 看更多

[與 Flutter WebView 奮鬥的故事](https://medium.com/@danielkao/%E8%88%87-flutter-webview-%E5%A5%AE%E9%AC%A5%E7%9A%84%E6%95%85%E4%BA%8B-a353f0094734)

[輕鬆完成 Flutter 上的 i18n](https://medium.com/@danielkao/%E8%BC%95%E9%AC%86%E5%AE%8C%E6%88%90-flutter-%E4%B8%8A%E7%9A%84-i18n-19655dbe7546)

[Implementation of Instagram-like Long Press popup Dialog in Flutter](https://medium.com/@danielkao/implementation-of-instagram-like-long-press-popup-dialog-in-flutter-25fd955fd38a)
