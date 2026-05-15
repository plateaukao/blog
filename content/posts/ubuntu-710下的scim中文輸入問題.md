+++
title = "ubuntu 7.10下的scim中文輸入問題"
date = "2008-04-07T18:45:00Z"
slug = "ubuntu-710下的scim中文輸入問題"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/04/ubuntu-710scim.html"
bloggerID = "3742659124418575106"
tags = ["Annecy Life", "Linux", "Ricoh GRD"]
[cover]
  image = "/images/blogger/3742659124418575106/2396031127_c09a764571.jpg"
+++

[![RIMG0168](/images/blogger/3742659124418575106/2396031127_c09a764571.jpg)](http://www.flickr.com/photos/plateau/2396031127/ "RIMG0168 by plateaukao, on Flickr")  
(Ricoh GRD Annecy. Cat)  
  
我知道你被綁著很不高興，  
不過也用不著瞪我嘛…  
  
\*\*\*\*  
  
這幾天在用ubuntu 7.10時，常會發生scim無法在emesene或是其他軟體輸入的情況。  
為此，我得要重開程式才行。  
剛剛找了一下網路上的資料（果然不光是只有我一個人遇到而已），  
發現好幾個source都有同樣的解法，  
我也搞不清哪個是源頭，只好在下面隨便附上一個我找到的link。  
解法則如下：  
  
 im-switch -s scim -z default  
 sudo apt-get install scim-qtimm  
 sudo apt-get install scim scim-pinyin scim-tables-zh im-switch scim-qtimm scim-bridge scim-bridge-client-gtk scim-bridge-client-qt scim-bridge-agent  
  
编辑im-switch生成的scim配置文件  
gksu gedit /etc/X11/xinit/xinput.d/scim  
将默认的 GTK\_IM\_MODULE=scim 修改为 GTK\_IM\_MODULE="scim-bridge"。保存退出.  
  
在scim Setup中進行下面的設定：  
scim设置－>全局设置－>将预编辑字符串嵌入到客户端中 前的勾去掉  
scim设置->gtk->嵌入式候选词标的勾去掉.  
  
重启scim  
打开终端,输入 pkill scim  
然后输入 scim -d  
  
\*\*\*\*  
  
聽說這樣子不但能讓我的輸入法不再三不五時出錯，  
還可以順便解決scim不能正常Onspot顯示候選字的問題。  
（這個問題我比較沒注意到，因為我都是盲打，很少在看候選字的）  
  
Reference Site:  
<http://askcuix.javaeye.com/blog/178916>
