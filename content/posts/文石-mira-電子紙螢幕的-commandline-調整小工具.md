+++
title = "文石 Mira 電子紙螢幕的 commandline 調整小工具"
date = "2023-01-24T06:06:08.492Z"
description = "文石針對 Mira 和 Mira Pro 雖然有推出官方的工具軟體，但是一年更新不到一次，而且介面又是用 Javascript 和 html 寫的，寫得不是很好用。這篇文章要來介紹一個使用者自己反組譯 Linux 上的官方工具後，開發出來的 command line 程式…"
slug = "文石-mira-電子紙螢幕的-commandline-調整小工具"
canonicalURL = "https://medium.com/@danielkao/%E6%96%87%E7%9F%B3-mira-%E9%9B%BB%E5%AD%90%E7%B4%99%E8%9E%A2%E5%B9%95%E7%9A%84-commandline-%E8%AA%BF%E6%95%B4%E5%B0%8F%E5%B7%A5%E5%85%B7-ffcccbc2afce"
mediumID = "ffcccbc2afce"
+++

### 文石 Mira 電子紙螢幕的調整小工具

文石針對 Mira 和 Mira Pro 雖然有推出官方的工具軟體，但是一年更新不到一次，而且介面又是用 Javascript 和 html 寫的，寫得不是很好用。這篇文章要來介紹一個使用者自己反組譯 Linux 上的官方工具後，開發出來的 command line 程式 `mira-js` 。以及我後來對它做的一點小修改。

```
# 大綱  
* 介紹 Mira-js 和使用方式  
* 少了什麼  
* 了解目前 mira-js 的實作  
* 如何修改它  
* 怎麼使用修改後的版本
```

### 介紹 Mira-js 和使用方式

Mira-js 是個用來調整 Boox Mira 和 Boox Mira Pro 電子紙螢幕參數和模式的小工具，可在 Linux, MacOS, 和 Windows 上執行。與官方版本不同的是，它是透過指令執行的，不需要用滑鼠點來點去。

[GitHub - ipodnerd3019/mira-js: Utility for Boox Mira](https://github.com/ipodnerd3019/mira-js)

安裝方式很容易，一行指令搞定 (要事先有裝 nodejs 就是了)。

```
npm install -g boox-mira
```

想要執行時，就根據需求，下不同的參數：

```
npx mira refresh  
npx mira settings --speed 3 --contrast 11
```

### 少了什麼

對於 Windows 或 Linux 用戶可能這樣子就很好用了，但如果是 Apple 新 CPU 設備的用戶(M1 或 M2 系列)，很可能就會跟我一樣遇到一接上 Mira 螢幕，畫面會閃個不停。在 reddit 上也三不五時有使用者在反應：

後來文石新版的官方小工具提供了一個新的選項，可以調整 anti-shaking 的程度。如果把它調到 high 的話，就能很有效地抑制 M1 CPU 系列的畫面閃爍問題。

![](/images/ffcccbc2afce/1_zwTCXXYAh1JkNCp4R3X5ew.png)

但是，這功能並沒有實作在 Mira-js 中。少了這個功能的話，我還是得要使用官方工具在每次接上螢幕時，重新做一次設定。每天往返在公司電腦和個人電腦間使用 Mira，操作到人都覺得煩了。

所以，我想要來試試看能不能將這個功能也加入到 Mira-js 中。

### 了解目前 Mira-js 的實作

首先，研究了一下 Mira-js 程式碼，它是用 javascript 寫成的，最終會變成 npm 的一個模組。所以，其他人在安裝時很方便，只要下一行指令就可以把作者發布到雲端的版本裝到 local。因為提供的功能不多，程式碼也不多，主要就兩個檔案：

`src/mira.js`: 真正在執行調整的實作，會從系統去拿到一個可能是類似 file descriptor 的 instance，對著它寫入各種不同的指令，達到調整的效果。

`bin/cli.js`: 處理下指令時輸入的參數，和做一些簡單的參數檢查和說明。

要新增 anti-shake 功能的話，分別需要在 cli.js 加上新的參數名稱和在 mira.js 中加入對應的實作。cli.js 的部分比較簡單，可以直接看最後的 pull request； mira.js 的話，先來看一下原先的指令是怎麼處理的。這邊截取部分的程式碼來說明： `OP_CODE` 是每個指令對應的代號，在寫入 file descriptor 時，要帶入想要的代號，後面再接上數值。

比方說想要設定畫面更新速度時，會用 `OP_CODE.set_speed` 這個代號，然後 `adjustedSpeed` 就是使用者輸入的數值。而單純想要讓畫面重新刷新的話，就只要代入 `OP_CODE.refresh` 就行。

```
const OP_CODE = {  
  refresh: 0x01,  
  set_refresh_mode: 0x02,  
  set_speed: 0x04,  
  set_contrast: 0x05,  
  set_cold_light: 0x06,  
  set_warm_light: 0x07,  
  set_dither_mode: 0x09,  
  set_color_filter: 0x11,  
};  
async refresh() {  
    await this.write([USB_REPORT_ID, OP_CODE.refresh]);  
  }  
  
async setSpeed(speed) {  
  let adjustedSpeed = clamp(speed, 1, 7);  
  adjustedSpeed = 11 - adjustedSpeed;  
  await this.write([USB_REPORT_ID, OP_CODE.set_speed, adjustedSpeed]);  
}
```

有了這基本認知後，再來就是要找出 anti-shake 的代號和它所需要的數值是多少。這就要開始到官方的程式中挖寶了。

#### **解開 electron APP，查看程式碼**

Mac 上的官方 Mira 工具程式是用 electron 包裝起來的 javascript 軟體 (其他平台應該也是)。要看裡頭程式碼的話，可以直接按快捷鍵 `option+command+i` 開啟 chrome debugger tool 來看。但是這樣子看 javascript 很痛苦，因為沒有縮排、換行，而且還充滿了混滛後的不知所云函式/變數名稱。

所以，首要步驟是先下載個好用的 IDE。原本想說用 VS Code 就好，但一想到還要熟悉它的操作，就覺得累。所以，利用之前申請到的 JetBrains license，直接下載 WebStorm 來用，整個介面就跟 Intellij IDEA 還有 Android Studio 幾乎一模一樣，完全無痛上手。

解開 electron APP 的方式很簡單，只要照著下面的說明，找到主要的程式碼壓縮檔，執行一行程式碼就行。

```
npx asar extract app.asar folder_for_unpacked
```

[GitHub - jonmest/How-To-Tamper-With-Any-Electron-Application: This work-in-progress outlines known…](https://github.com/jonmest/How-To-Tamper-With-Any-Electron-Application)

解開來後，再用 WebStorm 打開來搜索想要的資訊。

在茫茫程式碼中，找到了類似 mira-js 中的指令代號，其中的 autoDither: 18 應該就是我想要的 anti-shake 功能；程式碼裡稱之為 autoDither 。這裡先記著它的數值是 18。

```
        const Q = {  
                fullRefresh: 1,
```

有了指令代號後，再來要看官方工具中的 close , low, middle, high 要怎麼轉換成所需的數值。先沿著 `autoDither` 這條線索，找到它使用的方式：2875 行可以看到它會將 e 利用某個資料結構 te 轉為數值 t ，再呼叫 `setSettings` 功能。 `setSettings` 就是類似 mira-js 中的 `write` 函式。

![](/images/ffcccbc2afce/1_gARbyOms9bk8-JFLFHn_ng.png)

那麼，我們再來追一下 `te` 到底是什麼。果然沒錯，它就是個定義了 anti-shake 程度和數值之間的一個對照表。

![](/images/ffcccbc2afce/1_ahNBL2KofiSP_rHDT5MCOA.png)

收集到這些資訊之後，後續的事就簡單啦，只要拿著這些資訊，到 mira-js 中新增一個指令出來就行。

#### 修改 cli.js

先在 `cli.js` 中，加上新的參數。在這裡我只加了一個 `antishake` 的參數，沒有吃後續的數值。因為，應該不會有人會想要把 `antishake` 關掉才對，會來呼叫的人應該都是用了 Mac 系統，受畫面閃爍之苦才對。

![](/images/ffcccbc2afce/1_TwiFDKze_dCplcv6ILvimg.png)

#### 修改 mira.js

最後，在 `mira.js` 中補上將指令代號和數值餵給 USB HID 的實作。

![](/images/ffcccbc2afce/1_72Ijdn0j1CWDZridIb3Wdw.png)

`下面可以看到，我在 OP_CODE 中新增了 set_auto_dither_mode ，把值設為0x12 (還記得剛剛查到的值是十進位的 18 嗎？這裡得要用16進位才行)；另外，autoDitherMode` 的數值就仿照官方工具中的宣告建立一個 dictionary。

![](/images/ffcccbc2afce/1_s6d-GO47a5kQE0K1LKzg5g.png)

都完成後。就可以把它推到 local 端的 node module repository 中試試。

```
npm install -g .
```

再來，先在官方的小工具中將 anti-shake 設為 Close，關掉官方小工具(這點很重要，不然 mira-js 會無法執行！)，然後在 Terminal 中測試下面的指令：

```
npx mira antishake
```

如果一切順利，畫面不再閃個不停，就可以發 pull request 給原作者了！

### 怎麼使用 Mira-js 指令

指令，不就像最一開始介紹的那樣，在某個 Terminal 中輸入就好嗎？這麼說雖然沒錯，但每次想要調個參數都還要開個 Terminal 來執行指令，也是一樣麻煩啊。

最方便的方式應該還是要跟官方版本小工具一樣，能夠設定全域快捷鍵；隨時隨地想呼叫時，都能按按鍵盤就完成。

在 Mac 上，有很強大的 Automator 能幫忙達到這樣的小需求。只要先到 Automator 中新建一個 Quick Action，在其中加入 Run Shell Script，把 Mira-js 想要執行的指令輸入其中 (記得第一行要加上 `PATH=/opt/homebrew/bin/:$PATH` ，不然會找不到 `npx` )，為這個 Quick Action 取個好名字。

![](/images/ffcccbc2afce/1_25m4aUs15Zy7OAcABPSCRA.png)

然後，進到 System Preferences 的 keyboard 設定畫面，打開 Services，找到 General 的下拉選單，找到剛剛取好名字的 Quick Action，就能為它新增快捷鍵了。

![](/images/ffcccbc2afce/1_wxnWN2WOJfM6fr-j5IO9IA.png)

### 相關資料

[修改的程式碼](https://github.com/ipodnerd3019/mira-js/pull/8)
