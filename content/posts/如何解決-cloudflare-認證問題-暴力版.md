+++
title = "如何解決 CloudFlare 認證問題 (暴力版)"
date = "2023-02-26T16:20:40.994Z"
description = "最近 chatGPT 相當熱門，不論有什麼問題需要網路的協助，總是可以先找 chatGPT 聊聊，看看它有什麼想法。不過，在使用 EinkBro 想要登入 chat.openai.com 時，它會跳出下面的畫面要我先檢驗我是…"
slug = "如何解決-cloudflare-認證問題-暴力版"
canonicalURL = "https://medium.com/@danielkao/%E5%A6%82%E4%BD%95%E8%A7%A3%E6%B1%BA-cloudflare-%E8%AA%8D%E8%AD%89%E5%95%8F%E9%A1%8C-%E6%9A%B4%E5%8A%9B%E7%89%88-ce8899b6d8f0"
mediumID = "ce8899b6d8f0"
tags = ["EinkBro"]
[cover]
  image = "/images/ce8899b6d8f0/1_UuxwU-FYlm3_lLsJ3C0OPg.png"
+++


最近 chatGPT 相當熱門，不論有什麼問題需要網路的協助，總是可以先找 chatGPT 聊聊，看看它有什麼想法。不過，在使用 EinkBro 想要登入 chat.openai.com 時，它會跳出下面的畫面要我先檢驗我是 human。然後，我怎麼按它都會回傳失敗。也因此，一直無法在 EinkBro 中使用 chatGPT 網頁的服務。

![](/images/ce8899b6d8f0/1_UuxwU-FYlm3_lLsJ3C0OPg.png)

![](/images/ce8899b6d8f0/1_i2Qnfy91KguOFos16zoVYg.png)

![](/images/ce8899b6d8f0/1_vkRd7Rh6PK0ScOen2bs3og.png)

這幾天在 EinkBro 的 issue 列表中，恰好也有人回報了類似的問題，描述有些網站如果有利用 cloudflare 的 captcha 服務的話，會無法正常執行。

![](/images/ce8899b6d8f0/1_q6ZHz5TXMnOKGbVY-cuzaA.png)
*https://github.com/plateaukao/einkbro/issues/221*

### 解法

目前的解法，可能不是最好的方式，但至少是有效的：將 WebView 的 useragent 字串換掉就可以了。這解法是從另一個也被發了一樣 issue 的 github browser repo 看來的。

![](/images/ce8899b6d8f0/1_uKF7lttGOvthdjGdLCxzeg.png)

一模一樣的問題，卻是由不同的帳號詢問，而且是發在另一個 Open Source 的瀏覽器上。這個瀏覽器的作者也找到了解法，只要先把 useragent 字串換成 `Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36` 就可以了。

![](/images/ce8899b6d8f0/1__zK6R0y0SKJ-kwjYlmWlEQ.png)

在 EinkBro 上試了一下，確實可行。後來再找了一下，也在 reddit 上提到一樣的作法。

目前這作法雖然可行，但有點麻煩，因為在 EinkBro 中，useragent 字串的設定埋得有點深 (誰會沒事一直在換 useragent 字串)。希望哪天能找到真正的原因並把它完美地解決掉。

### 完成畫面

![](/images/ce8899b6d8f0/1_ShpeRNts9Oh2ObrSBq6ocQ.jpeg)

### 修改 EinkBro

雖然看起來只要修改 useragent 字串就可以成功，但目前在 EinkBro 中，只要有設定自訂的 useragent 字串，就默認會採用；也就是說如果在其他的網頁想要切回原本系統預設的 useragent 時，得要把原先加的 useragent 清空才行。這麼一來，下次再需要時，又要找個地方把那長長的 useragent 再複製貼上一遍，讓它生效。

這樣子太累人了，所以我在設定中新增了一個”是否要使用自訂的 usergent”的選項；這麼一來字串設定完後就可以一直留著，不用刪來刪去的。

![](/images/ce8899b6d8f0/1_UpeDqWL4urgmAr4EfPWRYA.png)

### 相關連結

[fix: support cloudflare check. · plateaukao/einkbro@f85195b](https://github.com/plateaukao/einkbro/commit/f85195beb22efe03e59d4f44f943c06b2f7748f3)
