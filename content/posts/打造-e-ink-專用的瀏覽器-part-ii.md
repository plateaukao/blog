+++
title = "打造 E-ink 專用的瀏覽器: Part II"
date = "2020-04-12T10:38:15.565Z"
description = "開始來改造 Browser 吧"
slug = "打造-e-ink-專用的瀏覽器-part-ii"
canonicalURL = "https://medium.com/@danielkao/%E6%89%93%E9%80%A0-e-ink-%E5%B0%88%E7%94%A8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-ii-a7bfb98233f7"
mediumID = "a7bfb98233f7"
+++

### 打造 E-ink 專用的瀏覽器 (II): 增加按鈕、桌面模式、改善 UI

開始來改造 Browser 吧

![](/images/a7bfb98233f7/1_Wj_38xUoGa66K0P3aQWwPA.png)

### 增加 PageUp / PageDown 按鈕

大部分的電子書閱讀器雖然有 A2 模式可以啟動，加速畫面繪製的速度，但是**如果能讓瀏覽器跟看書一樣，是以頁為單位往上或往下前進的話**，還是比較方便，而且會造成的殘影也會少一些。

目前 Onyx Boox 系列內建的瀏覽器有做方向鍵在畫面左下方，但點擊時上或下時，畫面還是以捲動的方式往上或往下一頁。

所以，第一個要新增的功能是為 FOSS Browser 加上翻頁的按鈕，成果如下圖標示。

![](/images/a7bfb98233f7/1_Pf99tMqcEKlIvN9xXlSYQw.png)
*PageUp /PageDown 按鈕*

要更改的程式碼不多，主要是幫 `NinjiaWebView` 加上 `pageDownWithNoAnimation` ，然後在翻頁時呼叫它。

```
public void pageDownWithNoAnimation() {                                        scrollTo(0, getScrollY() + getHeight() / 5 * 4);                              }
```

[modify scroll to bottom logic; modify button position; fix injectCSS ... ·…](https://github.com/plateaukao/browser/commit/0aa9441f0d2a8ba727e7e9b750d936cb89efe75f#diff-5141941817caa5178f6f95485c7a39c5R324)

往上翻頁的按鈕也比照辦理就行了。

有了上下翻頁的功能後，另一個很常要用到功能是跳到網頁的最上方。這個功能我把它加在長按 PageUp 按鈕。

```
public void jumpToTop() { scrollTo(0, 0); }
```

### 支援 Desktop 模式

目前的 E-ink 設備，6吋，7.8吋，一直到 10 吋，13 吋都有，除了6 吋有點太小，其他尺寸蠻適合用來瀏覽 PC 版的網頁，所以，讓 Browser 可以切換 Desktop 模式是很重要的。

在 reddit 上看到，在很早期的 FOSS Browser 是有支援這功能的，只是在後來不知道為什麼，就把這功能拿掉了。有了這資訊後，當然是先回去翻翻 commit，找原本的實作在哪裡，看有沒有機會直接再搬到最新版的程式碼中。

經過一陣搜尋後，發現在是 v5.6 升級到 v5.7 時，將它拿掉的(目前最新版是 v6.9了)。在稍微參考原先的作法後，我把 fast toggle 選單中的「反轉顏色」的功能，改成新版的 Desktop 模式的按鈕。對 E-ink 設備來說，應該不會有人想把底色換成全黑的吧。

[### v 5.6.1 (WIP) · scoute-dich/browser@95ca4aa](https://github.com/scoute-dich/browser/commit/95ca4aa0b7778e466d19d2c079638ba10a4c2c32)

如下圖所示，當長按三個點時，會跳出 fast toggle 的選單，紅色框選的按鈕就是新加的 Desktop 模式。點選後再按 RELOAD 就可以看到 PC 版的網頁了。

![](/images/a7bfb98233f7/1_WCWl2nokveuEU4aqkw09pg.png)

實作其實不難，只是塞一個類似 PC Browser 的 user agent string 給 WebView 而已。如果想離開 Desktop 模式，只要再把原本的 user agent string 重新設定回去就行。

### 改善瀏覽器 UI 的配色

FOSS Browser 原本的 icons 設定的顏色都是用 `"?android:attr/textColorSecondary"`。這是一個近似黑色的顏色，在 E-ink devices 上看起來灰灰的，視覺效果不是很好，所以全部都改成了黑色，讓這些 icon 在電子書上更顯眼。

[change icon color to pur black or white · plateaukao/browser@621a187](https://github.com/plateaukao/browser/commit/621a1873a47c550a7c0ec155416705414937b2ec)

### 顯示目前分頁數

FOSS Browser 雖然可以讓使用者開啟多個網頁，而且可以叫出預覽畫面，在不同的網頁間切換，但在正常模式下，看不出來目前有多少分頁；也不曉得點了連結後，是在原本的分頁開啟，還是又開啟了一個新的分頁。

如果能夠在下方把目前分頁數顯示出來的話，就能避免這樣子的問題。

![](/images/a7bfb98233f7/1_Oeih3dRi4_nP2sFwY1mIZg.png)
*修改前的功能列*

![](/images/a7bfb98233f7/1_2nqW3uxTyJL9LOWQogRJNw.png)
*修改後的功能列*

這修改也很容易，只要把原本的 icon image 換成隨便一個 checkbox 的圖案，然後在它上頭蓋上一個 `TextView` ，這個 TextView 在網頁數有增加時，都更新一下數字就可以了。

[add a tab count icon on bottom bar · plateaukao/browser@3a409e9](https://github.com/plateaukao/browser/commit/3a409e9b8e1c2a31cfb7839bfa340bbcb3938060#diff-3ebef0e9cb66c5269c8e14905f7a8402L2154)

### 系列文章

[打造一個電子書的瀏覽器: Part I](https://medium.com/@danielkao/%E6%89%93%E9%80%A0%E4%B8%80%E5%80%8B%E9%9B%BB%E5%AD%90%E6%9B%B8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-i-e6c3d2e55e82)

### 有用的連結

如果想裝來試試的人，可以安裝 Google Play Store 上的版本，或是下面已經編譯好的版本。

[EinkBro - Apps on Google Play](https://play.google.com/store/apps/details?id=info.plateaukao.einkbro)

[plateaukao/browser](https://github.com/plateaukao/browser/releases/tag/v7.0)
