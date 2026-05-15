+++
title = "Streamtuner and Streamripper in Linux"
date = "2008-07-22T15:30:00Z"
slug = "streamtuner-and-streamripper-in-linux"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/07/streamtuner-and-streamripper-in-linux.html"
bloggerID = "5409155854431738400"
tags = ["Computer", "Linux", "Olympus E300"]
+++

[![PB124789 (by plateaukao)](/images/blogger/5409155854431738400/2012710547_6cda7837f2.jpg "PB124789 (by plateaukao)")](http://www.flickr.com/photos/plateau/2012710547/ "PB124789 (by plateaukao)")  
Olympus E300  
Annecy. France  
2007.11.12  
  
相機參數亂調，結果就是這樣。  
雖然葉子黃得有點誇張，不過很喜歡這種畫筆亂灑的感覺。  
  
\*\*\*\*  
  

It's been a long time that I did not write posts in English. I am not sure that I am still capable of writing in English properly. Anyway, I still have to try , because this post is about software introduction for Linux (Ubuntu).

  

After the application of ADSL internet access, I am thinking of any way to maximize the usage of the bandwidth. One way I can think of is, of course, to download some good stuff by using bt. And another thing I would like to do is to record some internet radio programs, so that I can listen to the musique (or talk shows) without using the bandwith at work.

  

I used to use mplayer -dumpstream to do the job for me. However, after reinstalling linux for several times in these years, I lost all my information of the internet radios. This time, I want some software that can manage internet radios and record the programs when I want it to, just like Fr-Solo in Windows platform. Fortunately, it seems that a lot people have the same requirement as I do. I found one without spending too much time on googling the solution.

  

Streamtuner. It's a program written with GTK+2.0 interface. It supports internet radio directories such as SHOUTcast and Live365. If it's not enough for you, you can add the web radios you like in another tab page too. The detail feature list is on the website, I won't write all of them here. I just want to mention its seamless combination with Streamripper. Streamripper started as a way to separate tracks via Shoutcast's title-streaming feature. Now it's more powerful about how to separate songs from the streaming media.

  

In the interface of Streamtuner, there are buttons for triggering the radio channels and for recording the programs too. Once the record button is pushed, streamripper will be launched in a terminal window to do the recording job.

  

I was impressed the first time I saw the recording folder for a channel. It's full of separate files with filenames of songs. It takes no effort to have some many songs in one night!

  
REF:  
<http://www.nongnu.org/streamtuner/>  
<http://streamripper.sourceforge.net/>
