+++
title = "remote debugging with gdb"
date = "2005-12-20T18:30:00Z"
slug = "remote-debugging-with-gdb"
canonicalURL = "https://plateautip.blogspot.com/2005/12/remote-debugging-with-gdb.html"
bloggerID = "113510360900240552"
+++

Hm... some notes for myself:  
  
target: (where the program runs)  
  
 gdbserver host\_ip:port program\_name  
  
host: (debugging site)  
  
gdb program\_name  
 target remote target\_ip:port  
 continue (should be continue instead of run, cause the program is already running)
