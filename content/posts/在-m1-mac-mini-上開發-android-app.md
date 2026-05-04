+++
title = "在 M1 Mac Mini 上開發 Android App"
date = "2021-05-10T12:55:32.908Z"
description = "最近剛拿到 M1 Mac Mini 最基本規格(8GB RAM/256GB SSD)的機器，開始嘗試要用它來開發，所以會這兒記錄有哪些需要注意的地方。(持"
slug = "在-m1-mac-mini-上開發-android-app"
canonicalURL = "https://medium.com/@danielkao/%E5%9C%A8-m1-mac-mini-%E4%B8%8A%E9%96%8B%E7%99%BC-android-app-acf835681671"
mediumID = "acf835681671"
[cover]
  image = "/images/acf835681671/1_lezW1YgmFDsQFH7P6xmZfw.png"
+++


最近剛拿到 M1 Mac Mini 最基本規格(8GB RAM/256GB SSD)的機器，開始嘗試要用它來開發，所以會這兒記錄有哪些需要注意的地方。(持續更新中)

1. **Android Studio** 下載號稱有支援 M1 CPU 的 Arctic Fox Canary 15，但是速度還是很卡。所以後來改成使用 **IntelliJ Community Edition 2021.1.1**。原以為在 IntelliJ 上得要自己安裝 Android plugin，但似乎原本就有內建了，所以裝好後就可以直接開啟或建立 Android project。但有一點要注意的是，Gradle使用的 JVM要選 jbr-11，不然在編譯時會有錯誤產生。

![](/images/acf835681671/1_lezW1YgmFDsQFH7P6xmZfw.png)

2. 安裝有支援 M1 CPU 的 JDK。目前網上找到的文件，都是建議安裝 Zulu。

[Java Download | Java 8, Java 11, Java 13 - Linux, Windows & macOS](https://www.azul.com/downloads/zulu-community/?version=java-8-lts&os=macos&architecture=arm-64-bit&package=jdk)

3. 升級 Gradle 版本到 7.0。7.0 開始有支援 M1。

![](/images/acf835681671/1_f-blISRJh48KlvJ1s9FTLA.png)

[Gradle Release Notes](https://docs.gradle.org/7.0/release-notes.html#apple-silicon)

4. 安裝 Android Emulator

不知道為什麼，從 Intellij IDEA 中無法正常的下載 Arm64-v8a 的 ROM image，所以我是從裝好的 Android Studio Canary 版本中的 SDK Manager 中安裝，然後再回到 Intellij IDEA 中開發。目前只有 Android SDK 30 和 S 有適合 M1 CPU 的 ROM image，但也夠我用了，其他就接上實機來測試。

在使用的時候，發現 Android SDK 30 的 ROM image 有問題，裝好後能開啟，但是無法正常連上網路。改成下載 Android S 的 ROM image 就 okay 了。

5. 安裝 ohmyzsh

[ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)

6. 安裝 Brew

[Homebrew](https://brew.sh)
