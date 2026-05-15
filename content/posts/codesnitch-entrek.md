+++
title = "CodeSnitch - Entrek"
date = "2009-04-03T19:14:00Z"
slug = "codesnitch-entrek"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/04/codesnitch-entrek.html"
bloggerID = "1740167091780635489"
tags = ["Windows Mobile"]
+++

[![R8070164 (by plateaukao)](/images/blogger/1740167091780635489/2472518003_6edaefdfda.jpg "R8070164 (by plateaukao)")](http://www.flickr.com/photos/plateau/2472518003/ "R8070164 (by plateaukao)")  
Avignon.France  
  

Recently, I've been busy with digging out some possible memory leaks in the program. Without a good memory tracker, it means endless tests with different scenarios in order to narrow down the files where the code defects may lie on.

  

Some mechanisms are developed for this purpose by other teams; however, it did not help me a lot. Eventually, I gave Entrek CodeSnitch another try. I used it last summer when I just came back from France. The stability of CodeSnitch at that time is horrible! You can't even call it a product. Some patches should be installed in order to make it work on Windows Mobile 5. Even so, some minor tweaks are needed to make it run a little smoothlier. To be worse, it only works with small scale programs. Speaking of our program with a size of around 900 k, don't even think a bout it. Sometimes, the program can't be launched; sometimes, it terminates abnormally. After several weeks' trial, I gave up. I'd rather keep an eye on how I code instead of being a QA for Entrek and discuss the results with their engineers.

But this time, it may be my last resort. I re-checked its website. It seems that Entrek released a new version of CodeSnitch (Well, after all, it's almost a year since I tried it). To my surprise, it runs smoothly with my program this time. Although there's a downloadable trial version, it does not mention that the functionalities are RATHER limited for trial: You can see events and results in the main window; however, you can't see where it happens in the codes (unless you upgrade to paid version).

Well, I believe that my department did buy some licenses from Entrek; so I asked for one the next day. It did do a great job and helped me finding several memory leaks in a short time.

  
REF:  
<http://www.entrek.com/>
