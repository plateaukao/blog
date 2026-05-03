+++
title = "Twitter 上的心得整理 (I)"
date = "2021-12-23T12:46:34.040Z"
description = "2021/12/16"
slug = "twitter-上的心得整理-i"
canonicalURL = "https://medium.com/@danielkao/twitter-%E4%B8%8A%E7%9A%84%E5%BF%83%E5%BE%97%E6%95%B4%E7%90%86-i-efad4a1b7f1e"
mediumID = "efad4a1b7f1e"
+++

### 2021/12/16

今天看的是 NAVER DEVIEW 的 For Better Image Translation (Papago Image/AR Translation) [tv.naver.com/v/23649339](https://tv.naver.com/v/23649339) [#NAVER](https://threadreaderapp.com/hashtag/NAVER) [#DEVIEW](https://threadreaderapp.com/hashtag/DEVIEW)  
主要在講 Papago App (Naver出的翻譯軟體) 中對於圖片翻譯的改善技術。講得有條有理，而且投影片也做得很棒！

![](/images/efad4a1b7f1e/0_sMcGr4hAbNhwZFnc)
*더 감쪽같은 이미지 번역을 위해 (파파고 이미지/AR 번역 개발기) NAVER Engineering | 노영빈/김승재 — 더 감쪽같은 이미지 번역을 위해 (파파고 이미지/AR 번역 개발기)*

這幾張 slide 很清楚地描述了圖片(in-place)翻譯的四個步驟：1. 文字認識, 2. 組成單字, 3. 機器翻譯, 4. 重繪出結果。這個演講的主題主要是在講如何改善第二步和第四步，讓翻譯效果在某些情況下可以有更好的表現。最後還有一個 section 是在講即時翻譯的技術。

![](/images/efad4a1b7f1e/0_ccuL-Ydoj4g5_qyl.jpg)

![](/images/efad4a1b7f1e/0_CaVhon7_jhN5-Kog.jpg)

![](/images/efad4a1b7f1e/0_B9m-i2bweDIHtRpz.jpg)

![](/images/efad4a1b7f1e/0_pJGRATSpuyE_2Byv.jpg)

在組成單字，句子，和段落時，如果遇到圖片是菜單、收據，或是商品包裝上的介紹時，換行的位置常常需要判斷是要當成同一行，還是是不同的項目。這邊利用了 BERT 技術來做這個判斷。從第三張圖可以看出來，有了精準的斷行分析後，在產出結果時，不會再把每行黏在一起。

![](/images/efad4a1b7f1e/0_fwlEsdXeb49gq1Ud.jpg)

![](/images/efad4a1b7f1e/0_6sEbA3tdcPcb0PVr.jpg)

![](/images/efad4a1b7f1e/0_q2ryDcLGUOn7KfFO.jpg)

再來是講到繪製翻譯結果的改善：從第一張圖可以看得出來，翻譯後的文字背景很人工，是很明顯的色塊。這裡利用了 GAN 的技術，去更有效地算出文字的背景和前景，還跟其他演算法的效果做了比較。(中間有一大段聽不懂)。

![](/images/efad4a1b7f1e/0_i3x4_8W4UQHc2zeP.jpg)

![](/images/efad4a1b7f1e/0_oZJCqu7RsWOErYNb.jpg)

![](/images/efad4a1b7f1e/0_xzIL7IlXIhM4yMQI.jpg)

![](/images/efad4a1b7f1e/0_8pYFVkts8F7OBoVe.jpg)

從改善前改善後的差異看得出來，有了很明顯的進步，幾乎看不出來翻譯的文字是貼上去的，完全跟原本的圖片背景融合在一起。

![](/images/efad4a1b7f1e/0_kkDo2vjohlTkbLC5.jpg)

![](/images/efad4a1b7f1e/0_xoKf6LEeDtaFDpu2.jpg)

最後一段講的是即時翻譯，這邊有利用到 object tracking 的技術，大概的步驟是：1. 找出代表性的 frame, 2. 進行該 frame 的翻譯, 3. 持續利用 Optional flow 的方式追蹤翻譯好的區塊並重繪。

![](/images/efad4a1b7f1e/0_wf4VcTdY-DcDmBOU.jpg)

![](/images/efad4a1b7f1e/0_cdWsoP2dfDzAXQ_H.jpg)

我試了一下用 Papago App 跟 Google Translate 來翻譯這篇演講的大綱韓文版。先不論翻譯的結果，單就呈現效果來說， Papago 的效果確實好太多了。

![](/images/efad4a1b7f1e/0_gD8KhPDvz8WaBwj9.jpg)

![](/images/efad4a1b7f1e/0__N7nVwvMEI1ApNfB.jpg)

![](/images/efad4a1b7f1e/0_s2SFoCdymc304naY.jpg)

另一個有不同背景顏色和前景顏色的翻譯繪製效果。看起來好的那個是用 Papago App 翻譯的。

![](/images/efad4a1b7f1e/0_Ymae5qYcb8-CA-AG.jpg)

![](/images/efad4a1b7f1e/0_otAzgFpGMlEOF4Xm.jpg)

### 2021/12/16

今天看的是 NAVER DEVIEW 的這篇: 開發 CLOVA App 的 Android 開發者，後來也開發了 server side 所需要提供的相關 API。 [tv.naver.com/v/23652504](https://tv.naver.com/v/23652504) 後來發現 DEVIEW 介紹頁有英文版本，所以加減看了一下。結果發現竟然不是將韓文全部翻譯過來？連標題都不大一樣 [#NAVER](https://threadreaderapp.com/hashtag/NAVER) [#DEVIEW](https://threadreaderapp.com/hashtag/DEVIEW)

![](/images/efad4a1b7f1e/0_m05drNwJYxr619ll.jpg)

![](/images/efad4a1b7f1e/0_MQJHI9yxJbciQIQi)
*Android 앱 개발자는 왜 자진해서 서버 개발자가 되었나: 클로바앱의 점진적 배포와 호환성 NAVER Engineering | 정언 — Android 앱 개발자는 왜 자진해서 서버 개발자가 되었나: 클로바앱의 점진적 배포와 호환성 관리*

這頁原本還蠻想聽的， CLOVA 機器的演進和發表日期。結果講者竟然說因為時間的關係，所以直接跳過。這不是線下預錄的影片嗎？怎麼會有超過時間的問題。如果真的超過時間，那應該一開始就不放進投影片啊。圖片中 2017 的那個 CLOVA 機器，我家裡也有一台，好懷念啊。

![](/images/efad4a1b7f1e/0_vqG3a76FvZEkCQKN.jpg)

這個講者的投影片特色是，文字一堆，而且塞得很滿。這張算是還好的，因為至少中間是圖，而且很像是手繪的。這應該不是 designer 畫的吧？這頁也是少數我比較聽得懂的。後來在講怎麼設計 server side API，確保在不同機器間可以有不同的相容性之類的內容，我全都聽不懂。

![](/images/efad4a1b7f1e/0_AdR5NynrPcNEV48_.jpg)

常聽到的問題：這些真的都是你一個人開發的嗎？  
回答：幾乎是。

![](/images/efad4a1b7f1e/0_UUSoYTIWkWYyMUgf.jpg)

為什麼沒有使用 RN 或是 Flutter 之類的技術？  
因為有要串接藍牙，而且還有一堆機器，不同的 OS，可能會有很多底層要串接的，所以很難不用系統原生的 SDK 和 Kotlin 還有 Siwft。

![](/images/efad4a1b7f1e/0_0vDoA3LQs6D6TOYH.jpg)

原以為會聽到更多 APP 層面的內容，但比較多著墨在 API 的設計上，一直在講 json schema，和怎麼使用。再加上每一個畫面都充滿了文字，講沒幾句就換下一頁，實在是很難跟上他的演講。等聽力好一點後再回來聽一次看看。

### 2021/12/15

今天聽的是 NAVER DEVIEW 的影片 Replacing a natively developed app with Flutter (One year of applying Flutter to Naver Blog App) [tv.naver.com/v/23649861](https://tv.naver.com/v/23649861)

![](/images/efad4a1b7f1e/0_bYgkSMcp62D0V3SR.jpg)

![](/images/efad4a1b7f1e/0__gDFSBXdSFryNpqT)
*네이티브로 개발 된 앱을 플러터로 바꾸고 있습니다. (네이버 블로그앱에 플러터 도입 1년 NAVER Engineering | 김승원 — 네이티브로 개발 된 앱을 플러터로 바꾸고 있습니다. (네이버 블로그앱에 플러터 도입 1년의 과정)*

之前案子也有用 Flutter 開發，剛好可以參考他們導入的經驗。他們的 App 是原先就有 Native 的版本，然後不斷地利用 Add-to-app 的方式局部加入用 Flutter 開發的模組。下面兩張圖就是 Native, Flutter 混用的畫面，有在 Native 畫面上顯示 Flutter 元件的場景，也有兩種型式的全畫面互相切換的場景。

![](/images/efad4a1b7f1e/0_97XHiIPWGZ_BO1fp.jpg)

![](/images/efad4a1b7f1e/0_3sbfIIqoXHiAXBPw.jpg)

有提到某些元件是 Native 上才有的，所以在 Flutter 的實作上，會利用 platform-view 內嵌在 Flutter 的畫面中。

![](/images/efad4a1b7f1e/0_KA7u4kW0iiiIT5Hx.jpg)

Android 和 iOS 的原生元件長得不一樣，在 Flutter 上一直有爭論是不是要在 Flutter 上刻跟原生長得很像的元件。後來他們團隊討論的結果，自己開發在 Blog App 上統一的，比較中性的 UI 元件。

![](/images/efad4a1b7f1e/0_gTOZmWn-_XSsMazH.jpg)

5.4 提到的是他的一些感想，這頁的內容比較有收穫。目前都是每個畫面由同一個人做，如果能兩個平台各一個人一起做的話會更好。Add-to-app 的資訊比較少，做起來，在實作上或跟 Native 連動上並不容易。還提到個人未來發展的相關考量。

![](/images/efad4a1b7f1e/0_671D7BoMBY7XO96l.jpg)

5.5 講到哪些案子和怎樣的團隊適合用 Flutter 開發專案。主要有說到以內容消費為主的 App (像 Blog App 就是)，或是 UX 體驗大於複雜的商業邏輯(或很強調服務性能的)。或是在設計上，有很多 custom UI 的 App 也很合適。還有談到團隊成員的意願和能力也很重要就是了。真的。

![](/images/efad4a1b7f1e/0_etUrB1lwG2FKfZTt.jpg)

### 2021/12/14

今天看的是 NAVER 在 2020 東京奧運時直播運用到的 NAVER LIVE CLOUD 介紹 ([tv.naver.com/v/23651957](https://tv.naver.com/v/23651957))。簡單來說，流程大致上可以分為”發送訊號”，”中繼”，”生產”，”傳送”，”播放”等步驟。 [#DEVIEW](https://threadreaderapp.com/hashtag/DEVIEW) [#NAVER](https://threadreaderapp.com/hashtag/NAVER)

![](/images/efad4a1b7f1e/0_MSBK8sTX-xb4SwK2.jpg)

![](/images/efad4a1b7f1e/0_l5OYVr_XRnyIpfz3)
*https://tv.naver.com/v/23651957*

[**도쿄는 무관중, 네이버는 무한관중. 라이브로 함께한 2020 올림픽**](https://tv.naver.com/v/23651957)

[NAVER Engineering | 노혜성 — 도쿄는 무관중, 네이버는 무한관중. 라이브로 함께한 2020 올림픽](https://tv.naver.com/v/23651957)

前三個步驟都還是一對一對關係，但後面兩個步驟就會是一對多，或是需要傳送到無限多的使用者去播放內容。

![](/images/efad4a1b7f1e/0_wRB3gGJ7ihX5aC0m.jpg)

有趣的一點是，他有提到不同直播性質的活動，人員的流動模式也會有所不同：購物直播的話，會在開播時衝很高慢慢下降；運動比賽的直播的觀看人數會逐漸上升，並在不同局數休息間有起伏；新聞類直播的話，則是從頭到尾都會維持在一定的水準。這對於在安排 server 上，其實會有所影響。

![](/images/efad4a1b7f1e/0_57DkdN6ebivOIUep.jpg)

![](/images/efad4a1b7f1e/0_qaD8Pt4TxgETEGcd.jpg)

![](/images/efad4a1b7f1e/0_py_flMr5-5SYRfss.jpg)

關於直播的流量主要分為兩種，一個是會經由 CDN 的影像播放；另一個則是播放時， Player 端需要用到的一些資料傳輸，必須呼叫到後台的 Server API。(然後後面有些聽不懂)

![](/images/efad4a1b7f1e/0_eo-R16hRKkZyfHxH.jpg)

關於直播時遇到 traffic 突發狀況的應對策略階段：  
1: 由國內 CDN，追加 Global CDN  
2: 拿掉 Player 中的高畫質選項  
3: Step 2 之前已經在看高畫質的觀眾，改變其觀看的畫質  
4: 為保障已經加入在觀看的觀眾，不再接受新觀眾進入直播

![](/images/efad4a1b7f1e/0_gH3792lHSv5H0v7H.jpg)

有提到在 Player 端針對 QoE 有做哪些資料的 monitoring，其中包含使用的設備，網路環境，播放初始時間長度，buffering的時間等等。

![](/images/efad4a1b7f1e/0_91D8kpEt1pI24sku.jpg)

最終，很酷的是 NAVER 招募資訊竟然是寫成 gitbook 放在 [gitbook.io](http://gitbook.io/) 上！ [naver-career.gitbook.io/kr/service/ete…](https://naver-career.gitbook.io/kr/service/etech)  
等 conference 有興趣的影片看得差不多了，應該要來看一下他們的招募內容都寫了些什麼。

### 2021/12/12

今天聽的是 NAVER Live Commerce team 的演講 [tv.naver.com/v/23651510](https://tv.naver.com/v/23651510) 分享在疫情期間，針對遠端工作建立起來的工作文化。很多內容其實在非疫情期間也很適用就是了。影片中針對 LIVE Commerce 的服務只有稍稍介紹一下而已，第一張照片倒是讓我學到了什麼是 CBT (封測)和 OBT (公測) [#NAVER](https://threadreaderapp.com/hashtag/NAVER) [#DEVIEW](https://threadreaderapp.com/hashtag/DEVIEW)

![](/images/efad4a1b7f1e/0__Es0yjAircnFSBpp.jpg)

![](/images/efad4a1b7f1e/0_OzdoWE5X4WeXFU_8)
*https://tv.naver.com/v/23651510*

1. 演講稿沒有好好 review，竟然有標題拼錯的情況發生。2. KPT 跟 Scrum 的 retro 步驟差不多，只是換個名稱而已。3. 4. 利用 gather town 來模擬實際上的上班場景和進行 workshop。

![](/images/efad4a1b7f1e/0_Sd0_A4vSaD5r90fl.jpg)

![](/images/efad4a1b7f1e/0_0xaKYw8oVl1TnzdK.jpg)

![](/images/efad4a1b7f1e/0_osNdKKN2-y7ogsNk.jpg)

![](/images/efad4a1b7f1e/0_tEisseXhH4jBWAOl.jpg)

5. 這個蠻實用的，有講到怎麼在 IntelliJ 和 VS Code 中利用 plugin 來進行 pair programming。  
整個演講的架構還不錯，雖然長達40分鐘，但有把 key phrase 利用縮寫列出來，方便聽眾掌握整個演講的重點。

![](/images/efad4a1b7f1e/0_vByr0vxW-ZVx8dJS.jpg)

演講最後一段，利用 github API 進行 PR 的管理，也有 open source 出來讓大家參考用。

![](/images/efad4a1b7f1e/0_WscWpNrQ0fdY2KSe)

<https://github.com/withearth/deview-2021>

• • •

### 2021/12/11

今天聽的是 NAVER DEVIEW 2021 的 frontend session: [tv.naver.com/v/23652538](https://tv.naver.com/v/23652538) 介紹 NAVER 出的瀏覽器 Whale，以及怎麼為它開發 plugin。雖然 Whale 也是以 Chromium 為基礎，但它的 plugin 可以有個 sidebar 的介面，可以跟主畫面的元件互送訊息，還可以存 storage。應該要裝來看看有啥好玩的 plugin

![](/images/efad4a1b7f1e/0_MJAFED99vngRi2AK)
*https://tv.naver.com/v/23652538*

[**슬기로운 웨일앱 개발**NAVER Engineering | 김동훈 — 슬기로운 웨일앱 개발](https://tv.naver.com/v/23652538)

演講中的範例是在 instagram 網站上，顯示單一 post 時，利用 css 把右邊的留言欄隱藏，在圖片或影像左上方加一個下載的按鈕。點下去後會把資訊送到右邊的 sidebar 網頁，並存到 storage 中。

感覺這 UI 可以拿來寫個字典用用。  
[#NAVER](https://threadreaderapp.com/hashtag/NAVER) [#DEVIEW](https://threadreaderapp.com/hashtag/DEVIEW)

![](/images/efad4a1b7f1e/0_9rE6JghK4PhpNdlM.jpg)

### 2021/12/09

if(kakao)2021 竟然有 NFT 的主題，而且長達四十多分鐘，不過聽了一下，感覺是在科普 NFT，後面有一半以上的時間是在訪談數位創作者 NFT 對他們來說帶來的好處。 [https://if.kakao.com/session/50](https://t.co/Xp5zKR6Ypb)

![](/images/efad4a1b7f1e/0_vvMCtp9EQMl1WxPu)

### 2021/11/17

kakao 在網站 if(kakao) 2021 上有公開了 90 個以上的 sessions，分享他們開發中各項服務的技術。今天看了其中一部是在講如何用 android 開發 kiosk 機器，還蠻有趣的。除了講到跟一般手機上開發的差別外，也有實際提到實作面的內容。 [https://if.kakao.com/session/103](https://t.co/VerH2t59RU)
