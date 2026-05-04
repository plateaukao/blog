+++
title = "Flutter 中處理 Image 的方式"
date = "2019-04-13T05:27:06.297Z"
description = "在 Android 中，把圖片顯示出來前，如果對 Image 做點變化的話，通常會將 Image 先轉成 Bitmap，再針對 Bitmap 中的每個 pixel 去做處理，最終轉成 Drawable，再送給 View 去繪製。作法可以參加 CalliImageView 中的…"
slug = "flutter-中處理-image-的方式"
canonicalURL = "https://medium.com/@danielkao/flutter-%E4%B8%AD%E8%99%95%E7%90%86-image-%E7%9A%84%E6%96%B9%E5%BC%8F-edef5f47000b"
mediumID = "edef5f47000b"
[cover]
  image = "/images/edef5f47000b/1_q4e7UAFWxHbwBoskSmhAyw.png"
+++


![](/images/edef5f47000b/1_q4e7UAFWxHbwBoskSmhAyw.png)
*Image processing in flutter (remove white background)*

在 Android 中，把圖片顯示出來前，如果對 Image 做點變化的話，通常會將 Image 先轉成 Bitmap，再針對 Bitmap 中的每個 pixel 去做處理，最終轉成 Drawable，再送給 View 去繪製。作法可以參加 CalliImageView 中的 adjust function。

[plateaukao/CalliImageView](https://github.com/plateaukao/CalliImageView/blob/master/customviews/src/main/java/info/plateaukao/android/customviews/CalliImageView.java#L328-L357)

但是在 Flutter 的世界中，事情就不是那麼單純了。官方提供顯示圖片的 Widget 主要是 [Image](https://docs.flutter.io/flutter/widgets/Image-class.html)，可以透過 Image.network(), Image.asset(), Image.file(), Image.memory()，從不同來源載入圖片。但是 Image 並沒有提供取出 raw data 的 public function，即使你繼承它，也一樣找不到類似 onDraw() 的功能。想要更了解 Flutter 的繪製 Widget 架構的話，可以參考掘金上的這篇文章 [Flutter中的Image入门讲解](https://juejin.im/post/5c10871ae51d451402773231) 。

網路上建議如果想要 Flutter Image Processing ，是使用這個套件 <https://pub.dartlang.org/packages/image> ，但找到的範例都是要先從檔案中把圖片讀成 Bytes 再餵給 Image。

[View gist](https://gist.github.com/plateaukao/e9142028fb3a89df67e3c8ada74af1fb)

我的使用情境是：圖片會是從網路來的。所以我得先去研究怎麼把拿到的 url 先從網路下載到本地端才行。

在網路上找到一個比較簡單的 network cache image 範例如下：

[zmqgithub/Save-Server-Image](https://github.com/zmqgithub/Save-Server-Image/blob/master/lib/load_image.dart)

仔細研究一下它的 downloadImage() 可以發現，在第12行時它把 request (應該是 response 才對)的資料當成 bytes 讀出來，然後再寫到 file 中。這 bytes 應該就是可以直接用來塞到 Image.decodeImage() 中吧！如此一來，就不需要真的把圖存成圖片了。

[View gist](https://gist.github.com/plateaukao/fc07262f41bc4171e6d79fec7a1e7ce7)

我想做的事是把一張圖裡，白色的部分都變成透明的，只留下黑色的部分。接下來就容易了，只要參考 Image 套件中的各種 filter class，也寫一個自己的版本就行。下面是更改過的 downloadImage() 版本，加入了把圖片去背的功能。

[View gist](https://gist.github.com/plateaukao/ebb5e7169dd89cc52bda338762d4997e)

最終的效果，大家可以看文章一開始的圖片囉。沒去背之前，書法字旁邊因為有白色背景，所以背景畫的九宮格無法正確的顯示。去背後，一切就正常啦。
