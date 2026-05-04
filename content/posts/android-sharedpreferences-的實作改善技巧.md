+++
title = "Android SharedPreferences 的實作改善技巧"
date = "2022-12-24T13:48:26.314Z"
description = "在今年 iTHome 鐵人賽最後一天的文章中有介紹到，怎麼將 Boolean 的 SharedPreferences 包裝起來，讓原本很煩瑣的 value getter setter 可以透過 delegate 的方式，一行搞定。下面是包裝前和包裝後的程式碼。"
slug = "android-sharedpreferences-的實作改善技巧"
canonicalURL = "https://medium.com/@danielkao/android-sharedpreferences-%E7%9A%84%E5%AF%A6%E4%BD%9C%E6%94%B9%E5%96%84%E6%8A%80%E5%B7%A7-5651a732158b"
mediumID = "5651a732158b"
[cover]
  image = "/images/5651a732158b/1_85hSkEsxO_BRbjsz3PhVRA.png"
+++


在[今年 iTHome 鐵人賽最後一天的文章](https://ithelp.ithome.com.tw/articles/10304792)中有介紹到，怎麼將 `Boolean` 的 `SharedPreferences` 包裝起來，讓原本很煩瑣的 value getter setter 可以透過 delegate 的方式，一行搞定。下面是包裝前和包裝後的程式碼。

![](/images/5651a732158b/1_85hSkEsxO_BRbjsz3PhVRA.png)
*利用 getter / setter 讓外部可以簡單地對 SharedPreference 操作*

先實作一下 `BooleanPreference` ：

![](/images/5651a732158b/1_55kpTD2DQuT3otBC8q2omg.png)

改善之後的寫法如下。是不是更一目暸然呢？

![](/images/5651a732158b/1_DbV714Q_XxWIEQx6AVG9zQ.png)

---

上面的 `BooleanPreference` 中有個函式叫 `toggle()` 原先是預期外部的使用者可以呼叫它來改變當前這個 sharedPreference 的值，可以將醜醜的 `config.thisIsSomeKey = !config.thisIsSomeKey` 變成 `config.thisIsSomeKey.toggle()` 就好。不過，在真正執行時，卻發現這個函式無法被存取到。

原因在於當使用 `config.thisIsSomeKey` 時，`ReadWriteProperty.getValue()` 已經起了作用，拿到的已經是 `Boolean` 值了。 `Boolean` 值自然沒有什麼 `toggle()` 的函式可以使用。

那麼，究竟可以怎麼做，才可以達成 `config.thisIsSomeKey.toggle()` 的效果呢？先看結論，用下面的函式，就能擴充上面的 BooleanPreference ，讓它能執行 `toggle()` 這個函式。

```
fun KMutableProperty0<Boolean>.toggle() = set(!get())
```

至於什麼是 `KMutableProperty` 呢？在 Kotlin 中，可以利用 reflection 取得程式中的一些元素，而 `KMutableProperty` 就是其中一種。

![](/images/5651a732158b/1_RWZlXATIcxXdOzCLPiW59w.png)

一開始實作的 BooleanPreference 在 class 中被宣告為變數時，便可以利用 KMutableProperty0 來取得該元素，而不是被直接傳回 getter 執行後的 Boolean 值。

然後，再透過擴充 KMutableProperty0<Boolean> ，增加 toggle() 函式，就可以在還沒拿回 Boolean 值時，呼叫 toggle() 。而這裡的實作也利用了 KMutableProperty0 的原始函式 get() 和 set()，達成 true/false 互換的效果。

另外，在使用時，有點不同的是原先預期想要透過 `config.thisIsSomeKey.toggle()` ，因為利用了 KMutableProperty0 來實作；在使用時要改成 `config::thisIsSomeKey.toggle()` ，才能正確地拿到 reflection 的變數。

儘管只是一行程式碼，卻是我花了好幾個月才終於找到的解法。

修改完後，除了程式碼看起來更加清爽外，語意也更為明顯。

![](/images/5651a732158b/1_ClA7gBTGTJpmRJ323nBl6Q.png)

### 相關資料

- [EinkBro 中的修改](https://github.com/plateaukao/einkbro/commit/f8037c8296292a923bc10adacccd7b23c41e5354)

[Kotlin专题「二十五」：反射\_小丑超梦的博客-CSDN博客\_org.jetbrains.kotlin:kotlin-reflect](https://blog.csdn.net/m0_37796683/article/details/113603323)
