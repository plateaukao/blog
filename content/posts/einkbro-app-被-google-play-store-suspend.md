+++
title = "EinkBro App 被 Google Play Store suspend"
date = "2024-01-23T12:51:43.255Z"
description = "沒想到在 2024 年初竟然迎來了這樣子的結果，真的是始料未及。下面會來說說被 suspend 的原委，希望讓剛好看到這篇文章的讀者能夠有所警惕，不要踩到 Google 大大的雷。"
slug = "einkbro-app-被-google-play-store-suspend"
canonicalURL = "https://medium.com/@danielkao/einkbro-app-%E8%A2%AB-google-play-store-suspend-2022f827081d"
mediumID = "2022f827081d"
tags = ["EinkBro"]
[cover]
  image = "/images/2022f827081d/1_4DDeoNxtFDdExuaPxQzXzA.png"
+++


沒想到在 2024 年初竟然迎來了這樣子的結果，真的是始料未及。下面會來說說被 suspend 的原委，希望讓剛好看到這篇文章的讀者能夠有所警惕，不要踩到 Google 大大的雷。

在 2023 年 12 月，突然想到其實我可以在 EinkBro 中加入更方便的 App 更新機制。以我自己的使用習慣來說，我都會是安裝剛開發完的版本，所以都不是安裝 Google Play Store 上可能兩三週才更新一次的相對穩定版本。

為了要安裝最新的開發版本，我的流程會是：

1. 開啟 einkbro 在 github 上的網頁
2. 點擊 snapshot zip，下載它
3. 到檔案總管 App 中解壓縮這個 zip 檔
4. 到解壓縮後新建的資料夾中，點選 app-release.apk 安裝

這流程雖然不複雜，我也這麼進行了兩三年，但是身為工程師，就是會想要把所有 routine 的事用寫程式的方式來解決。所以，在 2023 年 12 月我在 EinkBro 中加了新的機制可以到設定畫面中點一下升級 button，就可以把上面的步驟都省略掉。

為此，我還很開心地寫了一篇實作的文章。

[從 EinkBro App 中直接安裝升級版本](https://medium.com/einkbro/%E5%BE%9E-einkbro-app-%E4%B8%AD%E7%9B%B4%E6%8E%A5%E5%AE%89%E8%A3%9D%E5%8D%87%E7%B4%9A%E7%89%88%E6%9C%AC-3fc8c7927a31)

在後續的改善中，也考慮到其實 Google Play Store 的使用者是無法享受到這個機制的，因為要上架到 Google Play Store 時，在編譯時用的是別把 upload key，上傳後 Google Play Store 會把收到的 aab 根據不同設備來的需求，拆成合適的版本，再發送到使用者的設備中。

所以，只要是判斷操作的使用者是原先利用 Google Play Store App 安裝的話，就會在點擊 button 時，開啟 Google Play Store 的 EinkBro 畫面，讓使用者經由 Play Store App 來升級。

可惜的是，我只做了半套。EinkBro 升級的按鈕有兩顆，一顆是升級成最新的 release 版本；一顆是升級成 snapshot 的版本。前者我有做了這個判斷，但後者卻忘了也加上這個判斷。

也因此，應該是有些使用者試著去點了該按鈕，想要升級成 snapshot 版本，卻失敗了。然後 Google 的偵測機制抓到了這些 event，發現 EinkBro 中提供了非來自 Google Play Store 的升級機制。

![](/images/2022f827081d/1_4DDeoNxtFDdExuaPxQzXzA.png)

在完全不給機會改善的情況下，於 2024 年 1 月 16 日收到 Google 的來信，說 EinkBro 因為違反政策，遭到了 suspension。這邊 suspension 的意思是：關於 EinkBro (info.plateaukao.einkbro) 這個 App，所有的使用者數據，下載量，使用者留言，全部都被清除了。使用者無法在 Google Play Store 上再找到 EinkBro App。

雖然來信中有提到可以申訴，不過，申訴了也沒有用，官方回覆了很官方的內容；而 EinkBro 也確實實作了升級的機制(雖然這機制 100% 無法在 Google Play Store 安裝的版本上有作用)。

如果開發者(我)真的很想要再上架，而且我的開發者帳號還存在的話(還沒被 ban 掉)，我是可以在修正問題後(拿掉升級的機制)，重新將 App 的 package id 改掉，然後再換個新名字重新上架一個新 App。我不理解為什麼得要再重新用一個 package id，以及重新申請一個 App。但是，這就是 Google 訂下來的遊戲規則，只能怪我一時疏忽了。

### 結論

原先上架 Google Play Store 也只是想說其他想安裝的人會方便一點，但沒想到弄到最後，我卻因為這件事被 suspend 了 app，而且在 Google 的名冊上多了一個 x ，感覺有點得不嚐失。我怎麼知道再重新上架的話，會不會哪天又不小心惹怒谷哥大大。

為了自己還有一段開發者的生涯著想，要顧好自己的 Google Developer Account，所以我就不打算再上架一次了。在 Github 玩玩就好。如果真的覺得 EinkBro 很有幫助或很好用的人，自然會找到方式安裝；如果找不到的話，那就只能說無緣了。
