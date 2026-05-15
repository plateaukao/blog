+++
title = "Flickr Random Image Picker"
date = "2010-04-03T19:54:00Z"
slug = "flickr-random-image-picker"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2010/04/flickr-random-image-picker.html"
bloggerID = "4571922296128273415"
tags = ["Computer", "Python"]
[cover]
  image = "/images/blogger/4571922296128273415/2600248130_711ec4f94e.jpg"
+++

[![P6216480](/images/blogger/4571922296128273415/2600248130_711ec4f94e.jpg)](http://www.flickr.com/photos/plateau/2600248130/ "P6216480 by plateaukao, on Flickr")  
Annecy.France  
  
It's a small tool written to randomly show my photos from flickr. I quite enjoy viewing photos in this way. It helped me to discover photos that I didn't notice before. However, there are some limitations to it:  
1. in current configuration, 10 photos will be shown every time I launch it. it takes too much time to do so. I have to wait for tens of seconds or even longer.  
2. in GUI version, no thread is implemented, so the UI is blocked after the button is pressed.  
  
To make it better, I did some minor changes:  
1. create a thread for fetching photos from flickr, and use wx events to post event to htmlwindow. Don't know how to use lock or mutex under python yet, though...  

```
import threading  
from time import sleep  
  
(FetchDoneEvent, EVT_FETCH_DONE) = wx.lib.newevent.NewEvent()  
  
class FetchThread(threading.Thread):  
    def __init__(self,w):  
        threading.Thread.__init__(self)  
        # windows for posting events  
        self.w = w  
  
    def run (self):  
        fi = None  
        for x in range(10):  
            print x  
            if fi == None:  
                (content,fi) = fetch_photo()  
            else:  
                content = fetch_photo(fi)  
  
            evt = FetchDoneEvent(source=content)  
            while (self.w.loading):  
                sleep(0.5)  
            wx.PostEvent(self.w, evt)  
  
class MyHtmlWindow(html.HtmlWindow):  
    def __init__(self, parent, id ):  
        html.HtmlWindow.__init__(self, parent, id, style=wx.NO_FULL_REPAINT_ON_RESIZE)  
        self.Bind(EVT_FETCH_DONE, self.OnFetchDone)  
        self.loading = 0  
  
    def OnLinkClicked(self, linkinfo):  
        import  os  
        os.startfile(linkinfo.GetHref())  
  
    def OnFetchDone(self, e):  
        #self.LoadPage("myflickr.html")  
        self.loading = 1  
        if self.start_fetching != 1:  
            self.AppendToPage(e.source)  
        else:  
            self.SetPage(e.source)  
            self.start_fetching = 0  
        self.loading = 0  
  
class SimpleFrame(wx.Frame):  
  
    def __init__(self, *args, **kwargs):  
        ...  
  
    def OnButtonClicked(self,e):  
        FetchThread(w=self.html).start()  
        self.html.SetPage("

# Fetching......

")  
        self.html.start_fetching = 1
```

2. add a function to only return a photo info at a time, instead of returning a html file with 10 photo infos.  

```
def fetch_photo(fi=None):  
    print 'fetch_photo'  
    if fi == None:  
        fi = FlickrIndex(API_KEY, SECRET_KEY, MY_USER_ID)      
        return fi.print_random_photos(10),fi  
    else:  
        return fi.print_random_photos(10)
```
