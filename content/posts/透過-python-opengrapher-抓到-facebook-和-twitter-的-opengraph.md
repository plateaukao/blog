+++
title = "透過 python opengrapher 抓到 facebook 和 twitter 的 opengraph"
date = "2020-12-10T15:33:25.925Z"
description = "之前寫了一篇文章，描述如何用 LINE 的 LIFF API 分享帶有圖案的連結訊息。除了介紹 LIFF 外，也提到了 python 的 opengrapher 函式庫。當時並沒有深入了解它，也因此錯失了一些資訊。"
slug = "透過-python-opengrapher-抓到-facebook-和-twitter-的-opengraph"
canonicalURL = "https://medium.com/@danielkao/%E9%80%8F%E9%81%8E-python-opengrapher-%E6%8A%93%E5%88%B0-facebook-%E5%92%8C-twitter-%E7%9A%84-opengraph-6a5e79ed92c"
mediumID = "6a5e79ed92c"
+++

之前寫了一篇文章，描述如何用 LINE 的 LIFF API 分享帶有圖案的連結訊息。除了介紹 LIFF 外，也提到了 python 的 opengrapher 函式庫。當時並沒有深入了解它，也因此錯失了一些資訊。

[開啟 LINE LIFF v2 的無限潛力 — liff.shareTargetPicker()](https://danielkao.medium.com/%E9%96%8B%E5%95%9F-line-liff-v2-%E7%9A%84%E7%84%A1%E9%99%90%E6%BD%9B%E5%8A%9B-liff-sharetargetpicker-24b47b0b4252)

在此，要再補充一點它的功能。下面先附上它的連結：

[0rang3max/opengrapher](https://github.com/0rang3max/opengrapher)

上篇文章有提到，它的應用很簡單，只要下面的呼叫方式就可以得到該 url 的 opengraph 資訊：

`result = opengrapher.parse(url)`

不過，真的在使用時發現，最常分享的 facebook link 以及 twitter link 都會失敗。原因是 twitter 有做 client side rendering，所以無法在一開始打 http request 時就取得相關的 meta data。(facebook 我就不知道了，可能是一樣的原因吧)。

對於這個問題，opengrapher 在一開始就考慮到了，它可以藉由代入 user-agent 的方式，讓 facebook / twitter 知道這個 request 是來自於 bot ，這樣子 facebook / twitter才會把 client side rendering 改成 server side rending，將 meta data 事前就先塞好。

在 github 的 README 最下方提及了這件事。(當時應該好好地把 README 看完的…)

![](/images/6a5e79ed92c/1_Uk1snSbP7eEtLoTTDAZ-CQ.png)

關於更詳細的解釋，可以參考 stackoverflow 的這篇文章：

[Twitter website doesn't have open graph tags?](https://stackoverflow.com/questions/62526483/twitter-website-doesnt-have-open-graph-tags/64332370#64332370)

---

現在我的 LIFF url sharer 可以正常的分享 twitter 連結了。:)
