+++
title = "new francais-anglais dictionary for onlinedic"
date = "2008-04-02T11:17:00Z"
slug = "new-francais-anglais-dictionary-for-onlinedic"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/04/new-francais-anglais-dictionary-for.html"
bloggerID = "6388428973726346216"
tags = ["Annecy Life", "onlineDic", "Python"]
+++

[![PA273853 (by plateaukao)](/images/blogger/6388428973726346216/1779980644_79f4b22b48.jpg "PA273853 (by plateaukao)")](http://www.flickr.com/photos/plateau/1779980644/ "PA273853 (by plateaukao)")  
(Olympus E300 France.Chamonix)  
  
週日有到夏慕尼滑雪的活動，光是車錢就要18歐。  
如果再加上一整天的forfait的話，大概總共要50歐。  
還在考慮中…  
  
\*\*\*\*  
今天在網上找資料時，看到有人說wordreference的解釋比較精確。  
我去找了幾個最近在學的les mots familiers，它裡頭大都有明確的英文解釋。  
所以，早上花了點時間把它也加到onlinedic裡頭。  
  
跟其他網站不一樣的地方是，wordreference會檢查request的header，  
看user-agent是不是一般常用的browser，如果不是的話會擋掉該request。  
這麼一來，python提供的最基本的  
 `urllib.urlopen`  
就派不上用場了。  
  
上網看了一下，要改掉預設的user-agent，得要改用urllib2才行。  
大致上的code如下：  
 `import urllib2  
 req=urllib2.Request(url=url_line,headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6) Gecko/20040113'})  
 f = urllib2.urlopen(req)  
 source = f.read()`  
  
嗯~又多了一個好字典 :)  
  
相關連結：  
[WordReference](http://www.wordreference.com/)
