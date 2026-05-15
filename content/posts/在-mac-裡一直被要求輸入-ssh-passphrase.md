+++
title = "在 mac 裡，一直被要求輸入 ssh passphrase"
date = "2017-02-16T07:01:00.002Z"
slug = "在-mac-裡一直被要求輸入-ssh-passphrase"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2017/02/mac-ssh-passphrase.html"
bloggerID = "6763686174160027143"
tags = ["SSH", "Mac"]
+++

不知道從哪次更新後，每次要用 git 指令跟遠端的 git server 互動時，都會跳出輸入 passphrase 的要求。一次兩次還好，久了就覺得很煩。  
  
上網找了一下，只要在 ~/.ssh/config 中加入下面這一小段，就可以了。  

```
Host *
    UseKeychain yes
```

  
  
參考網址：  
<http://superuser.com/questions/1127067/macos-keeps-asking-my-ssh-passphrase-since-i-updated-to-sierra>
