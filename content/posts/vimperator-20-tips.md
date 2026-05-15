+++
title = "vimperator 2.0 tips"
date = "2009-06-07T15:11:00Z"
slug = "vimperator-20-tips"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/06/vimperator-20-tips.html"
bloggerID = "3431096859907977089"
tags = ["Computer"]
[cover]
  image = "/images/blogger/3431096859907977089/3600520966_2acfeaf399_m.jpg"
+++

[![R8075502.JPG](/images/blogger/3431096859907977089/3600520966_2acfeaf399_m.jpg)](http://www.flickr.com/photos/plateau/3600520966/ "R8075502.JPG by plateaukao, on Flickr")  
油條.Taipei  
  
I've been using Firefox + vimperator 2.0 for quite some time. It makes my browsing experiences as smoothly as the silk. Today, I found some tips about how to make vimperator even better! These tips exist long before I found them. It's a pity that I did not do much survey on this before.  
  
First of all, some key mappings to make navigation more easily:  
 `map <c-c> Y  
map <c-g> YP  
map j 8<c-e>  
map k 8<c-y>  
map H gT  
map L gt`  
  

With these settings, you can use copy keyboard shortcut as before; the movement of pressing j and k is more obvious now (8 lines each time); and change among the tabs by H and L. It's easier than gt/gT or C-n, C-p.

  

Another good tip that I can't find til today: to disable system input method while switching to command line mode.

  
style -name commandline-ime chrome://\* #liberator-commandline-command input {ime-mode: inactive;}  
  

Moreover, starting from vimperator 2.0, it supports colorscheme just as vim does. You can download several color schemes from following link:

  
http://github.com/VoQn/vimperator-colorscheme/tree  
  

To jump quickly within current opened tabs, you can turn on the numbering label on tabs by following setting:

  
set guioptions=n/N  
  
N means displaying the number on the tab icon; n means displaying the number after the icon.
