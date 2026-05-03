+++
title = "Google Play Store: 您的裝置與這個版本不相容"
date = "2022-11-05T15:55:06.480Z"
description = "這也是老毛病了。三不五時會有使用者反應，雖然在 Google Play Store 中可以找到 EinkBro，但想要下載時，畫面上卻顯示 “您的裝置與這個版本不相容”。由於之前我也沒認真去研究為什麼會發生，所以通常解決方式都是：請使用者上 Github 網站，直接下載 apk…"
slug = "google-play-store-您的裝置與這個版本不相容"
canonicalURL = "https://medium.com/@danielkao/google-play-store-%E6%82%A8%E7%9A%84%E8%A3%9D%E7%BD%AE%E8%88%87%E9%80%99%E5%80%8B%E7%89%88%E6%9C%AC%E4%B8%8D%E7%9B%B8%E5%AE%B9-11a8a3bbccdb"
mediumID = "11a8a3bbccdb"
+++

這也是老毛病了。三不五時會有使用者反應，雖然在 Google Play Store 中可以找到 EinkBro，但想要下載時，畫面上卻顯示 “您的裝置與這個版本不相容”。由於之前我也沒認真去研究為什麼會發生，所以通常解決方式都是：請使用者上 Github 網站，直接下載 apk 來安裝或是去 f-droid 上安裝。

這幾天，想到了一個可能性是：前不久為了支援在某些語言教學網站上，需要錄音的需求，在 `AndroidManifest.xml` 中加了相關的需求：

```
<uses-feature android:name="android.hardware.microphone" />  
<uses-permission android:name="android.permission.AUDIO_CAPTURE" />
```

會不會就是因為這些需要 `uses-feature` 的設定造成部分的閱讀器被 Play Store 過濾掉呢？

有了這個懷疑後，自然是先去看一下 `uses-feature` 的官方說明。不看還好，一看才發現真的是那麼一回事。

[| Android Developers](https://developer.android.com/guide/topics/manifest/uses-feature-element)

官網說得很清楚：

> Google Play 會使用應用程式資訊清單中宣告的 `<uses-feature>` 元素，篩選不符合應用程式硬體和軟體功能要求的裝置。

> 您可以透過指定應用程式所需的功能，讓 Google Play 僅對裝置符合應用程式功能需求的使用者顯示應用程式，而不要向所有使用者顯示。

當時在修改 AndroidManfest.xml 時不以為意，沒想到因此而排除掉了一些電子書閱讀器裝置。很多 6 吋或 7 吋的設備，為了節省成本，將觸角伸到更多普羅大眾，機器本身很常不帶麥克風，甚至是喇叭也不見得閱讀器是標配。

### 解決方式

既然找到了原因，那要解決這問題就容易多了。加上 `uses-feature` 會讓 Google Play 去過濾掉裝置的話，那自然會有一些參數可以讓 Google Play 能忽略掉這些設定。其方式如下，在該 uses-feature 描述中，加上 `android:required=”false”` 的標識。

```
<uses-feature android:name="android.hardware.microphone" android:required="false" />
```

這樣就結束了嗎？還沒還沒。除了麥克風之外，會不會更早之前就有漏網之魚呢？再仔細研究一下 `uses-feature` 的說明後發現：原來有些 permission 的宣告，Android 是會幫你偷偷加上 `uses-feature` 的屬性的，也因此，會雞婆地幫你濾掉那些不符合的硬體設備。究竟有哪些 permission 會這麼幫倒忙呢？官網列了下面這張大表：

![](/images/11a8a3bbccdb/1_3B8bWSRpmnViR5E35PGvug.png)

![](/images/11a8a3bbccdb/1_aVGyW0XAlVv0nF9Vd06_Fg.png)

在表格中可以發現，針對位置資訊的 permission `ACCESS_FINE_LOCATION` 和 `ACCESS_CORSE_LOCATION`，它們都會隱含了對於 `android.hardware.location` 的硬體需求。

在 EinkBro App 中，有些網站會需要裝置的位置訊息來提供在地化的資訊，像是氣象網站之類的。這些應用場景 EinkBro 會跳出詢問使用者是否同意該網站要求的對話框。

對於沒有位置資訊的設備，頂多就讓它在這些網站抓不到位置資訊就好，沒必要完全禁止它們安裝 EinkBro 才對。所以，為些，我們也要額外再加上下面的宣告，讓 Google Play 不要雞婆濾掉這些裝置。

```
<uses-feature android:name="android.hardware.location" android:required="false" />
```

### 結語

新版 EinkBro 在 Google Play 上發布後，果然，我的文石 Book Poke 4 s 就可以正常地從 Google Play 上安裝 EinkBro 了。

### 相關連結

[| Android Developers](https://developer.android.com/guide/topics/manifest/uses-feature-element)

- [修正此問題的 commit](https://github.com/plateaukao/einkbro/commit/497b51940e33dd8199dc947a45ba843efac3aa02)
