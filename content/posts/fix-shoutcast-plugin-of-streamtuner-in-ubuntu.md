+++
title = "fix shoutcast plugin of Streamtuner in ubuntu"
date = "2009-03-01T13:43:00Z"
slug = "fix-shoutcast-plugin-of-streamtuner-in-ubuntu"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/03/fix-shoutcast-plugin-of-streamtuner-in.html"
bloggerID = "2898615677375585088"
tags = ["Linux"]
+++

[![pb120124 (by plateaukao)](/images/blogger/2898615677375585088/392553657_f54c633965.jpg "pb120124 (by plateaukao)")](http://www.flickr.com/photos/plateau/392553657/ "pb120124 (by plateaukao)")  
Purple Sunset   
Taipei.Taiwan  
  

Streamtuner is a good software under linux that can help you to launch internet radios easily. With combination of streamripper, you can even save songs as individual mp3s by just a simple click. However, After upgrading to ubuntu 8.10, Streamtuner fails to display the shoutcast raido listings, which contains most of the radio stations I listen to. That's realy pain in the ass for me. I had to manually insert the radio address for a long time.

Last night, I found the root cause as well as the solution on the internet, thanks to google.

  
  
Here's a quick fix to the problem that I had for a long time.   
  
\*\*\*\*\*   

Here's what you need to do in order to fix the Shoutcast plug-in. Fire up your favorite hex editor and use it to open up the shoutcast.so plug-in found in usr/lib/streamtuner/plugins. Now search for the two instances of www.shoutcast.com and replace them with 205.188.234.120 making sure you keep the spacing sane. Now save it back into your folder. Open up Streamtuner and go to the Shoutcast tab. You should now see your listings. If your don't just click on the Reload button.

  
For those of you who are saying that you don't know how to use a hex editor, no worries. Here is a link to the patched shoutcast plug-in. [Download Plugin](http://launchpadlibrarian.net/18438623/shoutcast.so)  
  
 \*\*\*\*\*\*  
  
REF:  
<http://tazbuntu.blogspot.com/2008/10/shoutcast-bug-in-streamtuner.html>
