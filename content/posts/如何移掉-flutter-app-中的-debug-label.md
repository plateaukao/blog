+++
title = "如何移掉 flutter app 中的 debug label"
date = "2019-05-11T15:21:10.178Z"
description = "在開發的時候，會注意到畫面的右上角有個 Debug 的標籤。官方的說法是，因為開發的版本開啟了很多協助開發或除錯的功能，所以運行速度會跟正式版差很多。為了避免使用的人以為這就是 flutter app 的速度，所以針對測試中的版本，預設都會加上 debug…"
slug = "如何移掉-flutter-app-中的-debug-label"
canonicalURL = "https://medium.com/@danielkao/%E5%A6%82%E4%BD%95%E7%A7%BB%E6%8E%89-flutter-app-%E4%B8%AD%E7%9A%84-debug-label-a157ebf2bfbe"
mediumID = "a157ebf2bfbe"
[cover]
  image = "/images/a157ebf2bfbe/1_IXdjHBpDOdbl1P5K01a5zw.png"
+++


![](/images/a157ebf2bfbe/1_IXdjHBpDOdbl1P5K01a5zw.png)

在開發的時候，會注意到畫面的右上角有個 Debug 的標籤。官方的說法是，因為開發的版本開啟了很多協助開發或除錯的功能，所以運行速度會跟正式版差很多。為了避免使用的人以為這就是 flutter app 的速度，所以針對測試中的版本，預設都會加上 debug 標籤，讓人比較不會誤會 (真的這樣就不會誤會嗎？)

單純在開發的話，右上角的標籤並不會造成困擾，但如果打算要正式發行 app，想要抓一些 app 運行中的畫面時，這就是個很大的問題了。網上到處都有提到怎麼把這標籤拿掉，如下圖 19 行，在 MaterialApp 中，將 debugShowCheckdModeBanner 設成 false 就可以了。

![](/images/a157ebf2bfbe/1_rdr6BenUPZN8_v6mr0ZH-g.png)

如果真的那麼簡單，我就不會寫這篇 blog 了。

對 iOS build 來說，要在 release build 中，才不會看到 debug 標籤，但是 release build 又無法執行於 iOS Emulator 中。也就是說，即使加了 debugShowCheckedModeBanner，還是一樣會在 iOS Emulator 中看到惱人的標籤。

在網路上找了很久，終於找到了解決這問題的方式：

1. 先將 app 執行於 iOS Emulator 中。
2. 在 Android Studio 中開啟 Flutter Inspector，從 More Actions 中找到 Hide Debug Mode Banner 的選項，關了它。

![](/images/a157ebf2bfbe/1_BNQJ37omAynSwqCaL7VofQ.png)

大功告成！
