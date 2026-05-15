+++
title = "How to launch media players with mms protocol in Firefox in Ubuntu"
date = "2009-09-26T13:46:00Z"
slug = "how-to-launch-media-players-with-mms-protocol-in-firefox-in-ubuntu"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/09/how-to-launch-media-players-with-mms.html"
bloggerID = "6759308596186169823"
tags = ["Linux"]
[cover]
  image = "/images/blogger/6759308596186169823/3955817398_96ec8f42c4.jpg"
+++

[![R8075953](/images/blogger/6759308596186169823/3955817398_96ec8f42c4.jpg)](http://www.flickr.com/photos/plateau/3955817398/ "R8075953 by plateaukao, on Flickr")  
Taipei.Taiwan  
  
J'ai fait le bar-bee-cue avec mes colleagues ce matin.  
Cet endroit se situe pres de ma compagnie;    
donc on s'est joint devant la compagnie.  
  
= = =  
  
In order to select a proper media player for the mss protocol in firefox, you have to add some new properties in about:config. Here's what I set for suit my own purpose.  
  
network.protocol-handler.app.mms user set string /usr/bin/X11/smplayer  
network.protocol-handler.external.mms user set boolean true
