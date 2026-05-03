+++
title = "LimeHD 在手機升級上 Android 13 後的小問題"
date = "2022-08-18T13:42:02.520Z"
description = "在 LimeHD 中有個功能是：如果懶得打字輸入的話，在候選列右邊有個麥克風圖案，可以點擊它啟動 Google Voice Input，直接換成語音輸入。這個功能從以前到現在都 work 得好好的。"
slug = "limehd-在手機升級上-android-13-後的小問題"
canonicalURL = "https://medium.com/@danielkao/limehd-%E5%9C%A8%E6%89%8B%E6%A9%9F%E5%8D%87%E7%B4%9A%E4%B8%8A-android-13-%E5%BE%8C%E7%9A%84%E5%B0%8F%E5%95%8F%E9%A1%8C-daf937ead2c4"
mediumID = "daf937ead2c4"
+++

在 LimeHD 中有個功能是：如果懶得打字輸入的話，在候選列右邊有個麥克風圖案，可以點擊它啟動 Google Voice Input，直接換成語音輸入。這個功能從以前到現在都 work 得好好的。

但是，有使用者反應升級到 Android 13 它就失效了。剛好我手邊的 Pixel 4 也升級到了 Android 13，所以我稍微試了一下，發現真的是一點反應也沒有。馬上打開程式碼來看出了什麼問題。

原本的實作方式是去取得目前系統中的所有輸入法列表；一個個看哪一個是 Google Voice Input，找到後，再叫系統切換成那個輸入法。

![](/images/daf937ead2c4/1_WAa-X-k2_wllf4HMa0hpcw.png)

看到這實作方式後，第一個猜想是：Google Voice Input 換 package name 了？果然，下了中斷點來檢查 Android 13 中的系統輸入法，發現它變成別的名稱了。

```
com.google.android.tts/com.google.android.apps.speech.tts.googletts.settings.asr.voiceime.VoiceInputMethodService
```

找到問題後，要修改就容易多啦，只要再多一個 if 判斷式就可以解決。不過，原本的程式碼實在是寫得有點醜，所以就順手再小小 refactor 了一下。

![](/images/daf937ead2c4/1_jybJ35Nq9S5S-xEwqHoVLg.png)

於是乎，又順手地發布了一個版本。

[Release Release v6.8.0 · plateaukao/sweetlime](https://github.com/plateaukao/sweetlime/releases/tag/v6.8.0)
