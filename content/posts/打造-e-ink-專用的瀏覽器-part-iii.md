+++
title = "打造 E-ink 專用的瀏覽器: Part III"
date = "2021-03-03T16:38:07.684Z"
description = "離 Part II 文章完成竟然快要一年了！我們在 Part III 裡，就來聊聊這一年多了那些新功能吧。如果你是第一次看到這系列文章，歡迎從下面兩篇先讀起。"
slug = "打造-e-ink-專用的瀏覽器-part-iii"
canonicalURL = "https://medium.com/@danielkao/%E6%89%93%E9%80%A0-e-ink-%E5%B0%88%E7%94%A8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-iii-5b0528220252"
mediumID = "5b0528220252"
+++

### 打造 E-ink 專用的瀏覽器 (III): 支援 VI 快速鍵

![](/images/5b0528220252/1_jRjy4uExMSLbeMhksIrQUg.png)
*去不了的滑雪場*

離 Part II 文章完成竟然快要一年了！我們在 Part III 裡，就來聊聊這一年多了那些新功能吧。如果你是第一次看到這系列文章，歡迎從下面兩篇先讀起。

[打造 E-ink 專用的瀏覽器: Part I](https://danielkao.medium.com/%E6%89%93%E9%80%A0%E4%B8%80%E5%80%8B%E9%9B%BB%E5%AD%90%E6%9B%B8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-i-e6c3d2e55e82)

[打造 E-ink 專用的瀏覽器: Part II](https://danielkao.medium.com/%E6%89%93%E9%80%A0-e-ink-%E5%B0%88%E7%94%A8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-ii-a7bfb98233f7)

---

### 利用音量鍵來控制翻頁

雖然下方的 bottombar 已經添加了上下按鈕，可以在不捲動畫面的情況下，往下一頁或往上一頁，但是能用來翻頁的方式，永遠不嫌多啊！最近購買的海信電子紙手機 A7 ，有特地把音量鍵做得比較偏於手機的中間，操作起來更像是一般電子書閱讀器翻頁鍵。所以為 EInkBro 瀏覽器加上音量鍵翻頁的功能，就顯得相當實用。

這功能的改動很小，只要在 `BrowserActivity` 的 `onKeyDown` 函式裡，處理音量鍵的 key event 就行了。

![](/images/5b0528220252/1_q0SEzeZmbUzcg-neOalkxA.png)

### **支援自己寫的字典 App 和支援 Multi-Window**

在看網頁時，難免會看一些外文的網站。如果遇到看不懂的單字時，通常會長按看不懂的地方，把該字選擇起來，然後在跳出的 popup window 中選擇一個適當的 action 。比方說如果有裝 Google Translate 的話，就可以選它；不然就是會按 Copy，然後跳到其他字典 App 中查尋。

如果次數少的話，這麼來來回回還不打緊；如果很頻繁的話，就會很惱人。為了解決這個問題，我另外寫了一個 naver dict ，把 Naver 字典包裝起來，讓它可以快速地幫忙查詢網頁。再透過 Multi-Window 的功能，一邊顯示 browser，一邊顯示 naver dict，達到不需要畫面跳來跳去的效果。對 naver dict 有興趣的人可以看一下下面這篇文章：

[更利於使用的 Naver 字典 App](https://medium.com/%E9%9F%93%E6%96%87%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98/%E6%9B%B4%E5%88%A9%E6%96%BC%E4%BD%BF%E7%94%A8%E7%9A%84-naver-%E5%AD%97%E5%85%B8-app-1354aaeabc30)

在 browser 中，長按文字後，跳出的選項相當多。常見的 Copy, Paste, 全選等，可能會列在最前面；自己安裝的一些 App 支援，則需要再點一次 more 才會看到。如下圖一般：

![](/images/5b0528220252/1_YAQVn5iMWeo-zr7m4dyrkA.png)

如果需要自己中意的某些選項排在前面一點的話，可以透過 override Activity 的 `onActionModeStarted` ，在裡頭把拿到的 menu 拿來改寫一下，把自己想要的選項留下。因為這功能不見得是所有人需要的。所以我會先判斷 device 上是不是已經有安裝了 naver dict，有的話才進行這操作。

![](/images/5b0528220252/1_5Quh4BK2XpTQgciKlgUf7A.png)

修改完後，menu 就只剩下我自己想要的選項：Copy 和 naver dict。如下圖：

![](/images/5b0528220252/1_Ji0TOrvby3s461AYq41SIw.png)

關於 Multi-Window 的支援，只要在 AndroidManifest.xml 中小改一下就行。

![](/images/5b0528220252/1_CBKCzIrMZRVfhzb5mLU-UA.png)

### 移除不必要的動畫

原本 browser 中許多 popup dialog 是利用 Android 的 BottomSheetDialog 實作的。 BottomSheetDialog 的好處是，會有上下滑動的感覺；但這效果在 EInk 設備上反而是種反效果，所以我把大部分的 BottomSheetDialog 都直接改成單純是 show/hide 的 View 而已，減少了畫面的閃動。

### **讓浮動 Navigation 按鈕更明顯**

browser 一開啟時，下方會有工具列。如果嫌它礙眼，可以長按 refresh 按鈕，它就會不見，變成一顆浮動的按鈕。需要時再點一下浮動按鈕展開它。浮動按鈕原本有底色，雖然有設定成半透明，但還是很礙眼。所以我把它改成只有一個圓圈，裡頭加三個點；而背景是全透明的。這麼一來，如果下方剛好有字或是圖案，就依然清晰可見。如下圖 (請見右下角)

![](/images/5b0528220252/1_f3YIJJeZCJ6Ub0zFucScpw.jpeg)

![](/images/5b0528220252/1_OntWtqmS4-uztfmCrOfuZg.jpeg)
*左圖：黑色底 / 右圖：白色底*

### **重新整理功能清單，並將字型縮放搬到第一層**

原本的功能清單有點累贅，每四到五個分成一個 tab。如果常用的不在第一個 tab，就得要多點幾下才能啟動想要的功能。所以我把它們全部排在一個畫面，並加入了我很常用的字型縮放功能。

![](/images/5b0528220252/1_Rpz7kTEtUxFH47besaIAlg.jpeg)

![](/images/5b0528220252/1_9ltMiDLLuy_ULB2W94bv0g.jpeg)
*左側：原本的設計 / 右側：新的設計*

### 更多的翻頁方式！

除了工具列的翻頁按鈕，音量鍵按鈕，我還加入了手勢翻頁(無處不翻頁啊)！目前在設定中，可以針對工具列還有浮動按鈕的手勢做功能設定。我在裡頭多了兩個選頁，讓使用者可以利用手勢執行翻頁。

![](/images/5b0528220252/1_0oC3ZUBLYzPgh6rOP0X6sA.jpeg)

![](/images/5b0528220252/1_TlRADYLnDxmDZGn2fVJwfA.jpeg)

### 支援 Vi Key Bindings

平常我會拿 13 吋的 Onyx Boox Max 3來看網頁。通常會把它放在架子上，然後連上藍芽鍵盤操作。這時如果要畫面內容上上下下，或是開新分頁，開網址，關閉分頁，切換分頁等動作時，免不了需要再用手去觸控畫面來達成。

如果是用一般 Mac 電腦的話，我都會在瀏覽器中加裝支援 Vi Key Binding 的套件，讓我省去大部分需要滑鼠操作的動作。那麼，要是在自製的 EInkBro browser 也能支援 Vi 的話那該有多好啊。

抱著這個想法，我把一些基本的 Vi Key Bindings 也都加上了！目前有支援的快捷鍵有以下這些：

**b** : open bookmarks

**d** : remove current tab

**gg** : go to top

**j** : page down

**k** : page up

**h** : go back

**l** : go forward

**o** : focus on url bar

**t** : new a tab

**vi** : zoom in font

**vo** : zoom out font

**/** : search in page

**G** : go to bottom (好像有點問題)

**J**: show next tab

**K** : show previous tab

---

雖然離第一版修改已經隔了快一年，但一直到最近幾週才有再認真的調整成適合 EInk 設備的操作方式。希望接下來能再做更多好用的功能，讓電子書設備能夠愈來愈適合看網頁。

### 下載連結與參考資料

[EinkBro - Apps on Google Play](https://play.google.com/store/apps/details?id=info.plateaukao.einkbro)

[plateaukao/browser](https://github.com/plateaukao/browser)

[EInkBro v8.0 Release](https://github.com/plateaukao/browser/releases/tag/v8.0)
