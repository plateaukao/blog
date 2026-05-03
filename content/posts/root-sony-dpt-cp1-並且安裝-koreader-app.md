+++
title = "root SONY DPT-CP1 並且安裝 KOReader App"
date = "2024-06-09T14:02:28.812Z"
description = "這篇要來說說怎麼在10 吋的 SONY DPT-CP1 電子書閱讀器上 root 並安裝 KOReader 的方式。"
slug = "root-sony-dpt-cp1-並且安裝-koreader-app"
canonicalURL = "https://medium.com/@danielkao/root-sony-dpt-cp1-%E4%B8%A6%E4%B8%94%E5%AE%89%E8%A3%9D-koreader-app-49a0755df67e"
mediumID = "49a0755df67e"
+++

![](/images/49a0755df67e/1_2AIHUr3Cu5T-reEKVFElRg.png)

上週在網上逛 Amazon 時，看到國際運費免費，失心瘋地買了二手的閱讀器 SONY DPT-CP1，一台 2018 年推出的超輕 10 吋閱讀器。這篇要來說說怎麼在 SONY DPT-CP1 上安裝 KOReader 的方式。

### 前言

目前我在買閱讀器時，在意的因素有兩點: 要嘛就是 CPU 性能要很強，因為要拿來上網，流暢度很重要；另外一點是要輕要好拿，能有多輕就多輕，因為看書時習慣拿在手上看，所以如果螢幕能很大，又能兼顧到重量的話，是最好的選擇。

以第一點 “CPU 性能” 要強來看，目前文石去年到今年推出的閱讀器都有很好的性能，很適合拿來上網用。所以目前瀏覽網頁的話，我使用的主力是 BOOX Tab Ultra C。

以第二點 “愈輕愈好” 來選擇的話，這一兩年陸續買了掌閱 Ocean2 (7"), Ocean3 Plus (8") 和 Ocean 3 Turo (7") 以及 Amazon 的 Kindle Oasis 3 (7")；重量都是在 170 克到 200 克左右，而且都有將閱讀器重量偏重一邊的設計，在手持上更加舒適。

但，總覺得還是少了一台 10 吋的輕型設備。目前市面上的10吋新機種，大都是在400~450克之間。好一點的，標榜很輕的，也是要 370~ 380 克。跟 8 吋只要 200 克的 Ocean3 plus 比的話，還是差了一大截，甚至要它兩倍的重量。

找著找著，就只好往舊的機種找去。剛好看到網路上有人寫到，其實 SONY 2018年出的 DPT-CP1 (10") 也是能 root，然後安裝 KOReader App 的。看到 KOReader app 我眼睛就亮了。只要能安裝 KOReader app，就表示能夠自己動手調整的可能性變得無限大；而且，10吋大的 DPT-CP1 只有 240 克！這才是真正的輕啊~

看了看，它似乎沒有再出新款的，但舊款的也沒有因此而降價多少。剛好最近美亞和日亞都有在促銷國際運費免費，所以在日亞上逛一逛，看到有二手的 DPT-CP1 只要半價。雖然知道應該已經被使用很長一段時間了，但，可以買來試試裝上 KOReader app，即使有些小缺點，也是可以忍受的。

於是，我入手了照片中左邊的 SONY DPT-CP1 (右邊是拿來對比用的文石 6 吋白色 Poke4s)。照著網路的教學 (大概 10 分鐘？)就 root 成功了，也裝上了 2024.04 版的 KOReader app。不得不說，KOReader 真的很神，連 6 年前推出的機種，Android OS 還在 5.1 ，都可以順利安裝。更重要的是！我修改的轉直排 patch 也可以套用上去。

### root 方式

root 的方式我主要是依照下面這篇文章操作的。在這邊先假設使用的環境是 MacOS，在電腦上也已經裝好了 python3 。

[Sony DPT-RP1 电子纸破解](https://yiruru.com/6%E4%BB%A3%E7%A0%81%E5%A6%82%E8%AF%97/Sony%20DPT-RP1%20%E7%94%B5%E5%AD%90%E7%BA%B8%E7%A0%B4%E8%A7%A3/)

1. 安裝 python 需要的一些套件

```
pip install httpsig pyserial urllib3 requests
```

2. 把下面 github repo clone 一份下來

<https://github.com/HappyZ/dpt-tools>

3. 開啟 DPT-CP1 的 wifi 連線，找到其 wifi IP，並且在終端機裡進到 dpt-tools 的目錄下，執行下面指令

```
python dpt-tools.py -ip your_device_wifi_ip
```

執行後，如果在 Terminal 中看到 DPT Tools 的字串，就表示完成了第一步。

4. 在 Terminal 中輸入 fw，按 Enter，然後填入以下的路徑：

```
fw_updater_packer_by_shankerzhiwu/pkg_example/hack_basics/fw.pkg
```

畫面出現提示 yes/no 時，打入 yes，再按 Enter

這時系統會重開機，並跑一些安裝程式，等它完成。如果畫面上有 update failure 或 uneable to update，都不要理它。(因為實際上已經裝了)

5. 依步驟 4，再安裝下面兩個路徑：

```
fw_updater_packer_unpacker/pkg_example/flashable_mod_boot_img_1.6.50.14130/FwUpdater.pkg
```

```
fw_updater_packer_unpacker/pkg_example/flashable_supersu/FwUpdater.pkg
```

6. 試試 adb devices，看看有沒有抓到 DPT-CP1。有的話，可以到下面的 github 抓一個小小的 App Launcher 來使用。

[Releases · Modificator/E-Ink-Launcher](https://github.com/Modificator/E-Ink-Launcher/releases)

下載後執行

```
adb install the_apk_you_downloaded.apk
```

7. 安裝好之後，為了讓它會出現在設備上方的選單中，要再進行下面的操作。第一行的 launcher\_mod.tar.gz 可以在 dpt-tools 中找到。都執行好之後，重開機，點擊設備上方的按鈕後，可以看到多了一個 Apps。

```
adb push /path_to/launcher_mod.tar.gz /sdcard/launcher_mod.tar.gz  
adb shell mount -o rw,remount /system  
adb shell rm -rf /etc/dp_extensions
```

#### 其他

上述流程算是完成了整個 root 的過程，而且還順便裝了個 App Launcher。以下則是一些可能會需要調整的設定；可以根據自己的需求，決定要不要做。

- 打開系統預設的設定 App

```
adb shell am start -a android.settings.SETTINGS
```

- 切換系統語系 (只有中英日三種語言)

```
adb shell am start -a android.settings.LOCALE_SETTINGS
```

- 切換輸入法

```
adb shell am start -a android.settings.INPUT_METHOD_SETTINGS
```

### 安裝 KOReader App

在 root 完之後，安裝 app 的方式其實就跟一般的 Android 設備差不多，能夠利用 adb install 的指令將 app sideload 進 DPT-CP1 中。

KOReader App 可以到 <https://github.com/koreader/koreader/releases> 下載比較新的版本。然後執行下面的指令：

```
adb install name_of_koreader_app.apk
```

#### 細步調整

在 root 後的 DPT-CP1 上，所有安裝的 app 的字體都會變得很小。在 KOReader 中能夠對此做一些設定：

> 設定 > 螢幕 > 螢幕 DPI > 自訂 : 200

因為 DPT-CP1 是黑白的，所以可以把用彩色繪製畫面的選項關掉

> 設定 > 螢幕 > 彩色顯示: 關閉它

如果在使用時，畫面會自動關掉的話，可以開啟。或是有時畫面重繪有問題的話，也可以把它打開來。

> 設定 > 螢幕 > 螢幕逾時 > 保持螢幕開啟

### 相關連結

除了上面參考的那篇中文文章外，最齊全的 Rooting 教學都在下面這個連結：

[The Ultimate Rooting Guide](https://github.com/HappyZ/dpt-tools/wiki/The-Ultimate-Rooting-Guide)

裡面有教到怎麼利用重新打包 framework-res.apk，來更換待機畫面。但我一直試不成功。因為這過程可能會不小心讓你的設備變磚，所以建議不要嘗試。
