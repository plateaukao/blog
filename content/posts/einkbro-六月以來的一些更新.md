+++
title = "EinkBro 六月以來的一些更新"
date = "2024-08-29T13:45:57.259Z"
description = "自從開始更大量地使用 ChatGPT 協助寫 code 之後，就漸漸失去了動力寫文章，因為大部分的功能只需要請 ChatGPT 幫忙產生所需程式碼，再稍微重構一下，將其套用到 EinkBro…"
slug = "einkbro-六月以來的一些更新"
canonicalURL = "https://medium.com/@danielkao/einkbro-%E5%85%AD%E6%9C%88%E4%BB%A5%E4%BE%86%E7%9A%84%E4%B8%80%E4%BA%9B%E6%9B%B4%E6%96%B0-1a091f99ab5f"
mediumID = "1a091f99ab5f"
+++

![](/images/1a091f99ab5f/1_U7_A7KAID90_lJW75td99g.png)

自從開始更大量地使用 ChatGPT 協助寫 code 之後，就漸漸失去了動力寫文章，因為大部分的功能只需要請 ChatGPT 幫忙產生所需程式碼，再稍微重構一下，將其套用到 EinkBro 中就行。如此一來，少了很多需要自己探索，或是值得記錄下來的內容。不過，一直這樣下去也不是辦法，所以，還是來寫寫最近有加入的新功能吧。

### v11.10.0

改善翻頁的作法。大部分的網頁會乖乖地在 Android WebView 呼叫`scrollTo` 函式時，將網頁內容向下位移指令的距離。但是，有很多網頁偏偏想要用一些特別的實作來捲動畫面，導致這樣的作法會失效。

為了解決這種情況發生，一個方式是找到目前畫面中具有 `overflow-y: auto` 的網頁元件，然後在按下翻頁按鈕或是翻頁按鍵時，針對那個元件進行捲動。

詳細的實作是利用 Javascript 來完成的，可以在下面的 commit 中看到。

[fix: #366 add javascript handling to fix scrolling issue on websites. · plateaukao/einkbro@23c3fc5](https://github.com/plateaukao/einkbro/commit/23c3fc576d1cdd52cde5f480e2e804d171444e0d)

然而，這個作法很陽春，也只能解決到一小部分的特例而已。不過，至少有了一點點的進步。

### v11.11.0

OpenAI ChatGPT 面世已經一年多了，在 EinkBro 中對於 GPT 的支援也愈來愈豐富。在這個版本中，支援了 OpenAI 的模型設定；並且，能夠指定其他跟 OpenAI API 相容的 API 服務；甚至，還加上了 Google Gemini 的支援。

這一版沒有什麼特別的技術需要多做解釋的；就是把原先的 API 呼叫做得有彈性一點，既能換掉 url entry point，也可以指定 model 罷了。

比較可以提的是：原來 Reader Mode 的字型設定壞了好一陣子。在網站上看到有使用者提出這個問題，才順手在這一版將它修復。

### v11.12.0

又再次試圖改善部分網頁的翻頁行為。

另一點是調整了儲存網頁列表的邏輯。正常來說，應該是要儲存每個分頁最終所在的網頁才對，而不是該分頁一開始被建立的網址。

這也是有網友建議這麼做的時候，我才想到：對啊，這樣才合理吧。

### v11.13.0

終於，開始又有想要實作的功能了！

早些時候開發的在 Youtube 中顯示雙語字幕。這功能在我使用 EinkBro 看 Youtube 時幾乎都會使用。不過，一直盯著影片看也是會累的。是不是可以直接將這些影片的雙語字幕儲存下來呢。

在不想看影片時，就可以看看字幕學習外語。如果儲存成 epub 格式，還可以再用 EinkBro 打開來，做後續的查單字，以及叫 ChatGPT 做很詳細的解釋。

之前雙語字幕的作法，簡單來說，是在 WebView 需要從網路下載 resource request 時攔截這需求，一次抓下來兩個語言的字幕，將它們合併成一個，再傳給 WebView。

這次，則是在這過程中，將要用來呈現的雙語字幕 resource 存在 WebView 中。當使用者想要對這個 Youtube 網頁儲存 epub 時，只要發現有雙語字幕的 resource，就改成儲存雙語字幕。

細節可以在下面這支 PR 看到。

<https://github.com/plateaukao/einkbro/commit/27caeff9530decb4ebd888583d08da642511a548>

### v11.14.0

#### 依網域做不同的設定

自以為的重磅功能來了！v11.14.0 中加入了一個之前很提不起勁加入的功能：根據網域的不同，提供不一樣的各種設定 (翻譯，背景色變白，等等)。

在這個版本裡，對於 per-site 的設定，還是很用土炮的方式實作：將每一個 configuration 從原先的 Boolean 值，改成 Set<String> ，能夠將開啟的網域都加入一個 Set 裡。每次新開網頁時，檢查當前的網址是不是有在這個 Set 中；有的話就當它是有啟用這項功能的。

詳細的實作可以在下面的 commit 看到：

[feat: support by site enabling translation feature now · plateaukao/einkbro@b2b424e](https://github.com/plateaukao/einkbro/commit/b2b424e5745601240197cde4907c190c65e7b575)

只要有想要 per-site 設定的項目，就都寫一段類似下面的程式碼。

![](/images/1a091f99ab5f/1_Xiva45-aXWd1UqJFu85ucg.png)

這方法雖然很遜，但有用。

#### 改善選取文字的方式：選取句子

像這個功能就是問 ChatGPT 而來的，所以雖然看起來很酷炫，不過功勞其實都是 ChatGPT 的。

作法是寫段 Javascript，讓它先取得目前 Web 中的 selection ，從這個 selection 去找到被選取的 container 。有了 container 後就可以取得裡頭的 textContent，再決定要從現有的選取位置往前移動或往後移動。

以選取句子來說，在選取的起始位置是要試著往回走，走到前一個句子的結束 (可能會是 . 。！!？?等字元)，而選取的結束位置則是要繼續往後走，走到這個句子的結尾 (另一個. 。！!？?)。

作法可以在這個 commit 中看到。

[feat: select context as a whole sentence · plateaukao/einkbro@e3132ea](https://github.com/plateaukao/einkbro/commit/e3132ea1e4d563c3b1179d360633bcef82e490af)

![](/images/1a091f99ab5f/1_U3WGeHwm831Sgbr8DBb-rg.png)

![](/images/1a091f99ab5f/1_XlOBr7s4Gd5MXRuvWvBRsQ.png)

#### 輸出 GPT 結果

不論是 gpt-4o 或是 Gemini-1.5-pro，都可以產生不錯的解釋內容。這些產出的結果，在閱讀之後如果能夠儲存下來，就能夠事後再拿來復習，溫故知新。

### 總是翻譯

某些特定的網站，每次進入就是要開啟翻譯的功能。按久了，偷懶的心漸漸冒出來。難道就不行讓它能自動判斷網址，來決定要不要自動翻譯嗎？

這版支援了！

在設定方面，就是剛剛提到的 per-site 設定作法。設定好之後，在 WebView 載入網頁時，當載入完成會進入 WebContentPostProcessor 的 `postProcess` 。

只要目前的網頁有在需要被翻譯的清單，翻譯的 Javascript 會將網頁翻譯成指定好的語言。

這點真是太好用了！我應該早點開發的。

![](/images/1a091f99ab5f/1_SbOtoygz2DrmqzfHN6n-VQ.png)

### v11.15.0

#### 選取文字的段落

延伸 v11.14.0 的選取句子功能，這一版加入了選取段落的功能。這對於常常需要翻譯的使用者來說，應該會很使用。

#### 將輸出 GPT 結果轉為 html 文件

gpt-4o 或是 Gemini-1.5-pro，常會在回覆中使用 markdown 的標記方式。雖然它是純文字，即使沒有特別的 rendering engine ，依然具有很高的可讀性。

但為了原先的 markdown 格式能更清楚易讀，這一版實作了 markdownToHtml ，利用外部的 javascript library 協助，讓產生的 html 能顯示漂亮的效果。

#### 支援 App 內切換語系

早知道程式內換語系這麼容易實作，應該早點就開發的。這功能也是透過 GPT 得到的答案。

Android 有提供了 Configuration.setLocale 的函式，讓開發者可以在 Activity 或是 Fragment 中即時去更換語言。不過，我不用那麼即時，只要重開 App 能解決就行；所以目前是在設定 > 介面 中新增選擇介面語言的設定，等設定好後，回到網頁時，會問使用者是不是要重啟 App，讓語言能夠生效。

實作內容都在這支 commit:

[feat: support in-app language setting · plateaukao/einkbro@bc900a2](https://github.com/plateaukao/einkbro/commit/bc900a278920603b062fd78cdb3062a49f2b184a)

有了這功能後，以往一些大陸買的閱讀器，系統中沒有繁中語言可選的，現在都可以用這方式單獨改變 App 的介面語言。

也因為這樣，我發現韓文的介面好像全部都是英文。所以，我把韓文的 strings.ml 丟給 ChatGPT，讓它幫我生出對應 ko/strings.xml。希望這樣能為我帶來更多韓國的使用者。
