+++
title = "調整 Jetpack Compose Dialog 的外觀"
date = "2023-09-20T17:37:14.336Z"
description = "這篇文章將說明怎麼實作 Jetpack Compose Dialog，讓它的外圈能夠沒有暗掉的效果，而且對話框周圍能有黑色的框線。"
slug = "調整-jetpack-compose-dialog-的外觀"
canonicalURL = "https://medium.com/@danielkao/%E8%AA%BF%E6%95%B4-jetpack-compose-dialog-%E7%9A%84%E5%A4%96%E8%A7%80-cf0d3e887312"
mediumID = "cf0d3e887312"
+++

這篇文章將說明怎麼實作 Jetpack Compose Dialog，讓它的外圈能夠沒有暗掉的效果，而且對話框周圍能有黑色的框線。

這個需求主要是來自於在開發 EinkBro 時，原生 Android Dialog 的介面並不是很適合於電子紙閱讀器。外圈的 dim effect (暗化、遮罩效果)在一般手機平板上，能讓使用者更專注於對話框的操作；但在閱讀器上，會造成畫面上的所有元素都要重新調整對比度，增加留下殘影的機會。

所以，如果能夠在顯示對話框時，單純只呈現對話框本身，不去調整它之外的區域，在電子紙上會是比較恰當的行為。

為了要達成這種效果，在早期使用 xml + viewbinding 開發介面時，能夠透過客製化的主題設定(Theme style xml)達成。而在使用 Jetpack Compose 時，我是最近才找到相關的實作方式！得知這個 UI 上的大障礙怎麼解決後，就可以逐步把 EinkBro 中既有的原生對話框一一改寫為 Compose 囉。

### 實作

下面來說明一下怎麼實作。主要可以分為兩個部分：

1. 確保對話框以外的區域不要暗化 (dim effect)
2. 為對話框加上黑色框線，讓使用者依然可以明確的知道對話框大小

#### 外圍不暗化

Compose Dialog 底層其實還是有 Window 存在。所以，只要能取得它底層的 window 元件，就可以去改變它的性質，達到想要的效果。真正的解法，說穿了，只需要一行程式碼：

```
(LocalView.current.parent as DialogWindowProvider).window.setDimAmount(0f)
```

以下是來自於 ChatGPT 的詳細解說：

`LocalView.current.parent`: 這一部分是使用 Jetpack Compose 的 `LocalView` 功能，它可以讓你訪問當前視圖（View）的層次結構。`.parent` 表示取得當前視圖的父視圖，也就是包含這個視圖的容器。

`as DialogWindowProvider`: 這一部分是將父視圖轉換為 `DialogWindowProvider` 類型。這意味著我們假設父視圖是一個能夠提供對話框窗口的提供者，這是用來設定對話框屬性的一種方式。

`.window`: 一旦我們將父視圖轉換為 `DialogWindowProvider` 類型，我們可以使用 `.window` 來訪問與對話框相關的窗口屬性。

`.setDimAmount(0f)`: 最後，我們調用 `.setDimAmount(0f)` 方法，將背景模糊度設置為 0。這意味著對話框的背景不會變得模糊，完全透明，因為模糊度設置為 0。

總結來說，這行程式碼的作用是設定 Jetpack Compose 中的對話框，讓其背景不會變得模糊，完全透明。這可能用於需要在對話框彈出時讓背景保持清晰的情況。

解決了這個問題後，下一個就容易多了。

#### 加上黑框線

在 Compose 中，如果想為元件加上邊線的話，只需要在 `modifier` 中，使用 `border` 的語法就行。如下圖，我為對話框加上了 1.dp 粗的框線，還加上圓弧邊角的效果。

![](/images/cf0d3e887312/1_paGSGyClklgUuQ8-0B_XuA.png)

這麼一來，就完成了 Compose Dialog 所需要客製化。出來的效果，也跟原先 xml 實作的方法差不多。

### 效果圖

目前，僅先在設定畫面中的 ChatGPT action list 中採用。

![](/images/cf0d3e887312/1_lZR8eceQaes3b-33cYq4fg.jpeg)

### 相關連結

commit: <https://github.com/plateaukao/einkbro/commit/9c43625198d5c5ca79e13d0fcee9cd7917b13726>
