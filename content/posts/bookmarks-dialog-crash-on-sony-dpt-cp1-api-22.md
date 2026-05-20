+++
title = "Bookmarks Dialog Crash on SONY DPT-CP1 (API 22)"
date = "2026-05-20T16:47:50.000Z"
description = "在 SONY DPT-CP1 (Android 5.1, API 22) 上修 EinkBro 書籤對話框崩潰的歷程，順便檢討讓 AI 鑽牛角尖、來回猜了八個原因才找到 reorderable 函式庫缺少 graphicsLayer 真因的教訓。"
slug = "bookmarks-dialog-crash-on-sony-dpt-cp1-api-22"
tags = ["EinkBro", "Android", "Sony Reader"]
[cover]
  image = "/images/bookmarks-dialog-crash-on-sony-dpt-cp1-api-22/claude-debug-hypotheses.jpg"
+++
好久沒有把 SONY DPT-CP1 拿出來用。想說可能又沒電了，所以把它充滿電，再寫了點內容。剛好最近在瘋狂地修改 einkbro，覺得是時候再為這台 SONY 老機器更新一下版本。
由於它真的很老了，Android 作業系統還停留在 lollipop 的年代 (5.1?)，而 einkbro 雖然有做了很不錯的向下相容了，但要我一路支援到 5.1 版本，留一堆根本沒有幾個人在用的版本確認邏輯做不同的處理，怎麼想都不是件令人愉快的事。所以，雖然有很多使用者在敲碗，我怎樣就是不想讓我的正式版還要塞一堆向下相容的程式碼。
不過，如果是自己的舊機器，自己的需求，怎樣都要來滿足一下。反正現在有免費的 claude code 可以代勞，要讓它偶爾支援一下 5.1 的 Android，也只是十幾二十分鐘的事。沒錯，讓它可以跑在 SONY 設備上，只花了十幾二十分鐘；但為了修一條 bug，倒是修了一兩個小時在找問題。這也是為什麼今天我要寫這篇文章來記錄一下，讓自己以後能記取教訓，以後讓 AI 做事時，自己要多用點腦袋，不要跟著 AI 在胡搞瞎搞，浪費我的時間。token 雖然不用錢，但我的時間可是很寶貴的。
在順利安裝上最新版的 einkbro 後，第一個遇到的 crash 是當書籤列表圖示被點擊的時候。這問題也在掌閱的設備上有發生，只是，因為掌閱閱讀器已經被廠商魔改過，根本連不到 adb，開了 usb debugging 也沒用，所以當時是愛莫能助，只能摸摸鼻子放棄使用書籤的功能。
但是，SONY 設備舊歸舊，依然可以連結到 adb 連線的，所以想抓錯誤訊息來研究是沒啥問題的。
言歸正傳，好不容易在一台可以用 adb debug 的設備上重現這個問題，自然起手式是叫 claude code 把 log 抓回來好好研究哪裡出了錯。這 log 竟然是 crash 在 native 端，而不是常見的 kotlin 程式碼。
```kotlin
F/libc : Fatal signal 11 (SIGSEGV), code 1, fault addr 0x0 in tid NNNN 
F/DEBUG : signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x0 
F/DEBUG : r0 00000000 r1 befbf7bc r2 00000000 ... 
F/DEBUG : backtrace: 
F/DEBUG : #00 pc 0008ac12 /system/lib/libandroid_runtime.so 
F/DEBUG : #01 pc 000b3de3 /data/dalvik-cache/arm/system@framework@boot.oat
```
通常如果是自己要處理這種 log 的話，我一般就束手就擒；但 AI 那麼厲害，它肯定能再往下鑽，找到可能的原因。後來發現，這個"肯定"其實也沒那麼肯定。因為它總共試(猜)了8個原因，來回改來改去，前前後後總共編譯了 16 次才總算找到真正的原因，並且把它解掉(繞過問題)。
以下是它猜測過的原因，以及嘗試過的解法。每次它都講得頭頭是道，但出來的結果就一樣會崩潰，弄得我也跟著一樣很崩潰。一路從 hardware-acceleration， vector drawable，猜到 favicon，launcher icon format。中途還牽拖，懷疑是更早之前請它調整 app pixcel density 時造成的。
![](/images/bookmarks-dialog-crash-on-sony-dpt-cp1-api-22/claude-debug-hypotheses.jpg)
最終，它終於像大夢初醒一般，去跟別的類似的 dialog，一樣樣比對是哪裡不同，發現或是想到在 reorderable 函式庫中的 `Column.verticalScroll` 是沒有 graphicsLayer 的。在沒有 graphicsLayer 的情況下，系統會用 veiwLayer 去代替，但當用了太多 viewLayer 時，可能就會因為 resource 不足，生不出 viewLayer，系統就直接崩潰在底層。
找到這根本原因後，目前是沒有打算自己跳進去 reorderable 這個函式庫去修改它，只是先繞過這個問題，把這個特別支援 5.1 的版本，拿掉書籤重新排序的功能。因為這台在操作上很慢，所以我大部分是把其他閱讀器的 einkbro 設定同步過來，而不會手動在 SONY 這台機器上加東加西的。少了排序並不會有什麼太大的不便。
整個 debug 流程如下，下次再遇到這麼亂搞的 issue，我應該都會叫 AI 先來看看這次的教訓，看它在找方法和方向時，不會再一直鑽牛角尖。
![](/images/bookmarks-dialog-crash-on-sony-dpt-cp1-api-22/debug-flowchart.jpg)



### 相關連結
https://plateaukao.github.io/ADR/#einkbro-bookmark-dialog-api22-native-crash.md
