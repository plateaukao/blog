+++
title = "Create an uninstaller for setup project in Visual Studio"
date = "2009-02-06T15:39:00Z"
slug = "create-an-uninstaller-for-setup-project-in-visual-studio"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/02/create-uninstaller-for-setup-project-in.html"
bloggerID = "4578549507194821697"
tags = ["Computer"]
[cover]
  image = "/images/blogger/4578549507194821697/3033314540_a32c1c2823_b.jpg"
+++

[![R1040868.JPG](/images/blogger/4578549507194821697/3033314540_a32c1c2823_b.jpg)](http://www.flickr.com/photos/plateau/3033314540/ "R1040868.JPG by plateaukao, on Flickr")  
Seattle.US  
  
regarde, quel beau le temp!  
  
\*\*\*\*  
  
In order to easily uninstall the software installed by msi file, which is created by setup project in Visual Studio, I searched a bit on the internet.  
  
At first, I have to create a bat file in my application folder of my set up project. And then, write in msiexec \x {xxxx-xxxx} in the bat file with proper product code, which can be found in the property of the setup project.  
  
Create a shortcut for the bat file in the program menu. And then, when the msi file is installed, you can find the uninstall shortcut.   
  
voila.  
  
http://www.simple-talk.com/dotnet/visual-studio/updates-to-setup-projects/
