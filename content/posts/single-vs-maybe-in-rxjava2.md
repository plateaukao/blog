+++
title = "Single vs Maybe in RxJava2"
date = "2018-06-14T13:33:46.905Z"
description = "在使用 Android Room 做 Query 時，有時不見得會找到想要的資料，所以當結果有可能是空的的時候，需要有個回傳值可以做後續處理。"
slug = "single-vs-maybe-in-rxjava2"
canonicalURL = "https://medium.com/@danielkao/single-vs-maybe-in-rxjava2-20d4b354125a"
mediumID = "20d4b354125a"
+++

在使用 Android Room 做 Query 時，有時不見得會找到想要的資料，所以當結果有可能是空的的時候，需要有個回傳值可以做後續處理。

以下面的 Query 為例子，某個 id 的 Magazine 就不見得找得到。

```
@Query("SELECT * FROM bookmark WHERE id=:id")  
fun getMagazine(id: String): Maybe<Magazine>
```

從 Single<ClassName>換成 Maybe<ClassName> 之後，處理方式就有點不同。Single 的話，只需要處理 onSuccess 和 onError 的情況， Maybe 要多處理沒有資料的情況，方式如下：

```
dataSource.getMagazine(id)  
    .doOnSuccess { // 有值的情況 }  
    .doOnError { // 失敗的情況 }  
    .doOnComplete { // Query 不到資料的情況 }  
    .subscribe()
```
