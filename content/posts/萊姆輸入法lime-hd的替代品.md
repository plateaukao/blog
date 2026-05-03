+++
title = "萊姆輸入法(Lime HD)的替代品"
date = "2022-03-30T17:01:51.779Z"
description = "前不久得知，在 Google Play Store 上的萊姆輸入法 (Lime HD) 被下架了。剛好前一陣子因為想要讓萊姆輸入法可以在 Android 平台的電子書閱讀器上有更好的 UI 呈現方式，所以有從萊姆輸入法在 Github 上的 repository 那兒 fork…"
slug = "萊姆輸入法lime-hd的替代品"
canonicalURL = "https://medium.com/@danielkao/%E8%90%8A%E5%A7%86%E8%BC%B8%E5%85%A5%E6%B3%95-lime-hd-%E7%9A%84%E6%9B%BF%E4%BB%A3%E5%93%81-3d3a7e8ce234"
mediumID = "3d3a7e8ce234"
tags = ["電子書閱讀器"]
+++

前不久得知，在 Google Play Store 上的萊姆輸入法 (Lime HD) 被下架了。剛好前一陣子因為想要讓萊姆輸入法可以在 Android 平台的電子書閱讀器上有更好的 UI 呈現方式，所以有從萊姆輸入法在 Github 上的 repository 那兒 fork 了一份程式碼來做適度的修改。詳情可以看我上一篇文章：

[改造 Android 上的無蝦米輸入法 — LimeHD](https://danielkao.medium.com/%E6%94%B9%E9%80%A0-android-%E4%B8%8A%E7%9A%84%E7%84%A1%E8%9D%A6%E7%B1%B3%E8%BC%B8%E5%85%A5%E6%B3%95-limehd-6e903668c21e)

在初步改完後，已經讓萊姆輸入法大幅度地瘦身了，也拿掉了(我覺得)很多不必要的功能和函式庫，讓它從原來的 10 MB 左右縮小到 4 MB。

今天是要再來說明一下到目前為止，還有做了哪些功能上的改善；技術細節的話，則是會記錄在下面。先在這兒附上最新版的連結：

[Releases · plateaukao/sweetlime](https://github.com/plateaukao/sweetlime/releases)

### 新增功能

- 將目前在打的拼字內容顯示在鍵盤正中間
- 當鍵盤型式是左右分離式，讓它的尺寸更大一些
- 長按 123 按鈕時，切換成 9 宮格的數字鍵盤
- 讓空白鍵更大，適合需要利用空白鍵送出候選字的輸入法

### 技術細節說明

#### 將拼字內容顯示在鍵盤中間

之所以會有這功能是因為，當我在使用無蝦米輸入法時，除了要看目前手上打的字母對不對，還要時不時的看一下候選字的區域，確認一切輸入是正常的。眼睛這樣子在候選字區域和鍵盤間來回，其實是比較沒有效率的。

當拼字字母可以顯示在鍵盤中間時，目光可以都注視在中間，然後輸入的字母其實用眼睛餘光就可以很精準的鍵入。這麼一來，可以省下眼睛不斷移動的缺點。

![](/images/3d3a7e8ce234/1_crY9f63X5qr1dwvsnRjbUQ.png)

![](/images/3d3a7e8ce234/1_EMpTkVi3cAspdD6vF7p4vw.png)
*左圖：原本的介面；右圖，將拼字字母顯示在鍵盤中間*

這只是我個人想要的功能，並非所有人都希望在畫面中看到礙眼的字母出現，所以我在設定畫面中加了一個選項可以開關這個功能。

![](/images/3d3a7e8ce234/1_RIQHpaCgOaXFeMMpGxkexQ.png)

第一支處理這功能的 commit 在[這兒](https://github.com/plateaukao/sweetlime/commit/972c823dba78aff4ae493a0dc71554049aa2e385)。主要的作法是把目前整個鍵盤的 layout 外層包上 `FrameLayout`，然後在正中間放上用來顯示拼字字母的 `candidateHint` `TextView` 。再來，就是隨著左上角的 candidate 有改變時，同時去改變 `candidateHint` 的字串內容。

#### **長按 123 按鍵時，切換至九宮格數字鍵盤**

這是 Github 上有使用者提出的需求。我自己也覺得這功能很實用，就研究了一下怎麼達成。最常遇到的使用場景是，在網路上常有需要輸入身份證字號的情況。通常在輸入第一個英文字後，後面全是數字。要在一長排的數字中，連續按上那麼多次，不如將畫面切換成面積更大的九宮格數字。

![](/images/3d3a7e8ce234/1_Lr095g4IxUBG-4XiiXjHpg.png)
*長按數字 123 按鈕*

![](/images/3d3a7e8ce234/1_0Xn7CfCnKTMGb3SHAkgY_A.png)
*這數字按鍵，是不是好按多了呢*

這功能的實作 commit 在[這兒](https://github.com/plateaukao/sweetlime/commit/6c5005d650d779d835330aa6a6bbd5ebb09793f3)。長按 123 按鈕時，我送出了一個新定義的 KEYCODE\_SYMBOL\_KEYBOARD。

![](/images/3d3a7e8ce234/1_Vizhja54OyLyRr660c-d7A.png)

然後在處理 onKeyboardAction 時，針對這個 keycode，將鍵盤型式切換到電話鍵盤。

![](/images/3d3a7e8ce234/1_4-75WzL8nKIqoHnqTT7a5w.png)

#### 讓空白鍵變更大

目前所有的鍵盤格式，幾乎都已經把畫面佔得滿滿的。想要把空白鍵變得更長，勢必有其他按鍵必須犧牲，做相對應的縮小。

看來看去，就只有最左邊的”閉閉鍵盤”按鈕最適合。

![](/images/3d3a7e8ce234/1_xFkRd5B2t5gBBb8WOXH5bg.png)

輸入法的程式，關於鍵盤的畫面配置，是透過定義 xml 來指定每一行要有什麼按鍵，對應到什麼 keycode，和每個按鍵的大小。萊姆輸入法因為支援了相當多不同型式的輸入法和鍵盤，所以程式裡也有許多對應的鍵盤配置 xml。

下圖以最基本的 lime.xml 來看，可以看到最後一行 (Row) 是由 **sym\_keyboard\_done**，**EN**, **,** , **sym\_keyboard\_space**，等等按鍵組成。找到這些 xml 後，只要將 sym\_keyboard\_done 的寬度從原本的 15%p 改成 10%p，然後再把 sym\_keyboard\_space 的大小由原本的 30%p 改到 35%p 就行了。

![](/images/3d3a7e8ce234/1_6kdiRekOm_kFsy308xqA_w.png)

**最近的修改**

拿掉了一堆原先功能才需要用到的 permission

![](/images/3d3a7e8ce234/1_mBzwkxkrG7SpuQcuu7bbYA.png)
