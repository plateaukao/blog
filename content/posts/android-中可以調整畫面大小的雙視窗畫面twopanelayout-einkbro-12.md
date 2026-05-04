+++
title = "Android 中可以調整畫面大小的雙視窗畫面(TwoPaneLayout) — EinkBro (12)"
date = "2021-07-20T15:52:12.600Z"
description = "如何建立一個 Android Custom View，讓畫面中的兩個 View 元件可以透過拖拉的方式調整畫面的比例，以及將它使用在 EinkBro App 中。內容包含如何自定義 view attributes 和使用範例。"
slug = "android-中可以調整畫面大小的雙視窗畫面twopanelayout-einkbro-12"
canonicalURL = "https://medium.com/@danielkao/android-%E4%B8%AD%E5%8F%AF%E4%BB%A5%E8%AA%BF%E6%95%B4%E7%95%AB%E9%9D%A2%E5%A4%A7%E5%B0%8F%E7%9A%84%E9%9B%99%E8%A6%96%E7%AA%97%E7%95%AB%E9%9D%A2-twopanelayout-einkbro-12-5db7795ccf48"
mediumID = "5db7795ccf48"
tags = ["EinkBro"]
[cover]
  image = "/images/5db7795ccf48/1_2DXukqc4AXSXmuOSfVMDNw.png"
+++


![](/images/5db7795ccf48/1_2DXukqc4AXSXmuOSfVMDNw.png)
*可以調整畫面大小的 Custom View*

在 EinkBro App 完成全文翻譯的功能後，使用上相當愉快，能夠快速地看左右對照翻譯完後的結果。但是用著用著，又覺得有那麼一點點不順手。原因是目前的實作方式是將畫面左右各切一半，左邊是原本網頁內容，右邊是翻譯後的結果。如果我是用海信 A7 手機在看網頁的話，由於手機的形狀是長形的，會造成兩邊的畫面相當窄，只能縮小字型來提高可見的文字量。有些時候會懶得一直對照著看。這時就希望視窗大小是可以調整的：想看翻譯時，可以把翻譯畫面變大；想看原文時，可以把原本網頁的部分變寬。甚至是，如果能改成上下分割的話，就更完美了！

為了達到這樣子的功能，我先是在網路上找了找，想看看是不是有現成的元件可以幫我做到這樣子的效果。但是繞了一大圈，這看似很常見的功能，卻找不到其他人有實作過類似的元件。(不然就是我關鍵字下錯了吧)既然沒有現成的，自己寫一個 Custom View 應該也不會太困難才對，畢竟，不就一個 container 中塞兩個 View，然後再加個 drag handler 來處理畫面大小的調整。

---

### Custom View — TwoPaneLayout

為了讓這功能將來能夠應用到其他 App 中，我把它寫成一個 Custom View，然後再套用到 EinkBro 中，避免它跟 EinkBro App 綁太深，相依性太高。

首先，我建立了一個 `TwoPaneLayout` 的 class，繼承自 `FrameLayout`。在 Android 中繼承 View，如果是用 Kotlin 開發的話，可以用下面的寫法，把傳統的三個 `constructor` 都涵蓋到：

![](/images/5db7795ccf48/1_zv8M6mawg9lrfadvuCwiqg.png)
*程式碼 I*

`constructor` 中的第 23 行是處理這個 Custom View 特有的屬性。待會兒下面會有更多的說明。

第 25 行的 `initViews()` 被包在 `doOnLayout` 中的原因是：初始化 `View` 時會需要知道元件被賦予的寬跟高，所以得先等 `onLayout` 完成後才拿得到。

#### 版面配置

畫面中兩個視窗的內容是需要使用者自己設定進來的，所以沒有辦法一開始預先建立。但是為了讓畫面可以調整大小，`TwoPaneLayout` 中要顯示一個可以拖拉的元件才行；另外，在沒有拖拉時，為了避免畫面兩側的邊界不是很明顯，我還加了一條淺淺的線在中間，讓使用者稍微看得出來兩者間的界線。這兩個元件都是事先產生好的。為此，我建了一個 `two_pane_layout.xml`

![](/images/5db7795ccf48/1_7AxeY-QIzE8dXGGrcjpByw.png)
*程式碼 II*

17 行的 `ImageView` 是一個長長的方塊，平常時它的透明度是 30%。一旦使用者開始拖拉它，我會將它以及 11 行的 `View` (一條線) 都調整成全黑的，讓使用者感覺到拖拉是有作用的。

#### 新增專用的 View 屬性

這在網路上找得到的 Custom View 教學中都會看到怎麼新增。一般會是在 `values/attr.xml` 中加入自定義的 `declare-styleable element`。以下是我針對 `TwoPaneLayout` 想要提供的參數加入的內容：

![](/images/5db7795ccf48/1_tg8jpguoSCxQgGfy4DVTLw.png)
*程式碼 III*

第 4 行: 當畫面建立時，是不是直接顯示第二個視窗

第 5 行：當拖拉 drag handler 時，是不是即時更新畫面大小 (在電子紙的情況下，會需要關閉這功能，避免畫面一直閃), 還是等手放開時才更新。

第 6 行：要垂直切割畫面，還是橫向切割。

這些參數建立好後，在實際使用 `TwoPaneLayout` 時就可以在 layout xml 中指定想要的初始值。範例如下：

![](/images/5db7795ccf48/1_mAR0vImAPNRnFb-wvR9RKQ.png)
*程式碼 IV*

上面的 layout 會建立一個雙視窗的畫面，預設第二個畫面也會顯示，切割方式是橫向的(會產生左右兩個畫面，左邊是 `panel1` ，右邊是 `panel2`)；在拖拉時，畫面大小會即時更新。

#### 讀取 attrs.xml 定義好的參數

剛剛在程式碼 I 中的第 23 行有看到，初始化 `TwoPaneLayout` 時，會順便把 layout xml 中設定的參數都讀進來。

![](/images/5db7795ccf48/1_C4tLmFNZmeHWedibsHm4TQ.png)
*程式碼 V*

第 79 行會將 xml 中的參數讀出來變成一包資料，再利用 `getBoolean()`, `getInt()` 等方式將它們轉成 class 中的變數以供後續初始化的執行。

---

### 功能實作

接下來會稍微說明一下各個功能是如何實作出來的。一樣一樣來看的話，其實都不會太複雜。

#### 顯示/隱藏第二個視窗

為了要做到顯示或隱藏第二個視窗，我們要先找出使用者塞進來的兩個 `View`。這件事是實作在 `initView()` 中：

![](/images/5db7795ccf48/1_xQ_Ltjlv-QOPp60AcMjg7w.png)
*程式碼 6*

在講解 layout 時有提到，我們會事先建好分隔線(`separator`)，拖拉長方塊(`dragHandle`)，所以只要把事前建好的這些 View 排除掉(第 119 行)，剩下的兩個 View 就(應該)是使用者塞進來的兩個元件。如果數量不是 2 的話，那就天下大亂了，因為目前我沒有做任何錯誤處理。

將這兩個 `View` 分別記入 `panel1` 和 `panel2` 參數，便可以根據剛剛讀來的 `shouldShowSecondPane` 值決定是否顯示。

![](/images/5db7795ccf48/1_an3Rgnlja4bvJfU4LNDQcw.png)
*程式碼 7*

如果要顯示的話，panel 1 和 pane2 的大小在一開始會先各分一半畫面的寬度(橫向的情況)。緃向的話，則是各分一半畫面的高度(第163行，省略)。由於畫面的分割位置會隨著拖拉後有所改變，所以 `showSubPanel` 需要代入目前調整後的位置。

#### 拖拉後調整畫面大小

這部分是整篇文章的精華。在長方塊(drag Handler) 被拖拉時，會收到 Touch 相關 event。針對這些 event 我們要記錄下來相關的變化，然後反應到畫面上。

![](/images/5db7795ccf48/1_QCuxEsSnn1YeU59JWwWdMg.png)
*程式碼 8*

這邊一樣是以橫向的例子來說明。第 221 行到 228 行會先將分隔線和拖拉長方塊初始化。在橫向時，長方塊要是直的，分隔線也要直的；在緃向時，長方塊要是橫的，分隔線也要是橫的。

第 230 行開始，實作 `dragHandler` 的 `TouchListener`。當收到 `ACTION_DOWN` 時，長方塊要變成全黑的；接著，不斷收到 `ACTION_MOVE` 時，要調整 drag Handler 的位置和 `finalX` 的值。如果 `dragSize` 是設定為 true 的話，便要直接調整畫面大小(第 249 行)。當最後收到 `ACTION_UP` ，使用者手離開畫面時，再調整一次畫面大小(第 254 行).

#### 切換畫面切割方向

這功能的實作很單純，把 `orientation` 值換掉，再重新初始化就行了。

![](/images/5db7795ccf48/1_lxXHa1Bx4dJBI_Gxjoh4yg.png)
*程式碼 9*

#### 切換兩個畫面的位置

這只要把 `panel1` 和 `panel2` 對調就行。

![](/images/5db7795ccf48/1_8gUV-Gt-cIAvKvUpP76OIA.png)
*程式碼 10*

---

### 套用到 EinkBro App 中

在 EinkBro 中，預設是不會開啟全文翻譯畫面，而且在拖拉時，不要即時更新畫面。所以在 xml 中是這麼寫的：

![](/images/5db7795ccf48/1_qGEqjBIXQgEszVpPI0g2Jw.png)
*程式碼 11*

第 316 行和 321 行分別是顯示網頁的 `WebView` 和負責全文翻譯的另一個 `WebView` (和翻譯時需要的一些小按鈕)。

另外，跟翻譯相關的邏輯全部都寫在一個 `TranslationViewController` 中。從它的 `constructor` 可以看到，我們傳入了 `TwoPaneLayout` 。

![](/images/5db7795ccf48/1_c3ff9gMQfvwwbNTrw1ECiA.png)
*程式碼 12*

在收到要全文翻譯的需求時，`TranslationViewController` 會去做一大堆事情，然後利用 `TwoPaneLayout` 顯示負責翻譯的 `WebView` (第94行)。

![](/images/5db7795ccf48/1_PDibCdxi33zoq0RDmP7Ihg.png)
*程式碼 13*

在 `TwoPaneLayout` 中，這個參數在被賦值時，會同時更新畫面：

![](/images/5db7795ccf48/1_X54Uxz6kBISWgaDFqcdEwg.png)
*程式碼 14*

---

### Demo

到這裡，關於 `TwoPaneLayout` 的實作，以及它的應用就都說明完了。下面是它在 EinkBro 中操作的效果。(為了顯示 drag and resize 的功能，我特地編譯了一版是會即時更新的版本)

---

### 相關連結

[EinkBro - Apps on Google Play](https://play.google.com/store/apps/details?id=info.plateaukao.einkbro)

#### EinkBro Source Code Repository

[plateaukao/browser](https://github.com/plateaukao/browser)

#### TwoPaneLayout.kt

[plateaukao/browser](https://github.com/plateaukao/browser/blob/f8d9b137ce3f4a797e0005302aefb716bf197e95/app/src/main/java/de/baumann/browser/view/TwoPaneLayout.kt)

#### TranslationViewController.kt

[plateaukao/browser](https://github.com/plateaukao/browser/blob/f8d9b137ce3f4a797e0005302aefb716bf197e95/app/src/main/java/de/baumann/browser/view/viewControllers/TranslationViewController.kt)
