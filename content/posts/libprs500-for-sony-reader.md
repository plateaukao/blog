+++
title = "libprs500 for SONY READER"
date = "2008-01-22T10:12:00Z"
slug = "libprs500-for-sony-reader"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/01/libprs500-for-sony-reader.html"
bloggerID = "895369896837961734"
tags = ["Olympus E300", "SONY READER"]
+++

[![Elephant Fountain (by plateaukao)](/images/blogger/895369896837961734/2205183132_762d3b8e45.jpg "Elephant Fountain (by plateaukao)")](http://www.flickr.com/photos/plateau/2205183132/ "Elephant Fountain (by plateaukao)")  
(Olympus E300 Chambery. Elephant Fountain)  
  
Finally I got it working for me!!!  
  
I installed it several days ago; however, when I tried to launch it, it told me that something wrong with the sqllite3:  
> Traceback (most recent call last):  
>  File "main.py", line 827, in   
>  File "main.py", line 816, in main  
>  File "main.py", line 154, in \_\_init\_\_  
>  File "libprs500\gui2\library.pyo", line 405, in set\_database  
>  File "libprs500\gui2\library.pyo", line 125, in set\_database  
>  File "libprs500\library\database.pyo", line 741, in \_\_init\_\_  
>  File "libprs500\library\database.pyo", line 602, in create\_version1  
> sqlite3.OperationalError: database schema has changed  
> Traceback (most recent call last):  
>  File "main.py", line 827, in   
>  File "main.py", line 816, in main  
>  File "main.py", line 154, in \_\_init\_\_  
>  File "libprs500\gui2\library.pyo", line 405, in set\_database  
>  File "libprs500\gui2\library.pyo", line 125, in set\_database  
>  File "libprs500\library\database.pyo", line 741, in \_\_init\_\_  
>  File "libprs500\library\database.pyo", line 602, in create\_version1  
> sqlite3.OperationalError: table books already exists

I don't wanna find out what's wrong with it and did not spend much time on searching a solution for it. But I did know it may be caused by the early installation of python on my system.  
  
Today, I surfed MobileRead website as usual and did a simple search: voila! I got the answer in this discussion thread:  
  
<http://www.mobileread.com/forums/showthread.php?t=15102&page=8>  
  
It seems that someone encountered the same problem as I did. The author of libprs500 jumped out and gave an answer to it. That's how I fixed the problem. Simple, isn't it?  
  
I will give out more details of libprs500 later.
