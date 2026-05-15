+++
title = "onlinedict線上版小改進"
date = "2010-03-22T14:54:00Z"
slug = "onlinedict線上版小改進"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2010/03/onlinedict.html"
bloggerID = "3122924360478465834"
tags = ["Python", "onlineDic"]
[cover]
  image = "/images/blogger/3122924360478465834/2013246339_5de3a794ba.jpg"
+++

[![PB124666](/images/blogger/3122924360478465834/2013246339_5de3a794ba.jpg)](http://www.flickr.com/photos/plateau/2013246339/ "PB124666 by plateaukao, on Flickr")  
lac d'Anncey.France  
  
在這邊看到，透過點小設定，可以讓Chrome的網址列充當搜尋引擎，自訂想要的搜尋。之前用Google App Enginen包裝出來的OnlineDict，只有吃由form餵入的資料，也就是只支援post的方式。為了要讓它也可以做為Chrome搜尋用的引擎，就得要為它做點小改變，讓它也支援get方式的查詢才可以。  
  
所以，我改了一下程式碼。有多簡單呢？就copy paste一行程式碼而已。  
原本def get(self)底下是直接呼叫OutputHtml()，現在改成呼叫post(self)，就可以跟post做一模一樣的處理了。  
  

```
#/usr/bin/env python  
  
import cgi  
  
from google.appengine.api import users  
from google.appengine.ext import webapp  
from google.appengine.ext.webapp.util import run_wsgi_app  
  
import os  
from google.appengine.ext.webapp import template  
  
import Dict   
  
class OnlineDic(webapp.RequestHandler):  
    def __init__(self):  
        self.fren_dic = Dict.collins_fren_dict()  
        self.ench_dic = Dict.yahoo_dict()  
        self.eijiro_dic = Dict.eijiro_dict()  
  
    def get(self):  
        self.post()  
          
    def post(self):  
        word = self.request.get('word')  
        dic = self.request.get('dic')  
        if dic == 'Fr-En':  
            content = self.fren_dic.doSearch(word)  
            content = content // handling  
        elif dic == 'Ja-En':  
            content = self.eijiro_dic.doSearch(word)  
        else:  
            content = self.ench_dic.doSearch(word)  
        self.OutputHtml(content,dic)  
          
  
    def OutputHtml(self, content="", dic=""):  
        template_values = { 'content': content,  
                            'dic': dic,  
                            }  
        path = os.path.join(os.path.dirname(__file__), 'index.html')  
        self.response.out.write(template.render(path, template_values))  
  
application = webapp.WSGIApplication(  
                                     [('/', OnlineDic)],  
                                     debug=True)  
  
def main():  
    run_wsgi_app(application)  
  
if __name__ == "__main__":  
  main()  
    
# vim:set nu et ts=4 sw=4 cino=>4:
```

  
網站在此：<http://onlinedict.appspot.com/>  
目前支援法翻英，範例如下：  
http://onlinedict.appspot.com/?dic=Fr-En&word=%s  
英翻中  
http://onlinedict.appspot.com/?dic=En-Ch&word=%s  
日翻英  
http://onlinedict.appspot.com/?dic=Ja-En&word=%s  
  
為了貼上面的程式碼，特別去找了一個透過javascript的syntax highlighter，路徑如下：  
<http://alexgorbatchev.com/wiki/SyntaxHighlighter>  
使用方式可以參考下面這個網址：  
<http://www.craftyfella.com/2010/01/syntax-highlighting-with-blogger-engine.html>
