+++
title = "Advanced isolate usage in flutter"
date = "2020-05-17T09:18:16.348Z"
description = "雖然標題是英文，內文還是用中文撰寫，造福一下看中文資訊的讀者。"
slug = "advanced-isolate-usage-in-flutter"
canonicalURL = "https://medium.com/@danielkao/advanced-isolate-usage-in-flutter-94b124deacdd"
mediumID = "94b124deacdd"
+++

![](/images/94b124deacdd/1_TYtiTKgefFO_2lSRwo9M0Q.png)

雖然標題是英文，內文還是用中文撰寫，造福一下看中文資訊的讀者。

在 flutter 中，如果遇到花時間的 task，小一點的 task 可以直接利用 async function 把這件事延後到 event loop後面；大一點的 task，則是建議利用 isolate，將它交給獨立的 isolate 處理完後，再送回主要的 UI thread。

dart 本身也知道 isolate 的寫法很煩瑣，所以特地包了一個 compute 的 function 讓開發者可以很快地將想處理的邏輯包在一個 top level function 中，再將它丟給 compute 就行。關於 isolate 和 compute的使用方式，可以參考我之前的一篇文章：

[幻滅，是成長的開始 — Flutter 的 async 與 isolate](https://medium.com/@danielkao/%E5%B9%BB%E6%BB%85-%E6%98%AF%E6%88%90%E9%95%B7%E7%9A%84%E9%96%8B%E5%A7%8B-flutter-%E7%9A%84-async-%E8%88%87-isolate-2f87321a7ba8)

compute 在使用上相當無腦，卻也不是萬靈丹。它底層還是會去建立新的 isolate，處理完 task 後再把該 isolate 砍掉。每次建立 isolate 的成本是很高的，可能需要花費 50 到 150 ms 的時間。如果同一個畫面中有多張圖片要處理，或是透過 isolate 方式在處理多個網路 request 的 response parsing。將會產生許多 isolate 開開關關造成不必要的資源浪費和時間上的延遲。

這時，其實不難想到，如果能有個類似 thread pool 的機制就好了：透過固定產生幾個 isolate 在那，由這幾個 isolate 輪流去處理不斷進來的需求。

isolate 這個 plugin 也為大家準備好了這樣子的solution，稱為 loadBalancer。先來看一下如果是 compute 的話，可以怎麼寫。在第 6 行利用 compute 執行 processImage function。

[View gist](https://gist.github.com/plateaukao/ef4a7f07b453ff130434f5581ecfdd07#file-dart_compute-dart)

下面是利用 LoadBalancer 的例子。利用 Loadbalancer 的話，主要是第 2行的建立 LoadBalancer instance，在第 9 行般取得資源，然後透過 loadBalancer.run() 執行 task。

[View gist](https://gist.github.com/plateaukao/13a8de5eb838a2aa926e77b611f2a521)

下面是套用了 LoadBalancer 的 Flutter App 的表現。

### 相關文章

[Flutter 中處理 Image 的方式](https://medium.com/@danielkao/flutter-%E4%B8%AD%E8%99%95%E7%90%86-image-%E7%9A%84%E6%96%B9%E5%BC%8F-edef5f47000b)
