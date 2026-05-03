+++
title = "幻滅，是成長的開始 — Flutter 的 async 與 isolate"
date = "2019-05-28T10:57:45.367Z"
description = "原以為 Flutter 寫起來很開心，有任何耗時比較長的工作，就塞到一個 Future<T> someFunction(…) async {…} 中就好，不需要像 Android 裡還需要用到 rxJava 或是自己建 thread…"
slug = "幻滅是成長的開始-flutter-的-async-與-isolate"
canonicalURL = "https://medium.com/@danielkao/%E5%B9%BB%E6%BB%85-%E6%98%AF%E6%88%90%E9%95%B7%E7%9A%84%E9%96%8B%E5%A7%8B-flutter-%E7%9A%84-async-%E8%88%87-isolate-2f87321a7ba8"
mediumID = "2f87321a7ba8"
+++

![](/images/2f87321a7ba8/1_yyCGSU6ph3dCpTMk1SfBGA.png)

原以為 Flutter 寫起來很開心，有任何耗時比較長的工作，就塞到一個 ***Future<T> someFunction(…) async {…}*** 中就好，不需要像 Android 裡還需要用到 rxJava 或是自己建 thread 來處理。但後來發現其實沒有那麼單純。就像下面這篇文章開頭講的一樣：剛接觸 Flutter 的人通常不會管到 asynchronous 的問題，直到 UI 開始變得很卡的時候。

[Flutter Threading](https://medium.com/@obrand69/flutter-threading-5c3a7b0c065f)

在 Dart 中 async 和 Future 無法解決所有耗時的工作。Dart 雖然支援 非同步執行，但其實如果是透過 async keyword 的話，只是把工作丟到同一個 event loop 中，讓它暫時不會卡住目前的工作，等到真的輪到它執行時，如果它真的很耗時，那 main **isolate** 還是會 freeze 住的。Dart 主要的 task 都是在 main **isolate** 中完成的，**isolate** 像是個 single thread 的 process。如果真的想要讓某些工作能夠同時進行，不要卡住 main **isolate** 的話，就得要自己產生新的 isolate 來執行。但 isolate 又不是那麼好寫，必須藉由ReceivePort來傳送資料。下面有個小範例：

[View gist](https://gist.github.com/plateaukao/b4e5fd32f2a39d5161584d4a6818b53c)

[Dart Fundamentals - Isolates](https://codingwithjoe.com/dart-fundamentals-isolates/)

好在針對一般需要比較多時間執行的工作，Dart 提供了一個比較容易使用的 compute() function，幫開發者包裝自建 **isolate** 的繁雜流程。

以下是個簡單的範例。原先第一行的 processImage() 因為需要針對圖片的每個 pixel 做處理，所以會很花時間，如果只是單純用 async 的話，在執行的時候依然會在 main **isolate** 做，造成畫面反應很不流暢。將它改成用 compute() 來呼叫後，Dart 會幫忙產生新的 isolate 同步執行。如此一來畫面就不會再卡卡的了。

[View gist](https://gist.github.com/plateaukao/ef4a7f07b453ff130434f5581ecfdd07)

將現有的 async function 改成呼叫 compute()，只是幾行 code 的事，就可以解決在同一個 event loop 中執行影響其他 task 流暢度的問題，但如同上面的例子所示， compute 呼叫的 function 必須要是top-level function 或是 static 才行，在實作上還要思考怎樣管理這些透過compute 完成的 function。

### **參考資料**

[Asynchronous programming: futures & async-await](https://dart.dev/tutorials/language/futures)
