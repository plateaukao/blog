+++
title = "讓 mac 可以顯示 remote 端的 raspberry pi 的 linux 畫面"
date = "2014-10-27T17:56:00Z"
slug = "讓-mac-可以顯示-remote-端的-raspberry-pi-的-linux-畫面"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2014/10/mac-remote-raspberry-pi-linux.html"
bloggerID = "8583338566013041465"
+++

1. 安裝 XQuartz X11 server  
  
2. 設定 sshd 的 config 讓它支援 xforwarding  
  

```
Host *
    ForwardAgent yes
    ForwardX11 yes
    ForwardX11Trusted yes
```

  
3. 利過 ssh -Y (or -X) plateau@xxx.xx.xxx 連到遠端的主機上  
  
ps. 設定 xterm 的字型大小可以用下面指令開啟 app  
  
xterm -fa 'Monospace' -fs 12&
