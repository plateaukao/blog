+++
title = "如何上架 Android App 到 F-Droid"
date = "2021-04-10T14:20:33.244Z"
description = "其實 F-Droid 上的文件也寫得蠻清楚的了，只是這兩週花了點時間在做這p件事，想說還是記錄一下，以後如果打算再發佈其他 App 時，可以再回來參考一下。這篇文章會先提一下什l麼是 F-Droid ，跟為什麼我要把 App 發佈到它上頭。接下來才是本文重點的 How-to…"
slug = "如何上架-android-app-到-f-droid"
canonicalURL = "https://medium.com/@danielkao/%E5%A6%82%E4%BD%95%E4%B8%8A%E6%9E%B6-android-app-%E5%88%B0-f-droid-952cc3ce6882"
mediumID = "952cc3ce6882"
+++

![](/images/952cc3ce6882/1_zhT1QmtbeKceJuD5ttes3g.png)

其實 F-Droid 上的文件也寫得蠻清楚的了，只是這兩週花了點時間在做這件事，想說還是記錄一下，以後如果打算再發佈其他 App 時，可以再回來參考一下。這篇文章會先提一下什麼是 F-Droid ，跟為什麼我要把 App 發佈到它上頭。接下來才是本文重點的 How-to 內容。

### 什麼是 F-Droid

白話來說，就是個自由開源軟體的 Google Play Store 。官網上的簡介是這麼寫的：F-Droid 是一個可在 Android 平台上安裝的自由與開源的應用程式目錄，可供妳輕鬆瀏覽，安裝並持續追蹤裝置上應用程式的更新。

Google 已經有推出了 Play Store，為什麼還會冒出 F-Droid 呢？Google Play Store 雖然方便，但要上架 App 必須要符合它訂下的各種規範；而且 Play Store 上的大部分 App 為了賺錢，或是為了保護自己的利益，都不會把程式碼釋出，而且還會在 App 中塞了一大堆追蹤使用者行為的實作，或是到處顯示廣告。

對於部分比較在意個人隱私，或是在遇到 App 不好用時，更想自己動手東改西改的人來說，如果使用的 App 是 Open Source的，在使用上可以有更大的彈性。另外，有些 Android 設備則是原本就沒有內建 Google Play Store，需要有其他比較方便的下載 App 方式。

不過，跟 Google Play Store 上的兩三百萬個 App 比起來，截至 2021 年 2 月，F-Droid 上只包含了約 3,800 個應用程式。少歸少，夠用就好，上面還有些軟體是 Google Play Store 上無法上架的好用工具，這就待大家自己去挖掘了。

### 為什麼我要發佈 EinkBro App 到 F-Droid

EinkBro 是一個專門開發給電子書閱讀器使用的瀏覽器。電子書閱讀器大致可以分成封閉式和開放式的系統。封閉式就是出廠時設備上有什麼軟體，就只能使用那些軟體，無法再自行安裝其他的程式。開放式則是可以透過某些方式安裝 Android App。但並不是所有的開放式閱讀器都支援 Google Play Store，這類的閱讀器使用者要自己想辦法下載 apk 再安裝，或是先找到一個專門在幫忙下載安裝 App 的軟體，省掉這些麻煩。

EinkBro 剛上線到 Google Play Store 時，最常被問的就是，有沒有上架到 F-Droid，以及是不是可以支援 Reader Mode。

所以，在完成 Reader Mode 之後，也花了點時間把它上架到 F-Droid，讓更多人可以方便地安裝和升級。

---

### 怎麼進行

為了讓開發者可以順利的上架 App 到 F-Droid 上，F-Droid 官方已經有寫了蠻完整的文件，詳細方法可以看一下面這篇文章

[Submitting to F-Droid Quick Start Guide](https://f-droid.org/zh_Hant/docs/Submitting_to_F-Droid_Quick_Start_Guide/)

再參考這篇

[How to publish your apps on F-Droid?](https://dev.to/sanandmv7/how-to-publish-your-apps-on-f-droid-2epn)

再來會介紹我操作的步驟和一些注意事項。這些內容可以縮短 merge request 時跟 F-Droid 維護者來來回回的修正。我大約花了一週才完成，有興趣的話，可以點文章最後面的 merge request 來看一下血̸淚̸史̸內容

- F-Droid 的程式碼都是放在 [Gitlab](https://gitlab.com/) 上，所以需要先建立自己在 Gitlab 上的帳號
- git clone fdroidserver 和 fdroiddata 這兩個 repo
- 在 fdroiddata 中，加入自己 fork 好的 repo 為 remote branch
- 在 /metadata/ 目錄中，建立屬於自己 app 的 yml 描述檔。以 EinkBro 來當例子的話，我建立的文件是 ，內容如下

![](/images/952cc3ce6882/1_wrW2OYxVMpwXp8_gw59GxQ.png)

官方文件有寫到，可以利用 `fdroid import --url github_repo app_dir` 建立 yml 檔。但我一直試不成功。所以後來是抓 template 下來改的。抓 template 的方式是：

```
wget -O metadata/info.plateaukao.einkbro.yml https://gitlab.com/fdroid/fdroiddata/raw/master/templates/app-full
```

template 中的欄位很多，但其實只要填我上面的那些欄位就行了。其他的資訊，F-Droid maintainer 會叫你寫在 fastlane 的相關文件裡。

- 在自己的 App Github repo 建立 fastlane 的相關訊息。fastlane 要寫哪些資料可以參考我在文章最後附的連結，主要是類似 Google Play Store Listing 中要填寫的資料。

![](/images/952cc3ce6882/1_dXxInQOaPRMZ2gYCqR0Sag.png)

- 將版本的 changelog 寫在特定的檔案，然後設定在 yml 檔案中，讓 F-Droid 可以讀得到
- 將使用到的權限要求寫在 fastlane 的文件中, 並解釋用途為何

---

### 後記

順利的話，在Gitlab Merge Request 中跟 F-Droid maintainer 來回溝通幾次，應該對方就會幫你 merge 描述檔到 fdroiddata repo 中。接下來，大約要等 2 到 4 天才會看到自己的 App 出現在 F-Droid 網站上或是 F-Droid App 中。

雖然整個流程沒有像 Google Play Console 那麼方便，審核也是人工的，而且 deployment 要等的時間是以天來計算，但可以因此造福到不同族群的使用者，還是件好事。

---

### 參考連結

#### EinkBro @ F-Droid

[EinkBro | F-Droid - Free and Open Source Android App Repository](https://f-droid.org/en/packages/info.plateaukao.einkbro/)

#### Merge Request on Gitlab

[add app with id info.plateaukao.einkbro (!8700) · Merge requests · F-Droid / Data](https://gitlab.com/fdroid/fdroiddata/-/merge_requests/8700)

#### Fastlane Data example for EinkBro

[plateaukao/browser](https://github.com/plateaukao/browser/tree/main/fastlane/metadata/android/en-US)
