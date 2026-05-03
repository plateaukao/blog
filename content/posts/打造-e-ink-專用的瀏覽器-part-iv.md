+++
title = "打造 E-ink 專用的瀏覽器: Part IV"
date = "2021-03-24T16:49:19.725Z"
description = "不知不覺，這系列已經來到第四篇了。雖然沒有什麼人在看，但畢竟是花了一點時間東拼西湊來的，要整理後記錄下來才是自己的東西。如果還沒有看過前幾篇的話，可以先從下面第一篇看起，因為，這篇是繞著 WebView 中的字體在打轉，跟第一篇的內容有些關聯。"
slug = "打造-e-ink-專用的瀏覽器-part-iv"
canonicalURL = "https://medium.com/@danielkao/%E6%89%93%E9%80%A0-e-ink-%E5%B0%88%E7%94%A8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-iv-effefafbbc1f"
mediumID = "effefafbbc1f"
+++

### 打造 E-ink 專用的瀏覽器 (IV): 字型

![](/images/effefafbbc1f/1_KvBG58L_-Sx9apLhgs1eHw.jpeg)
*不同尺寸的電子紙設備*

不知不覺，這系列已經來到第四篇了。雖然沒有什麼人在看，但畢竟是花了一點時間東拼西湊來的，要整理後記錄下來才是自己的東西。如果還沒有看過前幾篇的話，可以先從下面第一篇看起，因為，這篇是繞著 WebView 中的字體在打轉，跟第一篇的內容有些關聯。

[打造 E-ink 專用的瀏覽器: Part I](https://danielkao.medium.com/%E6%89%93%E9%80%A0%E4%B8%80%E5%80%8B%E9%9B%BB%E5%AD%90%E6%9B%B8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-i-e6c3d2e55e82)

#### **這次的重點是字型。先來說說字型大小。**

現在市面上的電子紙設備大大小小各種尺寸都有：從海信出的 A5 手機(5.8吋)，A7(6.7吋)，Kindle (6吋)，到 Onyx 出的 Nova3 (7.8吋)，Note3(10吋)， Boox Max Lumi(13吋)。每種尺寸都有比較合適的字型大小，如果瀏覽器可以快速地調整字型大小的話，應該是個很方便的功能。

這對 Android WebView 來說，是件很容易的事。在 WebSettings 中可以直接呼叫函式來達成。

```
webSettings.setTextZoom(100);
```

預設字型大小是 100，想要放大或縮小字型，只是改變這個數字就行。這方式雖然修改起來很快速，但是它只會調整到字型的大小，其他畫面上的元件並不會隨之放大。所以偶爾會看到放大的字體顯示超出它原本的範圍，是個稍微可以忽略的小缺點。

#### **調整字體粗細**

有些網站為了美觀，字體可能會選用比較細的，或是在呈現上把顏色調得比較淡。這對電子紙來說，在閱讀上都會帶來困擾。部分電子書閱讀器廠商(像是 Onyx) 提供較多元的系統調整方式，讓使用者可以視情況自己將字體加粗，或是調高對比度。但這並非每家廠商都有類似的設定可以修改。

所以，如果從瀏覽器本身能支援調體字型粗細和顏色的話，就能更不受 E-ink 設備本身的限制。實作這功能需要對 WebView inject javascript 。作法在第一篇文章中有提到，這篇再貼出來復習一下。將想要注入的 CSS Style 字串，先轉成 bytes ，再塞到下面的函式就可以。

```
private void injectCss(byte[] bytes) {  
    try {  
        String encoded = Base64.encodeToString(bytes, Base64.NO_WRAP);  
        loadUrl("javascript:(function() {" +  
                "var parent = document.getElementsByTagName('head').item(0);" +  
                "var style = document.createElement('style');" +  
                "style.type = 'text/css';" +  
                "style.innerHTML = window.atob('" + encoded + "');" +  
                "parent.appendChild(style)" +  
                "})()");  
    } catch (Exception e) {  
        e.printStackTrace();  
    }  
}
```

上面的作法大致上的概念是：注入 javascript，在現在的網頁中生出一個 `<style>` 的 element，裡頭有我們要的 style 描述。以加粗這個 style 來說的話，可以注入下面的內容：

```
* {  
  font-weight:700 !important;  
}
```

font-weight 可以是 100 ~ 900。詳細的說明可以參考 MDN。而 `!important` 表示，要蓋掉所有其他的設定。

[font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)

[CSS !important Property](https://www.w3schools.com/css/css_important.asp)

效果如下：

![](/images/effefafbbc1f/1_lkntehrdT8Rh40ZuogY_yg.jpeg)

![](/images/effefafbbc1f/1_J-pHUl3oKK-D2xLr_8td6A.jpeg)
*左：加粗 / 右：原始畫面*

#### 更換雲端字型

開啟 inject javascript 這扇大門後，許多事都變得可能了。換字型這件事，原本我想要做的是讓使用者可以下載字型到手機上，然後再去讀取字型來呈現。不過目前還沒有找到可以怎麼做。

網路上面的文章都只有提到怎麼將想要的字型塞到 Android 的 asset 目錄下，然後從 asset 目錄中讀取。這種方式沒有辦法解決使用者自行下載字型的情況。

既然還找不到怎麼讀取下載的字型，我又不想塞字型檔到瀏覽器 App 中，轉個念頭，不如去載入雲端字型好了。雖然每次都要載入，但至少是目前唯一可以換字型又不增加 App 大小的方法。

要載入網路字型的話，最有名的莫過於 Google 推出的 Google Font。其中包含了 CJK 字體(Chinese Japanese, Korean)，還有其他許多的選擇 (可以參考下面連結)。

[Google Fonts](https://fonts.google.com/)

目前 Onyx Boox 最新 firmware 使用的字體是細圓體；而海信手機用的則是黑體。以可讀性來說，海信的黑體比細圓體還要易讀。但其實我最想要的是明體。所以在 Google Web Font 中找了明體的字型，利用下面的 CSS Style 把網頁的字型改掉。

```
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400&display=swap');  
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400&display=swap');  
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400&display=swap');  
body {  
   "font-family: 'Noto Serif TC', 'Noto Serif JP', 'Noto Serif KR', serif !important;  
}
```

原先只加了 `Noto Serif TC` ，也就是繁中的明體。但是因為平常還有在看日文和韓文的網頁，只有中文變成明體，混在文章裡的日文和韓文還是原來的字型，整個感覺很差。所以就也把 `JP` 和 `KR` 也加了進來，在繁中找不到時，會依序再去找日文和韓文的對應字型。效果如下：

![](/images/effefafbbc1f/1_yufb5-IKIQ3XxbhHF14wrA.jpeg)

![](/images/effefafbbc1f/1_TMm2pAXVIma9vkL4Xyu38g.jpeg)
*左：原本字型 / 右：Google 字型*

這些更動都已經更新到最新版的 EinkBro 了。有興趣的人也可以去下載來試試。

[EinkBro - Apps on Google Play](https://play.google.com/store/apps/details?id=info.plateaukao.einkbro)
