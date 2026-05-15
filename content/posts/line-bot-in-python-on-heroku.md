+++
title = "line bot in python on Heroku"
date = "2016-12-30T10:25:00Z"
slug = "line-bot-in-python-on-heroku"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2016/12/line-bot-in-python-on-heroku.html"
bloggerID = "5891304227152096248"
tags = ["Bot", "Programming"]
+++

# 加入 cloud storage  
heroku addons:create cloudinary:starter  
  
# 加入 mongodb support  
heroku addons:create mongolab  
  
# ImageSendMessage  
一定要用 https 不然會報錯，然後不知其所以然。
