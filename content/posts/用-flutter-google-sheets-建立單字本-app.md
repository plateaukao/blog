+++
title = "用 Flutter + Google Sheets 建立單字本 App"
date = "2020-03-08T09:15:58.842Z"
description = "用 Flutter 開發 App 很快速，但遇到需要有後台的應用時，一般的考量都會是採用 Firebase。Firebase 的整合不會太困難，但是前置作業有點多，對於一個只是需要從雲端某處讀取資料，而又希望這份資料可以很方便地透過網路來編輯的話，Flutter +…"
slug = "用-flutter-google-sheets-建立單字本-app"
canonicalURL = "https://medium.com/@danielkao/%E7%94%A8-flutter-google-sheets-%E5%BB%BA%E7%AB%8B%E5%96%AE%E5%AD%97%E6%9C%AC-app-c51f198cfbf3"
mediumID = "c51f198cfbf3"
+++

### Flutter 整合 Google Sheets 建立單字本 App

![](/images/c51f198cfbf3/1_lQ_29FE33bt-ig-Yg0UcBQ.jpeg)
*Seoul. Korea*

用 Flutter 開發 App 很快速，但遇到需要有後台的應用時，一般的考量都會是採用 Firebase。Firebase 的整合不會太困難，但是前置作業有點多，對於一個只是需要從雲端某處讀取資料，而又希望這份資料可以很方便地透過網路來編輯的話，Flutter + Google Sheets 是個不錯的方案。

### 1. 在 Google Sheets 上建立資料表格

Google Sheets 的方便性在此不再多說，既然我們打算把資料放在它上頭，第一步驟自然是建立所需要的表格。

![](/images/c51f198cfbf3/1_zMJGQQn1Qnv8qVUd4WJrIw.png)

表格建立好後，需要把 url 中 spreadsheets/d/ 後面的 id 記下來，待會 Flutter 中會需要相關資訊。

### 2. 撰寫 Google AppScript

有了資料後，再來是需要寫點 script ，產生 data API 讓 Flutter app 可以隨時取得最新的資料。Google AppScript 可以讓你寫點 script 操作 Google apps (calendar, docs, drive, sheets, gmail, slide) 的資料。關於 Google AppScript 的介紹，可以在下面官網得到更多資訊，這裡也是不多作介紹。

[Apps Script | Google Developers](https://developers.google.com/apps-script)

進入 <https://script.google.com/home> 後，建立一個新的案子，它會跳出編輯器，讓你可以開始盡情發揮。

![](/images/c51f198cfbf3/1_T7sbvb3RRSgAg0KbDXSr6w.png)

填上案子的名稱，便可以開始 coding. 我的使用情境很單純，只需要讀取資料而已，不用從 app 端新增、更新或刪除資料。所以一支 get API 就很足夠了。下面是如何從 Google Sheets 讀取資料的範例，剛剛記下來的 sheets id 會在此時派上用場。另外，還需要指定 worksheet 的名稱和範圍。當然，這些都是可以隨著資料的定義方式有所調整。

[View gist](https://gist.github.com/plateaukao/a3b7f6216c85121e6addef3090b641ca)

寫好 script 後，可以點上方 menu 的 Deploy as web app，會跳出一個對話框，顯示 web app url，和相關的權限設定。執行時的角色和誰可以取得 access right，可以在下面的連結看到更多說明。

![](/images/c51f198cfbf3/1_n63RsFA3Yr8BW2gCcr12RA.png)

[Authorization for Google Services | Apps Script | Google Developers](https://developers.google.com/apps-script/guides/services/authorization)

### 3. 開發 Flutter App

接下來就是容易的部分了，Flutter 的網路存取以及 UI 撰寫都很直覺。連接網路的部分，我是用 Dio，程式碼如下，帶入在 app script 指定的 sheet id 和 range，然後將 json 結果解析成程式中使用的 data model。

[View gist](https://gist.github.com/plateaukao/0290169592b4e60b7002da98b3c896ad)

UI 的部分，顯示單字只需要用一般的 ListView 就綽綽有餘了。但有時例句和解釋比較長，可能用整頁來呈現比較好看，所以也加入了 PageView的型式。

[View gist](https://gist.github.com/plateaukao/a7505c42499900f1727d6d46d8165a2c)

完成的畫面長這樣，點擊單字會顯示綠色的意思，三秒後會再自動消失。右上方的兩個 icon，一個是可以 randomize 從 google sheets 抓下來的資料，不然資料量一大，可能看來看去，都是前十幾二十個單字和句子；第二個 icon 則是切換 listview, pageview 用的。

![](/images/c51f198cfbf3/1_ioV7QFv4BIqG8BJGR5sGPg.png)

### 後續

Flutter app 完成後，電腦常常會把 google sheets 畫面開著，遇到覺得值得記下的單字就會馬上填進去。下次在手機上再開啟 app 時，就能複習了。

後來其實又追加了文法的內容，這部分就下次再說了。

### 有用連結

[PatilShreyas/Flutter2GoogleSheets-Demo](https://github.com/PatilShreyas/Flutter2GoogleSheets-Demo)
