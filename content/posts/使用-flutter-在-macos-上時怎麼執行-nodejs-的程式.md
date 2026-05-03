+++
title = "使用 Flutter 在 MacOS 上時，怎麼執行 Node.js 的程式"
date = "2023-11-26T05:39:24.031Z"
description = "之前為了讓文石的 Mira 螢幕可以有比較方便的模式/參數調整方式，修改了 Open Source 的 Node.js App，讓它可以支援更多的參數。但是，該程式是 cli 型式，需要開啟 Terminal 並輸入指令才可以執行。雖然我有利用 Automator 做了幾個…"
slug = "使用-flutter-在-macos-上時怎麼執行-nodejs-的程式"
canonicalURL = "https://medium.com/@danielkao/%E4%BD%BF%E7%94%A8-flutter-%E5%9C%A8-macos-%E4%B8%8A%E6%99%82-%E6%80%8E%E9%BA%BC%E5%9F%B7%E8%A1%8C-node-js-%E7%9A%84%E7%A8%8B%E5%BC%8F-7a35cdf2b521"
mediumID = "7a35cdf2b521"
+++

![](/images/7a35cdf2b521/1_MmAoOHIWq8Y2UMbUeJL6fQ.png)

之前為了讓文石的 Mira 螢幕可以有比較方便的模式/參數調整方式，修改了 Open Source 的 Node.js App，讓它可以支援更多的參數。但是，該程式是 cli 型式，需要開啟 Terminal 並輸入指令才可以執行。雖然我有利用 Automator 做了幾個 script，並綁定系統快速鍵來操作；但還是覺得，如果能有個 UI 介面，滑鼠點一點就好的話，應該會是更理想的。

所以，用 Flutter + menubar plugin 快速刻了一個小 MacOS App，能夠常駐在 menubar 上，提供幾個我常用的選項(模式切換，重新啟動 antishake，關前光燈，畫面重繪等)。

不過，在使用上卻遇到了一個問題：如果是在 Android Studio 中編譯並順便執行的話，它可以正常運作；如果是從 commandline 執行的話，程式也可以正常運作。但偏偏最常的啟動方式 (從應用程式中，或是從 Finder 中雙擊程式執行) 是無效的。

由於在實作裡，是透過 `dart:io` 的 `Process.start` 呼叫已經編譯好的 Node.js App — mira ，所以我懷疑應該是這裡出了問題。要嘛就是沒有正確讀到所需要環境變數；不然就是 Flutter 要呼叫 Node.js 的 cli 時，需要再多動點手腳才行。

經過一番研究後發現，沒想到 mira 這 Node.js 程式，竟然是個 soft link，連結到一個 cli.js 檔案。也就是說 mira 其實底子裡是個 javascript 檔案。當 Flutter 透過 Process.start 想要去執行它時，應該是遇到了不知道怎麼處理 javascript file，所以無法正常執行。

為了解決這件事，我去找了一下要怎麼在 Terminal 中執行 Node.js 程式的說明。下面是個簡單的範例，可以透過 node some\_javascript.js 來執行。

```
echo "console.log(1+1);" >> test-node.js  
node test-node.js
```

當然，這樣子的呼叫方式是假設 node 已經在 PATH 環境變數中。如果想要降低這件事的不確定性，可以將 node 換成絕對路徑就行。在 Mac 上如果是用 brew 安裝 Node.js 的話，它的路徑應該會是

/opt/homebrew/bin/node

有了這些資訊後，我把呼叫 mira app 的函式再包了一層，變成以下的實作方式：

```
Future<void> _commandMiraJs(List<String> action) async => await Process.start(  
  '/opt/homebrew/bin/node',  
  [MIRA_JS_PATH, ...action],  
);  
  
const String MIRA_JS_PATH = '/opt/homebrew/bin/mira';
```

每個指令都會利用絕對路徑的 node 來執行；除了第一個參數是 mira app 外，後面的列表就會是各個所需要相關參數。以切換到閱讀模式這件事來當例子，它的函式就會是這麼實作：

```
Future<void> _commandRead() async => await _commandMiraJs(  
      'settings --dither-mode 3 --contrast 7 --black-filter 10 --white-filter 12 --refresh-mode direct'  
          .split(' '));
```

解決了呼叫 mira 的方式後，以後就可以開心地使用這個由 Flutter 寫成的 UI 界面了！哪天如果還有什麼常用的設定組合，只要再多個 menu item，然後加上對應的參數，重新編譯一下就行了！

### Flutter Mira App UI

![](/images/7a35cdf2b521/1_33HPuZs6DNfDh1K0pQuvgQ.png)

目前 Settings 是空的。哪天有空，會把一些可以調整的參數做成 progress bar，讓使用者(我自己)能夠臨時調整一些參數 (像是前光燈的色溫和亮度，對比度的高低，畫面更新快慢的程度等)。

### 相關連結

- [mira-js 的開發](https://medium.com/ereadertips/文石-mira-電子紙螢幕的-commandline-調整小工具-ffcccbc2afce)
- [How to Run a Node.js Application on a Mac](https://www.webucator.com/article/how-to-run-a-nodejs-application-on-a-mac/)
