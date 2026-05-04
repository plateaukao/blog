+++
title = "打造 E-ink 專用的瀏覽器: Part I"
date = "2020-04-05T05:31:12.831Z"
description = "這是一個程式阿宅追查為什麼 FOSS browser 在 Onyx Boox 電子書閱讀器上，會莫名奇妙地跳轉網頁的無聊故事"
slug = "打造-e-ink-專用的瀏覽器-part-i"
canonicalURL = "https://medium.com/@danielkao/%E6%89%93%E9%80%A0%E4%B8%80%E5%80%8B%E9%9B%BB%E5%AD%90%E6%9B%B8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-i-e6c3d2e55e82"
mediumID = "e6c3d2e55e82"
tags = ["EinkBro"]
[cover]
  image = "/images/e6c3d2e55e82/1_EgEAOM9E5TTNFHa_KWnAIA.jpeg"
+++


### 打造 E-ink 專用的瀏覽器 (I): Onyx Boox 上的怪現象

**這是一個追查為什麼 FOSS browser 在 Onyx Boox 電子書閱讀器上，會莫名奇妙地跳轉網頁的無聊故事**

![](/images/e6c3d2e55e82/1_EgEAOM9E5TTNFHa_KWnAIA.jpeg)

### 需求

目前的開放式電子書閱讀器都已經做得很方便，除了可以安裝一般的電子書 App 像是 Kindle, Kobo, Google Play Books, Hyread 之外，還有內建瀏覽器供使用者偶爾上上網，查查資料。如果切到 A2 Mode (註1)，其實使用起來的速度已經可以讓人接受，不會整個畫面閃不停。

但是，當愈來愈常使用電子書的 browser，還是會覺得在捲動畫面時，畫面更新速度跟不上手滑動的速度。那，我是不是可以把 browser 的瀏覽方式改得類似電子書，能夠一頁一頁往下翻，而不是不斷地捲動網頁呢？

有了這想法之後，首先是上 Github 看看是不是已經有別人將 WebView 包好的 小而美的 App。畢竟，我要的只是改造瀏覽的體驗而已，而不是從頭開始自己寫一個新的 browser。

經過一番搜尋和比較(可能一兩分鐘吧)，scoute-dich 的 browser 比較符合我的需求，程式碼數量也不會大到我需要花很多時間才能上手。這個 browser 的前身是從 ninjia 的 browser 來的，目前看來，一直到最近都還有在更新，應該比較不會遇到問題。

[scoute-dich/browser](https://github.com/scoute-dich/browser)

經過一兩個小時的研究，快速地把自己想要的翻頁功能做好了。(其實只是在點擊畫面某個地方時，讓內容可以直接往下前進 2/3 個畫面，不要有捲動的效果) 關於功能實作的說明，會留在 Part II。這一篇文章比較想要講功能完成後，放到電子書閱讀器上遇到的靈異現象。

---

功能完成後，我將 App 安裝到海信的 A5 (Hisense A5)，和博閱的 Likebook Mars，都可以很正常的運作。但安裝到 Onyx Boox Note Pro 時，就不是那麼一回事了。

App 一開始執行時，會正常出現預設的網頁，但隔一兩秒後就會突然跳到下面的畫面，然後開始鬼打牆，不斷地重新更新這個畫面，想要叫它停也停不下來。

![](/images/e6c3d2e55e82/1_kYPKeaM9mDZGi7MwR-oRog.png)

看到 javascript blah blah的，就覺得被**注入**了！明明預設網頁就是個很單純的網頁而已啊。究竟是哪裡出了錯呢？

思考的方向有下面幾點：

1. 預設網頁有問題，會偷偷導到某些不知名的地方
2. 這套 open source browser有問題，從程式碼中偷塞了要注入的 javascript
3. Onyx Boox Note Pro 的 WebView 有問題

要排除 1 的可能性很簡單，我只要把預設網頁網址換掉，重新編譯一版 App 來測試就行。事實證明，不是預設網址的問題。即使換成 www.google.com，畫面還是會回到上面的裡打牆狀態。

難不成會是 2 嗎？雖然之前常會聽到有很多惡意的 hack，故意藏在 open source code 中，但這套 browser 程式碼可是有 400 多顆星，100 多份 fork。在那麼多人研究後都沒出事，卻偏偏被我遇上了？

抱著無罪推定原則，如果是 2 的話，我得把它偷塞的javascript 程式碼找出來，才能把問題怪到它頭上。不過找了一輪，並沒有看到可疑的程式碼片段。有可能因為我不專業的 hacker，所以才找不到吧。

暫時放棄 2 這條線索，一早醒來，開始查第 3 種可能性，會不會是 Boox 的 WebView 有被動過手腳？其實這樣的懷疑也是很合理的，因為在另外兩個牌子的電子書閱讀器上並沒有問題，這現象只在 Onyx Boox 的設備上才會發生。

從問題的症狀來看，WebView 的 url 其實有被重新載入過，由一開始的 www.google.com，被改成預設的搜尋引擎加上一串 javascript 程式碼。所以，我在程式中跟載入網址有關的地方都加了 breakpoint，期待可以在某個時間點，找到凶手是誰。

![](/images/e6c3d2e55e82/1_1P7RNMMg4UuyyYfR7hfiLw.png)
*抓到凶手了*

抓到了！果然 WebView 會被塞入新的 url 。從上圖可以看到，將被載入的 url，就是這段可疑的 Javascript 程式碼。從圖左下角的 call stack 可以看出 *loadUrl()* 是被 *injectCSS()* 呼叫，而它的執行時間點是在 WebView 的 *onPageFinished()* 。injectCSS() 點進去看，並看不到對應的程式碼，因為它並不是正規的 WebView source code。看到它所屬的位置是在 android.webkit 的 WebViewClient，應該可以肯定是 Onyx Boox 的內建 WebView 有改過。

既然程式停了下來，我可以仔細看一下這段 javascript 到底寫了什麼。

![](/images/e6c3d2e55e82/1_LyruVOzg14y2SQt72yrCUw.png)
*url value in breakpoint*

以我粗淺的 web 程度，大概可以猜出來它是要找到 html 的 head element，在裡頭塞一個 style 的 element，然後要再塞一段 window.atob() 來的資料。為了確保我的理解沒錯，我把上面的內容拿去餵 Google ，得到這是塞 javascript 或 CSS 到 WebView 網頁中的常用方式 。下面是其中一個網站說明的範例程式；寫法完全一模一樣。

[View gist](https://gist.github.com/plateaukao/a0aa25ae61381036f2360d457255e4b9)

到現在，大概知道了這是 Onyx Boxx 的 WebView 搞的鬼，它會在 onPageFinished() 去呼叫新增的 injectCSS() 函式。 windows.atob() 的作用是把編碼過的 Base64 string 再轉回來，所以，如果我想知道被塞了什麼，就要把裡頭的那串

```
KiB7Cgljb2xvcjogIzAwMDAwMCFpbXBvcnRhbnQ7Cglmb250LXdlaWdodDo5MDA...
```

丟到網路上的 Base64 Decoder 去看看。

[View gist](https://gist.github.com/plateaukao/8f12e16251561597f658b417ba7184d7)

Voila~ 就是一堆在改顏色的 CSS codes。

### 解決的方法

知道是誰在搞鬼，和怎麼搞鬼之後。再來就是看怎麼對症下藥。

![](/images/e6c3d2e55e82/1_0FXBB9yhViRB1Td8_77-Wg.png)
*Sequence Diagram*

流程中的 3. → 4. → 5. 只要任何一步斷開就可以避免內建的 WebView 去注入 CSS。要斷開 3. → 4. 的話，可以在 NinjiaWebView 的 WebViewClient override onPageFinished 時，不要呼叫 super.onPageFinished()，這樣子就不會進到 4. 中。

如果不確定 super.onPageFinished() 做了什麼，想要保留的話，可以在 5. 的時候去判斷目前塞進來的 url 是不是 `javascript` 開頭的字串，如果是的話就直接 return，不做任何處理。這樣子也可以避開 injectCSS() 帶來的影響。

目前我的解法是採取後者，如下圖所示，在 205 行加入 url 的判斷，如果為真，就 return ，不做任何事情。(畫面中先 comment 掉是為了要重現錯誤的狀況)

![](/images/e6c3d2e55e82/1_1P7RNMMg4UuyyYfR7hfiLw.png)
*skip loading javascript*

### 結論

忙了一晚，都是在找問題，真正的翻頁功能倒是早早就寫完了。接下來可以慢慢改善 UI，讓翻頁的功能更方便使用。 :)

### 系列文章

[打造 E-ink 專用的瀏覽器: Part II](https://medium.com/@danielkao/%E6%89%93%E9%80%A0-e-ink-%E5%B0%88%E7%94%A8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-ii-a7bfb98233f7)

### **註釋**

註1

截自 [Hyread 網站](https://ebook.hyread.com.tw/activity/201902gaze/qa.jsp)

A2模式是什麼？

前面提到電子紙的特性會有殘影(電子墨水的殘留畫面)，製造商為了解決殘影的問題，設計了全螢幕刷新，全刷的過程螢幕就會閃一下，像是恢復初始狀態的畫面。Gaze上方系統列兩個逆時針箭頭的符號即為「A2模式」，開啟A2模式能讓你快速刷新螢幕，針對內容進行局部刷新，縮短螢幕刷新的時間，同時產生輕微殘影。因此，A2模式適合用於瀏覽網頁或閱讀漫畫，可增加視覺觀感的流暢度，減少全螢幕刷新的閃爍現象。

### 參考資料

[使用android中的webview將javascript文件注入我的網站-code log](https://www.aimz8.com/sp/?p=12527)

[Window atob() Method](https://www.w3schools.com/jsref/met_win_atob.asp)

[Base64 Decode and Encode - Online](https://www.base64decode.org/)

[modify scroll to bottom logic; modify button position; fix injectCSS ... ·…](https://github.com/plateaukao/browser/commit/0aa9441f0d2a8ba727e7e9b750d936cb89efe75f)
