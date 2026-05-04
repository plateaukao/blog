+++
title = "QuickRotate Utility on Android Devices — 肥大的 Android Library"
date = "2022-04-18T13:45:25.910Z"
description = "在文石的電子書閱讀器上，旋轉畫面的工具很不好用，要三個動作才能完成：1. 從畫面上方，下拉控制區塊；2. 點擊旋轉按鈕；3. 找到想要旋轉的方向，點下去。"
slug = "quickrotate-utility-on-android-devices-肥大的-android-library"
canonicalURL = "https://medium.com/@danielkao/quickrotate-utility-on-android-devices-%E8%82%A5%E5%A4%A7%E7%9A%84-android-library-e844a54c9e42"
mediumID = "e844a54c9e42"
tags = ["電子書閱讀器"]
[cover]
  image = "/images/e844a54c9e42/0_RuXfzPIIvX_ftizd"
+++


### QuickRotate Utility on Android Devices — 1.8 MB 與 57.9 KB 的距離

在文石的電子書閱讀器上，旋轉畫面的工具很不好用，要三個動作才能完成：1. 從畫面上方，下拉控制區塊；2. 點擊旋轉按鈕；3. 找到想要旋轉的方向，點下去。

![](/images/e844a54c9e42/0_RuXfzPIIvX_ftizd)
*圖1. 文石電子書閱讀器的旋轉功能*

為了讓第三個步驟能省略掉，我寫了一個小工具來幫我。Android 從 7.0 開始，有提供可以客製化 Quick Tile Settings 的功能。平常需要開開關關的功能，都可以包裝成一個 `TileService`，放到下拉通知欄的區域。詳細的教學可以看一下下面的文章。

### Quick Setting 實作

[Quick Settings Tiles](https://medium.com/androiddevelopers/quick-settings-tiles-e3c22daf93a8)

利用這方式，我建立了一個簡單的 `TileService` 來做畫面旋轉的功能。安裝後就可以在文石閱讀器中，加入新的旋轉按鈕，不用再從上面圖1中的四個方向做選擇。

[GitHub - plateaukao/quickrotate: quickly rotate screen on Android devices without second thought](https://github.com/plateaukao/quickrotate)

### 圖示

![](/images/e844a54c9e42/0_TP_MWQ5S6AYqMQ0X.png)
*圖2. 加入了左轉的按鈕*

### 如何縮小程式的大小

當我在完成這個小工具時，發現到明明只有寫了幾十行的程式碼，和放了兩張左旋轉和右旋轉的圖案，編譯出來的 apk 竟然要 1.8 MB 之大。這超出了我的想像。

我試著在 build.gradle 中加入 proguard 的設定，但似乎編譯完後，沒有什麼幫助。我再研究了一下 build.gradle 中的有使用到的函式庫：

```
implementation 'androidx.core:core-ktx:1.7.0'      
implementation 'androidx.appcompat:appcompat:1.4.1'    implementation 'com.google.android.material:material:1.5.0'    implementation 'androidx.constraintlayout:constraintlayout:2.1.3'
```

這個利用 Android Studio 建立出來的 Empty Activity project，預設就塞了這些函式庫。以這個小工具來說，除了在還沒取得系統設定讀寫的功能前，需要跳出系統的同意畫面讓使用者同意外，完全不會有 UI 呈現。

所以，這些函式庫應該都要有辦法拿掉才對。於是，我先把程式中唯一的 MainActivity 的 layout xml 從 ConstraintLayout 改成 LinearLayout；然後，把 MainActivity 的 parent class 從 AppCompatActivity 改成 Activity。

最後，我把 Android Studio 幫我生成的 App Theme 也拔掉了，這麼一來，就也可以把 **android.material** 和 **androidx.core** 的依賴也移除。

如此一來，整個程式的大小馬上縮小到 **57.9 KB** 。

詳細的 commit 可以看下面這個連結。

[refactor: remove un-necessary stuff: androidx support, material desig... ·…](https://github.com/plateaukao/quickrotate/commit/18eb53fb381a8dab6f9cd902525de86750c67ce0)

### 結論

如果只是想寫個 quick setting tile 的話，是可以把 Android 的各種函式庫都拔掉的。**1.8 MB 和 57.9 KB 的差別**，中間差了 30 倍呢。(雖然都很小就是了)
