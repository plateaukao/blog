+++
title = "改善 EinkBro 中的直排閱讀體驗"
date = "2024-11-30T13:27:35.457Z"
description = "兩三年前，透過很簡單的 css style 設定，讓 EinkBro 可以呈現最基本的網頁內容直排效果。這次，要來總結一下怎麼把直排體驗的小地方也都顧到，其中包含下面的各項調整："
slug = "改善-einkbro-中的直排閱讀體驗"
canonicalURL = "https://medium.com/@danielkao/%E6%94%B9%E5%96%84-einkbro-%E4%B8%AD%E7%9A%84%E7%9B%B4%E6%8E%92%E9%96%B1%E8%AE%80%E9%AB%94%E9%A9%97-c437b39f68e4"
mediumID = "c437b39f68e4"
+++

![](/images/c437b39f68e4/1_NmMNQIxxgNlaIUpfJgbXuw.png)

兩三年前，透過很簡單的 css style 設定，讓 EinkBro 可以呈現最基本的網頁內容直排效果。這次，要來總結一下怎麼把直排體驗的小地方也都顧到，其中包含下面的各項調整：

- 有單一數字時，讓數字保持是直立的
- 有連續 2 個數字時，讓數字保持是直立的，而且並排在一起
- 有 1. 2. 3. 之類的項目標題時，讓數字保持是直立的
- 有單一英文字母時，讓英文字母是直立的
- 有連續 2 個英文字母時，讓英文維持直接，而且並排在一起
- 有 a. b. c. 之類的項目標題時，讓它保持是直立的
- 微調直立的數字，確保它看起來是跟上下文有對齊的
- 在直排閱讀模式中，將 minute 這個閱讀時間單位做成多語化

---

### 單一數字與多個數字的處理

為了讓數字不要在直排閱讀時總是躺平，在顯示前必須掃過一次全部文字，把這些數字找出來，一一處理。

![](/images/c437b39f68e4/1_oiNp2ZfWnI1YjLPCmADnbQ.png)

在 EinkBro 中，寫了一段 javascript 來處理這件事：先找出網頁中的所有 TEXT\_NODE，利用正規式表示法把最少一個數字，最多連續 4 個數字挑出來。之所以要撈到 4 個數字，是因為我想同時處理年份的情況。以中文新聞和文章來說，常常會出現西元年份；如果能把連續 4 個數字也轉成正的會提高可讀性。

利用第 4 行的字串表示，在第 9 行逐步找出 TEXT\_NODE 中符合的情況，再為這些數字加上 span，補個 vertical 的 class name。針對 vertical class，會配上以下的 css style：

![](/images/c437b39f68e4/1_DqcZ7P3XENPgVHF-NyI9qw.png)

### 單一數字或是單一英文字母後後面有 .

接下來是處理條列式內容時常會用到的標號，像是：

1. 2. 3. 或是 a. b. c. 等

這時，我們得把上面的正規表示式改成下面的樣子(這寫法還是不完美，後面會再做修改)，除了撈1 到 4 個數字，跟後面有 . 的情況外，也對英文做同樣的處理：

```
 const regex = /(\d{1,4}\.?|[a-zA-Z]{1,50}\.?)/g;
```

這樣子撈到的符合字串會比較多，所以在處理時，要多點 if-else 來濾掉一些不要的情況：

![](/images/c437b39f68e4/1_egFS75otyptRXhV8dNh2Vg.png)

第 11 行會將長度超過 1 的符合情況，如果都是英文的話，跳過不處理。如果是較長的數字，但在長度 4 以內的話，就幫它們加上 verticalSingleChr 的 class name。這是為了將這一個個數字，獨立的轉成站起來。

![](/images/c437b39f68e4/1_GZXpRm12f66mEPs4m3joqg.png)

大致的作法就如同上面所述，能涵蓋到八九成以上的數字。

### ol 元件中的 li 標號轉正

接再來，介紹如何處理網頁中 ol (order list) 中的 li 元素。以下的程式碼是參考 taketori.js 來的。它的直排閱讀做得很完整，但太大包了，而且不大符合我的使用情景，所以只能抽取部分我需要的邏輯出來用。

為了讓 li 元件可以站起來，有幾個步驟：

1. 找出這些需要旋轉的 li 元件，判斷它是哪種型式 (1. 2. 3., or i, ii, ii, or I, II, III, or 一些日文的編號)
2. 將這些 li 塞入 data-marker 的屬性，填入想要顯示的標號
3. 將 li 上層的 ol 元件加上 cjk class name。

![](/images/c437b39f68e4/1_K-tnHNvdcbYrxtvWwTIDRQ.png)

cjk class 的 css style 如下。要先把 ol.cjk 的 list-style-type 清除，讓它不會有預設的標號文字；再來是在 li:before 中，將剛剛塞的 data-marker 放進 content，然後針對它做旋轉。

![](/images/c437b39f68e4/1_CwlAHliU1jcli4vTyDTQsg.png)

### 收尾：避免重覆旋轉同個字串兩次

在使用時，常常會遇到有些連續的 2 位數會轉過頭：原本是 90 度躺平，調整後變成 180 度躺平。一樣是躺平，只是方向不同。

後來發現可能在某些流程中，會造成部分符合的數字字串被處理了兩次，包了兩層的 vertical span 。為了避免重覆處理，在新增 vertical span 前，可以先看看 parent node 是不是已經是 vertical class 了：

![](/images/c437b39f68e4/1_usxd2pXyasvo7Uw-vUPkYA.png)

---

以上，就是大部分直排閱讀模式的改善邏輯。經過這番改造後，直排閱讀的體驗又更上一層樓了！

### 相關連結

- [相關的調整 commit](https://github.com/plateaukao/einkbro/compare/v14.0.0...v14.1.0)
- [EinkBro 的直排閱讀模式技術分享](https://medium.com/einkbro/%E6%89%93%E9%80%A0-e-ink-%E5%B0%88%E7%94%A8%E7%9A%84%E7%80%8F%E8%A6%BD%E5%99%A8-part-v-769216ef6db6)
- [直排書中的數字，該怎麼處理才好？](https://bobtung.medium.com/%E7%9B%B4%E6%8E%92%E6%9B%B8%E4%B8%AD%E7%9A%84%E6%95%B8%E5%AD%97-%E8%A9%B2%E6%80%8E%E9%BA%BC%E8%99%95%E7%90%86%E6%89%8D%E5%A5%BD-af9051e8dfd)
