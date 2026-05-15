+++
title = "A small utility to customize Manila Program Tab on HTC Windows Mobile devices"
date = "2009-06-12T17:25:00Z"
slug = "a-small-utility-to-customize-manila-program-tab-on-htc-windows-mobile-devices"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/06/small-utility-to-customize-manila.html"
bloggerID = "7979863045245312188"
tags = ["Windows Mobile"]
+++

[![2009-06-13_005711 (by plateaukao)](/images/blogger/7979863045245312188/3619245699_815989c5eb.jpg "2009-06-13_005711 (by plateaukao)")](http://www.flickr.com/photos/plateau/3619245699/ "2009-06-13_005711 (by plateaukao)")  
ManilaProgramSetting  
  

Because I constantly re-install my devices with different ROM builds, I used to installing softwares into my SD card. Although I don't have to reinstall all these softwares, every time I want to launch them, I have to launch File Explorer first; go to that directoy on SD card. And finally luanch it manually. It's so tiresome that I wanna configure these apps in my Manila Program Tab, so that I can launch them by no more than two clicks.

  

Current Manil Program Tab design only allows you to add programs which are listed in \windows\Start Menu\Programs. In official way, it's not possible to do so. As a consequence, I decided to write a small utility to help myself on this boring task, and by the way, I can practice my poor C# coding skills a bit.

  
  

It's very easy to create UI layouts with C# (though it's usually very ugly). As you can see on the screenshot, there are two buttons on the top, so that user can easily switch to other program icon settings. File Path and Display Name is what we need to fill in the registry keys. When you switch to a program icon, current setting will be brought out. And then, you can press "Select File" button to any other exe files on the device (or SD card). Before switching to other program icon, remember to press LSK: Update, to write the modification back to registry key.

  

Finally, you can exit the program and go to Manila Program Tab and take a loot. What? it's not as what you modified? oh, because Manila does not know you changed its registry keys. You need to do something to let it reresh the UI. this is very easy too: just press RSK: Remove and then press Done again. Your modification will be shown now.

  
Programming Tips:  

1. MS built-in OpenFileDialog really sucks!!! It will teat "My Documents" as root, and only lists files under it and one more subdirectory. It's not useful for most of the applications!! Anyway, I don't wanna write one by myself; so I found some simple classes written by others on the internet. It's from Reference 1. With his efforts, I can get my exe file name on sd cards now.

  
2. In order to read registry key, Microsoft.Win32 should be used. Here's how I use it:  
 RegistryKey regManilaSetting = Registry.LocalMachine;  
 regManilaSetting = regManilaSetting.OpenSubKey(@"Software\HTC\Manila\ProgramLauncher\" + (string)comboBox1.SelectedItem,true);  
 textBoxPath.Text = (string)regManilaSetting.GetValue(@"Path");  
  
  
  
REF:  
1. [MobilePractices](http://www.mobilepractices.com/2008/02/custom-openfiledialog-implementation.html)  
  
Download:  
<http://daniel.kao.googlepages.com/ManilaProgramSetting.exe>
