+++
title = "How to easily mount iso files in Ubuntu"
date = "2009-05-03T14:24:00Z"
slug = "how-to-easily-mount-iso-files-in-ubuntu"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/05/how-to-easily-mount-iso-files-in-ubuntu.html"
bloggerID = "4893482801200412097"
tags = ["Linux", "Annecy Life"]
+++

[![Courier (by plateaukao)](/images/blogger/4893482801200412097/1481641818_66812d214f.jpg "Courier (by plateaukao)")](http://www.flickr.com/photos/plateau/1481641818/ "Courier (by plateaukao)")  
Courier.Annecy.France  
  
Qu'est-ce qu'il y a??? J'ai oublie ou j'ai prise cette photo. C'est incroyable!!! Il es au milieu d'Annecy. C'est ou je faisais les courses souvent. Apres chercher sur GoogleMap, je le retrouve encore. Il s'appelle Courier~~~  
  

大白天的，還需要開燈嗎？看到天花板全是玻璃和天窗，走道上甚至連海灘傘都出現了。走道兩旁是營業中的店家。大大的走道上，除了服務的櫃台外，還放置了不少沙發。沒錯，是舒舒服服的沙發。讓顧客可以在這兒等人，休息，上網。是的，上網。這兒上網是不用錢的！不少沒有申請網路的學生，都會跑來這兒上網收收信，看看網頁。我是網路重度用者…要到Courier上網對我來說太累了。

  
\*\*\*\*  
  

Sometimes, I download iso files from internet without burning them into real CDs or DVDs, because I am not good at preserving disks and the DVD-ROM of my nb is not functioning well either. As a consequence, when it's necessary to use these iso files or access files inside, I prefer mounting them directly to the system. In Windows, I am pretty satisfied with the free version of Daemon Tools. However, in Linux (Ubuntu), I always need to mount these files manually in a console. It's not a big problem for me because I know these commands well. Nevertheless, it's tiresome to type in the command line every time I want to use them.

I know this is a pain for most linux users too, so I bet there's already an easier solution (or several more). With a simple search in Google, I got the answers I long for. I list the solutions I found below for later reference:

1. command line:

**sudo mkdir /media/iso**  
**sudo modprobe loop**  
**sudo mount -t iso9660 -o loop file.iso /media/iso/**  
  
2. create scripts for nautilus (gnome's file explorer)  
**cd .gnome2/nautilus-scripts/**  
**vi Mount**   

```
#!/bin/bash  
#  
for I in "$*"  
do  
foo=`gksudo -u root -k -m "Enter your password for root terminal access" /bin/echo "got r00t?"`  
sudo mkdir /media/"$I"  
sudo mount -t iso9660 -o loop "$I" /media/"$I" && nautilus /media/"$I" --no-desktop  
done  
done  
exit0
```

  
**vi UMount**  

```
#!/bin/bash  
#  
for I in "$*"  
do  
foo=`gksudo -u root -k -m "Enter your password for root terminal access" /bin/echo "got r00t?"`  
sudo umount "$I" && zenity --info --text "Successfully unmounted /media/$I/" && sudo rmdir "/media/$I/"  
done  
done  
exit0
```

  
make Mount and UMount executable.  

```
chmod +x Mountchmod +x Unmount
```

```
3. use a GUI tool similar to Daemon Tools
```

```
install gisomount
```

```

```

```
REF:
```

```
http://ubuntuguide.org/wiki/Ubuntu:Feisty#How_to_mount.2Funmount_Image_.28ISO.29_files_without_burning
```
