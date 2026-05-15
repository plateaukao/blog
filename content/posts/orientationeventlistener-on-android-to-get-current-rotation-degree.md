+++
title = "OrientationEventListener on Android to get current rotation degree"
date = "2013-05-28T06:33:00.001Z"
slug = "orientationeventlistener-on-android-to-get-current-rotation-degree"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/05/orientationeventlistener-on-android-to.html"
bloggerID = "1898616034331393813"
tags = ["programming", "Android"]
[cover]
  image = "/images/blogger/1898616034331393813/4120153199_93cc8874c2_b.jpg"
+++

[![](/images/blogger/1898616034331393813/4120153199_93cc8874c2_b.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBVQ2cfHm1kM4nepIjwibq6OaC71jHz9ag8kF6POLx5xp01sEnfj4Vu5yqscbUxLnqfm11986jvG_HuiSC0GGpelUtx5_bV-4aVlG5W5-Epv1OSNiT6MvxbP3_XDMF5AqbUxyIUmb4pp0/s1600/4120153199_93cc8874c2_b.jpg)

(Central Park.New York)  
  

Strangely, it's not possible to get current rotation angle in android directly, except for getting the fixed 4 rotation modes: 0, 90, 180, 270. In order to get precise rotation degrees instead of rotation modes, **OrientationEventListener** can be used. Once it's implemented, you can get the rotation degree in onOrientationChanged(). It's a lot easier than manipulating values from all the sensors like gyroscope, accelerator, etc.

REF:

<http://android-er.blogspot.tw/2010/08/orientationeventlistener-detect.html>
