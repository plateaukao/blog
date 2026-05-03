+++
title = "關於 Android adb 二三事"
date = "2018-06-10T14:28:19.574Z"
description = "開發 Android app 時，一直是用 command line 模式在操作 adb。沒有什麼不好，但很多參數太久沒用，每次要再使用時都要得看一次說明，久了，會覺得有點煩。"
slug = "關於-android-adb-二三事"
canonicalURL = "https://medium.com/@danielkao/%E9%97%9C%E6%96%BC-android-adb-%E4%BA%8C%E4%B8%89%E4%BA%8B-1f8627318d6f"
mediumID = "1f8627318d6f"
+++

![](/images/1f8627318d6f/1_Ley7dmpL7fUGk4RCNRnDWg.jpeg)
*花蓮七星潭*

開發 Android app 時，一直是用 command line 模式在操作 adb。沒有什麼不好，但很多參數太久沒用，每次要再使用時都要得看一次說明，久了，會覺得有點煩。

最近在 medium 上看到有人用 Java 開發了一套方便使用 adb 功能的圖形介面程式，而且是 Open Source 的，連結如下：

[yapplications/ADB-GUI](https://github.com/yapplications/ADB-GUI)

安裝方式可以從 Github 上下載 zip 解開透過 java -jar ADB-GUI-Tool.jar 來執行，或是下載程式碼後，透過 Intellij IDEA 自行編譯。

為了事後可以自己加新功能，我選擇了後者。編譯完啟動的畫面如下；畫面很工程師風格，沒有什麼多餘的美化。雖然有些操作上不是那麼直覺，但習慣之後，倒也沒有什麼大礙。

![](/images/1f8627318d6f/1_HEr75ef1yMHmarQR3a02fQ.png)

主要功能有下面幾項：

1. 執行批次指令，像是自動登入 app 的帳號，或一次安裝多個 apk 和 copy 檔案。
2. 截取畫面。(不過這功能現在在 Android Studio 中也很方便)
3. 透過 Intent / Broadcasts 測試 deep linking。
4. 從手機上擷取 apk。
5. 查看和匯出 adb logs。
6. 一鍵跑 Monkey。

雖然功能很多，但對我來說比較實用的應該是批次執行和下 Intent / Broadcasts 吧。稍微試了一下批次執行，想要啟動之前開發的書法加 app 起來，並查詢特定字串。

結果一試便遇到了兩個問題：

1. 進入 app 後，要輸入字串前，必須先將 focus 設在 EditText，但透過單純的 adb 指令無法達到這件事。

![](/images/1f8627318d6f/1_nEATcqHauMFatYAIopOTgw.png)
*書法加 app 畫面*

退而求其次，我在 ADB-GUI 中，新增了 adb shell touch 的動作。原先的 Commands Wizard 只有 Input text, Power, Back, Tab, Enter, Volume up, Volume down, Home, Recent 等動作。我照著 Input text 的作法，加了 touch position ( [commit 在這兒](https://github.com/plateaukao/ADB-GUI/commit/0184c661247e3d236fc6513d0ed98dc87b28d312))，然後多試著輸入幾次，就可以正確找到 EditText 的位置，把 focus 設到它身上。

![](/images/1f8627318d6f/1_j2aVdSJNRUAqhZFVMYLt_w.png)
*新增指令*

2. 另一個問題是，adb 功能儘管很強大，但並不支援輸入中文字。書法加是一個用來查詢中文字的書法 app，輸入英文的話什麼也找不到。

為了解決無法透過 adb shell input text 指令輸入中文的問題，在網路上找到了 ADBKeyboard。完成下一段落的步驟後，終於可以自動執行下面的批次指令。

![](/images/1f8627318d6f/1_gmAAfWzyXVzB9S8OlGBhAQ.png)
*在書法加 app 中搜尋「書法」的字帖*

這類簡單的操作，透過批次指令來進行，可以省去很多手動的不確定性和緩慢性，也不用特地寫程式。但如果要更進一步的和 app 互動，可能還是利用 espresso 或是 uiautomator 會更恰當。

![](/images/1f8627318d6f/1_d_ogTkER3yi1CYqAr6PHWA.gif)

---

### Github 上的 ADBKeyBoard專案

[senzhk/ADBKeyBoard](https://github.com/senzhk/ADBKeyBoard)

解決無法透過 adb shell input text 輸入中文的問題：

1. 下載現成的 apk 或是取得原始碼自行編譯。

2. 安裝 apk，並進入 Settings -> Languages & Input 的管理輸入法畫面，勾選 ADB Keyboard，或是執行下面指令：

```
adb shell ime enable com.android.adbkeyboard/.AdbIME
```

3. 取得現在的輸入法，並記錄下來，

```
adb shell settings get secure default_input_method  
--> net.toload.main.hd/.LIMEService
```

4. 切換成 ADBKeyboard，

```
adb shell ime set com.android.adbkeyboard/.AdbIME
```

5. 輸入中文

```
adb shell am broadcast -a ADB_INPUT_TEXT --es msg '可以輸入中文了'
```

6. 切回原本的輸入法

```
adb shell ime set net.toload.main.hd/.LIMEService
```

原始碼很小，只有一個檔案，裡頭實作了 BroadcastReceiver。原本編譯出來是 11 k，後來我把它改成 kotlin，結果 apk 變成了400多 k。好像有點多此一舉。
