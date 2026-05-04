+++
title = "在Intel Mac 上利用 M1 Mac mini build codes — mainframer"
date = "2021-05-14T11:47:04.343Z"
slug = "在intel-mac-上利用-m1-mac-mini-build-codes-mainframer"
canonicalURL = "https://medium.com/@danielkao/%E5%9C%A8intel-mac-%E4%B8%8A%E5%88%A9%E7%94%A8-m1-mac-mini-build-codes-mainframer-d99b00395f16"
mediumID = "d99b00395f16"
[cover]
  image = "/images/d99b00395f16/1_B_ukXYfsryFiBwYSMirrZg.png"
+++


在新的 M1 系列出來後，這一兩年有買 Mac 電腦的人不禁覺得苦惱。想要一嚐 M1 的強大性能，卻又苦於已經擁有了一台不算慢的 Mac 電腦，現在想轉賣又不見得能賣到什麼好價錢。一個折衷的方案是：買台最便宜的 M1 設備 Mac min，然後讓原本的 Mac 電腦能呼叫這台 Mac mini 幫忙執行很花 CPU 的工作，像是編譯程式！

### mainframer

為了要實現這想法，首先要來介紹一下一個好用的工具：mainframer。

[buildfoundation/mainframer](https://github.com/buildfoundation/mainframer)

mainframer Github 上寫得很清楚，**這個工具可以協助你在遠端上執行指令，同時把執行後的結果再同步回電腦。**

```
A tool that executes a command on a remote machine while syncing files back and forth. The process is known as remote execution (in general) and remote build (in particular cases).
```

在 Github 上，預設的分支是 3.x，但 3.x 的版本是有問題的（至少我試不出來，有人試成功的話，請留言告知，感謝），要先切到 2.x 的分支。

---

#### mainframer 的概念

在本地端執行指令 ➊ 後，mainframer 會私底下幫忙執行 ❷ ➌ ➍ ➎。

![](/images/d99b00395f16/1_B_ukXYfsryFiBwYSMirrZg.png)

### mainframer 設定

在 README 中有說明怎麼設定，我這邊快速用中文講一下。

#### **舊的 Intel Mac 設定**

有三個變數先定義如下：

```
REMOTE_MACHINE_ALIAS — 遠端 M1 Mac mini 的 SSH alias (我就取名為 m1)  
REMOTE_MACHINE_IP_OR_HOSTNAME — 遠端 M1 Mac mini 的　IP  
REMOTE_MACHINE_USERNAME — M1 Mac mini 上的使用者名稱
```

- 確認已經安裝了 ssh 和 rsync。
- 產生使用者的 SSH key

```
ssh-keygen -t rsa -b 4096 -C "{REMOTE_MACHINE_USERNAME}"
```

- 把下面設定加到 `~/.ssh/config` 中

```
Host {REMOTE_MACHINE_ALIAS}  
  User {REMOTE_MACHINE_USERNAME}  
  HostName {REMOTE_MACHINE_IP_OR_HOSTNAME}  
  Port 22  
  IdentityFile ~/.ssh/id_rsa  
  PreferredAuthentications publickey  
  ControlMaster auto  
  ControlPath /tmp/%r@%h:%p  
  ControlPersist 1h
```

以我自己的例子來說，會是長成下面這樣：

```
Host m1  
  User danielkao  
  HostName 192.168.1.145  
  Port 22  
  IdentityFile ~/.ssh/id_rsa  
  PreferredAuthentications publickey  
  ControlMaster auto  
  ControlPath /tmp/%r@%h:%p  
  ControlPersist 1h
```

- 利用下面指令複製 **SSH Key**，下面遠端的部分會用到**。**

```
$ pbcopy < ~/.ssh/id_rsa.pub
```

### .mainframer/ 目錄設定

將[最新版的 mainframer script](https://github.com/buildfoundation/mainframer/releases/tag/v2.1.0) 複製到 Android 專案的根目錄中。

- 在專案中**建立**`.mainframer` **目錄**，並建立 `config` 檔案，填入以下資訊：

```
remote_machine={REMOTE_MACHINE_ALIAS}
```

以我的例子來說，會是：

```
remote_machine=m1
```

- **設定 .mainframer/ignore**

一堆跟編譯無關的檔案，都不需要同步到 m1 去。

```
.gradle  
  
.git/*  
.gitmodules  
  
/.idea  
  
/local.properties  
  
/.mainframer
```

- **其他設定**

官方文件還有許多細步的設定，可以在整個流程都通了之後，再斟酙修改。

[buildfoundation/mainframer](https://github.com/buildfoundation/mainframer/blob/2.x/docs/CONFIGURATION.md)

#### 遠端 (M1 Mac mini)

- 先確認已經安裝了 SSH Server 和 rsync。
- 設定 user 的 SSH key (從剛剛 intel Mac 上 copy 來的值)

```
$ mkdir -p ~/.ssh  
$ chmod u+rwx,go= ~/.ssh  
$ echo {SSH_KEY} >> ~/.ssh/authorized_keys  
$ chmod u+rw,go= ~/.ssh
```

- 安裝編譯程式所需的其他軟體。以開發 Android 來說，我有先在 M1 Mac mini 中安裝 Intellij Community Edition，並且透過它安裝了 Android 相關的 SDK。另外，還裝了 Zulu 的 ARM 64 java，確定 Android projects 可以正常在 M1 Mac mini 中編譯。詳情可以看下面這篇文章：

[在 M1 Mac Mini 上開發 Android App](https://danielkao.medium.com/%E5%9C%A8-m1-mac-mini-%E4%B8%8A%E9%96%8B%E7%99%BC-android-app-acf835681671)

---

### 執行

一切設定好之後，進到 Mac 的 Android 專案下，可以來執行 mainframer 了！

```
sh mainframer.sh ./gradlew clean assembleRelease
```

如果你的 Android 專案原本在 Mac 中的編譯時間需要到一兩分鐘或更久的話，透過遠端的 M1 機器執行，再同步 binary 回本機，將會感受到差異。

---

### 後話

如果嫌打指令太麻煩的話，可以在 Android Studio 中建立 External Tools，並且加到工具列上頭，這樣子就可以點一下讓遠端的 M1 為你編譯程式了。

另外，遠端讓 M1 編譯還有一個好處時，當 binary傳回本機後，依然可以使用 emulator debug ，不用受限於現在還不是很完整的 M1 Android Emulator。
