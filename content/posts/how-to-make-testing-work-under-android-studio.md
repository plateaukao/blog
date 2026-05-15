+++
title = "How to make testing work under Android Studio"
date = "2013-06-03T18:10:00.002Z"
slug = "how-to-make-testing-work-under-android-studio"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2013/06/how-to-make-testing-work-under-android.html"
bloggerID = "5121282738638358012"
tags = ["programming", "Android"]
[cover]
  image = "/images/blogger/5121282738638358012/2044110721_0ef215ae91_b.jpg"
+++

[![](/images/blogger/5121282738638358012/2044110721_0ef215ae91_b.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRwdn-OO7RZKl-TOaAR_dCycKGE6rbR5gzsgfBeKfDdxBKWSyK9JGLMHe30e1oDSjrJ21NzdxDDYRzVKnLDxiB29grSsUyw3y7_AVIv2fbAegotzEN1_8mxvhbS2D0NR3jg7ju5zlTEoY/s1600/2044110721_0ef215ae91_b.jpg)

(Geneve.Swiss)  
  
It's such a pain to look for solutions for tasks on Android Studio. When can it be mature enough and more well documented for developers?  
  

I would like to write some test cases for my small app, but I couldn't find a way for adding test cases into Android Studio project and have it run successfully.

  

After wandering around on the internet for a long time, eventually I found a link that did helped me out (see reference below). As Google I/O 2013 video said, a new android build system made of gradle is released, which will be more flexible, more powerful, more etc, etc. However, currently, it 's not well integrated into Android Studio. Some modification in Android Studio won't be directly reflected in gradle build scripts. Well... then, how do I know when I should modify build scripts my self? And to write it by myself, I have to learn groovy first, because that's the language Gradle used to write its build configuration files. How could I master these things in a short time...

  
Anyway, the solution for my pain point above is to modify build.gradle under the root directory of app project, and make sure all the instrument source folders are well set up. Now I can use cradle to run test cases and generate report files. However, I can't make it work in Android Studio still. orz...  
  
  
REF:  
<http://blog.crowdint.com/2013/05/24/android-builds-on-travis-ci-with-gradle.html>
