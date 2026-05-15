+++
title = "le chat qui voit / improvement of FlickrRandomImage"
date = "2008-06-05T13:33:00Z"
slug = "le-chat-qui-voit-improvement-of-flickrrandomimage"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/06/le-chat-qui-voit-improvement-of.html"
bloggerID = "3834180221160781131"
tags = ["Computer", "Olympus E300"]
[cover]
  image = "/images/blogger/3834180221160781131/390302030_094cbffeea.jpg"
+++

[![p4050108](/images/blogger/3834180221160781131/390302030_094cbffeea.jpg)](http://www.flickr.com/photos/plateau/390302030/ "p4050108 by plateaukao, on Flickr")  
Olympus E300  
Taipei, Taiwan  
20060405  
  
旁觀者  
  
\*\*\*\*  
  
Originally, FlickrRandomImage only shows 10 images from a random page of my flickr account. I found that it's not so interesting. I want the results to be more various; in other words, I want to have 10 images individually from different pages, instead of from the same page.  
  
In order to make this modification, at first I have to know the total amount of my photos on flickr. I can get a Person object by calling the following API:   
 `Flickr.PeopleGetInfo(userid);`  
and then, with the Person object, I can access **PhotosSummary** object in which there's an attribute -- **PhotoCount**.  
  
Now, I can create a **PhotoSearchOptions** object with **PerPage = 1** and **Page = a\_random\_number\_genereted\_between\_1\_and\_photoAmount**  
  
Do a for loop for 10 times. That's it! Quite Simple, n'est-ce pas?  
  
Somehow, I found the performance is quite slow. Anyways, it works now. I will find another day to fix the performance issue.  
  
ps. With my new modification, I found this cute cat.
