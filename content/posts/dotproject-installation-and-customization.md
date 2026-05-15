+++
title = "dotProject installation and customization"
date = "2008-11-15T00:14:00Z"
slug = "dotproject-installation-and-customization"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/11/dotproject-installation-and.html"
bloggerID = "4291648494387931354"
tags = ["Travail", "Computer"]
[cover]
  image = "/images/blogger/4291648494387931354/2612236945_68b31e55d9.jpg"
+++

[![P3304429](/images/blogger/4291648494387931354/2612236945_68b31e55d9.jpg)](http://www.flickr.com/photos/plateau/2612236945/ "P3304429 by plateaukao, on Flickr")  
Tulips in Annecy.France  
  

After working for several months, it's gettting harder and harder to keep track of the working items among team members. Everyone needs to write an email to me to update his todo items and complete items every week. After the meeting, I summarize all the emails into one meeting notes. It does work; however, it's hard to know the progress for each item, and it's difficult to keep track of assigned tasks if I don't write it down, and team member forgets to write it down either.

  

Therefore, I started to survey open source tools that may fit my requirement. Not knowing why, I found dotProject and tried to installed it on my notebook. The system pre-request is a long list, including a runnable web server with php scripting language, a usable database, and etc. Following the recommendation on the offical wiki site, I downloaded apache2riad package, which is a all-in-one solution. It contains all the servers I need for running dotproject. And then I installed dotproject in it successfully. The layout of the webpage is professional, with a lot of items to use.

The main concept of dotproject is: company->(department)->project->tasks. The user administration is included too. A forum is ready for use as well. In the begining, I was confused by all the options and was not sure about the sequence of using the system. However, after two-day usage, I am getting used to it and found its task management/report quite useful for tracking works.

There's one minor bug though, during my recent usage: the week day names and month names can't be correctly dislayed in the built-in calendar view. It's kind of annoying reviewing the calendar without knowing which month I am looking and what day it is. I searched a bit on the internet about this problem. It seems to be related to the set locale thing. dotProject gets the default locale from operating system instead of from its own configuration settings. As a consequence, the sub-string funciton on multi-byte names will mess up the layout. The solution is quite simple if only the english locale is needed: put the following line into some functions in **PEAR\Date\Calc.php**:

**setlocale(LC\_TIME, "en");**

functions:

**function getMonthNames( )**

**function getWeekDays( )**

**function dateNow( )**

It looks better now!

REF:

<http://www.dotproject.net/>
