+++
title = "cross thread for control handling in C#"
date = "2009-01-20T05:38:00Z"
slug = "cross-thread-for-control-handling-in-c"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/01/cross-thread-for-control-handling-in-c.html"
bloggerID = "8229885877362660858"
tags = ["Computer"]
+++

[![P9200257 (by plateaukao)](/images/blogger/8229885877362660858/392809639_36f7a57ac5.jpg "P9200257 (by plateaukao)")](http://www.flickr.com/photos/92383858@N00/392809639/ "P9200257 (by plateaukao)")  
Home.Chez moi  
  
波紐～～～  
mais c'est pas vraiment de poisson d'or.  
  
\*\*\*\*  
  

In order to reduce the efforts of getting latest version of source codes from perforce server and compile it on the machine, I used the p4api .NET library in my program. However, it's a long process; so I have to use another thread to handle this task, and bring out the message sometimes to know current progress. I encountered a problem as the title says -- cross thread control handling. my task is done in a newly created thread; and the message will be printed in a listbox control, which is created by the main thread. To utilize the control in another thread, the delegation mechanism should be used. It's not so complicated. Here's a simple sample from codeproject.

  
<http://www.codeproject.com/KB/cs/Cross_Thread.aspx>
