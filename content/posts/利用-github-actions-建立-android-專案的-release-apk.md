+++
title = "利用 Github Actions 建立 Android 專案的 release apk"
date = "2022-06-05T14:09:09.662Z"
description = "網路上已經有很多教學在講怎麼利用 Github Actions 建立 CI 流程，在 push commits 或是發出 pull requests 後，啟動相關的 action flow 執行 unit test 和產生 debug apk。"
slug = "利用-github-actions-建立-android-專案的-release-apk"
canonicalURL = "https://medium.com/@danielkao/%E5%88%A9%E7%94%A8-github-actions-%E5%BB%BA%E7%AB%8B-android-%E5%B0%88%E6%A1%88%E7%9A%84-release-apk-17a0b3778d5f"
mediumID = "17a0b3778d5f"
+++

網路上已經有很多教學在講怎麼利用 Github Actions 建立 CI 流程，在 push commits 或是發出 pull requests 後，啟動相關的 action flow 執行 unit test 和產生 debug apk。

而這一篇主要的重點在於，怎麼利用 Github Actions 編譯 release apk。編譯 release apk 比較不一樣的地方是，必須要指定 keystore 給它。以往在發布 EinkBro release version 到 Github 中時，我都是自己手動在電腦上執行

```
./gradlew clean assembleRelease -Pandroid.injected.signing.store.file=/path_to/browser.keystore -Pandroid.injected.signing.store.password=xxx -Pandroid.injected.signing.key.alias=xxx -Pandroid.injected.signing.key.password=xxx
```

等編譯好後，再手動在 Github 上新增一個 release 版本，將 apk 從電腦拖拉進畫面，寫寫 what’s new，再按下送出。

目前這 flow 也沒有什麼不好，只是畢竟 release version 不會天天發布，但 code 倒是有可能天天在寫，時不時都會加點新的功能進去，或是又修了些畫面，解了些臭蟲。在驗證時，一般也只會在手邊的一台機器上進行而已。

如果家裡的其他台手機或閱讀器也想要安裝還沒正式發布的版本的話，就要乖乖接上電腦，把編譯好的版本傳進去，或是利用之前改過的 Sharik APP，從別台 Android 設備上傳進去(如果那台機器剛好就在手邊的話)。

不過，既然每次改完程式碼都會 push 到 Github 上，難道就不行叫 Github 幫我在上頭也直接針對最新的程式碼產生可用的 release 版本嗎？這麼一來我隨時想要裝最新的都可以直接連到網路下載就行了。

### 實作

1. 建立 Github Actions 需要的 yml 設定檔
2. 將本地端在使用的 keystore 檔案先 encode 成 base64 的字串，當成 secret 塞到 Github 中
3. 在 yml 中指定 tasks，然後在編譯完後，指定要留存的 artifacts (以我要的場景來說，就是那個 app-release.apk

接下來我們一步步來看

#### 建立 yml 設定檔

建立一個 yml 放在 .github/workflows 下

![](/images/17a0b3778d5f/1_Tt8m3F2IhvBRXYMizfOjnw.png)

#### 將 keystore encode 成字串

在 Mac 上，執行下面的指令

```
openssl base64 < ~/browser.keystore | tr -d '\n' | tee browser_keystore_base64_encoded.txt
```

然後，將上面的 txt 文件內容，連同幾個必要的值 (alias, store password, keystore password) 填到 Github Settings 中的 Secrets 中。

![](/images/17a0b3778d5f/1_f_RtVOLfvkm7jp_l6r1PAA.png)

撰寫 yml 檔內容

![](/images/17a0b3778d5f/1_sE6KS6Mvx9CWDkwcfvWP2w.png)
*https://github.com/plateaukao/browser/blob/main/.github/workflows/buid-app-workflow.yaml*

2 行設定只有在 pull requests 和 commit 被 push 時，會被執行，

7 行是先把程式碼抓下來，

9 行把 keystore 字串還原成檔案，

15 行開始編譯。這邊會利用指令把 Github secrets 中存的值取出來使用

17 行是在編譯結束後取出想要的 artifacts。因為我只想留 apk ，所以在 21 行只寫了 apk 的路徑。

### 實際運作畫面

一切都設定正確後，就會看到 Actions 中只有要 pull requests 或是 commit pushed，都會有新的 workflow 被執行。

![](/images/17a0b3778d5f/1_BfYGoWYmp5x0Z6ZaSjO2vg.png)
*https://github.com/plateaukao/browser/actions*

如果想要取得最新的 release build，可以點畫面最上方的 Successful build，就能看到 app-release.apk 供用戶下載。

![](/images/17a0b3778d5f/1_bQwTzpRCdG-LLf-G_8sWxg.png)
*https://github.com/plateaukao/browser/actions/runs/2443113086*

目前有個小缺點是：雖然只設定了一個 app-release.apk 的 artifacts，但點擊後，其實它下載的會是一個 zip 檔。所以如果想要安裝的話，還得要先解壓縮才行。這似乎是目前 Github Actions 的限制，還沒有找到可以解決這行為的方式。

### 後記

雖然前後花了點時間才找到怎麼完成想要的功能，但不得不說 Github Actions 還蠻方便的。編譯好的 artifacts 預設會保留 90 天，也很夠使用了。如果單純只是要驗證 pull requests 的 debug apk 的話，說不定可以設定成幾天後就 expire。

另外，還找了一下是不是有 fixed url 可以取得 latest workflow built artifacts。有的話我就可以把它放在 readme.md 中，不用再層層進到 Actions 下載 artifacts。不過，目前似乎還沒有比較直覺或官方的作法。這點應該會再找時間看能不能改善。
