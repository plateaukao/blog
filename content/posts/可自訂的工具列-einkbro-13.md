+++
title = "可自訂的工具列 — EinkBro (13)"
date = "2021-09-11T17:53:27.484Z"
description = "隨著開發的功能愈來愈多，工具列的空間已不足以將所有的功能都排在上面；而且也不是每個功能都是使用者會常用的功能。為了要解決這個問題，工具列開始支援自訂，讓使用者可以自訂工具列上的功能和排序方式。如果能在上面放上最常用的功能，使用者就不用頻繁地開啟層層選單找尋功能按鈕。"
slug = "可自訂的工具列-einkbro-13"
canonicalURL = "https://medium.com/@danielkao/%E5%8F%AF%E8%87%AA%E8%A8%82%E7%9A%84%E5%B7%A5%E5%85%B7%E5%88%97-einkbro-13-c00350972a7a"
mediumID = "c00350972a7a"
+++

### 可自訂的工具列 — EinkBro (14)

隨著開發的功能愈來愈多，工具列的空間已不足以將所有的功能都排在上面；而且也不是每個功能都是使用者會常用的功能。為了要解決這個問題，工具列開始支援自訂，讓使用者可以自訂工具列上的功能和排序方式。如果能在上面放上最常用的功能，使用者就不用頻繁地開啟層層選單找尋功能按鈕。

我們先來看看一般瀏覽器的工具列都長得怎樣

![](/images/c00350972a7a/1_HSqcpXujTwA3bh9KpyUYAw.jpeg)

![](/images/c00350972a7a/1_9NLlDicaZC5Rj_lqCh7B8g.jpeg)

![](/images/c00350972a7a/1_YumbkEU410JDUBEXPDlfgw.jpeg)
*Chrome / Firefox / NeoBrowser*

Chrome 包含了幾個常用的功能，Onyx 電子書設備內建的 NeoBrowser 跟 Chrome 蠻相似的；Firefox 則是相當簡潔，幾乎沒有任何按鈕可用。

### 擴充工具列界面

原本的工具列只是在一個水平的 `LinearLayout` 中，放入多個 `ImageButton`，為了避免使用者塞入太多按鈕，造成工具列超過畫面寬度，我們先在外面包上一層 `HorizontalScrollView`。

![](/images/c00350972a7a/1_8Vo-48Lfs7OFJcWVlS735A.png)

![](/images/c00350972a7a/1_bmx9nnw470v-nsBg1C9gqw.png)

在畫面初始化時，我們就會先把所有的按鈕生成出來；之後再根據使用者的設定，將其重新排列和隱藏不必要的按鈕。

對於工具列的操作，因為有點多，所以另外寫了一個 `ToolBarViewController` 來處理。其中比較重要的函式是 `reorderIcons()`。

```
fun reorderIcons() {  
    toolbarActionViews.size
```

```
    val iconEnums = config.toolbarActions  
    // 先移除全部按鈕，再依照設定中的資訊來重新塞入按鈕  
    if (iconEnums.isNotEmpty()) {  
        iconBar.removeAllViews()  
        iconEnums.forEach { actionEnum ->  
            iconBar.addView(toolbarActionViews[actionEnum.ordinal])  
        }  
        // Settings 這個按鈕如果不小心被使用者刪除了，這裡會強制將它顯示出來  
        // 因為沒有 Settings 按鈕，就無法再進到工具列設定的畫面。  
        if (ToolbarAction.Settings !in iconEnums) {  
           iconBar.addView(  
              toolbarActionViews[ToolbarAction.Settings.ordinal])  
        }  
        // 重新配置工具列的呈現  
        iconBar.requestLayout()  
       …  
    }  
}
```

`toolbarActionViews` 則是在畫面生成的時候，先把裡頭的每個按鈕元件的 reference 都先記錄下來。

```
private val toolbarActionViews: List<View> by lazy {  
    val childCount = iconBar.childCount  
    val children = mutableListOf<View>()  
    for (i in 0 until childCount) {  
        children.add(iconBar.getChildAt(i))  
    }
```

```
    children  
}
```

### 建立可拖拉排序的選項對話框

這一部分的實作需要一個可以拖拉的 `ListView`。花了點時間在網路上找到堪用的元件 `DragSortListView`，將它置於對話框 `ToolbarConfigDialog` 內，並且依照使用者儲存的設定，初始化它的狀態。

![](/images/c00350972a7a/1_NFi8nfPpqO5xjLPPs7Utcw.png)

然後，為了儲存和管理所有的工具列按鈕，建立了 `ToolbarAction` 的 `Enum`：

![](/images/c00350972a7a/1_F8DN8sXqPSFYhJYP5AOhMg.png)

全部實作完後，只要再在設定畫面中，再加上一個工具列設定的按鈕就行了！`BrowserActivity` 裡設定 `onClick` 的實作

```
R.id.toolbar_setting -> ToolbarConfigDialog(this).show()
```

下面是完成的工具列設定對話框

![](/images/c00350972a7a/1_rigf0M4qDS0zZho_KDOEjQ.jpeg)

![](/images/c00350972a7a/1_iCBdrXJlHLwTWU0zyE8mHw.jpeg)

下面是我在 Onyx Nova 3 Color 上常用的設定

![](/images/c00350972a7a/1_4kIEiMbf7Qcw-0zwaR3dIQ.jpeg)
*標題/刷新/返回/觸控翻頁/放大/縮小/翻譯/分頁列表/書籤/直排/閱讀模式/設定/旋轉畫面*
