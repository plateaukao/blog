+++
title = "SONY DPT-CP1: 加上 KOReader 啟動圖示及安裝 AssistiveTouch, 萊姆輸入法"
date = "2024-06-10T08:50:09.713Z"
description = "這篇文章講說明如何在系統選單中加入 KOReader 圖案，並且，在設備上顯示懸浮球，方便返回上一步和開啟系統選單。"
slug = "sony-dpt-cp1-加上-koreader-啟動圖示及安裝-assistivetouch-萊姆輸入法"
canonicalURL = "https://medium.com/@danielkao/sony-dpt-cp1-%E5%8A%A0%E4%B8%8A-koreader-%E5%95%9F%E5%8B%95%E5%9C%96%E7%A4%BA%E5%8F%8A%E5%AE%89%E8%A3%9D-assistivetouch-%E8%90%8A%E5%A7%86%E8%BC%B8%E5%85%A5%E6%B3%95-3fea512ed890"
mediumID = "3fea512ed890"
tags = ["電子書閱讀器"]
[cover]
  image = "/images/3fea512ed890/1_eggxpN7QAmHDunKlGw3iSQ.png"
+++


![](/images/3fea512ed890/1_eggxpN7QAmHDunKlGw3iSQ.png)

這篇文章講說明如何在系統選單中加入 KOReader 圖案，並且，在設備上顯示懸浮球，方便返回上一步和開啟系統選單。

### 在系統 Launcher 加上 KOReader App 圖案

本小節的作法主要是參考[這個連結](https://github.com/HappyZ/dpt-tools/wiki/ADB-Tricks,-DIY-Launcher-App#launcher-app)。如果對於 Android 開發有點概念的話，操作上很容易。但，就算沒有概念的話，一步步照著作也是可以的。

1. /etc/dp\_extensions 是系統用來放選單中每一個按鈕的設定。我們先將 Launcher 中的隨便一個設定目錄複製到電腦中。這邊舉的例子是 NoteCreator。

```
adb pull /etc/dp_extensions/NoteCreator
```

2. 再來是把這份目錄以及下面的每個檔案根據我們想要新增的應用作調整。首先，是把目錄名稱和檔案名稱都改掉。這邊以 KOReader 當例子的話，要進行以下的操作。

```
cp -R NoteCreator  KOReader  
cd KOReader  
mv NoteCreator_extension.xml KOReader_extension.xml  
mv NoteCreator_strings-en.xml KOReader_strings-en.xml  
mv NoteCreator_strings-ja.xml KOReader_strings-ja.xml  
mv NoteCreator_strings-zh_CN.xml KOReader_strings-zh_CN.xml  
mv ic_homemenu_createnote.png ic_homemenu_koreader.png
```

3. 改好檔名後，開啟 KOReader\_extension.xml，這是指定按鈕被點擊時要怎麼啟動 App。這需要你先知道你想呼叫的 App 的 main activity 名稱才行。以 KOReader app 為例，這可以在其 github repo 中的 AndroidManifest.xml 中找到。找到後，把內容中的 name 和 component, icon 換掉。修改如下：

```
<LauncherEntry name="NoteCreator" category="Launcher" uri="intent:#Intent;launchFlags=0x10000000;component=com.sony.apps.notecreator/.activities.MainActivity;end" string="STR_ICONMENU_1005" icon="ic_homemenu_createnote.png" order="5"/>  
=>  
<LauncherEntry name="KOReader" category="Launcher" uri="intent:#Intent;launchFlags=0x10000000;component=org.koreader.launcher/.MainActivity;end" string="STR_ICONMENU_1005" icon="ic_homemenu_koreader.png" order="5"/>
```

內容中還有 **order** 參數可以修改，我並沒有特別做調整。如果希望它的位置前面一點或後面一點的話，可以自行再調整。

4. 再來是修改一下字串檔的內容。進到每個 KOReader\_strings-\*.xml 中，將內容中的 Create&#010;New Note 置換掉。以 KOReader 為例，則是全換成 KOReader 就行，因為它沒有其他語言的翻譯。

```
<string name="STR_ICONMENU_1005">Create&#010;New Note</string>  
=>  
<string name="STR_ICONMENU_1005">KOReader</string>
```

5. 需要把圖檔 (ic\_homemenu\_createnote.png) 換成一個你想要的圖。我的作法是先打開原檔，將原先的圖檔 clear 掉，再從想要的 App 中，拿它的圖來縮小後，塞到原檔中，儲存。這麼一來，圖檔的寬高 (220x120) 就會跟原先的一樣，不需要擔心新的圖檔有相容性的問題。

6. 完成上述所有調整後，再來是把這個目錄放到設備中，讓系統在重開機時能重新處理，找到這個新的目錄。DPT-CP1 除了會在 /etc/dp\_extensions/ 下找資訊外，也會到 /data/dp\_extensions 下找。而 /data 下是不需要什麼特別權限的。所以我們要將目錄複製到這兒。首先，先建立 /data/dp\_extensions 這個目錄，再將調整完的目錄 KOReader 複製過去。

```
adb shell mkdir /data/dp_extensions  
# 要先跳出 KOReader 這個目錄  
cd ..   
adb push KOReader/ /data/dp_extensions/
```

7.做完後，要將暫存的相關資料清掉，以便設備在重開機時，會重新建立選單的內容。這麼一來就大功告成啦！

```
adb shell  
cd /data/system  
mv ExtMgr.db ExtMgr.db_bak  
mv ExtMgr.db-journal ExtMgr.db-journal_bak  
# 先離開 adb shell  
exit  
# 重開機  
adb reboot
```

上述步驟都沒出錯的話，重開機後應該就可以在系統選單中看到 KOReader 圖案出現在 Create New Note 旁邊。

### 安裝 AssistiveTouch

原以為修改來給 Pubu Pubook SE 的 AssistiveTouch app 可以直接安裝到 SONY DPT-CP1 上，但事情總沒有想像中的順利。DPT-CP1 是 Android OS 5.1 的老機種了，而且有可能 SONY 也有做過一些系統調整，所以在取得系統權限上遇到了一些問題。把之前 AssistiveTouch 裝上後，執行會因為檢查 overlay 權限 API 不存在而馬上 crash。詳細的各種錯誤可以在這個[與 ChatGPT 的請教](https://chatgpt.com/share/ee41078f-3924-4c1a-99d2-330fc8a91287)中看到。

後續做了一堆修改，包括

- overlay on top of other windows 的權限修改；
- 加上版本的判斷，避免 Android 6 以後的程式碼被執行；
- 將懸浮球的尺寸變大；
- 將原先送出 Accessibility key code 的方式換為從程式裡執行 `adb shell input keyevent key_code_name` 。(反正已經 root 了，目前就只有這方式能測試成功)

主要的實作如下：

[View gist](https://gist.github.com/plateaukao/989010a8745ca003ddd0813180cd7880)

- 在 commandline 呼叫下面的給予權限方式 (不確定有沒有效，但我都有執行)

```
adb shell pm grant com.android.mirror.assisttouch android.permission.SYSTEM_ALERT_WINDOW
```

經過這麼胡亂的操作後，終於可以把 AssistiveTouch 懸浮球安裝上去，並且正常執行。

通常在電子書閱讀器上我是不大想用這類軟體的；但安裝懸浮球的好處是：

- (單擊) 在 SONY 設備上提供方便的返回方式
- (雙擊) 減少需要一直點實體按鍵開啟系統功能選單，降低這台二手機壞掉的可能性
- (長按) 之前在 Pubook 上的長按功能是用來刷新整個畫面。不過，這在 SONY 設備上因為都沒殘影，好像不用提供這功能。可以留著以後如果有更常用的功能時，再實作上去。

### 安裝萊娒輸入法

之前自己在維護的萊娒輸入法，經過下面修改後，也可以安裝到這台設備上：

- 將 minSDK 降到 21
- 升級 gradle 的版本，並且處理一下新版的需求 (像是要加上 name space)

![](/images/3fea512ed890/1_gi-GR-b32S0bExL7B1v9mA.png)

### 相關連結

- [AssistiveTouch 的 commit](https://github.com/plateaukao/AssistiveTouch/commit/b9bb9d43f75a01338d8dbda2d1d5e2672f46fcea)
- [萊姆輸入法的修改](https://github.com/plateaukao/sweetlime/commit/caee6bdcbfe1a34f3042a21126ebf89f6b39ed56)
