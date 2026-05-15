+++
title = "Gradle build error in comman line for Android Studio app projects"
date = "2013-06-01T10:48:00.001Z"
slug = "gradle-build-error-in-comman-line-for-android-studio-app-projects"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/06/gradle-build-error-in-comman-line-for.html"
bloggerID = "4105251298569710537"
tags = ["Programming", "Android"]
[cover]
  image = "/images/blogger/4105251298569710537/IMAG1396_ZOE001-MOTION.gif"
+++

[![](/images/blogger/4105251298569710537/IMAG1396_ZOE001-MOTION.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-WHtgdkil91ENmSTBLGwpAI9QULuGSjCaYJLrnDE1O3sX0ihyphenhyphenyQKP8H77b43aEiu8NebiD3nK4aZHPjabq0M-cMprgc9UpLu6ZM0FitVeZWmMQ2t8bkkcuehDzt9ysZkwS15b89i8y04/s1600/IMAG1396_ZOE001-MOTION.gif)

I saw someone met the same problem on StackOverflow. Fortunately,  I found out how to make it work. So leave some notes here:  
1. upgrade Gradle version to 1.6  
2. Afterward, running "gradle build --stacktrace", you will see that ANDROID\_HOME environment variable is required to be set up.  
3. on Mac, add following line to your ~/.bash\_profile  
export ANDROID\_HOME="/Applications/Android Studio.app/sdk/"  
  
Now it should work like a charm!
