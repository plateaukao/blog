+++
title = "firebase in Android"
date = "2016-11-27T14:42:00Z"
slug = "firebase-in-android"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2016/11/firebase-in-android.html"
bloggerID = "919743682431431406"
tags = ["Android"]
+++

忘記當初用 parse 時是不是也是這麼簡單。目前對於 firebase 的運作方式還沒有很了解，但單純要塞點東西到 firebase ，然後事後再抓下顯示在畫面上，基本上是會了。  
  
firebase 的 database不用事先建立，只要一直呼叫 child 就可以建立起資料的階層架構。但由於事後的 query 有些限制，所以在建立 child 的 hirarchy 時要先考慮到之後讀取資料的方便性。不然可能空有資料在 server，卻沒有好的方式來抓回自己想要的資料。  
  
再來是登入帳號的部分， firebase 提供了 facebook, google account, twitter, etc 等常見的帳號登入連結方式；為了讓還沒登入的 user 也能夠記錄一些資料在雲端，它還提供了 anonymous sign in 的功能。完成 anonymous sign in 後會得到一個 anonymous 的 user object，這個 firebase user object 就可以拿來塞屬於這個帳號的相關資料。  
  
等哪天 user 想要用真的帳號登入時，等登入完可以再將 anonymous user 跟後來登入的帳號做綁定，避免之前的資料因此都被清光光。
