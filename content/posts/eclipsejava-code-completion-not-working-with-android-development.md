+++
title = "Eclipse/Java code completion not working with Android development"
date = "2013-05-14T23:01:00.003Z"
slug = "eclipsejava-code-completion-not-working-with-android-development"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/05/eclipsejava-code-completion-not-working.html"
bloggerID = "4151509157271445010"
tags = ["Android", "eclipse"]
[cover]
  image = "/images/blogger/4151509157271445010/5009629221_af0f304ee4_b.jpg"
+++

[![](/images/blogger/4151509157271445010/5009629221_af0f304ee4_b.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWD5DajVevEEXO70JJYqbtuGDomjvxH1OhU6sTdprq4kdBarjOt4570fYwX6qtMYEUNWCgRdWH277rrOjoUy7Ixg7XmO0mKyPdckLKSBp84y7ySxXJ0kSEvldFB1Id4Qy1UhGL_PL0Gco/s1600/5009629221_af0f304ee4_b.jpg)

(GreatWall.Beijin.China)  
  

While watching some video tutorials about android development, I found that the lecturer can call out the class completion helper dialog during typing class names. However, I only have the function/variable autocompletion feature after typing a . after a class name in my eclipse. Without entering the class name correctly, I can not get any help from eclipse, which is quite strange comparing to what I've seen for others.

Well, it seems that many people encountered the same problem as I did. This is being discussed on various posts. One way to make it work is to check the "Java Proposal" in Eclipse's `Preferences > Java > Editor > Content Assist > Advanced`'.

But for me, it seems that something's wrong with my workspace configurations too. The answer from [hoipolloi](http://stackoverflow.com/users/788883/hoipolloi) in following reference post helped me to fix this issue. Here's his suggestion:

- Quit Eclipse
- Go to workspace/.metadata/.plugins/org.eclipse.jdt.core
- Remove \*.index and savedIndexNames.txt
- Restart Eclipse and search Ctrl+T for the offending type. The indexes will be rebuilt.

  
REF:  
<http://stackoverflow.com/questions/908489/eclipse-java-code-completion-not-working>
