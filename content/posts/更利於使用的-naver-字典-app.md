+++
title = "更利於使用的 Naver 字典 App"
date = "2021-02-17T14:39:23.115Z"
description = "在學習韓文的路上，Naver 字典是公認的好用。但如果在平板或手機上想一邊看電子書或是看網頁，然後一邊使用 Naver 字典的話；不論是網頁版或是 App 版本的 Naver 字典，用起來都很麻煩，得在不同的 App 間不停地切換。來回個幾次之後，就會放棄這麼做。"
slug = "更利於使用的-naver-字典-app"
canonicalURL = "https://medium.com/@danielkao/%E6%9B%B4%E5%88%A9%E6%96%BC%E4%BD%BF%E7%94%A8%E7%9A%84-naver-%E5%AD%97%E5%85%B8-app-1354aaeabc30"
mediumID = "1354aaeabc30"
+++

在學習韓文的路上，Naver 字典是公認的好用。但如果在平板或手機上想一邊看電子書或是看網頁，然後一邊使用 Naver 字典的話；不論是網頁版或是 App 版本的 Naver 字典，用起來都很麻煩，得在不同的 App 間不停地切換。來回個幾次之後，就會放棄這麼做。

為了有效解決這個問題，我寫了一個 Android App (naverdict)，裡頭包了一個 WebView，負責幫忙去網頁版的 Naver 字典做查詢。它的運作方式如下：

1. 在電子書 App 裡，從字典清單中選用 naverdict 當成預設的字典
2. 先將 naverdict 開成 multi-window 的其中一個 App
3. 使用者在電子書 App 中查詢單字
4. naverdict 被開啟，並在其 WebView 中的 Naver 網站做查詢

---

### 從字典清單中選用 naverdict

一般電子書 App 都會支援 colordict 或 mdict 的字典搜尋方式。以 Android 程式碼實作來看的話，這些 App 都會去掃系統有哪些程式支援 `colordict.intent.action.SEARCH` Action 的 `intent` 。能吃這個 `Action` 的程式，就是能用來查詢單字的程式。只要在我的 naverdict 的 Activity 加上這個 Action 的 `intent-filer` 就可以達到被其他 App 喚起的功能。更詳細的設定可以參考這篇文章：

[ColorDict Intent API for 3rd party developers](http://blog.socialnmobile.com/2011/01/colordict-api-for-3rd-party-developers.html)

如果是想出現在一般瀏覽器選擇字串後的 action bar 上的話，則是要支援 `android.intent.action.PROCESS_TEXT` 才行。

設定好的 Activity xml 大概會長成下面這樣：

![](/images/1354aaeabc30/1_t49TylwSpEcFb0g2WEx7UQ.png)

當 Activity 收到這 `intent` 時，只要從 `intent` 中抽出字串，把該字串組合成 Naver 字典網頁查詢的 `url` ，往 `WebView` 中送就行了。實作如下：

![](/images/1354aaeabc30/1_J5AWSA8lmJPkbU_XmYiDew.png)

### 將 naverdict 開成multi-Window 的其中一個 App

Android 從 7.0 開始有支援 Multi-Window 的功能，但是因為使用上不是很好用，而且也不是那麼直覺地可以開啟這功能，所以一直沒有被廣為使用。關於 Multi-Window 的介紹可以自行前往下面 Android 官網瞧瞧。

<https://developer.android.com/guide/topics/ui/multi-window>

通常它的啟動方式是做在 Recent App 的介面中，中文叫做「分割畫面」。在進入 Recent App 列表後，點選該選項即可。然後畫面的下方再看想要開啟什麼電子書 App 或是一般的瀏覽器。

![](/images/1354aaeabc30/1_vAJyEbRRXEIQcgOjVGg6Pw.png)

### 在電子書 App 中查詢單字

我比較常用的電子書 App 是 Moon+ Reader Pro。它支援長按畫面文字時，會自動截取前後 space 間的字串，然後餵給事先設定好的字典程式。

比方說在看書時，遇到 나뉘고，不確定這是什麼意思，也不知道它是什麼樣的動詞形容詞變化而來的時候，長按畫面，它會很聰明地抓取這段文字，然後往我寫好的 naverdict App 送。這時上方的字典就會去 naver 網站查詢，並把結果顯示出來。

畫面已經切成兩個同時開啟的 App 了，所以不會有畫面蓋來蓋去的問題。Naver 字典也很聰明地會幫你判斷這個字串，真正的單字原形是什麼，並且給你相關的解釋。

![](/images/1354aaeabc30/1_aoyJJm_9kw-r1Q-sMrOn2A.png)

### **改善 Naver 字典網站的呈現方式**

如果直接到 Naver 字典網站查詢一樣的 나뉘고，你會發現畫面中充滿了不必要的元素：厚厚的標題、搜尋列、輸入方式選項、不同結果的 tab。這些元素在長按單字啟動搜尋的情境中，都是可以拿掉的。

![](/images/1354aaeabc30/1_-pmCIMewVobtMGJFZ5y0aQ.png)

所以，在 naverdict 中的 WebView 還動了點手腳：在收到 `onPageFinished` callback 時，塞了點 JavaScript 到網頁中，把上述的那些原始移除或是隱藏。實作方式如下：

![](/images/1354aaeabc30/1_P0UEBebanKvnzqQJhs411Q.png)

這麼一來，進入 Multi-Window 模式時，不論是上方的 naverdict 或是下方的 moon+ Reader Pro，都沒有什麼多餘的元素干擾閱讀，可以很享受地在這樣子的組成中開心地讀書和查詢不懂的單字。

### 後話

目前只串了 Naver 字典，因為目前只有學習韓文的需求。如果想把字典換成日文或英文的話，只要有合適的線上字典，稍微改一下 App 就可以使用了。

### 參考資料

[plateaukao/naverdict](https://github.com/plateaukao/naverdict)
