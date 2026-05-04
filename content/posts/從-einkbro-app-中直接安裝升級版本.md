+++
title = "從 EinkBro App 中直接安裝升級版本"
date = "2023-12-19T15:02:08.652Z"
description = "本篇說明怎麼實作從 EinkBro App 中直接下載 apk zip 檔案並進行升級，省去許多 unzip 和切換 App 操作的麻煩事。"
slug = "從-einkbro-app-中直接安裝升級版本"
canonicalURL = "https://medium.com/@danielkao/%E5%BE%9E-einkbro-app-%E4%B8%AD%E7%9B%B4%E6%8E%A5%E5%AE%89%E8%A3%9D%E5%8D%87%E7%B4%9A%E7%89%88%E6%9C%AC-3fc8c7927a31"
mediumID = "3fc8c7927a31"
tags = ["EinkBro"]
[cover]
  image = "/images/3fc8c7927a31/1_4qyFXmCSAe973WhJ8K3pRg.png"
+++


### 早該做的提升效率的事 — 從 EinkBro App 中直接安裝升級版本

手邊的 Android 手機，外加電子書閱讀器設備，總共有十幾台。常常在 EinkBro 更新後，不論在使用哪一台，都要開網頁到 Github 網站，下載 snapshot 版本，或是最新的 release 版，再安裝。

如果是最新的 release 版，操作上容易一些，因為從 Release 網頁可以直接下載到 apk 檔案，下載完成後就能直接安裝 (但還是需要去檔案總管刪掉這個下載好的 apk 檔案)；如果是想要安裝剛開發完但還沒 release 的 snapshot 版本的話，就麻煩多了。因為在 EinkBro Github 首頁的下載連結，目前只有辦法拿到 apk 的 zip file，所以在手機上得要多一個步驟將 zip 解壓縮，才能安裝裡頭的 apk。

在大部分的設備上，如果裝了 unrar 時或是 ZArchiver 之類的軟體，在 zip 下載後，可以選擇用它們來開啟，就有機會在不手動 unzip 的情況下，直接安裝 apk。不然，就是得要分成兩三個步驟：先下載 zip 檔案；到檔案總管想辦法 unzip 這個 zip file，然後再進到 zip 解開的目錄，去安裝裡頭的 apk 。

偶爾做一兩次就算了，但我幾乎每週都有在開發；以前則是幾乎天天在開發。這麼一來，如果我不勤於在每台設備上更新版本的話，往往都會用到舊的版本，享受不到我剛開發好的新功能。但要更新又覺得有夠麻煩。

終於，前一兩天心血來潮，把這件事變得比較容易一點了！！除了在設定的 About 頁面中，加入了一鍵從 Github 更新 release 版本外，還加上了今天要紹的如何實作更新至 snapshot 版本。

### 實作內容

主要會有以下幾個步驟：

1. 下載 zip file
2. 解壓縮成 binary stream
3. 將裡頭的 app-release.apk 檔案寫到暫存檔中
4. 呼叫系統的安裝程式 Intent
5. 前面暫時寫入的 File 物件有加上 deleteOnExit() ，所以當 App 被關閉時，這個暫存檔理論上就會被刪除。

### 詳細說明

#### 下載 zip file

不論是下載一般檔案，或是 zip 檔，作法都是一樣的。

先將 snapshot zip url 包裝成 Request，再呼叫 OkHttpClient 的 newCall()。這時，會回傳 response, 就可以再拿著 response 做一番操作。

這裡使用的是 execute() 而不是 queue() 是因為我把整個大函式設定為 suspend function。

```
        val url = "https://nightly.link/plateaukao/einkbro/workflows/buid-app-workflow.yaml/main/app-release.apk.zip"  
        val request = Request.Builder().url(url).build()  
        client.newCall(request).execute()
```

拿到 response 後的實作：從 response.body 中取得 byteStream，然後再餵給 extractApkAndInstall() 函式，抓出裡面的 apk，和安裝它。

```
client.newCall(request).execute().use { response ->  
        if (!response.isSuccessful) throw IOException("Failed to download file: $response")  
  
        val inputStream = response.body?.byteStream()  
        extractApkAndInstall(inputStream, context)  
    }
```

完整的 extractApkAndInstall() 實作如下：因為已經事前知道回傳資料是 zip，所以這裡會用 ZipInputStream 把它包起來，再 while loop 去取裡面名稱叫做 app-release.apk 的文件。找到後，將它寫入到 cache 中的暫存檔，取名為 app.apk。如果這個檔案事前已經存在了(比方說，前不久也裝過新的版本)，就會先刪掉舊的，再寫入一次。這邊呼叫了 tempFile.deleteOnExit()，希望可以在離開程式時，系統會自動將 app.apk 刪掉，但試了幾次好像都不成功。反正，名稱都是取一樣的，而且會刪除已經存在的檔案，所以，最多系統裡就只會存在一個 app.apk，才 4 MB，就算了。

```
private fun extractApkAndInstall(inputStream: InputStream?, context: Context) {  
    val zipInputStream = ZipInputStream(inputStream)  
  
    var zipEntry = zipInputStream.nextEntry  
    while (zipEntry != null) {  
        if (zipEntry.name == "app-release.apk") {  
            val tempFile = File("${context.cacheDir.absolutePath}/app.apk")  
            if (tempFile.exists()) {  
                tempFile.delete()  
            }  
            tempFile.createNewFile()  
            tempFile.deleteOnExit()  
            FileOutputStream(tempFile).use { fos -> zipInputStream.copyTo(fos) }  
  
            installApkFromFile(context, tempFile)  
  
            break  
        }     
        zipEntry = zipInputStream.nextEntry  
    }     
    zipInputStream.closeEntry()  
    zipInputStream.close()  
}
```

最後一個函式是 installApkFromFile() ，這就沒有什麼好解釋的了，網路上都找得到。比較需要注意的地方是：因為暫存檔是寫到 EinkBro App 的相關 cache 資料夾，所以要把該檔案分享給其他 App 或是系統使用時，得透過 fileprovider 的方式來提供。這件事我在之前就做過了，所以這裡只要單純的利用 FileProvider 拿一下 Uri 就行。

```
private fun installApkFromFile(context: Context, file: File) {  
    val apkUri = FileProvider.getUriForFile(  
        context,  
        BuildConfig.APPLICATION_ID + ".fileprovider",  
        file  
    )  
  
    val intent = Intent(Intent.ACTION_VIEW).apply {  
        setDataAndType(apkUri, "application/vnd.android.package-archive")  
        flags = Intent.FLAG_ACTIVITY_NEW_TASK  
        flags = Intent.FLAG_GRANT_READ_URI_PERMISSION  
    }  
  
    context.startActivity(intent)  
}
```

開發完成後，以後想要更新版本，就只要進到 Settings > About，點一下就行了。未來還是有可以再簡化的地方：比方說，隔個幾天就查一下是不是有新的版本，有的話不用等使用者點，可以在畫面上直接提示用戶。

這種作法有可能會有點煩人，所以之後如果有要做的話，應該也會做成是選項，預設會是關閉的。只有像我這種一定都要用最新版的人，再自己去打開來用就好。

### About 頁面

![](/images/3fc8c7927a31/1_4qyFXmCSAe973WhJ8K3pRg.png)

### 相關連結

[feat: add update with snapshot feature · plateaukao/einkbro@1b8a487](https://github.com/plateaukao/einkbro/commit/1b8a487213d7f6cf579c6377b8aadc9aeac1f82b)
