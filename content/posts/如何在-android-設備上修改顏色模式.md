+++
title = "如何在 Android 設備上修改顏色模式"
date = "2023-12-03T13:27:28.526Z"
description = "會想要修改模式是因為在彩色電子紙閱讀器上，廠商通常只有提供增強整體顏色，加強鮮豔度和色彩亮度等選項，但並沒有提供 R, G, B 個別顏色的調整方式。"
slug = "如何在-android-設備上修改顏色模式"
canonicalURL = "https://medium.com/@danielkao/%E5%A6%82%E4%BD%95%E5%9C%A8-android-%E8%A8%AD%E5%82%99%E4%B8%8A%E4%BF%AE%E6%94%B9%E9%A1%8F%E8%89%B2%E6%A8%A1%E5%BC%8F-4d4eead4ed19"
mediumID = "4d4eead4ed19"
tags = ["電子書閱讀器"]
[cover]
  image = "/images/4d4eead4ed19/1_ZR1KLpfP94QtjFuIsBSSqA.jpeg"
+++


會想要修改模式是因為在彩色電子紙閱讀器上，廠商通常只有提供增強整體顏色，加強鮮豔度和色彩亮度等選項，但並沒有提供 R, G, B 個別顏色的調整方式。

![](/images/4d4eead4ed19/1_ZR1KLpfP94QtjFuIsBSSqA.jpeg)

每個人對於色彩的接受程度不同，比較嚴重的像是色盲，無法分辨自然世界中的某些顏色。這時，如果可以調整顏色模式的話，對於閱讀來說，會更加舒服。另一點是，雖然買的是彩色電子紙閱讀器，但有的時候還是會希望畫面以灰階的方式呈現，避免顏色的干擾。純脆黑白的畫面，解析度也比較高。

### 手動調整

今天在看 Android 預設的 Setting App 時，發現在無障礙設定下有個色彩校正的選項，開啟後可以調整為”綠色弱視”、”紅色弱視”和”藍色弱視”。雖然這是用來讓色弱的人透過調整不同顏色的比重，讓他們更容易識別畫面，但是對於一般人來說，剛好也可以拿來切成自己比較喜歡的色彩組合。像我常常覺得文石 Onyx Tab Ultra C 的紅色總是過於鮮豔，如果切換到”紅色弱視”的選項，整個畫面對我來說會更協調。

![](/images/4d4eead4ed19/1_IBBI4u86Iy1ZqBqMUswKcg.jpeg)

將這個發現分享到網站上後，有網友問說，不知道有沒有可以切換成灰階模式的方法。仔細想想，確實有的時候會希望將模式改成黑白的。在彩色閱讀器上，如果畫面是黑白的，它的解析度是 300ppi，但在顯示彩色內容時只有 150 ppi。如果是在文字較多的情況，或是不想因為顏色而分心的場合時，能夠切換到灰階模式會是更為理想的。

經過一番搜尋後，發現其實可以透過設定 Developer Options 中的參數達成。在開發者進階選項中，比一般設定裡多了一個 “全色盲” 的選項，設定後就會讓整台設備以灰階的方式呈現。

![](/images/4d4eead4ed19/1_1pleNzawCcWJOWMa3vtFNw.jpeg)

### 開發快速鍵來開關灰階模式

找到灰階模式可行的方式後，接下來就想說是不是能有更方便的操作方式。不然，每次都要進到開發者選項也是很煩人的。既然是在開發者選項中，通常都會有其他非手動的設定方式，能讓開發者快速地做調整，進行測試。

很幸運地，找到 Android 原始碼中關於 Accessibility 的相關程式碼片段:

[platform\_frameworks\_base/core/java/android/view/accessibility/AccessibilityManager.java at master ·…](https://github.com/aosp-mirror/platform_frameworks_base/blob/master/core/java/android/view/accessibility/AccessibilityManager.java#L132C29-L132C61)

[platform\_frameworks\_base/services/core/java/com/android/server/display/color/ColorDisplayService.jav…](https://github.com/aosp-mirror/platform_frameworks_base/blob/main/services/core/java/com/android/server/display/color/ColorDisplayService.java#L582-602)

![](/images/4d4eead4ed19/1_ZH-hNyBPd-voaSzaCq9G2A.png)

再順著這些關鍵字到 github.com 上找一找，就找到已經有人做了我想要的功能：把切換灰階模式實作在 TileService 中。如此一來使用者就可以很方便的將這個功能加到系統選單中。

[GitHub - fei-ke/Greyscale: 快速切换灰度模式](https://github.com/fei-ke/Greyscale/tree/master)

整個程式主要就兩個檔案，一個是 TileService 的實作，而真正的邏輯是在 Util.java 中。

```
public static boolean isGreyscaleEnable(Context context) {  
     ContentResolver contentResolver = context.getContentResolver();  
     return Secure.getInt(contentResolver, DISPLAY_DALTONIZER_ENABLED, 0) == 1  
          && Secure.getInt(contentResolver, DISPLAY_DALTONIZER, 0) == 0;
```

如同其他系統設定，想要修改的話，得透過調整 Secure Setting 中的參數；因此，需要事前為 App 取得相關的權限。

取得權限的方式，不像一般的權限可以跳出對話框讓使用者同意，而是需要使用 adb，在電腦上操作，或是如果已經 root 過的設備，可以利用 su 來給予權限。

adb 的指令如下(info.plateaukao.quickrotate 是我的 application id)：

```
adb shell pm grant info.plateaukao.quickrotate android.permission.WRITE_SECURE_SETTINGS
```

### 整合到 QuickRotate

雖然有好心人已經開發出來 App 了，但早就已經為好多個功能寫了 TileService 的我怎麼會想就這麼再裝一個別人寫好的 TileService 呢？所以，迅速打開 QuickRotate 專案，新增了一個 TitleService，把找到的實作給搬了進來。這就是 Open Source 的威力呀~

[feat: add colorspace grayscale toggle · plateaukao/quickrotate@66dbefe](https://github.com/plateaukao/quickrotate/commit/66dbefe308ace951fd750d7cda2a9a6572c86dc9)

### 示範影片

[demo of QuickRotate App with Grayscale toggling](https://youtube.com/shorts/J4xO-00fKSs)

### 相關連結

- [QuickRotate v2.2.0](https://github.com/plateaukao/quickrotate/releases/tag/v2.2.0)
