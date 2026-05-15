+++
title = "New version of Vimperator and some plugins"
date = "2009-01-27T18:58:00Z"
slug = "new-version-of-vimperator-and-some-plugins"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/01/new-version-of-vimperator-and-some.html"
bloggerID = "4903054953261248609"
tags = ["Computer"]
+++

[![PB080634.JPG (by plateaukao)](/images/blogger/4903054953261248609/3014594012_b7e3633348.jpg "PB080634.JPG (by plateaukao)")](http://flickr.com/photos/plateau/3014594012/ "PB080634.JPG (by plateaukao)")  
Seattle.US  
  

I tried to install Vimperator 2.0 several weeks ago ( or one month ago?). The speed of auto completion is aweful. So, I turned back to use version 1.2 without second thoughts. At that time, I know there's still some improvements to go for version 2.0. Tonight, I gave it another try and found it quite joyful! The speed of auto-completion is quite impressive, and the categorized suggestion list is much clearer than older versions. That's the first impression I had for this new version. Out of interests, I searched for other useful plugins too. I installed char-hints-mod2.js, gvimail.js, and lookupDictionary.js.

  

char-hints-mod2.js is a plugin to display character hint labels instead of digits. It will reduce more finger movements for keyboard lovers and you can even set up the characters you like! Now, I don't have move my fingers all around, or go back and forth with my mouse. I can stick on my keyboard, almost all the time.

  

gvimail.js is a plugin to solve the conflicts between gmail and vimperator. When I used gmail, I can only go back to my stupid mouse and use click. It's quite painful to do so once you get used to the vimperator. gvimail can solve this problem for me. I can use gmail as I like with vimperator!

  

Last one, lookupDictionary is a plugin written by a Japanese. It seems that vimperator is very popular in Japan because a lot of Japanese wrote plugins for it. Fortunately, I can read Japanese. It's not a hidden world for me. this plugin has some built-in dictionaries. You can use the vimperator command line to search these dictionaries. It will bring out a window with -- more, when the search is done. In this way, you can lookup word without leaving the lovely firefox. I thought this is a plugin to search word in the webpage directly. Obviously, I was wrong. I hope that one day it's powerful enough to do so.

`javascript 〈〈EOF  
(function(){  
var feedPanel = document.createElement("statusbarpanel");  
feedPanel.setAttribute("id", "feed-panel-clone");  
feedPanel.appendChild(document.getElementById("feed-button"));  
feedPanel.firstChild.setAttribute("style", "padding: 0; max-height: 16px;");  
document.getElementById("status-bar")  
 .insertBefore(feedPanel, document.getElementById("security-button"));  
})();  
EOF`
