+++
title = "利用 Calibre Plugin 將 Netflix 字幕轉成 epub 電子書"
date = "2020-12-19T14:18:44.173Z"
description = "在前一篇文章中有提到怎麼將從 Netflix 下載下來的字幕轉成電子書(請看文章最下方連結)，不過流程很複雜，而且還有許多要打指令的地方。這一篇則是要介紹如何藉由 Calibre Plugin 來達到同樣的目的。"
slug = "利用-calibre-plugin-將-netflix-字幕轉成-epub-電子書"
canonicalURL = "https://medium.com/@danielkao/%E5%88%A9%E7%94%A8-calibre-plugin-%E5%B0%87-netflix-%E5%AD%97%E5%B9%95%E8%BD%89%E6%88%90-epub-%E9%9B%BB%E5%AD%90%E6%9B%B8-fb1401bc2584"
mediumID = "fb1401bc2584"
tags = ["電子書閱讀器"]
+++

在前一篇文章中有提到怎麼將從 Netflix 下載下來的字幕轉成電子書(請看文章最下方連結)，不過流程很複雜，而且還有許多要打指令的地方。這一篇則是要介紹如何藉由 Calibre Plugin 來達到同樣的目的。

### 安裝 Calibre

在 Calibre 官網下載最新的版本，並安裝。 (目前只支援 Calibre 5.x)

[calibre - Download calibre](https://calibre-ebook.com/download)

### 安裝 Calibre Plugin — WebVttConverter

1. 先到 [GitHub](https://github.com/plateaukao/webvtt_converter_plugin/releases) 下載最新的 WebVttConverterPlugin-xxx.zip
2. 開啟 Calibre，進到它的設定介面，點選 Plugins (畫面左下角)

![](/images/fb1401bc2584/1_Q_PXc2w-IZEMNV8-86zNqw.png)

3. 在 Plugins 視窗中，點選右下方的 `Load plugin from file` ，選擇剛剛下載好的 WebVttConverterPlugin.zip。於下方的兩個對話框中，點 Yes，和 OK。然後重新啟動 Calibre。

![](/images/fb1401bc2584/1_d3xHxz3Y_vDNIrrxEC-kZQ.png)
*Security Risk Confirmation*

![](/images/fb1401bc2584/1_5epcs6OlO02vLZikjKH9qg.png)
*Installation Success*

4. 此時，plugin 已經安裝好了，但畫面上還看不到。我們需要將它加到主畫面的工具列上。請再次進到設定中，點選第一排右邊的 `Toolbars & menus` ，在下拉選單中，選取 main toolbar。

![](/images/fb1401bc2584/1_h1vHyC-vaYLnuowaC3iMMA.png)
*WebVtt Converter at the left panel*

5. 在左邊的 panel 最下方，可以看到一個 WebVtt Convert，請選擇它，並按畫面中間的 > 讓它加入 main toolbar 中，然後按畫面下方的 `Apply` 按鈕，再按 `Close` 。這時，應該在主畫面的右上方就可以看到 WebVtt Convert 了。

### 如何操作 WebVttConverter

如果不知道要如何下載字幕的 zip 檔案，請先看文章最後的連結。

1. 下載好字幕檔後，在 Calibre 中點 WebVtt Converter 按鈕，會跳出一個設定的對話框：

![](/images/fb1401bc2584/1_yFp-I0n3XDiDd4js6Mbm-Q.png)
*WebVtt Converter Dialog*

2. 字幕 zip 檔沒有解開的話，可以點 `subtitle zip file`，從系統中選擇 zip 檔案；如果 zip 檔案有解開來的話，可以點 `subtitle directory` ，選擇該目錄。選完後，Main language 和 Second language 會跳出字幕語言的選項，請選擇想要的語言。如果只想要有一種語言的話，`Second language` 就保持 `-` 。

3. (此步驟非必須) Calibre 預設的 epub 電子書封面很醜，所以我多了一個可以自己設定字幕書封面的功能。你可以先從網路上下載想要的圖片(建議是直的，因為書本通常是直的)，然後點`Choose Cover image`按鈕。

4. 最後，再按下 `Convert` 讓它開始運作。

5. Plugin 在處理檔案時，右下角會有運作中的圖示(Jobs: 1) 在旋轉，等一切完成後，就會出現完成的對話框。

![](/images/fb1401bc2584/1_RMCM1CnvkuhPR5HDDqdVsg.png)
*Jobs running*

![](/images/fb1401bc2584/1_gmZCFNpoVhq1EvpByLz1Qw.png)
*Conversion done dialog*

6. 關掉對話框，就可以雙擊生成的電子書起來看看效果囉。下面是 Calibre 內建的 e-book viewer 大概會看到的樣子。

![](/images/fb1401bc2584/1_Rlf4lhpni6QbKBvIyaxWnA.png)

---

將轉完的電子書，一字排開，真是賞心悅目啊~

![](/images/fb1401bc2584/1_VyeEjMdub1rPJbrLynlBTg.png)

---

[如何將 Netflix 上的字幕檔轉成 epub 電子書](https://danielkao.medium.com/%E5%A6%82%E4%BD%95%E5%B0%87-netflix-%E4%B8%8A%E7%9A%84%E5%AD%97%E5%B9%95%E6%AA%94%E8%BD%89%E6%88%90-epub-%E9%9B%BB%E5%AD%90%E6%9B%B8-bd2c78cb1694)

[Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en)

[Netflix - subtitle downloader](https://greasyfork.org/en/scripts/26654-netflix-subtitle-downloader)
