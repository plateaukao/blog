+++
title = "升級 android studio"
date = "2016-11-26T09:10:00.002Z"
slug = "升級-android-studio"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2016/11/android-studio.html"
bloggerID = "409242588430470794"
tags = ["Programming", "Android"]
+++

有半年以上沒有動 Android Studio 了吧。最近又要開始使用 NerAudioList ，想說把原本串 parse.com 的部分改為 firebase，因為 parse.com 的大限快到了。為了改 code，只好升級一下 android studio，沒想到這是條漫長的路。  
  
首先是 Android Studio app的升級，花了點時間升級到 2.3 版，再來是一堆 build tools 和 sdk 的升級。再來是 plugins 的升級。為了在 Mac 上可以直接 debug，不用再接上我的手機，試開了一下 Genymotion，結果也開不起來了。  
  
把 VirtualBox 和 Genymotion 都下載了最新版來裝，才又開了起來。結果在 adb devices 找不到  Genymotion 的 emulator，上網找了一下，是要在 Genymotion 的設定畫面設定自己安裝的 sdk 的路徑才能 work。  
  
> error: could not install \*smartsocket\* listener: Address already in use

  
再來是在 Android Studio 中會遇到下面的問題。這問題則是把 project 的 java sdk 指到 1.8 的版本就行了。  
  
java.lang.UnsupportedClassVersionError: com/android/build/gradle/AppPlugin : Unsupported major.minor version 52.0  
  
好了，可以開始寫 code 了~
