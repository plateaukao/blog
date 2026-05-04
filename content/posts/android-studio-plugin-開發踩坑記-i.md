+++
title = "Android Studio Plugin 開發踩坑記 (I)"
date = "2019-10-06T04:25:54.458Z"
description = "對一個 Android app 開發者來說，工作中使用時間最長的軟體，我想應該就是 Android Studio 了吧。"
slug = "android-studio-plugin-開發踩坑記-i"
canonicalURL = "https://medium.com/@danielkao/android-studio-plugin-%E9%96%8B%E7%99%BC%E8%B8%A9%E5%9D%91%E8%A8%98-i-3dc031481883"
mediumID = "3dc031481883"
[cover]
  image = "/images/3dc031481883/1_3hGdtBUoV54tmrSwqM8AsQ.png"
+++


對一個 Android app 開發者來說，工作中使用時間最長的軟體，我想應該就是 Android Studio 了吧。

工欲善其事，必先利其器。除了要花時間熟悉內建的各項功能外，有些時候，根據自己的開發習慣，會希望它再額外多些功能，讓自己的開發流程更加順手。

下面這是官方提供的教學網頁。做為一個 Hello, World 的示範，還算可以。但如果是真的打算開發一個能用的 plugin，這網頁遠遠不足。大部分的說明都是文字描述，而不是以開發時所需要的步驟來講解；常會有看完某個段落後，似乎多懂了一點點，但卻完全不知道怎麼使用該 Class，因為大都沒有附上沒有相關的程式碼範例。

[Creating Your First Plugin](http://www.jetbrains.org/intellij/sdk/docs/basics/getting_started.html)

相對於開發 Android app 來說，明明只是要做個簡單功能的 plugin，卻得花上許多時間東查西查的，還不見得可以找到對的方式。所以想說應該記錄下包，以防以後想再寫別的 plugin 時，又得再重新來一次。或者，如果也有其他人跟我一樣，遇到各式各樣問題，不得其門而入時，可以剛好看到這幾篇分享。

### GUI Desinger 不產生程式碼的問題

開發 Android Studio Plugin 的過程中，常常會需要產生 UI 的畫面：比方說想要在 Preference 中讓使用者可以更改一些相關的設定，或是有些選項希望可以跳出對話框，讓使用者當下選擇後，就可以繼續運作。

在 Intellij IDEA 中，建立 Java UI 的方式是使用它自帶的 GUI Designer，透過拖拉元件的方式，讓你可以很方便地產生你想要的畫面，然後 Intellij 再幫你產生所需要的 Java 程式碼，讓你可以在專案中使用。不過，就是這個不過，如果你跟我一樣，利用 Gradle 建立專案的話，會遇到 GUI Designer 怎樣就是不動。

千辛萬苦查了官網的說明，結果官網只簡短地說了，它在 Gradle 下不會產生對應的程式碼(下圖黃色框框)。

![](/images/3dc031481883/1_3hGdtBUoV54tmrSwqM8AsQ.png)

[GUI Designer](https://www.jetbrains.com/help/idea/gui-designer.html)

咦，如果不產生的話，官網說明總要給我一些方向吧，不然我怎麼知道要怎麼接下去做。難不成我要重新建一個 plugin 專案，然後把系統改成 maven 嗎？

試了各種方式，最終還是在某篇 StackOverflowF上的文章找到了符合我的解法。

1. **在 build.gradle 中加入下面 library 的引用就好啦。**

```
dependencies {  
    implementation 'com.intellij:forms_rt:7.0.3'  
}
```

2. 在 Preference 中，記得要把設定切為 Generate GUI into Java source code

![](/images/3dc031481883/1_O4pMp3Br1rYWM2CGoNzN4g.png)

3. 再 build 一次 plugin 看看。

[Intellij Idea 13 UI Designer and automatic Gradle building](https://stackoverflow.com/a/27079572/1265915)
