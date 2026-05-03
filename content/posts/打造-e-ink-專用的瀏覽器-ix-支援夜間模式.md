+++
title = "打造 E-ink 專用的瀏覽器 (IX) — 支援夜間模式"
date = "2021-06-04T12:40:29.413Z"
slug = "打造-e-ink-專用的瀏覽器-ix-支援夜間模式"
canonicalURL = "https://medium.com/@danielkao/%E6%89%93%E9%80%A0-e-ink-%E5%B0%88%E7%94%A8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-ix-%E6%94%AF%E6%8F%B4%E5%A4%9C%E9%96%93%E6%A8%A1%E5%BC%8F-4c39c58dac87"
mediumID = "4c39c58dac87"
+++

程式碼寫多了，總是會有技術債要還。剛開始改造 FOSS Browser 時，因為懶，而且為了求快，在把既有的 icon 改成純黑色時，都是直接用 `@android:color/black` 寫死在 xml 中。將各種對話框改成純黑白型式，或是加外框時，也都是直接用上面的黑色色碼。

現在，因為我也常常在一般手機中使用 EinkBro App，就很希望它能也提供黑色的介面，讓我在使用手機時不要那麼刺眼。但一想到要改一大堆 icon 的顏色和對話框的顏色，就覺得很麻煩，所以遲遲未動手。

昨天心血來潮，開始了這個大工程。下面列出我實作的步驟，以後如果有類似的需求，就可以拿這次的經驗當作參考。

---

### 設定符合 App 需求的 Theme

#### 使用 DayNight 的主題

原本 EinkBro 使用的主題是從 `Theme.AppCompat.Light.NoActionBar` 延伸而來的。如果想讓 App 可以跟著系統當下的設定採用一般或夜間的主題，要將主題改成像是 `Theme.AppCompat.DayNight.NoActionBar` 才可以。

#### 在主題中指定自己想要的主要顏色

以下是針對電子紙，也就是在一般主題下的設定值

```
<style name="AppTheme" parent="Theme.AppCompat.DayNight.NoActionBar">  
    <item name="android:textColor">@android:color/black</item>  
    <item name="colorControlNormal">@android:color/black</item>  
    <item name="android:colorAccent">@android:color/black</item>  
    <item name="backgroundColor">@android:color/white</item>  
</style>
```

`colorControlNormal` 是用來指定 Vector Asset 中的線條顏色。以正常主題而言，我希望它們全是純黑色的，可以在電子紙上達到最高的對比度。

#### 設定夜間主題的顏色

雖然 DayNight 的主題已經有幫忙指定夜間模式下的相關顏色變化，但因為我還是想要微調，所以，必須先建立 values-night 目錄，在底下也放入 styles.xml，然後在相同的主題名稱下，指定夜間模式的顏色選擇。

```
<style name="AppTheme" parent="Theme.AppCompat.DayNight.NoActionBar">  
    <item name="android:textColor">@color/lightGray</item>  
    <item name="android:colorAccent">@color/lightGray</item>  
    <item name="colorControlNormal">@color/lightGray</item>  
    <item name="backgroundColor">@android:color/black</item>  
    <item name="background">@android:color/black</item>  
</style>
```

針對夜間模式的字型顏色，我希望它不是完全純白的，稍微有點灰灰的感覺看起來比較舒服，所以我自己定義了一個 `lightGray` 的顏色。

---

### 原先寫死的顏色設定，改成參考 Theme 中的值

#### 先從 Vector Asset 改起

很多 icon 是我利用 Android Studio 的 Asset Studio 產生的，附檔名全是 xml，所以比較容易利用字串找到所有 `@android:color/black` 的 xml 檔，然後再利用取代的功能把它們全部換成 `?attr/colorControlNormal` 。在正常模式下，會是全黑的；在夜間模式下則是 `lightGray`。

#### 處理各種對話框和 layout xml

因為之前寫介面時的壞習慣，色碼散在到處的 layout 中；有的 TextView 也莫名奇妙地寫死了顏色。所以當一切到夜間模式時，很多對話框都是一片黑，都看不到字。

關於這一個步驟，只能一個一個修。有些 icon 並不是 xml 型式，而是png。這時，只能利用 `app:tint=”?attr/colorControlNormal”` 將它的顏色換掉。

---

### 修改程式碼

#### 開啟 App 對夜間模式的支援

新建一個 Application class，並在裡頭加入 `setDefaultNightMode`

![](/images/4c39c58dac87/1_9FTUGJSXRiinCihRTfulFg.png)

#### 動態改變主題

雖然使用到的機會不多，但總是希望當使用者從通知欄開啟夜間模式時，當下的 App 介面能馬上切換到黑色的主題。

為了達到這功能，Activity 必須要去聽 configuration change，當改變的是 uiMode時，再做相對應的處置。簡單起見，我直接將 App重啟。

![](/images/4c39c58dac87/1_14IVhNXFb-GhtRymgab2Xg.png)

#### WebView 的夜間模式

因為 EinkBro 是個瀏覽器，所以除了改改介面變黑色模式外，如果 Web 部分也可以變成夜間模式的話，會是更好的體驗。Android 官方有專門的文章在解釋怎麼做。以下我只講我的實作方式。

<https://developer.android.com/guide/webapps/dark-theme>

首先要在 build.gradle 加入 webkit 的函式庫：

![](/images/4c39c58dac87/1_6a197zWPI8oQAsOH7WA3lQ.png)

然後在 WebView 初始化的時候，根據系統的狀態和對夜間模式的支援程度來開啟夜間模式。

![](/images/4c39c58dac87/1_VRMiuTroRXCmKh0LEnq9xw.png)

```
修正：上面畫面中設定的 ForceDarkStragegy 用的是 DARK_STRATEGY_WEB_THEME_DARKENING_ONLY。這麼設定的話，其實只有少部分的網站內容會跟著變成黑色底的顯示方式。
```

```
如果把它改為 DARK_STRATEGY_PREFER_WEB_THEME_OVER_USER_AGENT_DARKENING 則大部分的網站都可以以黑底的方式呈現
```

修正後如下：

![](/images/4c39c58dac87/1_eueUSuULv48d_WK09bei7A.png)

---

看來畫面啦

![](/images/4c39c58dac87/1_xggECa9F2snIi9dCPNLGXg.png)

![](/images/4c39c58dac87/1_QOfaZy23fDDtLmRNvTKoBA.png)

### 後話

如此一下，就大功告成啦。美中不足的是，很多網站目前還沒有支援 Dark mode，所以常常還是只能看到工具列是黑的，但內容是白的。以後有時間的話，應該要再研究一下 Firefox 的 plugin — Dark Reader 是怎麼動態把大部分的網頁都變成黑色底的。
