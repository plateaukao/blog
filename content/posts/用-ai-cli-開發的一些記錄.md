+++
title = "用 AI CLI 開發的一些記錄"
date = "2026-02-19T15:55:38.994Z"
description = "從前年開始，就陸續開始用 copilot 和其他 AI 工具來開發 EinkBro。這幾個月來，就幾乎都是用 CLI 的工具在進行開發，不太使用 IDE 來自己寫 code，甚至連 code review 也沒有什麼在做了。"
slug = "用-ai-cli-開發的一些記錄"
canonicalURL = "https://medium.com/@danielkao/%E7%94%A8-ai-cli-%E9%96%8B%E7%99%BC%E7%9A%84%E4%B8%80%E4%BA%9B%E8%A8%98%E9%8C%84-933152a04882"
mediumID = "933152a04882"
tags = ["EinkBro"]
[cover]
  image = "/images/933152a04882/1_vK2smFo5jOY-iHIGx_IM5g.png"
+++


![](/images/933152a04882/1_vK2smFo5jOY-iHIGx_IM5g.png)

從前年開始，就陸續開始用 copilot 和其他 AI 工具來開發 EinkBro。這幾個月來，就幾乎都是用 CLI 的工具在進行開發，不太使用 IDE 來自己寫 code，甚至連 code review 也沒有什麼在做了。

目前 CLI 的 AI 工具愈來愈多，雖然大家還是說最強的是 claude code，但因為沒有訂閱，所以我使用 claude code 的經驗是最少的。目前有輪流在使用的是： Google 的 Antigravity，OpenAI 的 codex，和 Github copilot。

#### Antigravity

Google Antigravity 底子裡是 VS Code，但因為它有個 Agent Manager，勉強算得上是類 CLI 的介面吧？這是這一陣子用比較多的工具；免費的 token 對我來說也還算夠用，因為想開發的功能沒有很多。

前一陣子利用它開發了個 Chrome extension — Ask Web，可以用來針對網頁內容設定一大堆動作，並且給予每個動作不同的快捷鍵；也可以進入對話模式，直接跟網頁內容對話。雖然這樣的 extension 應該有超多的，但是總沒有找到合用的，或是有開放原始碼，可以讓我比較安心使用的，所以還是自己叫 AI 寫了一個。功能完全針對我自己的需求量身打造，相當順手。如果還缺什麼功能，或是 UI 不夠簡潔，隨時可以再叫 AI 調整一下。

[GitHub - plateaukao/ask\_web: A chrome extension to use openai API to query web content](https://github.com/plateaukao/ask_web)

![](/images/933152a04882/1_njN6IX0e2xLvDmJLhNBSqQ.png)

為了要隨時知道 Antigravity 各 model 的使用情況，有裝了一個用來看使用量的 plugin — Antigravity Quota Monitor。有了它，就比較可以知道何時應該再換下個 model，甚至是工具來繼續開發。

![](/images/933152a04882/1_jhLn4bRH8DkEz52xXrYOnA.png)

#### Codex

OpenAI Codex 是最近才開始在嘗試的。因為沒有訂閱 Pro 或是 Plus ，照理來說，是不行使用的。但因為我有買 API 點數，而且有加入 Data Sharing 的計畫，所以有一定的 quota 可以用來使用 OpenAI 的各種 LLM models。

上週利用它來改善 KOReader plugin — AskGPT，讓它能夠提供摘要章節內容的功能。只給了一個 prompt，它就先去找文件來看，然後完成了開發。這點讓我蠻訝異的。一來 KOReader 只是個 github 上的專案，並不是什麼大案子，有很完整的 API 文件，二來，這只是個 plugin 的開發，相關的參考文件應該更少才對。但，它還是一次開發就順利能使用；只是…它用了超多的 token。雖然我的 OpenAI free token for gpt-5.1-codex 有 1m，想說很夠用的，但它硬是用了兩三百萬的 token 數，花了點我自己的儲值 (一兩美元左右)。

[feat: support chapter summary · plateaukao/AskGPT@ac0951f](https://github.com/plateaukao/AskGPT/commit/ac0951f57c82c4845ddc480d4a392b7ab2bc92e6)

#### Copilot

Github Copilot 的 pro 帳號，是 Github 給 open source developer 的福利。以前還在自己寫 code 時，會拿來做 super powerful autocomplete 的工具，用得還蠻開心的。但當各種 CLI 工具出現時，Copilot 就被我冷落了感覺至少有一年吧。

這兩天其他的 CLI 工具 quota 都用得差不多了，想說再回過頭來看一下 Copilot 是不是有點進步，發現它其實也有了 CLI 型式可以使用，於是馬上裝了起來。看來各家提供的功能都大同小異。

雖然用的是 Copilot CLI，但是模型的選擇上，它也提供了 Claude 在用的 Sonnet / Opus 系列，Google 的 Gemini 3 pro。所以如果不喜歡 OpenAI 自家的模型表現，大可使用其他家的模型。不同模型會扣的點數也有些不同。

![](/images/933152a04882/1_t854Mkwv7tTFP01CZLHStw.png)

現在 EinkBro 對於文字選取後的 AI 應用，已經提供了還算完整的設定彈性，讓使用者能夠自訂各種提示詞，以及使用不同的 AI 方案。不過，對於整份網頁內容的操作，現在只有提供 chat with web，得要進到另一個對話型式的分頁後，跟網頁內容對話才行。這樣子的操作，雖然很有彈性；但是對於常用的功能就很麻煩：比方說，我可能會需要請 AI 列出網頁中的重點，請它摘要；請它生成表格；或是做為一個外文老師，把網頁內容用教學的方式整理出來。

發現 Copilot 有 CLI 模式後，我請它幫忙為 EinkBro 加上這個功能。為了達到這需求，它得要去修改 GptActionInfo，讓 genAI 行為能夠先指定該行為是文字選取的操作，還是是要針對網頁全文；另外，還得要去修改翻譯的結果視窗，以及整合既有的 chat with web 畫面。

來回幾個 prompt 後，它就把這功能開發出來了。雖然過程中有幾個 import 該加沒加，我是手動自己加的，但除此之外，它已經完全能按照平常我開發的方式(參考之前的開發模式和寫法，找到需要調整或擴充的地方)把這功能加進來了。原來自己來要兩三個小時，或是一整個晚上的工夫，現在加上 UI 的微調，只需要十幾分鐘就可以完成。

[feat: support page ai toolbar action · plateaukao/einkbro@cdc9f42](https://github.com/plateaukao/einkbro/commit/cdc9f42ea6e52616e1e46d824a059cdeecef35a7)

![](/images/933152a04882/1_OAXwhZz3nlLf1oeXD9C41Q.png)

#### 後記

現在的開發漸漸變成，要自己先在腦海裡對於想要的需求有相對明確的想法，然後再給 AI 足夠明確的指示，讓它能逐步開發出來。實作的細節，如果能在一開始給它多點提示的話，它會比較快找到要著手的地方，省點 token 量，或是少花點 planning 的時間。

AI 可以完成你要它做的功能，但功能要怎麼表現出來，怎樣用起來才順手，現階段我覺得還是要人為地去給意見，請 AI 修改。但我相信很快地，會變成 AI 思考後，給出幾個後續加強方案來讓我選吧。
