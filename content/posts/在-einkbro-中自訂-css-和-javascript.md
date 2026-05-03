+++
title = "在 EinkBro 中自訂 CSS 和 Javascript"
date = "2026-05-03T12:00:00+08:00"
description = "自從推出 EinkBro 後，一直有人在敲碗的功能就是希望可以針對每個網站，能夠自訂 CSS 和塞入 Javascript。在 AI coding 幾乎完全取代手工寫程式之後，這件事變得是舉手之勞。"
slug = "在-einkbro-中自訂-css-和-javascript"
tags = ["EinkBro"]
+++

自從推出 EinkBro 後，一直有人在敲碗的功能就是希望可以針對每個網站，能夠自訂 CSS 和塞入 Javascript。很多時候，使用者會希望隱藏網頁上的某些元件，或是修改一些行為，讓閱讀時能更流暢。但是，因為之前並沒有為每個網站建立獨自的資料儲存，而且，在手機上如果想要手動輸入 CSS 和 Javascript 也不太實際，所以並沒有想過將這功能實作出來。

## 實作

但，這一切在 AI coding 幾乎完全取代我手工寫程式之後，就變得是舉手之勞的一件事。首先，之前就已經實作了在網頁載入後，啟動客製化 CSS 和 Javascript 的流程，包含字型變粗體，更換字體，以及各種翻譯的操作，都是透過這套實作機制來達成的。現在要額外增加的只是：在網頁載入後，先判斷該網站使用者是不是有自訂了 CSS 和 Javascript，有的話就再執行一下。

而資料輸入很麻煩的這個問題，也在整合了 AI 之後，有了更好的解法：讓 AI 幫忙看一下要怎麼產生所需要的 CSS 和 Javascript 程式碼，由它來幫忙在 EinkBro 中加上所需的程式片段。使用者甚至可以不用去了解它是怎麼達成的，只要在它完成後，測試看看有沒有達到自己想要的效果就好。

## 例子說明

舉個例子來說，平常偶爾會看一下公視的新聞網站。每次進入時，都會跳出蓋板的對話框建議登入。如果能直接將這個對話框隱藏，體驗會更好。這時，操作的流程會是：

1. 點擊 Page AI Actions
2. 點擊 Tasks
3. 點擊 Custom task... 然後跟它說：想要將這個網站上的建議註冊畫面給隱藏，把它寫到 domain config 中

由於現在 EinkBro 已經支援類似 functions 的功能給整合進來的 AI (OpenAI, Gemini, Alternative LLM) 使用，其中包括取得網頁原始內容，撈出網頁中所有連結，讀取和寫入目前網站的 personal config (CSS, Javascript snippets)。上述的第 3 步驟，在跟 AI 講完需求後，它會先試著從網頁原始碼中找到需要隱藏的元件，寫成 javascript snippet，再寫入 domain config 中。

這時，使用者只要再重新載入網頁，就知道是不是有達到需求。如果沒有的話，可以在聊天介面中多給 AI 一點資訊，看它是不是能順利修改好。整個過程使用者不需要自己輸入任何程式碼，相當直覺。

實作完這功能後，我自己也針對好幾個網站做了調整，包含把 reddit 的 use app banner 也都隱藏了，整個的使用體驗大幅提升！

###  相關連結

- https://github.com/plateaukao/ADR/blob/main/einkbro-per-site-configuration.md
- https://github.com/plateaukao/ADR/blob/main/einkbro-agent-in-chat-with-web.md
- https://github.com/plateaukao/ADR/blob/main/einkbro-agent-domain-patch-tools.md
