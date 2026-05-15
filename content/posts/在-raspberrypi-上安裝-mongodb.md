+++
title = "在 raspberrypi 上安裝 mongodb"
date = "2014-07-23T05:04:00.004Z"
slug = "在-raspberrypi-上安裝-mongodb"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2014/07/raspberrypi-mongodb.html"
bloggerID = "8011221910639584033"
tags = ["RaspberryPi"]
[cover]
  image = "/images/blogger/8011221910639584033/4107616709_5d1be58bb9_o.jpg"
+++

[![](/images/blogger/8011221910639584033/4107616709_5d1be58bb9_o.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-omuZlBk7xfXCODYkUcJrXe9JJrlKXQCbwnkNAk4lKUMdzbZmk1tgY0UEu3eCR3uMuF3Pu1ukko6Pr30XMQEouUcROy2SovI4ckZ7O3mu-mi8b9EXpkaAoYDMuzNv1dwUDTgaVuKFmE4/s1600/4107616709_5d1be58bb9_o.jpg)

(Central Park.New York.US)  
  
忘了為什麼要裝 MongoDB 了。不過看來要編繹的話，要很久，所以找到了一個 binary zip 來安裝。解開 zip 後，要用 root 執行下面這些指令，然後，就可以用了。  
> ```
> adduser --firstuid 100 --ingroup nogroup --shell /etc/false --disabled-password --gecos "" --no-create-home mongodb
>
> cp -R mongodb-rpi/mongo /opt
> chmod +x /opt/mongo/bin/*
>
> mkdir /var/log/mongodb 
> chown mongodb:nogroup /var/log/mongodb
> mkdir /var/lib/mongodb
> chown mongodb:nogroup /var/lib/mongodb
>
> cp mongodb-rpi/debian/init.d /etc/init.d/mongod
> cp mongodb-rpi/debian/mongodb.conf /etc/
>
> ln -s /opt/mongo/bin/mongod /usr/bin/mongod
> chmod u+x /etc/init.d/mongod
>
> update-rc.d mongod defaults
> /etc/init.d/mongod start
> ```

  
REF:  
<http://www.widriksson.com/install-mongodb-raspberrypi/>
