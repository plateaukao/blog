+++
title = "Add Global Hotkeys for OnlineDic on Windows platform"
date = "2008-05-07T20:29:00Z"
slug = "add-global-hotkeys-for-onlinedic-on-windows-platform"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/05/add-global-hotkeys-for-onlinedic-on.html"
bloggerID = "1646829690445729770"
tags = ["Annecy Life", "Online Dictionary", "Ricoh GRD", "Python"]
+++

[![R8070831 (by plateaukao)](/images/blogger/1646829690445729770/2474074696_0f5d8f18cb.jpg "R8070831 (by plateaukao)")](http://www.flickr.com/photos/plateau/2474074696/ "R8070831 (by plateaukao)")  
(Ricoh GRD Marseille, France. ile d'if)  
  
到馬賽沒上伊芙島，大概算不上是到過馬賽吧。不過伊芙島卻一點兒也不吸引我。來回的船票要十歐，上了島，還得一定要再交五歐參觀Chateau d'if才行。(如果有買馬賽一日周遊券的話，會比較划算，因為20歐裡面便包含了來回船票，城堡門票，還可以參觀很多市區內的博物館，一日的交通票，Tram，地鐵，巴士坐到爽，還可以坐上山的市區觀光小火車)。可惜我發現有一日券的時間太晚了，所以沒來得及買。  
  
從伊芙島往陸上看去，海的顏色是漸層的，很夢幻。很多家庭拿著食物，就在城堡四周野餐起來，完全不介意這曾經是個關犯人的地方。小時候看過的"基度山恩仇記"早就忘光了，所以不大體會得到被關在這兒的痛苦。  
  
\*\*\*\*  
  
from long time ago, I've kept trying to add supports of global hotkeys for onlinedic; however, it's always in vain. Tonight, I finally found a way to achieve it!!! (though it only works for Windows platform) Why didn't I find the API earlier, I keep wondering....  
  
This feature is supported by wxWidgets. As consequences, it's been ported to wxPython too. Actually it's quite easy. All I need to do is to invoke RegisterHotKey provided by Frame.  
 `self.RegisterHotKey(  
 self.hotKeyIdToggleScan, #a unique ID for this hotkey  
 MOD_WIN, #the modifier key  
 VK_F3) #the key to watch for`  
The usage of the parameters are rather obvious. The last two parameters should be filled in by definitions from win32con. If you don't have installed win32 extension, you can just find out the right definitions you want to used by the second following references.  
  
Once you want to quit the program, you have to unregister the hotkey:  
 `self.UnregisterHotKey(self.hotKeyIdToggleScan)`  
REF:  
[Sample of RegisterHotKey for wxpython](http://wiki.wxpython.org/RegisterHotKey)  
[Virtual Key Definition in win32con](http://pyxr.sourceforge.net/PyXR/c/python24/lib/site-packages/win32/lib/win32con.py.html)
