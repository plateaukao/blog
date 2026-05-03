+++
title = "自製 iThome 鐵人賽參賽主題電子書"
date = "2024-02-02T15:12:46.930Z"
description = "這篇文章將介紹怎麼把 iThome 鐵人賽的參賽文章集結成冊，變成可以離線閱讀的電子書。就算一時半刻沒有時間閱讀，也可以有種自己收藏了不少好書的滿足感。"
slug = "自製-ithome-鐵人賽參賽主題電子書"
canonicalURL = "https://medium.com/@danielkao/%E8%87%AA%E8%A3%BD-ithome-%E9%90%B5%E4%BA%BA%E8%B3%BD%E5%8F%83%E8%B3%BD%E4%B8%BB%E9%A1%8C%E9%9B%BB%E5%AD%90%E6%9B%B8-52c13131e222"
mediumID = "52c13131e222"
+++

這篇文章將介紹怎麼把 iThome 鐵人賽的參賽文章集結成冊，變成可以離線閱讀的電子書。就算一時半刻沒有時間閱讀，也可以有種自己收藏了不少好書的滿足感。

### 更新

最新版本只需要一行指令就可以製作好 epub 了。詳情請見 github repo:

[GitHub - plateaukao/ithome\_ironman\_crawler](https://github.com/plateaukao/ithome_ironman_crawler)

---

![](/images/52c13131e222/1_U186tbCkk4C2pTL2qcqyuA.png)
*截自網頁: https://ithelp.ithome.com.tw/2023ironman/reward*

### 緣起

一到每年的九月十月，如果我不是在參加 iThome 鐵人賽的路上，就是在閱讀各個厲害的鐵人們每天攪盡腦汁生出來的文章。到十月中時，每個主題都陸陸續續完結，然後大約在十二月時會公布得獎名單，並在一月初頒獎。

對於被評審青睞的作品，通常內容和文筆都有一定的水準，很值得拜讀。閱讀這些文章的方式不外乎連上網路，坐在電腦前，一篇篇地看；不然就是等著這些作者再接再厲與出版社合作，花上好幾個月甚至是半年的時間，把這些文章經過潤飾，變成實體的書籍。

除了這兩個方式之外，是不是有可能自己將這些文章集結起來，做成離線的電子書方便自己隨時閱讀呢？如果會寫點 python 語言，又懂得如何利用 calibre 這強大的電子書管理工具的話，其實是可以做到的。以下是我開發的一些步驟說明。

### 步驟

1. 將某個想閱讀的參賽主題的每日文章抓下來。通常會有三十篇左右。
2. 取出每篇文章中，屬於內文的部分，排除系統的元件(像是 header， footer，使用者評論等)。
3. 將這三十篇左右的內文全塞進同一份 html 文件中。
4. 用自己熟悉的瀏覽器打開這份 html，並且用 “完整的網頁” 另外新檔。
5. 透過 calibre 軟體中提供的文件轉換工具 `ebook-convert` ，將 html 轉換成 epub 格式的電子書。

### 步驟 1 ~ 3

上述的步驟 1 ~ 3 可以透過一支 python script 搞定。我有把程式碼公開在 github上。

[ithome\_ironman\_crawler/fetch\_as\_single\_html.py at main · plateaukao/ithome\_ironman\_crawler](https://github.com/plateaukao/ithome_ironman_crawler/blob/main/fetch_as_single_html.py)

如下面程式碼所示，要先帶入 iThome 主題的第一頁，它會從每一頁裡撈出每篇文章的 url，儲存網頁；再前往下一頁，處理下一頁的文章列表。

> iThome 的設計還很原始，明明最多就三十幾篇文章，偏偏還要分成三頁，要使用者在看完十篇後，手動再進到第二頁，閱讀十一到二十篇，然後再往下)，

![](/images/52c13131e222/1_vE47Lx4En57Cb4OYg6hoqg.png)

以我在 2021 年參加比賽的主題來做例子 (<https://ithelp.ithome.com.tw/users/20140260/ironman/4027>)，下面就是第一頁的內容。

![](/images/52c13131e222/1_vyUKENGekp1HgXQMiEudHA.png)

![](/images/52c13131e222/1_-Amo3LgSMkv-z0nC2qd1AQ.png)

儲存好每篇的文章後，再來是把它們的內文部分全寫到同一個檔案中。在下面的 49 行會先打開第一篇文章 html，從裡面抓出整個主題的標題，當成這份 merged html 的標題。

接下來 61 行的 loop 是建立電子書目錄。這裡後來我就全 comment 掉了，因為目錄可以在最後一個步驟時使用 ebook-convert 生成就好。

68 行開始從每一篇文章 html 中抽取重要的部分 (class name 為 qa-panel\_\_content)，將其寫到 merged html 中。

![](/images/52c13131e222/1_E3BgAcf4WuibFSpeYmELxA.png)

### 步驟 4

一切順利的話，在執行 python script 的目錄，會生成一個以主題標題為名的檔案夾，裡面會有一個 combined.html；而且 python script 會自動去開啟這個網頁。這時，使用者要用 “**完整的網頁”** 另外新檔。

以我的參賽作品來說，要下的指令會是

```
python3 fetch_as_single_html.py https://ithelp.ithome.com.tw/users/20140260/ironman/4027
```

而產生的檔案夾會像下面這個樣子

![](/images/52c13131e222/1_kWp16jcwwe4hBREuVyXkmg.png)

> 目前還沒有找到比較合適的工具，所以必須要手動進行。(希望以後有機會也整合到 python script 中。

這時，要利用瀏覽器的另外新檔，覆蓋掉目錄中的 combined.html。

![](/images/52c13131e222/1_uCyATcbLZCMEmLlowcy2Pg.png)

完成後，會看到除了原先就存在的 combined.html 後，還會把網頁中的圖片，css styles, 也都一併存到一個目錄中。

![](/images/52c13131e222/1_rmRg3u5xvVWQWUlUzzg4RQ.png)

### 步驟 5

完成步驟 1 ~ 4 後，最後一步就容易了。只要事前在電腦上安裝好 [calibre](https://calibre-ebook.com/)，找到它附帶的 ebook-convert 路徑，再執行一下 command 就可以轉換成 epub 電子書。

#### 建立 alias

calibre 在 Mac 上安裝後，預設會安裝到 /Application/calibre.app 下，而它附帶的 ebook-convert 也會在對應的目錄中。為了讓執行指令容易一點，可以先為它建立好 alias (這步驟是可以省略的，如果不嫌指令會過長的話)。

```
alias convert=/Applications/calibre.app/Contents/MacOS/ebook-convert
```

#### 執行 html to epub 的轉換

轉換很容易，只需要來源檔案名種，和目標檔案名稱。但如果想要轉得夠漂亮，而且還可以生成正確的書籍目錄，就必須要下點工夫才行。

關於 ebook-convert 的參數設定說明，可以到官網看到很詳細的說明：

[ebook-convert - calibre 7.4.0 documentation](https://manual.calibre-ebook.com/generated/en/ebook-convert.html)

以下是我在轉換時使用到的一些參數。

關於**生成正確的書籍目錄**，可以加上 `— level1-toc “//h:h2[re:test(@class, ‘qa-header__title’, ‘i’)]”` 。它會抓取 html 中具有 qa-header\_\_title 名稱的 h2 元件，這些都是鐵人賽文章中用來表示文章標題的元件。

再來是 ebook-convert 預設會在每個 h1, h2 的元件前畫蛇添足地加上 page break，從新的一頁開始顯示。這點對於鐵人賽的文章內容來說，很不必要，會讓閱讀體驗很差。所以，必須調整一下參數，讓它可以正常的顯示那些利用 h1 來表示小標題的內容。下面的參數就是告訴 converter，只有在章節 element 前再加上 page break 就好。其他的場合不用雞婆。

```
--page-breaks-before "//h:h2[re:test(@class, 'qa-header__title', 'i')]"
```

最後一個要介紹的參數是`— output-profile tablet` ，這是為了避免 calibre 預設會將圖片做處理，將其 rescale 成較小的檔案。這參數也是可加可不加。如果產生的 epub 檔案太大的話，有可能是其中引用的圖檔太大，就可以考慮不加這參數，讓 calibre 幫忙把圖都重新處理過。不然，建議還是保留原始圖檔就好。

完整的指令如下

```
convert combined.html einkbro.epub --level1-toc "//h:h2[re:test(@class, 'qa-header__title', 'i')]" --page-breaks-before "//h:h2[re:test(@class, 'qa-header__title', 'i')]" --chapter-mark "none" --output-profile tablet
```

執行指令後，等個幾秒鐘，或是十幾二十秒，電子書就完成啦！

### 效果展示

以下是 einkbro 第一次參賽的文章產生出來的電子書模樣 (用電腦上的 ebook-viewer)

![](/images/52c13131e222/1_5EHLLD3YlWRie4f6FQqP0g.png)

![](/images/52c13131e222/1_nxW0IGP1SbiXQcJhylaIaw.png)

在文石 Tab Ultra C 的效果如下：

![](/images/52c13131e222/1_NzEjvyjl6oDQhwzZDR5w-A.jpeg)

![](/images/52c13131e222/1_HCpt9_ZkWh_44MQ5Vy5nHw.jpeg)

在 pubook 上用 koreader 閱讀的效果：

![](/images/52c13131e222/1_Yuyxf58W6bclaAuK43AQ7w.jpeg)

在 calibre 中，一大排自己轉換好的書籍。有沒有注意到，這些電子書都是封面的。沒錯，在使用 ebook-convert 時，它會主動幫你生成一個帶有標題的封面，是不是很貼心呢！如果不喜歡的話，還可以手動再調整就是了。

![](/images/52c13131e222/1_z6JkPqEhRHJ-eBxSvvU97Q.png)
