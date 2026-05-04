+++
title = "打造 E-ink 專用的瀏覽器: Part V"
date = "2021-03-28T15:14:33.405Z"
description = "這一篇的技術成份稍微高一點點。要談到的功能，從一開始開發 EinkBro 就有想要做，但是一直找不到比較好的實作方式。在經過兩三週忙於其他的功能開發後，終於在這週找到比較恰當的切入點和相關技術的參考，得以完成心目中大致上的效果。"
slug = "打造-e-ink-專用的瀏覽器-part-v"
canonicalURL = "https://medium.com/@danielkao/%E6%89%93%E9%80%A0-e-ink-%E5%B0%88%E7%94%A8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-v-769216ef6db6"
mediumID = "769216ef6db6"
tags = ["EinkBro"]
[cover]
  image = "/images/769216ef6db6/1_LIxGqqUB2gI79A5o54oZ_w.png"
+++


### 打造 E-ink 專用的瀏覽器 (V): 閱讀模式與直排模式

這一篇的技術成份稍微高一點點。要談到的功能，從一開始開發 EinkBro 就有想要做，但是一直找不到比較好的實作方式。在經過兩三週忙於其他的功能開發後，終於在這週找到比較恰當的切入點和相關技術的參考，得以完成心目中大致上的效果。

講了一堆廢話，究竟是什麼功能呢？

#### **閱讀模式和直排模式！**

我們先從閱讀模式說起。不知道閱讀模式的人，可以看一下下面的文章介紹。這功能在兩年前由 Apple 先在 Safari 瀏覽器中推出，讓使用者可以更專心地閱讀網頁內容，不被廣告和不必要的元件(標題欄，底部欄，側邊欄位等)干擾。

[iOS上Safari瀏覽器新功能：啟用閱讀介面，還能變更字體與背景 | T客邦 | LINE TODAY](https://today.line.me/tw/v2/article/9PxxRK)

之後，各家瀏覽器大廠也開始推出了類似的功能。 Brave 瀏覽器在推出他們自家的 SpeedReader 功能時，有順便把市面上主要的實作都拿來做比較，有興趣的人可以下載下面的 pdf 檔來了解一下。主要比較了 Readability.js，Safari Reader View, Google Chrome DOM Distiller，BoilerPipe 和他們的 SpeedReader。

### Original Readability.js

對於這功能有了大致的了解後，要來決定一下怎麼開發 EinkBro 中的這功能。第一個想法自然是找 Readability.js 來使用；一來它是 Open Source 的，二來，許多瀏覽器的閱讀模式也是從它延伸而來的。用它的話，網路上可以找到的資源也會比較多一些。所以先上 Github 找了一個早期的版本來用。

[Kerrick/readability-js](https://github.com/Kerrick/readability-js)

把 `readability.js` 放到 Android 的 assets 目錄中，然後利用下面的方式載入檔案，塞到目前的網頁中。由於 `readability.js` 裡頭已經包含了初始化自己的程式碼，而且會把處理過的內容，直接蓋掉目前的網頁內容，所以只要載入它就等著它把畫面換成比較單純的顯示模式。

![](/images/769216ef6db6/1_LIxGqqUB2gI79A5o54oZ_w.png)

這方式實作上雖然很簡單，但是產生出來的效果卻不是很好。第一點是，很多應該不屬於主要內容的部分，還是留在畫面中；第二點是圖片的部分，通常會過大。

![](/images/769216ef6db6/1_GIEsk7R1P4UWEfH_Fbvv8w.png)

![](/images/769216ef6db6/1_Nd-Lgc5RVtavtKn1m6mJng.png)

![](/images/769216ef6db6/1_1i0miZnw3nOXyMBe-PlnOA.png)

![](/images/769216ef6db6/1_UPLrk24OA8Mf36fblLlxmA.png)
*EinkBro v8.3.1*

字型忽大忽小尚可忽略不去計較，但是該小一點的圖，大得嚇人；和一堆不必要的元素依然存在，這效果很難讓人有想閱讀下去的念頭。

### **Original readability.js + readability.css**

仔細再研究了一下 readability.js 的內容，它在處理 html elements 時，除了會刪除不必要的元素之外，也會把想要留下的元素加上特定的 class 或 id；然後它另外還有一個 readability.css 檔案，應該就是用來規範這些新加的 class 是要怎麼呈現在畫面中的。

難怪只有執行 readability.js 的話，跑出來的畫面有點慘不忍睹。

於是接下來的版本，我把 readability.css 也加進去。(也順便把 WebView 從 Java 重構成 Kotlin 檔案，不然改起來有點痛苦)

![](/images/769216ef6db6/1_Zfb3Il-qYZWsvVeYk8R6nw.png)
*Add readability.css in v8.4.2*

結果好像沒有什麼幫助。在 Medium.com 中的文章的圖片還是大得驚人。看來用原始的 readability.js 不是好的方向。(不然就是我對 javascript 和 css 太不熟了，找不出為什麼結果沒兜起來)

### crux — stand-alone library

接下來的選擇原本是想要找別人已經包好的 library，可以直接處理 html raw data，產生出可以拿來呈現用的 html，我再塞回 WebView。在測試的時候，因為也需要先 inject javascript 到現有的網頁中，拿到 raw html，不知道為什麼常常會拿不到資料。有可能有時候在網頁還沒完全被載入時我就先按了按鈕造成的。不管怎樣，這個方式還是不理想。

[chimbori/crux](https://github.com/chimbori/crux)

### readerview feature from Mozilla Mobile

在開發的過程中，我主要拿來比較閱讀模式效果的 reference app 分別是 Brave Browser 和 Firefox。Brave 在前面的 pdf 中有提到，它們的作法是在畫面還沒有真的繪製之前就可以先處理，速度會比其他的方案快；但缺點是，它的作法相對上也比較複雜，我不見得能夠比照辦理。

所以，我去找了 Firefox App的原始碼來看(早該這麼做了)。原來 Mozilla 也有把它們的原始碼放在 Github 上。而且針對 Readability 的改良版也特地獨立成一個 repository 開發。

[mozilla/readability](https://github.com/mozilla/readability)

一開始我很開心地拿了這版本來套用。但又犯了一開始就犯的錯誤。javascript 只處理了資料的去留，但是真正呈現的部分還是需要對應的 css style file 來輔助才行。於是我找到了 Firefox Mobile App 的 repository，也找到了它 reader view 真正實作的地方。

[mozilla-mobile/android-components](https://github.com/mozilla-mobile/android-components/tree/master/components/feature/readerview)

`android-components/components/feature/readerview/src/main/assets/extensions/readerview/` 目錄下，除了有上述的 readability.js 外，它又包了一層 `readerview.js` 和輔助的 `readerview.css` 。這兩者的實作才是真正發揮 Readability 威力的地方。有興趣的人可以進去看一下。大概說就是：`readability` 把資料處理完變成 `article` object 後， `readerver.js` 會拿 `article` 中的每個資料欄位，一個個貼上特定的 `class` name，然後在 `readerview.css` 中，針對這些 class 加上 UI 的呈現方式。

因為 readerview.js 中有很多是跟 firefox App 互動的實作，我不行整個檔案直接拿來套用，所以我是抽取裡頭我需要的程式碼來用而已。抽出來的程式碼都在這兒：

[plateaukao/browser](https://github.com/plateaukao/browser/blob/my_version/app/src/main/assets/MozReadability.js#L2261)

於是，跟 Firefox App 效果幾乎一樣的閱讀模式完成了！(還有預估閱讀時間要多久，不過這數值感覺不是很準確)

![](/images/769216ef6db6/1_KSheH00hQuQmc-_gHGzHKg.png)

![](/images/769216ef6db6/1_jBl31aOE2L1kPWRDmtwNlA.png)
*v8.5.0 圖片大小正確，字型不會太雜亂*

### 直排閱讀

這功能對於瀏覽器來說，應該是個沒人想過會存在的功能。

從十幾二十年前開始有瀏覽器以來，瀏覽器就一直是以橫讀為主。而中文閱讀習慣，也漸漸地變成橫式閱讀。除了實體出版的小說有一定比例還是會用直排發行之外，連電子書有支援直排功能的也不多(最近有愈來愈多的趨勢就是了，很好)。

所以網路上找得到的文章或是討論，也大都圍繞著電子書的直排支援上。在電子書都還支援得不是很完整的情況下，何況是一般的網頁瀏覽呢？

下面是一篇對我幫助很大的文章。裡頭提到中文直排的現況，和 css style 的相關語法支援。透過文章中提到的 css style 語法，我得以初步的將網頁轉為直排。

[電子書直橫轉換有什麼困難？](https://bobtung.medium.com/%E9%9B%BB%E5%AD%90%E6%9B%B8%E7%9B%B4%E6%A9%AB%E8%BD%89%E6%8F%9B%E6%9C%89%E4%BB%80%E9%BA%BC%E5%9B%B0%E9%9B%A3-5926fa019003)

程式碼如下：

![](/images/769216ef6db6/1_ctg7IVkUJ8rFZ41E2FDnhA.png)

雖然文字部分可以成功轉為直排，而且是由左往右讀；但是畫面中的其他元素全都不受控制地散在畫面中：

![](/images/769216ef6db6/1_ptymxhUfjf_mygLb4IVg_A.png)

![](/images/769216ef6db6/1_qnP-n-pSQZQtXVB4o7FQ8A.png)
*v8.4.2*

這功能雖然加了好幾週，但是轉換後的直排效果，就要看每個網頁的特性。有的看起來走位的元素比較少，可以正常的直排閱讀；有的就跟上面的例子一樣，把畫面東一塊西一塊地蓋住，想看也看不了。

### Combo 技： 閱讀模式 + 直排

直排功能的窘境，無法直接在直排的實作上排除，因為網頁上的元件寫法千千萬萬種，不大可能針對每一種都去處理直排的應變方式。

但是，搭配上最近剛實作好，接近完美的閱讀模式，讓直排重生了！開啟閱讀模式後，畫面上的元件已經是可以完全(幾乎？)在掌控之中；這時再加上直排的處理 — 一個堪用的瀏覽器直排功能誕生了！

![](/images/769216ef6db6/1_IlGcol-MA5SOLpkOnDaLNA.png)

![](/images/769216ef6db6/1_CnbKaxh2dmQhfDb2R7UApw.png)
*v8.5.0 直排效果*

雖然還有些小地方要處理，但現在的直排模式已經可以拿來日常使用了。對於內容較多的中文網頁內容，切換成直排模式，在閱讀上的感覺會更接近於電子書。

至於內容裡夾雜的數字，桌上型電腦的瀏覽器其實有支援 css style 語法可以將其轉正；但在 Mobile 上的 WebView 目前都還沒有支援；得要自己撈出這些數字，再利用 <span> 將它轉正。以後有時間應該會再補一下這個修正。而內容中的英文單字和句子…就無能為力了。

### 參考資料

[EinkBro - Apps on Google Play](https://play.google.com/store/apps/details?id=info.plateaukao.einkbro)

[plateaukao/browser](https://github.com/plateaukao/browser)
