+++
title = "在Lime HD中快速啟動語音輸入法"
date = "2013-06-09T16:14:00Z"
slug = "在lime-hd中快速啟動語音輸入法"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/06/lime-hd.html"
bloggerID = "8586416849300642508"
tags = ["Programming", "Android"]
[cover]
  image = "/images/blogger/8586416849300642508/8988184819_15e50ca1d3_k.jpg"
+++

[![](/images/blogger/8586416849300642508/8988184819_15e50ca1d3_k.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjET2NbPqiLgS1jQfefljsHsCOhB_RguQIl6CxPH8NfB6LI7LheAdl4swjFw-C97xjwnm0YeHF_vXL-4rEPHw1vNx0_yGY4PizHpXRSiNPQ1K7a48oElZ7jd7yGjMc3VICBG0yJaZIpkmI/s1600/8988184819_15e50ca1d3_k.jpg)

(富貴角.Taiwan)  
  
剛剛試了一下谷歌的語音輸入，覺得有些時候應該蠻實用的。所以打算幫它在Lime HD中加個快速切換的功能。在Lime HD中原本就有開啟Google語音輸入法的方式，只是我覺得有點太麻煩了。原本的方式是：  
1. 長按左下方的設定鈕，這時會跳出一個對話視窗，可以設定輸入簡繁中文的切換，分割鍵盤等一些選擇。畫面最下方則是切換成語音輸入法。  
  
通常會想用語音輸入的時機，都是在手不方便慢慢點螢幕的時候，所以，操作步驟愈多，就愈麻煩。原本我是打算在長按(中/En)按鈕時，直接啟動語音輸入。目前這個按鈕的長按並沒有預設的作用，所以很適合。  
  
可惜的是，我不知道怎麼debug InputMethodService，所以沒有辦法短時間內看清楚在LIMEService中的長按功能，是怎麼前後串起來的。一直找不到好的interception point。  
  
無意中卻發現了，原來Lime有針對輸入的整個面版實作swipe的key listener！！做為一個多年的Lime HD愛用者，竟然不知道有這麼一回事。看了原始碼後，它的目前對應功能是：  
滑上：開啟設定對話窗(跟長按設定按鈕一樣)  
滑下：關閉輸入法  
滑左：模擬刪除鍵  
滑右：送出目前選擇的候選字  
  
既然設定對話窗已經可以很方便地長按設定鍵來開啟，我把"滑上"給改成呼叫Google語音輸入法。程式碼很簡單，在LIMEService中的swipeUp()，把原本的code換成StartVoiceInput()就可以了。
