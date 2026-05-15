+++
title = "DirDiff: 透過 vim 來比對目錄的差異"
date = "2014-06-12T15:28:00.002Z"
slug = "dirdiff-透過-vim-來比對目錄的差異"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2014/06/dirdiff-vim.html"
bloggerID = "5848435926831965020"
[cover]
  image = "/images/blogger/5848435926831965020/IMAG7089.jpg"
+++

[![](/images/blogger/5848435926831965020/IMAG7089.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMFV_DzXEIypci5yDE-Ed7WQ_w755PfG1y9kX7FiHxkwx6I1-O_HAPEMzeRZYTGCSL2U2T8k2L8H84tTH7vOUqD7kN-bP1tokq_GhBoEIDNj_lYXmJHW-pkXw4vAv6pSTE8uPqcmbcK2Y/s1600/IMAG7089.jpg)

(吳留手.Taiwan)  
  
好久沒有幫朋友慶生了。  
不過這樣說好像我朋友很少的樣子… XD   
  
\*\*\*\*   
最近由於工作上的需要， 得在Mac上找個能夠比較目錄差異的工具。Mac內建的 filemerge雖然可以比對目錄，但呈現的方式又不盡如人意。找來找去，不是要花錢就是不大好用。後來退而求其次，看看是不是有好用的vim plugin可以幫忙解決這個問題。果然一找就找到了，而且用起來還蠻簡易的。  
  
DirDiff，只要在安裝好之後，先進到vim，然後打下面的指令就可以了。  
:DirDiff dir\_a dir\_b  
  
它會在畫面下方列出目錄兩邊各自才有的檔案，再來是兩邊都有卻有差異的檔案列表。用上下鍵移到每個檔案，再按下Enter就可以在上面呈現 diff。  
  
DirDiff.vim:  
<http://www.vim.org/scripts/script.php?script_id=102>
