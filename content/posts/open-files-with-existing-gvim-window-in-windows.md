+++
title = "Open files with existing Gvim window in Windows"
date = "2005-10-06T06:53:00Z"
slug = "open-files-with-existing-gvim-window-in-windows"
canonicalURL = "https://plateautip.blogspot.com/2005/10/open-files-with-existing-gvim-window.html"
bloggerID = "112858167130714029"
+++

from Vim Tip #1003:  
  
`For example,  
  
assoc .php=PHPFile  
ftype PHPFile="C:\Program Files\Vim\Vim63\gvim.exe" --remote "%1"  
  
then whenever you double click a .php file in explorer, it will be opened in existing Gvim window (or it will open new Gvim window if there is no already opened Gvim window).`
