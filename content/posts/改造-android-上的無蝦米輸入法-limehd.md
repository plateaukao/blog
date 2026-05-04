+++
title = "改造 Android 上的無蝦米輸入法 — LimeHD"
date = "2021-06-19T08:06:40.727Z"
description = "從開始用手機以來，中文輸入法就一直是使用 LimeHD 加上嘸蝦米的字根檔。由於用習慣了，對於它一直沒有什麼新功能也不是很在意。不過，在這兩年，使用電子紙設備的時間愈來愈多，所以開始有了想要改造它的念頭。"
slug = "改造-android-上的無蝦米輸入法-limehd"
canonicalURL = "https://medium.com/@danielkao/%E6%94%B9%E9%80%A0-android-%E4%B8%8A%E7%9A%84%E7%84%A1%E8%9D%A6%E7%B1%B3%E8%BC%B8%E5%85%A5%E6%B3%95-limehd-6e903668c21e"
mediumID = "6e903668c21e"
[cover]
  image = "/images/6e903668c21e/1_CMWmaQRJWVJoFFqZlaSDOg.png"
+++


![](/images/6e903668c21e/1_CMWmaQRJWVJoFFqZlaSDOg.png)

從開始用手機以來，中文輸入法就一直是使用 LimeHD 加上嘸蝦米的字根檔。由於用習慣了，對於它一直沒有什麼新功能也不是很在意。不過，在這兩年，使用電子紙設備的時間愈來愈多，所以開始有了想要改造它的念頭。

LimeHD 雖然在某些畫面塞了廣告，不過它有開放原始碼在 Github 上，所以只要稍具開發能力的話，就可以抓下來自己調整成自己喜歡的樣子。以下是這陣子以來，我針對 LimeHD 有做的修改。另外，我把自己在修改的版本改稱為 sweetlime，希望它是個有甜味的檸檬。

#### 整理原始碼

- 把原始碼版本控制輕量化
- 拿掉其他不必要的輸入法設定
- 拿掉跟 Google Drive 和 Dropbox 的整合
- 拿掉用不到的函式庫
- 拿掉廣告

#### 新增的功能

- **長按鍵盤按鈕，叫起切換鍵盤的系統介面**
- 支援 scope storage
- **長按空白鍵，叫起對話框，增加新增詞彙的功能**
- 將介面改成適合電子紙螢幕的設備
- 減少候選字，改善執行的效能

---

### 整理原始碼

[lime-ime/limeime](https://github.com/lime-ime/limeime)

#### 輕量化

一開始下載原始碼時發現，它的 Github repository 的大小竟然有 900 多MB。對於一個只有不到 10 MB的輸入法來說，似乎不成比例。仔細看了一下，很多是其他輸入法的資料，然後每次更新都會再疊加上去，造成 git repository size 太大。所以，我的第一步就是先把這些歷史痕跡刪掉，反正最終我只想留的就只有那個 customization 的自定義輸入法和偶爾不知道怎麼拼字時，得應急的注音。

重新建立一個 git 後，再來是把設定畫面中的其他輸入法選項都移除。既然是用不到的功能，留在畫面上只是增加畫面的複雜度 。

#### 移除雲端備份還原

再來，是拿掉雲端備份的功能。這功能說實在話，還蠻有用的。在用正式版 LimeHD 的時候，我也經常使用 Google Drive 的備份幫我的新設備輸入法還原無蝦米的字碼庫。不過，既然要整理，就順手把它移除了。原因是還原和備份(對我來說)並不是常常會做的事。如果真的有需要的話，可以先備份到手機端資料夾，再傳到新的設備上進行還原就好。或是，可以把手機端備份好的 ziop 檔，自行上傳到常用的雲端儲存去。等有需要時再手動下載 zip 檔，然後讓 LimeHD 從手機端進行還原。

這麼做確實會有點麻煩，但移掉這功能後，LimeHD 就可以完全不需要 internet 的權限，還可以拿掉 `android.permission.GET_ACCOUNTS` 的權限。這在現今的輸入法 app 中，應該是碩果僅存完全不需要網路功能的輸入法吧。

#### 移除無用的函式庫

原本的 dependency 有下面這麼多：

![](/images/6e903668c21e/1_s1HJvLmRYsgrzhwHKHUFQA.png)

移除後只剩下：

![](/images/6e903668c21e/1_UZ0Q1GLDvsd66PRjq3GPgg.png)

#### 移除廣告

再來是拿掉廣告模組，這樣子就完全不需要網路功能了。

經過這一番整理後，binary size 已經從 10MB 減少到小於 4MB。再來要再瘦身就會有點困難了，因為很大一部分的 size 是來自於裡頭的資料庫，包含表情字符對照，簡繁轉換對照，還有英文字典檔。

---

### 新增功能

#### 快速切換鍵盤

幫 sweetlime瘦身只是順手做，但主要目的是為了要加入一些我自己想要的功能。由於有學習其他的語言，常常會需要利用不同的輸入法 App 輸入文字：英文法文的話，習慣用 Gboard；日文的話，會用 simeji 或是 Google 日文輸入法；韓文的話則是 Naver SmartBoard。

要在不同的輸入法間切換，通常要先 focus 到文字輸入框，下拉系統通知欄，點擊通知欄中輸入法通知，再做切換。一直這麼操作很花時間。Gboard 有個功能是長按地球圖案就可以列出系統中所有安裝的輸入法。但這功能似乎沒有下放給非 Google 自家的其他輸入法。

唯一能做的就是從自己的輸入法介面中呼叫系統輸入法選單，讓使用者再自己切換過去。

```
val imm = getSystemService(INPUT_METHOD_SERVICE) as InputMethodManager  
imm.showInputMethodPicker()
```

這點 LimeHD 也有做，但步驟有點多。要長按畫面左下方的鍵盤圖案，等到 popup 畫面出來後，再按`系統輸入法`切換。這時才會跳出系統的輸入法選項。

![](/images/6e903668c21e/1_YTjtZIoxGX0utmwWYZ_kzg.png)

我的修改只是把長按鍵盤按鈕，直接變成是跳系統的輸入法選單。然後原本該要出現的 popup 畫面，則改成是長按空白鍵時出現。

#### 支援 scope storage

新版的 Android，對於系統的權限愈來愈嚴。之前只要取得讀寫 external storage 權限，就可以隨意讀取系統的外部儲存裝置的任何目錄，但現在已經不行這麼做了。

<https://developer.android.com/about/versions/11/privacy/storage>

因為我把 compileSdkVersion 和 targetSdkVersion 都改成了 30，所以舊的備份還原功能會有問題，我把它改成了使用 system document picker 的方式。

![](/images/6e903668c21e/1_B5wwpJIT2X0iu9QRx5HxSw.png)

#### 快速新增詞彙

在使用手機或平板時，常常需要輸入自己常用的電子郵件地址，這在比較新的輸入法中，都可以自動幫使用者記下這些資料，讓使用者可以快速再次輸入。但是 LimeHD 並沒有這功能，所以我幫它加了一個快速的選項，能夠自行加入常用的字串。

![](/images/6e903668c21e/1_fdoWnbzNom0hJiiGdm3jQg.png)

(在中文輸入法中)長按空白鍵後，跳出的 popup 最下方的 新增常用字，可以讓使用者加入字串。

#### 修改介面

除了一般的手機和平板外，我還有許多 Android 的電子書閱讀器，通常只有黑白畫面，而且對比度不好，更新頻率不高。對於這行設備來說，動畫效果和大幅度的更新畫面內容都是不好的。為了讓 sweetlime 也可以適用於電子書閱讀器，我把按鍵的 layout 做了修改。只剩下外框；點擊後的效果也改為只加粗外框。

![](/images/6e903668c21e/1_CMWmaQRJWVJoFFqZlaSDOg.png)

#### 改善執行效率

在電子書閱讀器上 CPU比較弱，而且檔案系統的讀取速度(可能)也比較慢，所以如果能減少 IO 的話，會讓效能有所提升。

無蝦米以重覆字不高著名，所以其實在輸入時，並不需要從資料庫中取出太多候選字。因此，我稍微改了一下 sweetlime 的參數，讓它不要做太多白工。

![](/images/6e903668c21e/1_Duqn3yr8zXXBa-eTxAR6Bw.png)

#### 後話

雖然 LimeHD 很久沒有新功能了，但該有的功能都有了，經過一番調整後，還是可以再戰十年的。關於上述的所有修改，已經有編譯成 apk 放在下面的 github 連結中，有興趣的人也可以裝來試試看。

---

### 相關連結

**下載連結**

[Releases · plateaukao/sweetlime](https://github.com/plateaukao/sweetlime/releases)

**原始碼連結**

[plateaukao/sweetlime](https://github.com/plateaukao/sweetlime)
