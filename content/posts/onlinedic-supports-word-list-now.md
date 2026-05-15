+++
title = "OnlineDic supports word list now!"
date = "2008-05-16T15:01:00Z"
slug = "onlinedic-supports-word-list-now"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/05/onlinedic-supports-word-list-now.html"
bloggerID = "5134133652107807728"
tags = ["onlineDic"]
+++

[![onlinedic_word_list (by plateaukao)](/images/blogger/5134133652107807728/2497410610_472791d66a.jpg "onlinedic_word_list (by plateaukao)")](http://www.flickr.com/photos/plateau/2497410610/ "onlinedic_word_list (by plateaukao)")  
  
it's awkwardly implemented yesterday. The word list support was not considered in the original design of Dict module so it's hard to find a place to fit it in.  
  
Finally, I decided to add a default function for Dict base class: get\_word\_list(). Currently, this new feature is only supported for dictionary files with stardict format .  
  
After calling match() from FileDB in stardict module, it will not only return the word explanation, but also provide a list of words that are before and after current word.  
  
When the MainWindow receives SearchDone event, it will upate the left side panel if word list is available. If not, the word list panel won't be displayed.
