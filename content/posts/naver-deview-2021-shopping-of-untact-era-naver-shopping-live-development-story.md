+++
title = "NAVER DEVIEW 2021 — Shopping of Untact era, Naver Shopping Live Development Story"
date = "2021-12-18T17:10:27.775Z"
description = "這篇是 Naver Shopping Live Development Story 的摘要。前一陣子也有在做跟 LIVE Commerce 相關的案子，剛好這篇可以拿來參考一下別人的經驗。"
slug = "naver-deview-2021-shopping-of-untact-era-naver-shopping-live-development-story"
canonicalURL = "https://medium.com/@danielkao/naver-deview-2021-shopping-of-untact-era-naver-shopping-live-development-story-58a8a56f7f80"
mediumID = "58a8a56f7f80"
tags = ["conference_summary"]
+++

### **Shopping of Untact era, Naver Shopping Live Development Story —**NAVER DEVIEW 2021

這篇是 Naver Shopping Live Development Story 的摘要。前一陣子也有在做跟 LIVE Commerce 相關的案子，剛好這篇可以拿來參考一下別人的經驗。

[언택트 시대의 쇼핑, 네이버 쇼핑라이브 개발기](https://tv.naver.com/v/23651144)

### 主要內容

![](/images/58a8a56f7f80/1_UjsPkDYljAarxnAMfEgCiQ.png)

![](/images/58a8a56f7f80/1_7D90wR7AonJid00zTYDXmw.png)

1. 介紹從前身 Selective 演變成 Shopping LIVE 的歷史
2. 如何快速開發
3. 確實的？開發
4. 安定地營運系統
5. Shopping LIVE 的現在與未來展望

### 1. Selective Service to Shopping LIVE

![](/images/58a8a56f7f80/1_pyQo_6C8J-1kulzCq7Eu-g.jpeg)

![](/images/58a8a56f7f80/1_jNRVpqKVgPDyKZrwVfG_rA.jpeg)

![](/images/58a8a56f7f80/1_h909w6wXHdKNO9EQqzXkUQ.jpeg)

![](/images/58a8a56f7f80/1_ziS9g9-sdDb8MLnDoe_TYQ.jpeg)

Selective 一開始還沒有 LIVE 的功能，後來為了要試試 LIVE 是否有這市場，所以在兩個月內快速地開發了封測的版本 (CBT)，一個月後推出對外測試版本；然後再三個月後推出了正式版。

### 2. 如何快速開發

原來的 Selective 服務是 monolith 型式，為了要讓 LIVE 服務可以快速推出，對於 LIVE 相關的實作，是建立在原先 Selective 服務之外，但中間會有模組是去跟原先的服務溝通，將 LIVE 需要的功能提供出來。

針對主要的功能(直播、聊天、商品呈現)他們也儘量採用 NAVER 現有的技術，降低重新開發的時間。最後一張圖紫色的部分就是使用 NAVER 現有的技術。

![](/images/58a8a56f7f80/1_fgdT8PS_4h4BIiW3axUVzg.jpeg)

![](/images/58a8a56f7f80/1_R41G6GAEyY3X0Z2V-No8Hw.jpeg)

![](/images/58a8a56f7f80/1_B1pBPe_gYUduA7z0Xw_4bg.jpeg)

![](/images/58a8a56f7f80/1_tw_wTpIQh7kv0QECCCljRw.png)

下面的流程則是說明怎麼透過 NAVER 提供的方案來完成由直播方開始一場直播，到顧客觀看直播。

![](/images/58a8a56f7f80/1_77dbDVZJ4BeE76bENmu-GA.png)

![](/images/58a8a56f7f80/1_bFKhkSfyM9GnbaYn_m5tSw.png)

![](/images/58a8a56f7f80/1_34kv5arKJt9Sh3_kyE9AFQ.png)

![](/images/58a8a56f7f80/1_aLmh9mdjGAjEQdsjROEqSw.png)

![](/images/58a8a56f7f80/1_t0wDR358UKJQsuf11UDdOQ.png)

![](/images/58a8a56f7f80/1_ZBUHCFV8ga-E5KVrfpC82A.png)

![](/images/58a8a56f7f80/1_IqIeefgdCMcHcDR9XSWQMw.png)

### 3. 確實的開發

第三點比較是偏向伺服器端的介紹，這裡只稍微帶一下最終的摘要。

- monolith 的架構 → 及早開發和測試
- 主要功能切分成不同服務 → 能錯誤發生的地方隔離開來
- IDC 由原先的單一位置，改為兩個地方(?)，提高系統的可用性
- 主要功能切分成不同服務 → 在開發時可以提高生產力而且系統更為穩定
- Auto Scaling, Rate Limiting → 可處理流量爆衝的情況，擴大高可用性

![](/images/58a8a56f7f80/1_ZShdU0pPgECdJ4c6bIxARQ.png)

### 4. 安定地營運

主要是提到關於防止系統出錯的相關測試，如何進行各項功能的 monitoring，以及如果系統出錯時，怎麼樣將使用者導到說明的畫面。

### 5. Shopping LIVE 的現在與未來

![](/images/58a8a56f7f80/1_mDud-7dQTofIC3zAo457Ow.jpeg)
