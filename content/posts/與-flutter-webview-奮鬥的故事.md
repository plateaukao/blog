+++
title = "與 Flutter WebView 奮鬥的故事"
date = "2020-08-06T14:57:17.365Z"
description = "如果 App 完全用 Flutter 開發，是件很愉快的事情，什麼都是在掌控之中。但如果扯上 WebView 時，就完全不是那麼一回事了。"
slug = "與-flutter-webview-奮鬥的故事"
canonicalURL = "https://medium.com/@danielkao/%E8%88%87-flutter-webview-%E5%A5%AE%E9%AC%A5%E7%9A%84%E6%95%85%E4%BA%8B-a353f0094734"
mediumID = "a353f0094734"
[cover]
  image = "/images/a353f0094734/1_wkDc2HijgBPP8qrAWPTV6w.jpeg"
+++


### 與 Flutter WebView 奮鬥的那些日子

![](/images/a353f0094734/1_wkDc2HijgBPP8qrAWPTV6w.jpeg)
*新北市的天空*

如果 App 完全用 Flutter 開發，是件很愉快的事情，什麼都是在掌控之中。但如果扯上 WebView 時，就完全不是那麼一回事了。

---

### 選擇

在 Flutter 中要套用 WebView 的話，通常有兩個比較主要的選擇：一個是 Flutter team 官方推出的 [webview\_flutter](https://pub.dev/packages/webview_flutter) 。這個套件跟其他的比起來，至少維護性是可以保證的，因為官方會不斷地修正問題和配合新的 Flutter 版本改善其實作。但它的缺點是，彈性不高，很多想要針對 WebView 做的操作，都會因為它沒有開洞讓你去 hook function 而無法達成。要嘛，就是要自己 fork 一份 webview\_flutter plugin，然後自己開洞來完成；不然就是要等得天荒地老，看哪一天 Flutter team 佛心大發，幫你將想要的功能實作在新版裡頭。

第二個主要的選擇是 [flutter\_inappwebview](https://pub.dev/packages/flutter_inappwebview) 。相較於 webview\_flutter 的小而美，flutter\_inappwebview 則是個包山包海的大補丸。它除了提供一般人比較需要的 inappwebview UI component，讓你可以將WebView Widget 塞到現有的Flutter Widget Tree 裡，跟其他的 Flutter Widget 可以在畫面上互相配合；也提供全畫面，類似 Android 中 Activity的 WebView 模組，可以在不需要跟其他 Flutter Widget 互動的情況下，直接跳個 WebView 畫面出來。

[flutter\_inappwebview | Flutter Package](https://pub.dev/packages/flutter_inappwebview)

看一下上面 flutter\_inappwebview 的 Readme，內容多到眼花暸亂。它的長度大概是 webview\_flutter 的50倍以上吧；就提供的功能來說，說不定也是。如果覺得 Readme 太雜，不好閱讀的話，最近flutter\_inappwebview 的作者 Lorenzo Pichilli，很佛心地寫了兩篇 medium 來介紹他開發的 plugin 要怎麼用，有提供那些好用的功能，以及~~如何用他的 plugin 開發出一個 Browser App！

[InAppWebView: The Real Power of WebViews in Flutter](https://medium.com/flutter-community/inappwebview-the-real-power-of-webviews-in-flutter-c6d52374209d)

[Creating a Full-Featured Browser using WebViews in Flutter](https://medium.com/flutter-community/creating-a-full-featured-browser-using-webviews-in-flutter-9c8f2923c574)

看到這麼厲害的文章，可能會想說，連 Browser 都可以自己寫一個出來了，看來在 Flutter 上使用 WebView，應該是一塊蛋糕吧！只要把 WebView Widget build 出來，塞塞參數，然後叫它 `loadUrl()` 應該就沒有工程師的事了吧。

但其實魔鬼都是藏在細節裡的。當你大意地踏入整合 WebView 之後，才會發現這其實是一個很大的坑。

- WebView 的生成效能不好 (其實在 native 時本來就沒有好到哪去)，所以如果有 page transition animation 的話，可能會看到卡卡的。
- 根據 device 的不同，有的 device 在 WebView Widget 生成時，畫面會先黑一下。
- Url navigation, 在 Android 和 iOS 的行為有時相同，有時不同。
- 有些功能在 Android 上可以運作，有些則是在 iOS 上才有作用。
- **!!! 在 Android 平台上，有些中文輸入法是殘廢的 !!!**

這點很重要，所以要畫粗體字。作者是外國人，跟大部分的開發者都是針對歐美國家開發 App 的，所以不見得會遇到輸入法的問題；但對於開發給 CJK 之類語言的 App 來說，就會有很大的影響。Chinese, Japanese, Korean，都是需要組字來完成輸入的。有些輸入法(特別是大量被內建在很多手機中的 gboard)的組字方式，在目前的 Flutter WebView plugin 中都是沒有作用的，不論是 webview\_flutter 或是 flutter\_inappwebview 都一樣。

### 解決問題

關於 Android / iOS 平台的行為不一，只能遇到一個處理一個，但至少還算是可控的。

效能不好，也可以透過一些偷吃步的方式，讓畫面看起來比較順暢一點。

畫面會先黑掉再顯示 Web 內容的問題，也可以藉由事先顯示一個畫面中央的載入中 icon來拖點時間，等到 WebView loading progress 來到 20% 或 30%時，再把載入中 icon 移除；這樣子就能很巧妙地隱藏住黑畫面。

#### 中文輸入法問題

最難解的中文輸入問題，就不是從 app 層可以解決的了，因為這牽扯到 Flutter 底層實作 PlatformView 的方式。 PlatformView 是用來將平台上原生的 View 元件，包成像 Flutter Widget的樣子，讓它可以嵌入在 Flutter Widget Tree 中。關於 PlatformView 的實作詳細介紹，和為什麼它會造成輸入法有問題，可以參考下面這篇介紹：

[Flutter完整開發實戰詳解(二十、AndroidPlatformView和鍵盤問題)](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/714998/)

下面這一篇則是從 flutter 的程式碼來分析

[5分钟彻底搞懂Flutter中PlatFormView与Texture](https://cloud.tencent.com/developer/article/1584477)

既然這是 Flutter framework 的問題，應該很多人也都遇到，而且有發 issue 吧；自己解決不了，總可以時時關注官方的資訊，看何時有被列入開發，何時可以正式 release。

所以，先上了 flutter github 試著找找相關的 issue。果不其然，很快地就找到了下面這一條 issue (和一堆類似的)。

[[webview\_flutter] Keyboard language can't change on Android · Issue #41089 · flutter/flutter](https://github.com/flutter/flutter/issues/41089)

![](/images/a353f0094734/1_QHhhXvZhJ3nlQeuxqyEGJQ.png)

雖然這條 issue 的對象是 webview\_flutter，但因為每個 webview plugin 的作法都是透過 PlatformView，所以問題點其實都是一樣的。看到這條 issue 被提出的時間是在去年(2019)的9月多；到現在還是 open 的狀態，心就涼了一半。

以後要記得，任何 promotion 式的數據和動人故事，都只會訴說美好的一面，但絕對都不會提到這個平台或架構是不是有數不盡的 issue，萬年臭蟲。一旦其中一條踩到了你的 App 的核心功能，那真是欲哭無淚。

也不知道是運氣好，還是 Flutter 要出頭天了，在我查到這條 issue 的幾天後，Google Flutter dev Blasten 在這條 issue 上提及了另一條他新開出來的 issue，並留言說，有一大掛的 issue 將會由某個 PR 給一口氣解決掉。

[[webview\_flutter] Add new entrypoint that uses hybrid composition on Android · Issue #61133 ·…](https://github.com/flutter/flutter/issues/61133)

瞧下面這截圖列的 issue 之多，讓人又興起了一絲期待。

![](/images/a353f0094734/1_iKYWYkLGp3gQureR5g4QQg.png)

對於這 PR，自然是充滿了好奇，到底是什麼黑魔法，可以一次解決那麼多 PlatformView 帶來的各種問題。進到該 [pull request](https://github.com/flutter/plugins/pull/2883) 看了一下：

![](/images/a353f0094734/1_1Tt5vAtr5Oz8AToTB0D1FA.png)
*pull request cotent*

可以看到其實在這 PR 中， `SurfaceAndroidWebView` 只是把 `AndroidWebView` 的 build 覆寫掉。

`AndroidWebView` 原本是建立一個 `AndroidView` 。從下面的程式碼可以看出來， `build` function 中 41 行的 `AndroidView` ，在 `SurfaceAndroidWebView` 的 `build` 中，被覆寫成使用 `PlatformViewLink`元件。

![](/images/a353f0094734/1_Aiew76ZTRz7LurVczMBw8Q.png)

原來這個 PR 只是換個元件而已，真正的改動，應該是在其他 flutter framework的 PR 中吧。不過既然有了這支 PR 可以支援 webview\_flutter 的中文輸入法；如果我如法炮製，也在 flutter\_inappwebview 中也把 `AndroidView` 換成 `PlatformView` 的話，是不是也一樣行得通呢？

**發 PR 不落人後**

於是，我 fork 了一份 flutter\_inappwebview，參考上面的 PR，把它也改了一下；並且把 flutter 版本升級到當時的 dev channel 1.20.xxx (因為當時的 flutter beta/stable channel 都還不支援 `PlatformViewLink`)，很開心地發現，中文輸入法就出現了！而且可以用！

為了希望這個 fix 能趕快也被加入 flutter\_inappwebview，不讓官方的 webview\_flutter 專美於前，所以我也趕緊發了個 PR 到 flutter\_inappwebview去。

[Use PlatformViewLink widget for Android WebView by plateaukao · Pull Request #462 ·…](https://github.com/pichillilorenzo/flutter_inappwebview/pull/462)

作者說，他也在等 hybrid composition 進到 flutter stable channel。在那之後他就要進 code 啦。不知道 hybrid composition 是什麼的話，可以參考下面這個 wiki 說明。

[flutter/flutter](https://github.com/flutter/flutter/wiki/Hybrid-Composition)

在我 PR 發完的九天後，也就是昨天(8/5)， Flutter SDK 也正式 release 了 1.20.0！一切看起來都是那麼地順利。

[Flutter SDK releases](https://flutter.dev/docs/development/tools/sdk/releases)

再來，就等 flutter\_inappwebview 進版，然後就可以一飛沖天囉！希望以後不需要再跟 WebView 搏鬥了。
