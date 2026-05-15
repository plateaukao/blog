+++
title = "Tips for using AdMod module in Android Studio"
date = "2013-05-24T12:53:00.004Z"
slug = "tips-for-using-admod-module-in-android-studio"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/05/tips-for-using-admod-module-in-android.html"
bloggerID = "7263569642981193798"
tags = ["programming", "Android"]
[cover]
  image = "/images/blogger/7263569642981193798/2043865899_2f123a0ab8_b.jpg"
+++

[![](/images/blogger/7263569642981193798/2043865899_2f123a0ab8_b.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjg6140x8Ka-rgVPQWxfU_YXAzJ7ymtb5F4_yx0JJBowZTWLLgvrCz00OyCDKFSiN9H3WMNvgdgpLnui-WjDT-ZXNdLcQgCCqVqxvnbGYNqosuO3OkxljAFsWpeRgAevknJzUVYWMVFja4/s1600/2043865899_2f123a0ab8_b.jpg)

(Geneva.Swiss)  

It's pain in the ass to use Android Studio now, since it's just published, which implies bugs appear every now and then, and you're not sure it's due to your misunderstanding of this IDE, or it's really an issue. In addition, it's  relatively hard to find How-to answers comparing to ADT plugin with Eclipse.

  

While trying to set up AdMob module in my project on Android Studio, it took me some time to fix some external library import errors that should be clearly mentioned in online AdMob doc, or even better, just integrate it into "Android Studio".  Isn't Android Studio meant to make Android developers' life easier?

Problem 1: Add **com.google.ads.AdView** element  in my layout xml as doc says, but it generates compilation error.

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
              xmlns:ads="http://schemas.android.com/apk/lib/com.google.ads"
              android:orientation="vertical"
              android:layout_width="fill_parent"
              android:layout_height="fill_parent">
  <com.google.ads.AdView android:id="@+id/adView"
                         android:layout_width="wrap_content"
                         android:layout_height="wrap_content"
                         ads:adUnitId="MY_AD_UNIT_ID"
                         ads:adSize="BANNER"
                         ads:testDevices="TEST_EMULATOR, TEST_DEVICE_ID"
                         ads:loadAdOnCreate="true"/>
</LinearLayout>
```

Anser: Pay attention!! **You also have to add the red line attributes to the container layout!!** It's not clearly mentioned in document. What I just did in adding com.google.ads.AdView component. Obviously, it told me that it can't compile.

Question 2: Don't know how to add the AdMob library to my project in Android Studio. The AdMob doc only has flows for eclipse. I always meet "**NoClassDefFoundError**" during runtime. This took me most time to wandering on the internet, looking for a right answer.

Answer: it's a bit tedious. Please just check detail information in reference link below. In brief:

1. Put the jar into the **libs** folder

2. Right click it and hit **'Add as library'**

3. Do a clean build (you can probably do this fine in Android Studio, but to make sure I navigated in a terminal to the root folder of my app and typed **gradlew clean** (I'm on Mac OS X, the command might be different on your system)

Question 3: sometimes, even questions above are all fixed, you still can't get the AdMob View. Why? You have to declare a specific Activity for it including configChanges. This is mentioned in [Introduction](https://developers.google.com/mobile-ads-sdk/docs/), but ... I just have ignored it, since who would have thought that creating a View in my own activity needs to declare a specific Activity for it?

```
    <activity android:name="com.google.ads.AdActivity"
              android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|uiMode|screenSize|smallestScreenSize"/>
 
```

REF:

[Add a jar library](http://stackoverflow.com/questions/16608135/android-studio-add-jar-as-library/16628496#16628496)
