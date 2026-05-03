+++
title = "LINE LIFF server API wrapper: pylineliff"
date = "2018-06-24T09:34:39.226Z"
description = "看到有人把 liff 的 API 包了起來，使用時不用再拿著 Access Token 去寫 curl command 了。但是他用的是 javascript，要用 npm 安裝。基於之前使用 npm 時常出現一大堆問題，所以我決定寫一版 python 版的。"
slug = "pylineliff"
canonicalURL = "https://medium.com/@danielkao/pylineliff-37479d1814d8"
mediumID = "37479d1814d8"
+++

看到有人把 liff 的 API 包了起來，使用時不用再拿著 Access Token 去寫 curl command 了。但是他用的是 javascript，要用 npm 安裝。基於之前使用 npm 時常出現一大堆問題，所以我決定寫一版 python 版的。

<https://github.com/plateaukao/pylineliff/>

使用上很簡單，本來的 curl script 也沒有多複雜就是了。一開始要先呼叫下面指令，把從 [https://developers.line.me/console/channel/**<channel\_id>**/basic/](https://developers.line.me/console/channel/1488346112/basic/) 拿到的 Channel Access Token 存到本地。

```
./liff.py init <accessToken>
```

接下來就可以呼叫其他的功能了。

#### list

列出所有註冊過的 LINE LIFF apps

```
$ ./liff.py list
```

#### add

新增一個 LIFF app

(type 可以是下列其中一種: full, tall, compact)

```
$ ./liff.py  add <url> <type>
```

#### delete

刪除目前的某個 LINE LIFF app

```
$ ./liff.py delete <liff-id>
```

#### update

更新現有的 LINE LIFF app

```
$ ./liff.py update <liff-id> <json_string>
```

### 參考資料

<https://github.com/morugu/liff-cli>

[plateaukao/pylineliff](https://github.com/plateaukao/pylineliff/)

### 延伸閱讀

[初探 LINE Message API 的新功能 LIFF](https://medium.com/@danielkao/%E5%88%9D%E6%8E%A2-line-message-api-%E7%9A%84%E6%96%B0%E5%8A%9F%E8%83%BD-liff-51d5e7ff1a6a)
