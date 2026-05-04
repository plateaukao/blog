+++
title = "你的 issue 不是你的 issue"
date = "2020-08-11T16:54:41.942Z"
description = "寫程式難免要 debug。 de 自己寫出來的 bug，也 de 別人寫出來的 bug。除蟲的探索過程中，總有無盡的苦悶與黑闇，和伴隨著解完 issue 而來的通體舒暢。"
slug = "你的-issue-不是你的-issue"
canonicalURL = "https://medium.com/@danielkao/%E4%BD%A0%E7%9A%84-issue-%E4%B8%8D%E6%98%AF%E4%BD%A0%E7%9A%84-issue-5732068cae02"
mediumID = "5732068cae02"
[cover]
  image = "/images/5732068cae02/1_cDLCXlAq1PESlHt_2qLoTg.jpeg"
+++


### 你的 bug 不是你的 bug

![](/images/5732068cae02/1_cDLCXlAq1PESlHt_2qLoTg.jpeg)

寫程式難免要 debug。 de 自己寫出來的 bug，也 de 別人寫出來的 bug。除蟲的探索過程中，總有無盡的苦悶與黑闇，和伴隨著解完 issue 而來的通體舒暢。

今天要來記錄一下最近經歷的神奇追蟲過程。

---

### 蟲來了

有一天突然被找去一起查一條 crash issue，因為好像我負責的元件有可能是造成問題的原凶之一。稍微看了一下系統上記錄的 crash log，發現全是 native 的 call stack，最後掛在一個 native 的 image library。沒有相關的 map file 的話，native call stack 可以提供的線索其實很少。

這條 issue 開始大量發生的日期，並不是在 app release 後的那幾天，而是在兩個 release 之間，青黃不接的時期，所以很難去斷定是不是某個特定版本改出來的問題。但 crash 確實是在某一個版本(這裡稱它為 A 版好了)之後才開始有的，這個 crash 只發生在幾家特定品牌作業系比較早期版本的手機上；而且有使用者反應：如果透過刪除會 crash 的 app，再裝回 A 版之前的版本就沒事了。

### 追蟲去

追蟲第一步驟：如果 log 看得出來在哪出問題，就直接看 code 去找解法；如果 log 看不出來的話，就要試著去重現問題，然後，再回頭去找有用的 log 來找原因。

這次遇到的 issue 屬於後者，完全沒有頭緒的 crash，只知道在某些手機上會發生。很幸運地，我從 QA 那邊借來了一台型號一樣的手機，可以讓我試著看能不能做出跟使用者遇到一樣的 crash 。在經過一番努力之後，終於有時可以遇到 crash 的情況，但還是摸不著它 crash 的條件。把相關的 logs 收集了之後，交給比較會看 native crash logs 和 app 中其他元件的同事研究。

藉由 app logs 和 native crash logs 的時間交叉比對，研判可能是 app 中某個功能在下載圖片時，會造成這個 crash。因為圖片的來源是網路，現有的 app 中用來記錄圖片資訊的 log 並不夠多，所以無法從 log 中得到更詳細的資訊。

### 加強版抓蟲器

強人同事，一個晚上的時間，把下載圖片的 http 實作加上了 logging interceptor，build 了一版可以提供更多關於圖片來源的 app。方法類似下面的連結：

[square/okhttp](https://github.com/square/okhttp/tree/master/okhttp-logging-interceptor)

有了更詳細的 logs 之後，我又再試著去重現 crash，看能不能收集到更多有用的資訊。同時，也試著去把 crash 時，手機上已經有下載好的圖片，檢查看看是不是有破圖。破圖倒是沒有發現，但新增的 log 資訊中，倒是讓我看出了點端倪。

大部分的圖檔路徑和名稱都很正常，但卻有一張比較像是畫面在做效果時才會取的檔案名稱。抱著不妨一試的心情，我把這張圖的路徑在 app 中試著直接開啟; 果不其然！它 crash 了！

找到了會讓 app crash 的圖檔之後，再來的調查就順手多了。crash 的源頭在 native image library，而這個 library 是內建在手機裡，不是 app 自帶的。那麼，如果用手機裡的其他 app 來開啟這張圖的話，是不是也一樣會 crash 呢？Bingo！大家都 crash 了！

**看來，解決這條 issue 的方式是：請使用者再買台好一點的手機。**

當然不是這樣子的啦~

最終的解法是：換一張不會造成 crash 的圖 — 結案！連 app 都不用 release 新版，就解了這條 crash issue。

雖然 issue 解了，但為了避免往後有類似的問題發生，或是一旦又發生了，要怎麼讓 issue fixing 的時間可以再縮短(從幾天到幾個小時？)，內部還是有了很多後續的檢討和討論。

---

以後，如果收到我傳給你的圖檔，記得要打開喔。 :)
