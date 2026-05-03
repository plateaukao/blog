+++
title = "JB Kindle Voyage 和 AskGPT plugin for KOReader"
date = "2024-05-05T14:30:39.974Z"
description = "kindle voyage 買來有快十年了吧，隨著最近又買了 kindle scribe 和 kindle oasis3，以及對於 koreader 的熟悉程度愈來愈高，終於下定決心來越獄一下，為它安裝 koreader app。"
slug = "jb-kindle-voyage-和-askgpt-plugin-for-koreader"
canonicalURL = "https://medium.com/@danielkao/jb-kindle-voyage-%E5%92%8C-askgpt-plugin-for-koreader-17e17ce7bc39"
mediumID = "17e17ce7bc39"
+++

kindle voyage 買來有快十年了吧，隨著最近又買了 kindle scribe 和 kindle oasis3，以及對於 koreader 的熟悉程度愈來愈高，終於下定決心來越獄一下，為它安裝 koreader app。

jb 的過程有點煩瑣，不過，照著”書伴”網站上的教學一步步來，應該十幾二十分鐘可以搞定。裝好 koreader app 後，自然是先裝上前幾天研究好的直排 patch，再換上自己轉好的偽直排字型，從此，可以開心地用著它直排地看 epub 電子書了。

[Kindle 通用越狱教程：适用固件版本 5.12.2.2~5.14.2](https://bookfere.com/post/970.html)

![](/images/17e17ce7bc39/1_K5s6N20THFZ8SPSXuKa8kA.jpeg)

![](/images/17e17ce7bc39/1_d5Ym7U8_31Hwj-7T0pYwFQ.jpeg)

![](/images/17e17ce7bc39/1_KEivOCxms0BwIi73H-QpHw.jpeg)

另外，基於 koreader 強大的擴充性，有強者為它寫了 askGPT plugin。只要你有 OpenAI API key，就可以直接在 koreader 中跟 chatgpt 互動！我稍微調整了一下 UI，把 plugin 連結放在留言處。有興趣的人可以試試。

另外，因為 OpenAI API 是要錢的，如果大家會寫程式的話，可以考慮把 gpt\_query.lua 中的 api entrypoint 改成 local 自建的 ollama api server 或是其他跟 openAI API 相容的 API server，就可以少一筆支出。(雖然目前 openai API 的收費已經便宜到不行)

![](/images/17e17ce7bc39/1_OwhreO5kwQu_UBkw1SzRaA.png)

---

對了，另外跟大家分享一下小發現：

1. 如果在 kindle 上執行 koreader 的話，可以在 koreader 中自定休眠的圖案喔！可以用目前閱讀中的書籍封面、或是某個特定資料夾下的一堆圖片，或是以目前的畫面做為修眠畫面。還可以自訂在休眠時，畫面是不是要有個提醒的 message，像是 書中自有黃金屋 之類的。
2. koreader 對於許多系統(像是文石和 kindle)的畫面刷新都有支援，所以可以設定當點擊畫面某個區域，或是做了某個手勢之後，可以讓畫面全刷。對於不愛用懸浮球的我來說，這個功能在 kindle 和 文石機器 上很實用！(kindle 不太需要重刷畫面就是了)

### 相關連結

[GitHub - plateaukao/AskGPT](https://github.com/plateaukao/AskGPT)
