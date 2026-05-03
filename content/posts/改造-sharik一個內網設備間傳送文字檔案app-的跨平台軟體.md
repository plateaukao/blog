+++
title = "改造 Sharik：一個內網設備間傳送文字、檔案、APP 的跨平台軟體"
date = "2022-05-08T09:44:18.037Z"
description = "在電子書閱讀器上用瀏覽器時，有些時候會覺得當下的內容用手機或電腦看會比較恰當，想要快速地切換過去。或是不同的設備間也常常會有想要把檔案傳到另一台上做處理或閱讀。以前可以使用 LINE Lite 來稍微達到這需求，但隨著 LINE Lite 停止服務後，一直找不到一個合用的工具。"
slug = "改造-sharik一個內網設備間傳送文字檔案app-的跨平台軟體"
canonicalURL = "https://medium.com/@danielkao/%E6%94%B9%E9%80%A0-sharik-%E4%B8%80%E5%80%8B%E5%85%A7%E7%B6%B2%E8%A8%AD%E5%82%99%E9%96%93%E5%82%B3%E9%80%81%E6%96%87%E5%AD%97-%E6%AA%94%E6%A1%88-app-%E7%9A%84%E8%B7%A8%E5%B9%B3%E5%8F%B0%E8%BB%9F%E9%AB%94-41b6fb990c12"
mediumID = "41b6fb990c12"
+++

在電子書閱讀器上用瀏覽器時，有些時候會覺得當下的內容用手機或電腦看會比較恰當，想要快速地切換過去。或是不同的設備間也常常會有想要把檔案傳到另一台上做處理或閱讀。以前可以使用 **LINE Lite** 來稍微達到這需求，但隨著 **LINE Lite** 停止服務後，一直找不到一個合用的工具。

### 需求

每個人的使用需求不大一樣，下面是我自己想要解決的問題：

1. 跨平台，希望能包含 Android 設備(有的設備無內建 Google Services)，MacOS, iOS 設備。
2. 能夠傳輸字串、檔案。
3. 步驟不要太複雜(不然我自己打網址就好了)。
4. 能不要跨到外網去就不要(當然最好也不要有任何 tracking 的記錄)。

### 研究

**LANDDrop:** 之前有在使用 LANDrop，它可以在同個網路下，不同設備間很方便的傳輸檔案，但並**不支援單純只傳字串。另外**，LANDrop 在 Mac 上的操作步驟多了點，不是那麼順手。

**Android Nearby Share**: 只有部分的 Android 設備支援。使用前必須要開啟 Wiki 和 Location Service。

PushBullet (TBD)

SendAnywhere (TB)

### Sharik 和修改內容

後來終於找一個還不錯的 open source 軟體 — [Sharik](https://github.com/marchellodev/sharik)，可以達到我的需求；而且因為是開源的，所以想要怎麼改或是加功能都可以。它原本就已經包含了大部分我需要的功能：在同個 wiki 網路下，兩台設備間傳送”字串”，”檔案”，或 APP，只是他的 UI 沒那麼直覺。所以我把它拿來改了改，並且在 MacOS 版本，加上了比較直覺的 drag and drop 的文件分享功能，並且拿掉了追縱使用者行為的相關程式碼。

#### 移除不必要的 UI 元件

Sharik 就只提供分享檔案，和接收別台設備分享出來的檔案，就功能來說很單純；但是原作者加了一堆(我覺得不必要的)畫面，像是 introduction 用的三個畫面，切換介面語言的 UI，是否要關閉 user tracking 的對話框，和大大的 About 畫面。

這些都是可以拿掉，讓整個畫面看起來更簡潔的。這部分沒有什麼細節可以分享，單純是把一堆 Screen 都移除。

commit 程式碼：

[remove redundant UI. shorten searching time · plateaukao/sharik@e779454](https://github.com/plateaukao/sharik/commit/e779454aa8ce5d01945449890ee965aabd194dcf)

#### 加入拖拉檔案，啟動分享的功能

在手機上，檔案拖拉沒有那麼實用，但是在 MacOS 上如果想要分享文件的話，從開好的 Finder 中拖拉檔案到某個區域的話，會是比較好的操作流程 (跟開啟一個莫名的 File Picker，再自己一層層地進到檔案所在的目錄比較)。

Sharik 不意外，是用 Flutter 開發的。為了讓 MacOS 支援拖拉的功能，先是加入了 [desktop\_flutter](https://pub.dev/packages/desktop_drop) 這個套件：

```
desktop_drop: ^0.3.3
```

再來是把現在的主畫面，用 `DropTarget` 包起來，處理當有物件放進來時的行為。下圖的 62 行可以看到當 `onDragDone` 行為被呼叫時，會去執行 `_handleDroppedFile` 函式。

![](/images/41b6fb990c12/1_C1zKZnGUs8zXreSTsEkkWg.png)

`_handleDroppedFile`的內容很單純，把收到的檔案訊息包裝成原本就已經實作好的 `SharingObject`，再去呼叫也是原先就實作的 `_shareFile()` 函式，就會進入分享的畫面。

![](/images/41b6fb990c12/1_R-YBnSMWR39ZvXeLSRuogg.png)

commit 程式碼：

[add file drag and drop feature for macos · plateaukao/sharik@cdb5bf9](https://github.com/plateaukao/sharik/commit/cdb5bf9465e1e72ca7017d9238372adf4a047ae4)

#### 加速分享來源的搜尋速度

原本的實作方式是先取得目前設備中的網路 ip，經過分析後，將 ip 的最後一個區段變換為 1 ~ 254 的數字，利用 for loop 去 ping 這些 ip (的某兩個 寫死的 port)；在一定的時間內有反應的話，就表示該 ip 有別台設備正在做分享。

這時，會進行下一個步驟：將該 ip 轉成網址，去抓取遠端設備上提供的 json 檔案。json 檔案中包含了遠端設備的 OS, name, 分享的種類(文字、檔案或 APP)和 ip 訊息。

因為要把 1 ~ 254 個 ip 都掃過一次，常常要好幾秒才會完成；所以我在這邊做了點改善：如果已經掃描過，而且完成過分享的 ip，我會把它記錄下來。下次要再接收別台設備的分享時，就會優先掃描這些已經傳送過的 ip。

以正常的使用情況來說，一個人頂多擁有五到十台設備，掃描十台設備，比起掃描 254 個 ip 還是快很多的。

**儲存已經傳送過的 ip**

Sharik 使用 [Hive](https://pub.dev/packages/hive) 套件儲存設定的資訊，所以我也利用同樣的機制來儲存 ip 清單。

我先把 `NetworkAddr` class 抽出來成為獨立的檔案，並加上要讓 Hive generator 能看得懂的 annotations。

![](/images/41b6fb990c12/1_Ol7MLDtzy5LnromJ-kKpGw.png)

然後利用下面的指令產生所需的 Adapter class

```
flutter packages pub run build_runner build --delete-conflicting-outputs
```

在 APP 啟始時，會去初始化 hive 相關的 storage:

```
const KEY_SENDER_IP_LIST = 'sender_ip_list';
```

```
Box<NetworkAddr>? senderIpList;  
...  
senderIpList = await Hive.openBox<NetworkAddr>(KEY_SENDER_IP_LIST);
```

在有成功傳送後，會將其寫入 hive storage

```
receiverService.addListener(() {  
      if (receiverService.receivers.isNotEmpty) {  
        final address = receiverService.receivers.first.addr;  
        if (senderIpList?.values.contains(address) != true) {  
          senderIpList?.add(address);  
        }  
      }  
    });  
}
```

下次，在掃描 254 個 ip 前，就可以針對 hive storage 中的 ip 先掃描一次，有找到的話就直接回傳，沒有的話才會再往下執行：

![](/images/41b6fb990c12/1_dw8-xfLlF3thTEb7X42h4A.png)

這麼一來，只要是之前有收過檔案的來源，下次再分享的話，就可以馬上收到，不用等上太久。

commit 程式碼：

[keep a list of transferred sender, for speeding up search · plateaukao/sharik@7ffe317](https://github.com/plateaukao/sharik/commit/7ffe31704d16d543477f24a291de35e97433f4b6)

#### 傳送網址的示範影片

---

### 相關連結

#### 下載位置

[Releases · plateaukao/sharik](https://github.com/plateaukao/sharik/releases)

#### 原始碼

[GitHub - plateaukao/sharik: Sharik is an open-source, cross-platform solution for sharing files via…](https://github.com/plateaukao/sharik)

最原本的 Sharik 版本

[Sharik - file sharing via WI-FI - Apps on Google Play](https://play.google.com/store/apps/details?id=dev.monora.sharik)
