+++
title = "老姐要用 Kotlin 寫專案 -- 從 Server 到 Android APP 的開發生存日記, Kate"
date = "2022-05-29T05:04:00.003Z"
slug = "老姐要用-kotlin-寫專案-從-server-到-android-app-的開發生存日記-kate"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2022/05/kotlin-server-android-app-kate.html"
bloggerID = "8308786760128851279"
tags = ["Books"]
[cover]
  image = "/images/blogger/8308786760128851279/AVvXsEhvJJ6_XtWsu9jiU0WxhtceFBuo9Ahw_ZsLsqWt9NJL_GRwrk_o_NxBd-cmO8Mz4eqjjHtoU_xSczvoJIGX70_woDN7ztIlYU3EIhKuABWd0eXEPBGbXFVi6s2uPjBWWt5YlP8REbUGWkZk2r0-V3IiwA7D2BkDISOP52f8bJrCF4IRewp2qLHCMZjh.jpg"
+++

[![](/images/blogger/8308786760128851279/AVvXsEhvJJ6_XtWsu9jiU0WxhtceFBuo9Ahw_ZsLsqWt9NJL_GRwrk_o_NxBd-cmO8Mz4eqjjHtoU_xSczvoJIGX70_woDN7ztIlYU3EIhKuABWd0eXEPBGbXFVi6s2uPjBWWt5YlP8REbUGWkZk2r0-V3IiwA7D2BkDISOP52f8bJrCF4IRewp2qLHCMZjh.jpg)](https://blogger.googleusercontent.com/img/a/AVvXsEhvJJ6_XtWsu9jiU0WxhtceFBuo9Ahw_ZsLsqWt9NJL_GRwrk_o_NxBd-cmO8Mz4eqjjHtoU_xSczvoJIGX70_woDN7ztIlYU3EIhKuABWd0eXEPBGbXFVi6s2uPjBWWt5YlP8REbUGWkZk2r0-V3IiwA7D2BkDISOP52f8bJrCF4IRewp2qLHCMZjh)

與一般死板的技術教科書不同，這本書是用姐弟倆的對話來展開每個章節中的主題。有劇情就比較容易讀。雖然大部分的內容都點到為止，但因為本身就已經對 Android APP 夠熟悉，所以都很能快地看過去；但在 server 端可以感受到也是講得比較快，所以細節無法帶到太多。對於初學者的話，應該比較容易卡關，或是自己要再多花點時間去閱讀相關的延伸主題。

書中的 server 端比較特別的是採用了 Ktor，以 Kotlin 開發的伺服器端解決方案，讓已經會 Kotlin 的工程師不用再學新的語言，就可以快速上手。在發布服務時，書中選用的是 Heroku，不過，比較不同的是，它並不是直接推上 Github 的 repo 讓 Heroku 幫忙發布，而是將程式 build 成 Docker image，再利用 Heroku 的 CLI 程式來發布。以這型式發布的話，每次有改版，應該是本地端要再自行 upload Docker image 到 Heroku。這應該就有賴於自己有沒有建立自己的 CI/CD pipeline 吧？

下次有空應該也要來試一下這種發布的方式看看。
