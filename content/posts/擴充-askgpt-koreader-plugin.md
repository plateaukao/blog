+++
title = "擴充 AskGPT KOReader plugin"
date = "2024-05-28T17:43:07.815Z"
description = "這篇文章介紹了如何改良 KOReader 的 AskGPT plugin ，讓它預設就有 context-aware 字典和翻譯的功能，還可以將查詢結果儲存到文字標記的筆記中。"
slug = "擴充-askgpt-koreader-plugin"
canonicalURL = "https://medium.com/@danielkao/%E6%93%B4%E5%85%85-askgpt-koreader-plugin-d53aa5f5a38b"
mediumID = "d53aa5f5a38b"
+++

KOReader 的 AskGPT plugin 沒有任何預設的 prompt；再加上 KOReader 中又只能用它內建很陽春的軟體鍵盤，在使用上並不是很方便。因此，這幾天我一邊看書，一邊改良了一版，加入了最常使用的幾個 template，讓它們直接以按鈕的型式出現在選單中，也加入了 Google Gemini Model 的支援。

雖然 Google Gemini 1.5 Flash 的表現跟 OpenAI Gpt-4o 還有段差距 (比較慢，產出結果也比較不優)，但是畢竟它現在是近乎免費的，還是蠻香的。

![](/images/d53aa5f5a38b/1_vpkT4Spo1oqWx_a0jnXxug.png)
*KOReader 選擇文字後的功能選單，新增 GPT Dictionar, GPT Translate 和 Gemini Dictionary*

#### 下面記錄一下我做的改良

- 修正 loading 對話框太慢出現
- 新增 Dictionary, Translate 按鈕
- 實作 context-aware 字典解釋
- 新增 Gemini Dictionary 按鈕
- 將結果存入 Notes

---

### 修正 loading 對話框

如果在同個函式中呼叫的話，它會一直等到 http request 回來後，才會跟著結果內容一併顯示。這麼一來就失去了顯示它的用意。為了解決類似的問題，KOReader 實作裡的 `UIManager` 有提供函式可以讓部分操作在下個 UI cycle 中再執行。因此，可以先顯示 loading 對話框，然後讓 http request 在下個 UI cycle 中再執行。

```
UIManager:scheduleIn(0.1, function()  
    showChatGPTDialog(self.ui, _reader_highlight_instance.selected_text.text)  
    _reader_highlight_instance:onClose()  
end)
```

完整修改如下：

![](/images/d53aa5f5a38b/1_onWDXak2NTpDLRooH9mmWg.png)

### 新增 GPT Dictionary, Translate 按鈕

這一部分沒啥技術難度，就跳過原先會呈現的輸入框，直接將寫好的 prompt 餵給 http request 去執行。

主要的修改在這支 [commit](https://github.com/plateaukao/AskGPT/commit/94874b76a3191b0c30f4ee4b501857fb341f3a0c)。關於加 dictionary button 的程式碼如下：

![](/images/d53aa5f5a38b/1_DvvLsmi4Nflq3DSAT2WGcQ.png)

在 dictdialog.lua 中，有塞入比較合適的 prompt，讓它可以做為字典。下面的程式碼有怪怪的兩個值：prev\_context 和 next\_context。它們的用途會在後面做說明。

```
local context_message = {  
   role = "user",  
   content =   
      "完整句子: " .. prev_context .. "<<" .. highlightedText .. ">>" ..   
      next_context .. "\n" ..  
      "將上述句子中 <<>> 中的內容 1. 翻譯成 zh-TW\n" ..  
      "2. 顯示單字原型;如果是日文單字，則顯示漢字拼法 (原本語言)\n" ..  
      "3. 舉一個新的例句 (原本語言與 zh-TW 對照，各佔一行)\n" ..  
      "只回答，不要重覆提示\n\n" ..  
      "<<" .. highlightedText .. ">>",  
}
```

GPT Translate 的話，跟做為字典差不多，就是 prompt 有點差別而已。

### 實作 context-aware 字典解釋

在使用字典時，常會遇到一個問題：有些常用字的解釋少說也有十幾二十個。在查詢時往往得要將所有解釋一個個看過一次，再來研究文章中的用途究竟是哪一個。如果剛好遇到一句話裡有兩三個字看不懂，那排列組合下來，要看懂那句話可能得花上不少時間。等搞懂後，應該也沒有心情再往下讀了。

如果有個字典能夠根據文章的前後文，直接給出當下最合適的解釋的話，不就可以省下很多時間，而且可以讓使用者快速地再回到書籍上，不用在字典停留太久。

以往的字典無法做到這一點是因為它都是以單字或是片話為搜尋的 key，然後解釋為其 value。如果一個 key 可以對應到超過一個 value 的話，它就頂多只能依常用度來排序，無法再依照其他方式排序或是提供額外的查詢方式。

有幸生在 ChatGPT 出現的年代，這個限制被打破了。ChatGPT 就是個可以了解整段文字，再來回答你問題的好工具。拿它來當 context-aware 字典真是再適合不過。

KOReader 的實作中，除了可以拿到 selected text 外，它還很貼心的提供了 context string，可以取得 selected text range 的往前和往後字串。這可以透過 `ui.highlight:getSelectedWordContext(context_length)` 。`context_length` 可以指定要往前和往後抓多少文字進來。這個函式的回傳值有兩個，用法如下：

```
prev_context, next_context = ui.highlight:getSelectedWordContext(15)
```

拿到前後 context，就能在 prompt 中請 chatgpt 根據前後文來給出 selected text 的意思。作法可以看上方提供的 prompt。

### 新增 Gemini Dictionary 按鈕

今年五月多的 Google IO 宣布了 Gemini 1.5 Flash 的新 model，能夠更快更便宜地提供服務。如果每分鐘呼叫次數在 15 次以內的話，是不需要收費的。拿來個人使用的話，很少會需要有這麼大呼叫次數。因此，很適合拿來做一些不需要太高品質的呼叫。

Google Gemini 取得 API key 的方式比 OpenAI 還容易，也不容事前先儲值，所以我很快地也整合了 Gemini 進 AskGPT plugin。

主要的修改在這個 [commit](https://github.com/plateaukao/AskGPT/commit/af5568db27bbb174d570930cdf2376da6c2ec818)。

參考原先的 `gpt_query.lua`，複製成 `gemini_query.lua`。把 `api_url` 換成了 Google 的 `“https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=" .. API_KEY.key`

在 prompt 方面，則是代入跟 ChatGPT 一模一樣的內容，方便兩者在使用上作效果的比較。

### 將結果存入 Note

好不容易搜尋到的結果，如果過一會兒忘了怎麼辦？是不是能將它記錄下來，方便事後再閱讀呢？

KOReader 原先的實作就已經有將標記的文字儲存下來的功能，也支援針對選定的文字內容輸入一些文字記錄到 Notes。利用後者，就能將 AskGPT 搜尋的結果偷塞到 Notes 中。

所以，我在搜尋結果對話框下方，多了一個加入筆記的按鍵。

![](/images/d53aa5f5a38b/1_WkHIIlvGfFN2MZ0IUj4Wtg.png)

實作方式如下：

- 在 chatgptviewr.lua 中加入按鈕

![](/images/d53aa5f5a38b/1_6a3oSEgJ7lrXxWXLtXW1bQ.png)

- 在 dictdialog.lua 中生成結果對話框時，代入 handleAddToNote 函式。

![](/images/d53aa5f5a38b/1_gEVqWlj_yaTJIUDa0KdtAw.png)

- 而 handleAddToNote 的實作就是去呼叫原先 KOReader 就有的功能

![](/images/d53aa5f5a38b/1_H44flgox3pawUlBMFJwjew.png)

主要的修改在下面這一支 commit：

- [feat: support adding results to note.](https://github.com/plateaukao/AskGPT/commit/51f0a90427c3d78bf101be9667c41666456973fd "feat: support adding results to note.")

存入 Notes 的內容，可以在點擊標記時看到：

![](/images/d53aa5f5a38b/1_XQ_mBQmOz-jftSf85DkjFg.png)

#### 將選取文字在結果對話框裡標成粗體字

最後對於 UI 上的一點小改善，把被選取的文字用粗體表示。這樣做會比顯示醜醜的 << 和 >> 來的美觀一些。

主要的修改在這支 [commit](https://github.com/plateaukao/AskGPT/commit/0f5f6784519c0b44229ff08939d0baa820527624)。

KOReader 的 Text Widget 支援利用某些 tag 來標示哪些文字片段要以粗體顯示，實際作法如下：在字串的最開始加上 `TextBoxWidget.PTF_HEADER`，告知字串裡會有其他的 tag。然後利用 `TextBoxWidget.PTF_BOLD_START` 和 `TextBoxWidget.PTF_BOLD_END` 將粗體字包住。這樣子就可以啦

![](/images/d53aa5f5a38b/1_UudBNj91AAPGT-rsa2_0vQ.png)

顯示的效果如下：

![](/images/d53aa5f5a38b/1_sbzVpP1DgRFl48tRKBKzEw.png)

### 相關連結

[GitHub - plateaukao/AskGPT](https://github.com/plateaukao/AskGPT)
