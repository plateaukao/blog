+++
title = "在 MacOS 快速啟動 Android Emulator"
date = "2021-08-16T16:02:57.238Z"
description = "雖然無法做到如同 M1 chip 的 Mac 設備可以直接執行 iOS App，但是經過點小巧思，還是有辦法在 MacOS 上無縫地使用 Android App。本篇文章將會描述怎麼設定，讓你可以很方便地在 MacOS 中使用 Android App。"
slug = "在-macos-快速啟動-android-emulator"
canonicalURL = "https://medium.com/@danielkao/%E5%9C%A8-macos-%E5%BF%AB%E9%80%9F%E5%95%9F%E5%8B%95-android-emulator-674585499447"
mediumID = "674585499447"
[cover]
  image = "/images/674585499447/1_25a44wP9U8WL0mSJB7MRWA.png"
+++


目前在 M1 chip 的 Mac 設備上，可以很方便的安裝 iOS App，執行上也都沒有什麼問題，除了有些 App 因為還沒有針對 MacOS 做處理，所以畫面大小不能很彈性地調整。如果是 Android App 的話，就沒那麼好命了；要在 Mac 設備上執行的話，還是得透過 Emulator 來執行。

目前比較流行的是 Blustacks 和 Genymotion，還有開發者最常用的 Android Emulator (常常會讓風扇高飛)。前兩者我在 MacOS Moneterey 上安裝都有些問題，所以還是只能退而求其次，利用 Android Emulator 來執行 Android Apps。

之所以要在 MacOS 上執行 Android App 的原因是：自己寫的 EinkBro App 可以雙開全文翻譯，用來看外文網頁相當方便。在 MacOS 上要做到一樣的功能的話，得要自己手動開兩個 Chrome Window，同時連到同樣的網址，然後將其中一個 Chrome 全文翻譯成其他語言。偶爾如此操作還可以；但如果每天都有一堆文章想要這麼觀看的話，就會覺得很花時間。這時，如果能夠在 MacOS 上直接開啟 EinkBro App 來看網頁的話，就可以很方便地以我習慣的方式瀏覽網頁。

### 利用命令列啟動 Android Emulator

Android Emulator 有支援命令列的呼叫方式, 詳細參數資訊，可以參考官網的說明：

<https://developer.android.com/studio/command-line/avdmanager>

可以先用下面指令找出目前系統有建立的 Android Emulators:

```
avdmanager list avd
```

以我的情況，系統會列出下面資訊：

```
Available Android Virtual Devices:  
    Name: Nexus_10_API_30  
  Device: Nexus 10 (Google)  
    Path: /Users/danielkao/.android/avd/Nexus_10_API_30.avd  
  Target: Google APIs (Google Inc.)  
          Based on: Android API 30 Tag/ABI: google_apis/x86_64  
    Skin: 2560x1600  
  Sdcard: 512 MB  
---------  
    Name: Pixel_XL_API_21  
  Device: pixel_xl (Google)  
    Path: /Users/danielkao/.android/avd/Pixel_XL_API_21.avd  
  Target:  
          Based on: Android 5.0 (Lollipop) Tag/ABI: default/x86_64  
    Skin: pixel_xl_silver  
  Sdcard: 512M
```

```
The following Android Virtual Devices could not be loaded:  
    Name: Pixel_3_XL_API_30  
    Path: /Users/danielkao/.android/avd/Pixel_3_XL_API_30.avd  
   Error: Google pixel_3_xl no longer exists as a device  
---------  
    Name: Pixel_3a_OS_8_27  
    Path: /Users/danielkao/.android/avd/Pixel_3a_OS_8_27.avd  
   Error: Google pixel_3a no longer exists as a device
```

因為我想要大畫面的 Emulator來顯示網頁，所以我要啟動的是 `Nexus_10_API_30` 。我可以利用下面的指令來啟動它：

```
emulator -avd Nexus_10_API_30
```

了解怎麼用指令來啟動 Emulator 後，算是完成了第一個步驟。但我真正想做的是，可以在 MacOS 的 Dock 上有個 icon 讓我點一下就啟動，而不是總是要開啟 Terminal 來執行指令，所以，下面會講怎麼讓指令能包裝一下，搬到 Dock 中。

### 建立 Dock 上的 指令 Icon

在 Dock 上新增 Icon

這件事比較容易達成。可以先建立一個文字檔，將其副檔名改為 `.app` 就可以成功將它拖拉到 Dock 上。以我的情況來說，我將檔名取為 `emulator_tablet.app` ，然後在裡面輸入以下內容：

```
#!/bin/zsh
```

```
~/Library/Android/sdk/tools/emulator -avd Nexus_10_API_30
```

其實到這邊，就已經達到我要的目的了，但是還有一點不完美的地方是：Dock 上預設的 App Icon 有點醜，看不出來是要做什麼用的。

![](/images/674585499447/1_25a44wP9U8WL0mSJB7MRWA.png)
*default Dock icon: not recognizable*

#### 更改指令 App 的圖案

為了讓 Dock 上的圖案更有辨識性，我們可以為文字檔加上圖案。首先，利用 `command + i` 叫出檔案訊息，然後可以在訊息框的最上方看到目前的圖案。我們要做的就是把下載好的圖案，拉到預設的圖案上，讓系統採用新的圖案。

![](/images/674585499447/1_kNGxD1ju0lK2Op_Hy5QtGQ.png)

從上圖可以看到，右邊就是系統預設的圖案；而右邊的 emulator\_tablet.app 的圖案則是我已經置換過的樣子。

自己要畫出這些圖案不是件難事，好在網路上已經有人幫忙收集了很多 icon 供使用者下載使用。我是到下面這個網站找到合適的 icon：

[Over 5000+ free icons for macOS Monterey, Big Sur & iOS - massive app icon pack](https://macosicons.com/)

換完圖案後，這時再把檔案從 Finder 中拖拉到 Dock 上時，就會是新的圖案。

![](/images/674585499447/1_csENn9oFRHTRre0O0Ylrag.png)

### 調整 Android Emulator 外觀

由於我建立的是 Nexus 10 的 Emulator，預設在畫面下方會有系統的 navigation bar；但其實在畫面右端也有了相關的動作按鈕 (Back, Home, Recent Apps)，所以我想要移除畫面下方的 navigation bar，讓整個模擬器看起來更像是 MacOS 上的 App。

作法可以參考下面這篇 StackOverflow 的介紹：

[How to remove button bar at the bottom screen](https://stackoverflow.com/a/40569962/1265915)

進到 `~/.android/avd/your_device_name.avd/config.ini` ，然後把下面兩個值改成 yes 就可以了。

```
hw.mainKeys=yes  
hw.keyboard=yes
```

### 大功告成！

經過上述的調整後，在 Mac 上就能像是操作一般 App 的方式來啟動 Android Emulator 囉。省下了我重新開發 MacOS App 的時間。

![](/images/674585499447/1_Lc4AyxsvpI5rIFs-T9slAA.png)
