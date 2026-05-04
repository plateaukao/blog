+++
title = "如何安裝 Google Apps 在海信 A5PRO / A5PRO CC / A7 上"
date = "2021-01-15T12:53:35.903Z"
description = "從去年起(2020年)，海信出了一系列純電子紙螢幕的手機，從一開始的 A5，到 A5PRO 系列，再到去年底的 A7，海信不斷地改善電子紙做為手機螢幕上的體驗。但礙於市場的關係，這幾款手機都沒有內建 GMS (Google Mobile Service)：沒有 Google…"
slug = "如何安裝-google-apps-在海信-a5pro-a5pro-cc-a7-上"
canonicalURL = "https://medium.com/@danielkao/%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%9D-google-apps-%E5%9C%A8%E6%B5%B7%E4%BF%A1-a5pro-a5pro-cc-a7-%E4%B8%8A-4b2c5d30562"
mediumID = "4b2c5d30562"
tags = ["電子書閱讀器"]
[cover]
  image = "/images/4b2c5d30562/1_AG27Z9a4iIfKqBVRRRx7kQ.png"
+++


從去年起(2020年)，海信出了一系列純電子紙螢幕的手機，從一開始的 A5，到 A5PRO 系列，再到去年底的 A7，海信不斷地改善電子紙做為手機螢幕上的體驗。但礙於市場的關係，這幾款手機都沒有內建 GMS (Google Mobile Service)：沒有 Google Play Store, Gmail, Youtube等等。其他有跟 Google Play Service 整合的 App 在這幾款手機上也會遇到無法登入的問題，讓很多人因此打了退堂鼓。

不過，只要用的人夠多，總是會有神人找出方式來達到想要的使用方式。A5在去年時，有人發表了怎麼透過 root 來裝上 GMS 的服務，其中要用到一些刷機的程式。一來，我不想 root 手機，因為通常 root 完，就表示跟之後官方的自動升級說 bye bye，享受不到升級帶來的新功能；二來那些刷機程式是 Windows 版的，我手邊只有 Mac，就算想裝也很麻煩；所以當時也只是看看而已。

但就在前幾天，我入手了海信 A7，開始又在網路亂逛相關資訊時，看到了一篇介紹如何為 A5Pro 系列和 A7 裝上 Google 服務的文章，經過十幾二十分的操作，在沒有 root 的情況下，我的 A7 就可以正常地使用 Youtube App，而且還登入了我購買了 Premium 的 Google Account。瞬間讓 A7 的價值大大提升，之後，又陸續裝了幾個之前 Google Play Store 上面買的 App，也都可以正常運作。

以下，就來介紹一下怎麼樣讓你的海信電子紙手機，在不 root 的情況下，就可以正常地使用 Google Apps 和其他整合 Google Play Services 的 Apps。

---

### 安裝步驟簡介

以下是簡短的步驟列表，後面會一項一項解釋。

前置步驟：確保你的手機已經開啟了**開發人員選項**。

1. 下載並安裝 adb 程式
2. 關閉一堆系統內建的 Apps 的功能(非必要的步驟，自行決定)
3. 下載 Aurora Store (之後 Apps 都要從這兒下載)
4. 先 **依照順序** 安裝 4 個 apk
5. 進到**設置 App** 下的 **其他帳戶**，登入 Google 帳號
6. 再 **依照順序** 安裝 3 個 apk
7. 從 Aurora Store 安裝 2accounts App
8. 從 Aurora Store 下載想要的 App，再透過 2accounts App 來使用它

---

### 前置步驟

請利用 Google 搜尋 android 開啟開發人員選項 ，然後找自己看得懂的文章操作。下面附上三星手機的作法。在 A7, A5proCC, A5 上也是類似。

[設定 : 如何開啟 / 關閉「開發人員選項」？ | Samsung 台灣](https://www.samsung.com/tw/support/mobile-devices/how-to-open-close-developer-options/)

### 步驟 1 下載並安裝 adb 程式

Windows 平台的話，可以考慮原作者寫的另一篇教學

[Install and use ADB on HISENSE A5PRO / A5PRO CC](https://www.booksebook.it/?p=255&lang=en)

如果是 Mac 平台的話，可以透過 `Hombrew` 來安裝

```
brew install android-platform-tools
```

然後試一下有沒有作用

```
adb devices
```

---

### **步驟 2 停掉一堆系統內建的 Apps (Optional)**

其實這邊我覺得不見得要執行。建議可以把步驟 2 移到最後一步再做，或是如果看得懂下面是在停哪些 App 的話，只執行自己想停的就好。

比方說 `com.hmct.music` 是系統內建的播音樂軟體，停掉的話，就得自己再裝一個。所以看不懂的人，建議先不要進行這一個步驟。

```
adb shell pm disable-user --user 0 com.android.hplayer  
adb shell pm disable-user --user 0 com.android.browser  
adb shell pm disable-user --user 0 com.android.calendar  
adb shell pm disable-user --user 0 com.android.firewall  
adb shell pm disable-user --user 0 com.android.sos  
adb shell pm disable-user --user 0 com.hmct.account  
adb shell pm disable-user --user 0 com.hmct.antivirus  
adb shell pm disable-user --user 0 com.hmct.assist  
adb shell pm disable-user --user 0 com.hmct.imageedit  
adb shell pm disable-user --user 0 com.hmct.mobileclear  
adb shell pm disable-user --user 0 com.hmct.questionnaire  
adb shell pm disable-user --user 0 com.hmct.theme  
adb shell pm disable-user --user 0 com.hmct.voiceassist  
adb shell pm disable-user --user 0 com.hmct.voicetranslate  
adb shell pm disable-user --user 0 com.hmct.music  
adb shell pm disable-user --user 0 com.hmct.hmctmanual  
adb shell pm disable-user --user 0 com.hmct.userexperienceprogram  
adb shell pm disable-user --user 0 com.tencent.soter.soterserver  
adb shell pm disable-user --user 0 org.hapjs.mockup  
adb shell pm disable-user --user 0 com.hmct.jdreader  
adb shell pm disable-user --user 0 com.tencent.android.location  
adb shell pm disable-user --user 0 com.hmct.hiphone.juplugin  
adb shell pm disable-user --user 0 com.hmct.ftmode  
adb shell pm disable-user --user 0 com.hmct.semantic.analysis
```

---

### 步驟 3 下載 Aurora Store

用你的海信手機，到下面的網頁下載 Aurora store 的 app，然後安裝它。

[AuroraOSS](https://auroraoss.com/)

---

### 步驟 4 依序安裝 4 個 apk

到下面的網址下載 Huawei.zip

[Huawei](https://www.mediafire.com/file/ej6acz9xyq636sm/Huawei.zip/file)

上面這連結不知道何時會失效，失效了就無解了。所以想要操作的人，趕快先下載一份下來。

下載後，解開 zip 檔案可以看到 7 個 apk 檔案。請開個 Terminal 進到這個目錄下執行以下指令，把前 4 個 apk 裝上。

```
adb install 001-Google\ Play\ services-com.google.android.gms-19275048-v19.2.75\ \(120408-269183835\).apk
```

```
adb install 002-Google_Account_Manager.apk
```

```
adb install 003-Google\ Play\ Store.apk
```

```
adb install 004-com.google.android.syncadapters.contacts_10-29_minAPI29\(nodpi\)_apkmirror.com.apk
```

---

### 步驟 5 在”設置 App”中的“其他帳戶”中登入 Google Account

進到手機中內建的**設置 App**，可以看到 **其他帳戶** 中多了 Google 的項目可以新增帳號，請在這邊加入你的 Google 帳號。

---

### 步驟 6 安裝剩下的另外 3 個 apk

用下面的指令安裝剩下的三個檔案

```
adb install 005-Google\ Services\ Framework-com.google.android.gsf-29-v10.apk  
adb install 006-modagain1gsm.apk  
adb install 007-com.google.android.gms2.apk
```

---

### 步驟 7 從 Aurora Store 安裝 2Accounts App

這步很直覺，沒有什麼需要額外說明的

---

### 步驟 8 按照下面方式安裝 App 來使用(以Youtube為例)

![](/images/4b2c5d30562/1_AG27Z9a4iIfKqBVRRRx7kQ.png)

1. 開啟 Aurora Store
2. 從 Aurora Store 中安裝 Youtube
3. 裝好後，去執行一次 Youtube App。這一步可有可無，聽說會讓之後第7步比較順一些
4. 開啟 2Accounts App
5. 2Accounts 畫面右下角有顆 + 號的圓型按鈕，請點下去，並找到 Youtube，按它右邊的 + 號。
6. 完成 5 之後，2Accounts 會複製一份 App 資料；然後你在 2Accounts 畫面上會看到多了 Youtube。長按那個 Youtube，會跳出個選單，點第一個項目，建立桌面捷徑。
7. 回到桌面，點你剛剛建立好的 Youtube捷徑，就可以在 Youtube 中登入你的 Google 帳號囉。

---

#### 注意事項

當一切都可以正常運作後，平常需要什麼軟體，就可以透過 Aurora Store 下載或更新。但是，**千萬要注意！千萬不要升級 Google Play Services 和 System WebView。這兩樣如果不小心升級了，可能會造成需要 GMS 的 App 產生異常。**

---

#### **參考資料**

[【海信A7】海信（Hisense）A7 阅读手机A7 6.7英寸水墨屏 电纸书阅读器 6GB+128GB 全网通5G手机 曜石黑【行情 报价 价格 评测】-京东](https://item.jd.com/100009643325.html)

[Install the GAPPS on HISENSE A7 / A7CC / A5PRO / A5PRO CC (updated on 15/01/2021)](https://www.booksebook.it/?p=223&lang=en)

歡迎大家轉些贊助金鼓勵**上面這篇文章的作者**

[Pay davide patanè using PayPal.Me](https://www.paypal.com/paypalme/davidePax)
