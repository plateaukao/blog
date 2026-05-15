+++
title = "Sqlite Commands in Terminal"
date = "2014-05-24T17:10:00Z"
slug = "sqlite-commands-in-terminal"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2014/05/sqlite-commands-in-terminal.html"
bloggerID = "1275633876043124496"
tags = ["Computer", "Android"]
[cover]
  image = "/images/blogger/1275633876043124496/8989297086_0d7c0a4ca6_o.jpg"
+++

[![](/images/blogger/1275633876043124496/8989297086_0d7c0a4ca6_o.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_pon3b3H8hupWDiagKfBTv2fy5rG5oRXZPCujHpzMGuBRd11IALGAZK9by7wUSKKI7YweA4Le4hM8m2dYusCB01yF3NzYiTa-WDttHnjO1RDuCsB_dpw0q4woyxly1jozxkv1G_8zyvQ/s1600/8989297086_0d7c0a4ca6_o.jpg)

(Shimen.Taiwan)  
  
Recently, I need to use sqlite commands to check data for my android app. Thanks to the rooted android ROM, the shell environment is much useful than before. It's possible to use Tab key to auto complete filenames and directories, and I can use sqlite3 command directly in adb shell. It saved time from pulling the database file out back and forth.  
  
However, it's been quite a while that I almost forgot how to deal with a sqlite database. The following link is a handy Url to help me on this:  
  
http://www.sqlite.org/cli.html  
  
To name a few:  
.mode  // select different modes, eg, list, line, column  

```
select * from tbl1; // select all from table tbl1
```

```
 
```
