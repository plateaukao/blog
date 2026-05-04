+++
title = "支援 Android multi-window 模式時需要注意的事情"
date = "2018-10-19T11:57:15.153Z"
description = "通常在 Activity 中使用 WebView 時，會習慣在 onPause 裡頭，呼叫 WebView.onPause()，順著 Activity 的生命週期，將 WebView 順手停下來 ；然後在 onResume 來的時候，再呼叫…"
slug = "支援-android-multi-window-模式時需要注意的事情"
canonicalURL = "https://medium.com/@danielkao/%E6%94%AF%E6%8F%B4-android-multi-window-%E6%A8%A1%E5%BC%8F%E6%99%82%E9%9C%80%E8%A6%81%E6%B3%A8%E6%84%8F%E7%9A%84%E4%BA%8B%E6%83%85-674194e67f1"
mediumID = "674194e67f1"
[cover]
  image = "/images/674194e67f1/1_ZkBhwEpKnZq5olcjUH1XLg.jpeg"
+++


![](/images/674194e67f1/1_ZkBhwEpKnZq5olcjUH1XLg.jpeg)
*Chamonix, France*

通常在 Activity 中使用 WebView 時，會習慣在 `onPause` 裡頭，呼叫 `WebView.onPause()`，順著 Activity 的生命週期，將 WebView 順手停下來 ；然後在 `onResume` 來的時候，再呼叫 `WebView.onResume()` 讓 WebView 可以繼續運作。

這樣子的實作，在一般情況下是很 Okay 的。但一旦你的應用程式支援 multi-window 模式，上述的實作很有可能會造成你的 WebView 畫面在進入 multi-window 模式時，變成白色畫面。

觀察結果如下：

[View gist](https://gist.github.com/plateaukao/4552f92373ea8fd1840b63258f98259a#file-android_activity_lifecycle_in_multiwindow_mode)

如果 `WebView.onPause()` 在 Activity 的 `onPause` (第 8 行和第 12 行) 就被呼叫的話，在 2. 裡頭的最後一步，系統會把畫面上方的 Window 又呼叫一次 `onPause` 。造成它雖然是在畫面上，但實際上狀態是 PAUSE 的。

目前的解法是，如果你的畫面中有用到 WebView，你要把 `WebView.onResume()` 的呼叫時機改到 Activity 的 `onStart()`；然後 `WebView.onPause()` 延後到 Activity 的 `onStop()` 才做。

**更多閱讀**

[Multi-Window Support | Android Developers](https://developer.android.com/guide/topics/ui/multi-window#lifecycle)

[5 tips for preparing for Multi-window in Android N](https://medium.com/androiddevelopers/5-tips-for-preparing-for-multi-window-in-android-n-7bed803dda64)
