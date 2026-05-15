+++
title = "Android Studio 升級至 2.2 後的 gradle 問題"
date = "2016-12-19T15:26:00Z"
slug = "android-studio-升級至-22-後的-gradle-問題"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2016/12/android-studio-22-gradle.html"
bloggerID = "3509823763714373228"
tags = ["Programming", "Android"]
[cover]
  image = "/images/blogger/3509823763714373228/Screen_Shot_2016-12-19_at_11.24.58_PM.png"
+++

Android 升到 2.2 後，原本在取得 version name 的方式更改了，所以下面原先的作法行不通：  

[![](/images/blogger/3509823763714373228/Screen_Shot_2016-12-19_at_11.24.58_PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiShCr_jIiCyI21z6LERUm70IL1B-NZL2pwtAxGZAOXrrVM7m2WlhyPlfDZDpzuS_6clbimp7umqLYiILuuzRAMVMX-t6PgcZ1jxQK6nesM8txJbpFQLqDn_DhQ9yDDu52n0p7YfCrVmyY/s1600/Screen+Shot+2016-12-19+at+11.24.58+PM.png)

錯誤訊息會說找不到 DefaultManifestParser。  
  
新版的gradle，其實可以直接用 variant 取得 version name了：  
  

[![](/images/blogger/3509823763714373228/Screen_Shot_2016-12-19_at_11.26.16_PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0-B4vC_Oj_oxKMJJeaJ57m4CZPlADW_Gu_3KZptc4ekcPdzYplO7lMJi6hFKeSkdI6Id_7-nKGQz13bSsMvS_GnKnagvwxe9KwV0DfGdNsJpbdJS_IvNjWOv71go-2K3qpFKpn_Ep7j8/s1600/Screen+Shot+2016-12-19+at+11.26.16+PM.png)
