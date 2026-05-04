+++
title = "擴充 signature_pad javascript library"
date = "2018-06-14T00:32:41.077Z"
description = "在開發 LINE Message API 的 LIFF 新功能時，藉由 signatue_pad javascript library 在 html canvas上寫字或畫圖。signaure_pad 把這件事包裝得很好，可以很容易地把 canvas 上的圖案輸出成圖片…"
slug = "擴充-signature_pad-javascript-library"
canonicalURL = "https://medium.com/@danielkao/%E6%93%B4%E5%85%85-signature-pad-javascript-library-b659f1c2430a"
mediumID = "b659f1c2430a"
[cover]
  image = "/images/b659f1c2430a/1_rlNmoxbL1qKfmTBLB02YrQ.jpeg"
+++


### 擴充 signature\_pad javascript library

![](/images/b659f1c2430a/1_rlNmoxbL1qKfmTBLB02YrQ.jpeg)
*Sky*

在開發 LINE Message API 的 LIFF 新功能時，藉由 s[ignatue\_pad](https://github.com/szimek/signature_pad) javascript library 在 html canvas上寫字或畫圖。signaure\_pad 把這件事包裝得很好，可以很容易地把 canvas 上的圖案輸出成圖片 (png 或 jpeg)，再傳送到自己想要儲存的地點。

在官網上還有一個[範例](https://jsfiddle.net/osenxvjc/285/)介紹了怎麼樣提供 Undo 的功能，程式碼如下

[View gist](https://gist.github.com/plateaukao/f5cf746063bba702cdb00f91d4991fa9)

這裡的 data 是 Array of IPoingGroup，每 pop() 一次，就是把前一次的線條資料刪掉，再把 data 餵回 signaturePad 重新繪製。

[View gist](https://gist.github.com/plateaukao/e43ed054ab560498917ac92b833d0600)

由於 IPointGroup 中只包含了線條的顏色和線條所經過的點的位置，如果在每一次描繪線條時，都改變筆刷的大小，在 data 中其實並沒有記錄到當時的筆刷大小；這樣會導致 Undo 再重畫時，所有的線條全都成了同樣的粗細。

舉個例子來說，我畫了 5 條線 (A, B, C, D, E)，分別是筆刷大小 1, 2, 3, 4, 5。這時我不想要第 5 條線 E，我執行了 Undo 功能，畫面重繪後只會剩下 A, B, C, D 4 條線，但是筆刷大小全成了 5。(因為最後一刻的筆刷大小設定是 5)

也就是說， Undo 功能在有更換筆刷大小的情況下，會是有問題的。原本有用粗筆來填充畫面的話，一旦做了 Undo，就很有可能只剩下細細的一堆線。會讓人有種前功盡棄的感覺，需要全部再重新來一次。

為了讓 Undo 在更換筆刷後，依然能正常運作，我把 signaure\_pad 的 IPointerGroup 稍做更動，針對每一筆線條的資訊，加入當時筆刷大小的資訊。這樣子即使是事後重畫，也可以確保每一筆線條的原始大小。

[View gist](https://gist.github.com/plateaukao/0bc78650e539efb5893e03856600c84f)

針對這修正，我也發了 [*pull request*](https://github.com/szimek/signature_pad/pull/369) 給 signature\_pad 作者。只是該 repo 的更新似乎沒有很活躍，不知道要多久之後才會被看到。

### 前情提要

[初探 LINE Message API 的新功能 LIFF](https://medium.com/@danielkao/%E5%88%9D%E6%8E%A2-line-message-api-%E7%9A%84%E6%96%B0%E5%8A%9F%E8%83%BD-liff-51d5e7ff1a6a)
