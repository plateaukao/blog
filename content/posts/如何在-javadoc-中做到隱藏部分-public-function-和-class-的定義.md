+++
title = "如何在 javadoc 中做到隱藏部分 public function 和 class 的定義"
date = "2018-10-20T03:24:56.210Z"
description = "有時，雖然部分的 classes 或是 functions 是設為 public 的，但在產生 javadoc 文件時，我們卻希望不要將這些資訊呈現給看文件的使用者。一種可能的情況是，我們在程式碼中已經有實作某些新的功能，卻不希望使用者事前知道這些功能的存在。"
slug = "如何在-javadoc-中做到隱藏部分-public-function-和-class-的定義"
canonicalURL = "https://medium.com/@danielkao/%E5%A6%82%E4%BD%95%E5%9C%A8-javadoc-%E4%B8%AD%E5%81%9A%E5%88%B0%E9%9A%B1%E8%97%8F%E9%83%A8%E5%88%86-public-function-%E5%92%8C-class-%E7%9A%84%E5%AE%9A%E7%BE%A9-848119471f66"
mediumID = "848119471f66"
[cover]
  image = "/images/848119471f66/1_NhLD_BIklQgsLk8jIDqmLA.jpeg"
+++


![](/images/848119471f66/1_NhLD_BIklQgsLk8jIDqmLA.jpeg)

有時，雖然部分的 classes 或是 functions 是設為 `public` 的，但在產生 javadoc 文件時，我們卻希望不要將這些資訊呈現給看文件的使用者。一種可能的情況是，我們在程式碼中已經有實作某些新的功能，卻不希望使用者事前知道這些功能的存在。

最基本的 javadoc 並不支援這樣子的功能，我們可以透過 doclava 這個 客製化的 javadoc doclet 來幫我們達成。

首先要先在你的 gradle 文件中加入 dependency，並在 javadoc task 中多幾行設定。基本上就完成了。

![](/images/848119471f66/1_kOaiMM360Fkj2I_jd6xPMA.png)

再來就是在你想要隱藏的 class 或 function 的 javadoc comment 上，加上 `@hide` 的 annotation。像是以下的例子：

![](/images/848119471f66/1_ySQ1DIMqnpOhC81jzAZgtA.png)
*hide class*

![](/images/848119471f66/1_xpt6mQ8K43qqnYW_IcqgMA.png)
*hide function at line 17*

我在 github 上放了一個很簡單的 android 範例

針對他產生出來的 javadoc 文件則可以在下面看得到：

完整的文件，沒有套用 doclava doclet

![](/images/848119471f66/1_vlcFrgsTVlNQAN0WWx9stQ.png)

套用過 doclava 的文件：

![](/images/848119471f66/1_I5-Q-DJa4ojfYj41AHdPow.png)

可以看得出來，兩份文件的長相其實並不太一樣。但至少，可以達到我們想要的功能了。

[Google Code Archive - Long-term storage for Google Code Project Hosting.](https://code.google.com/archive/p/doclava/)
