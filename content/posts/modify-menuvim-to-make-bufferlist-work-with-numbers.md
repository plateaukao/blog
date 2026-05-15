+++
title = "modify menu.vim to make bufferlist work with numbers"
date = "2005-09-27T06:14:00Z"
slug = "modify-menuvim-to-make-bufferlist-work-with-numbers"
canonicalURL = "https://plateautip.blogspot.com/2005/09/modify-menuvim-to-make-bufferlist-work.html"
bloggerID = "112780185964556829"
+++

in line 720, I did the following modifications:  
  

```
  let name2 = fnamemodify(name, ':t')  
  if a:bnum >= 0  
    " daniel  
    let name2 = name2 . ' (' . '&' . a:bnum . ')'  
    "let name2 = name2 . ' (' . a:bnum . ')'  
  endif  
  let name = name2 . "\t" . BMTruncName(fnamemodify(name,':h'))  
  let name = escape(name, "\\. \t|")  
  " daniel  
  "let name = substitute(name, "&", "&&", "g")  
  let name = substitute(name, "\n", "^@", "g")  
  return name  
endfunc
```
