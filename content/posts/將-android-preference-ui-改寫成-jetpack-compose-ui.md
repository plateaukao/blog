+++
title = "將 Android Preference UI 改寫成 Jetpack Compose UI"
date = "2023-02-26T15:44:33.703Z"
description = "Android 原本內建的 Preference UI 還算方便，只要利用 xml 定義好想要的 SharedPreference 項目並指定好相關的標題、描述、key 值，預設值，Android 就可以幫忙建立對應的畫面。"
slug = "將-android-preference-ui-改寫成-jetpack-compose-ui"
canonicalURL = "https://medium.com/@danielkao/%E5%B0%87-android-preference-ui-%E6%94%B9%E5%AF%AB%E6%88%90-jetpack-compose-ui-15a8386983a5"
mediumID = "15a8386983a5"
+++

Android 原本內建的 Preference UI 還算方便，只要利用 xml 定義好想要的 SharedPreference 項目並指定好相關的標題、描述、key 值，預設值，Android 就可以幫忙建立對應的畫面。

不過，既然導入了 Jetpack Compose，逐步地移除 xml 是必然的事，其中自然也包含了 Preference UI。Preference UI 方便歸方便，但畢竟是用 xml 描述的，不是透過程式碼來指定 key 值或預設值。一旦程式碼有任何更動，或是想要對 preference 的讀取或操作做更細微的邏輯判斷時，內建的 Preference UI 就力有未逮了，也是要在 Activity 中把一個個 preference 抽出來，然後針對它的行為做攔截，加上自己想要的動作。

如果把它全換成了 Jetpack Compose 的話，就不會有這種兩段式處理的煩惱了。只是，網路上查了一下，似乎 Android 官方並沒有出一套 Jetpack Compose 版的 Preference UI。雖然自己刻一套也不算太難，但…就覺得 Android 官方不能好人做到底嗎？

所以，對於 EinkBro 中需要的所有 Preference UI，我都自己刻了一套。其中有些需要透過顯示對話框修改值的情況，我還是保留舊的方式 — 呼叫傳統的 Dialog 起來做事。Jetpack Compose 的 Dialog 要透過 state 來 show/hide，目前我還是覺得很不習慣，情願用比較單純的傳統 Dialog。

### 架構

![](/images/15a8386983a5/1_BxUrzMlGHlDAwxdifPZhwg.png)

關於 Setting 的實作，全放在同個 pakcage 下：

![](/images/15a8386983a5/1_3AVGMdLrUD-mrrh5WbJXjg.png)

程式主要分為資料部分和介面部分；資料部分全都繼承了 `SettingItemInterface`，然後針對不同的資料，提借了額外變數。而介面部分則是對應到不同的資料，利用 `Compose` 描繪了這些資料，在畫面上負責畫出各自該有的現狀。`SettingScreen` 則是可以容納不同設定的集合，它可以吃進一個資料的列表，然後把這個列表依照各自的型態畫出來。

![](/images/15a8386983a5/1_KyhANwBf7yz3Dw-Tp95DoQ.png)

![](/images/15a8386983a5/1_bMyppBFrUEptLzndftNy_A.png)
*Data*

UI 的實作約略如下：

![](/images/15a8386983a5/1_l3wQ6fNYlkdBWIOyRXhjdw.png)
*SettingScreen*

![](/images/15a8386983a5/1_1EpvA4Hzrt4VKb0PZ48eaw.png)
*最基本的 SettingItemUi*

再由最基本的 `SettingItemUi` 衍伸出其他稍微不同的

而最上層的 `SettingActivity` 則是所有設定的 Compose UI 的入口點，它也實作了許多需要和其他地方互動的功能，像是叫起對話框，書籤管理的呼叫等。

整套開發下來，建立資料格式和刻 Ui 的時間並不長，主要的時間都是花在把各項資料從原本的 xml 中拔出來，放到建立好的資料結構中，並確保沒有塞錯，全都能正常運作。

### 完成後的畫面

前兩張看起來似乎跟原先的 xml preference 時看起來差不多，只有選項右側多了個打勾的圖案；但實際上它的實作已經是 Jetpack Compose 了。一旦設定介面是由程式碼所建立起來的，它的彈性頓時變得很大：能夠在不同的畫面寬度下，很輕易地呈現不同的效果。

手機上，因為畫面較窄，所以用類似原本 preference screen 的方式條列式呈現；如果是在平板或閱讀器上，因為畫面比較寬，就可以改為雙列的方式顯示。大部分的設定畫面也因此可以在一個畫面中全部看得到，不再需要捲動畫面。

![](/images/15a8386983a5/1_jMHnzA4jKiB83eNbZb0_jg.png)

![](/images/15a8386983a5/1_PLvb-rnSpQqf_iSuo9MlYQ.png)
*正常在手機大小上的顯示畫面*

![](/images/15a8386983a5/1_lYS0m7lEh3ymTEu881Ut-A.png)

![](/images/15a8386983a5/1_v0_TMe8hhfI92vxUu9ahpA.png)
*當設備畫面大於一定寬度時，會採用雙列方式呈現，更加節省畫面的使用，一次能顯示更多項目*

對於需要跳出對話框修改設定值的項目，也整合了原生的對話框，避免需要在程式中多出一堆判斷是不是要顯示對話框的狀態。

### 相關連結

[Comparing v9.15.0...v9.16.0 · plateaukao/einkbro](https://github.com/plateaukao/einkbro/compare/v9.15.0...v9.16.0)
