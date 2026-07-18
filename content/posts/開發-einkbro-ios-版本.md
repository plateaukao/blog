+++
title = "開發 EinkBro iOS 版本"
date = "2026-07-18T10:05:45.000Z"
description = "在 Fable 5 掌舵下，Claude Code 三天內就把 EinkBro 移植到 iOS：以 Compose Multiplatform + KMP 重用大部分 Kotlin 程式碼，九成以上 Android 功能順利移植。"
slug = "開發-einkbro-ios-版本"
tags = ["EinkBro"]
[cover]
  image = "/images/開發-einkbro-ios-版本/einkbro-ios-android-side-by-side.webp"
+++

![](/images/開發-einkbro-ios-版本/einkbro-ios-android-side-by-side.webp)

兩三個月前曾用 Opus 4.6還是 4.7, 4.8 嘗試過一次，但是當時是以悲劇收場。當時 claude code 花了一兩個小時生成出一個版本，完全是慘不忍睹，只能說是生出了一個四不像。EinkBro 的 UI 和 iPhone 的介面設計相去甚遠，在放手讓 AI 自由發揮的情況下，兜出了一個不知所云的軟體，而且真正有完成的功能也是少之又少；連最表層的 UI 也沒有達到最基本的功能要求。

但這次沒想到，在 Fable 5 的掌舵之下， iOS 版本的開發在兩三天內就幾乎完成了。一方面是 Fable 5 的能力跟之前的 Opus model 比起來，完全不是同一個量級，在思考上更為全面；另一方面是，這次採取的作法比較像是漸進式的：先請 Claude Code 把所有 EinkBro 的 UI 利用 Jetpack Compose 實作在 iOS 平台上，讓我可以先看一下大部分 UI 在 iPhone 上是不是會顯得很格格不入。由於下了這個指令，Claude Code 採取的實作方式是 Compose Multiplatform + KMP。這方向大幅提高了可以重用的程式碼，而且大部分的程式依然是用 Kotlin 撰寫，然後外面再用薄薄的一層 SwiftUI wrapper 來包裝。雖然我並不會實際進去看實作的程式碼，但跟 Android app 保持同樣的程式語言，我想，對於 Claude Code 在參考實作和搬移時，應該也會省事很多才對。這三天來，很多時候請它回去參考 Android 版本的作法，相信它也少了很多轉換的 token。

UI 完成後，乍看之下，在 iOS 上似乎沒有什麼違和感，反正很多時候在看網頁時都是全畫面在操作的，原先手機是 Android 或 iOS 根本沒有差別；只有在要跟系統或是其他 App 互動時，才會有平台上的差異。既然介面看起來都已經移植過來了，下一步可以開始請 Claude Code 把畫面上的功能補起來：包含一個先能動的 WebView 畫面，以及所有工具列按鈕功能、選單中的功能，和一堆設定畫面中的功能。這些功能彼此間可能有先後順序要注意，所以 Claude Code 前後分了兩次，把所有大的項目都排序好，一樣一樣進行移植和開發。一開始，它做完一項就會問我一項；但這樣實在是太花我時間了。在經過一兩個循環境，它其實已經能利用 sim-use 驗證每一個環節要達到的完成條件；所以，我就都直接跟它說，反正有 plan 了，就一路全部開發到底，不要再問我了。因為我自己就是使用者，我可以在整個 plan 完成後，再稍微來做一下驗證就行。

第一次有機會讓 claude code 在半夜狂奔，辛勤地工作。一早起來，在 ADR 網站看到 plan 中的每一項大功能都已完成，並且寫成開發的文件。

同樣的 flow 跑了兩三輪後，幾乎大部分 Android 版本的功能都順利移植到 iOS 上，有些因為平台特性不支援的項目，過程中做了點討論，就請 Claude Code 直接拿掉；也有些是 iOS 上要採取不同的方式實作：像是 chat with web 就無法跟 android 一樣，透過 webview 的 javascript interface 來互動，只能用 native 實作聊天的畫面，事前把網頁的資訊給導出來使用。

才經過三天，iOS 版的 EinkBro 已經包含了 Android 版本的至少 9 成以上功能。透過 multicast 做區域網路的備份資料傳送和接收功能，因為要 Apple 網站的認證，所以打算整個拿掉，改成只支援 Google Drive Sync 就好。這個功能也在這兩天順手做進 Android 版本中了。再來只要再調整一下作法，讓 Android / iOS 的資料可以互通，就可以快速地讓我把 Android 上已經累積一段時間的 Site Settings / GenAI Settings 能直接無痛同步到我的 iPhone 中。

生在這個 GenAI 時代，真是太幸福了。真是已經進步到只要出一張嘴，就能心想事成。

ref: https://plateaukao.github.io/blog/posts/einkbro-ios-three-day-port/
