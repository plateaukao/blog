+++
title = "Kotlin Coroutine Channel 的使用簡介"
date = "2023-12-10T08:46:33.671Z"
description = "這篇文章會分享 EinkBro 在整合 OpenAI tts API 時，藉由 Kotlin Coroutine Channel 處理 API 邏輯和播放的實作。"
slug = "kotlin-coroutine-channel-的使用簡介"
canonicalURL = "https://medium.com/@danielkao/kotlin-coroutine-channel-%E7%9A%84%E4%BD%BF%E7%94%A8%E7%B0%A1%E4%BB%8B-2b95a342a8b3"
mediumID = "2b95a342a8b3"
tags = ["EinkBro"]
+++

這篇文章會分享 EinkBro 在整合 OpenAI tts API 時，藉由 Kotlin Coroutine Channel 處理 API 邏輯和播放的實作。

![](/images/2b95a342a8b3/1_CZivT9zQC0OMJ7kW6Z6Peg.png)

### 前言

原先在 EinkBro 的朗讀功能，是利用系統的文字轉語音功能。這樣做的好處是，不用處理太多複雜的邏輯，只需要把文字丟給系統就好；但缺點是每一台設備上的文字轉語音功能支援度不同。很多時候還需要使用者事前先下載好相關資料檔，或是從系統設定中指定好想要的語音語言。對一般使用者來說，難度有點高。在使用時，也需要請使用者自己指定一下語言，不然可能會唸不出來。即便是我自己的設備，也不見得每一台都能夠正常運作。

2023 年 11 月初，OpenAI 公布了一支 tts 的 API，可以很完美地將文字轉為語音，效果比市面上大部分系統內建的 tts 好很多。如果是英文的話，幾乎聽不出來是機器唸的，該有的抑仰頓挫也都有。

既然 EinkBro 已經整合了 chatgpt API，再順便整合一下 tts API 並不需要太大的工夫。

### 整合 OpenAI tts API

這部分是比較單純的地方，只要對著 endpoint 把需要的 request parameters 代入就可以得到產生好的語音 binary。

tts 的 endpoint 是 <https://api.openai.com/v1/audio/speech> ，需要的參數我把它包裝成 TTSRequest class：

```
@Serializable  
data class TTSRequest(  
    val input: String,  
    val model: String = "tts-1",  
    val speed: Double = 1.0,  
    val voice: String = "alloy",  
    val format: String = "mp3"  
)
```

詳細的 tts API 說明可以參考官網：<https://platform.openai.com/docs/api-reference/audio>

![](/images/2b95a342a8b3/1_5Kv2pLiUlQ87rmNqNp7vmA.png)

#### 回傳值的處理

如果一切順利的話，在 response 中會是語音的 binary 內容。在這裡，我先用 SuspendCoroutine 實作，確保 tts 可以在拿到語音後，才回傳 ByteArray 結果。

```
    suspend fun tts(text: String): ByteArray? = suspendCoroutine { continuation ->  
        val request = createTtsRequest(text)  
        client.newCall(request).execute().use { response ->  
            if (response.code != 200 || response.body == null) {  
                return@use continuation.resume(null)  
            }  
  
            try {  
                continuation.resume(response.body?.bytes())  
            } catch (e: Exception) {  
                continuation.resume(null)  
            }  
        }  
    }
```

拿到語音內容後，關於怎麼播放，主要有兩種方式：一是利用 Android 很早就有提供的 MediaPlayer 來進行；另一個方式是更有彈性，能提供更多細微操作的 ExoPlayer。後者實作必須要再 import 相關的函式庫才行，所以為了實作上簡便，而且不想增加 App size，我選擇了前者。

MediaPlayer 的實作雖然很簡單，但它有個限制是：它無法直接播放來自於記憶體中的 ByteArray。為了繞過這個問題，拿到語音內容後，必須先把它儲存成文件，再讓 MediaPlayer 去播放該 File。

下面的實作便是先建立暫時檔案，將資料寫入，再交由 MediaPlayer 播放。MediaPlayer 實例是在事前先建立好的，避免不斷產生新的 instance，造成資源的浪費。每次播放完畢，會收到 onCompletionListener ，這時，可以呼叫 reset() ，讓 MediaPlayer 可以再進行下次的播放。

```
    private suspend fun playAudio(context: Context, data: ByteArray) = suspendCoroutine { cont ->  
        // Creating a temporary file  
        val tempFile = File.createTempFile("temp", "aac", context.cacheDir)  
        tempFile.deleteOnExit()  
        val fos = FileOutputStream(tempFile)  
        fos.write(data)  
        fos.close()  
  
        java.io.FileInputStream(tempFile).use { fis ->  
            mediaPlayer.setDataSource(fis.fd)  
            mediaPlayer.prepare()  
            mediaPlayer.start()  
  
            mediaPlayer.setOnCompletionListener {  
                tempFile.delete()  
                mediaPlayer.reset()  
                cont.resume(0)  
            }  
        }  
    }
```

在 [Android 官網](https://developer.android.com/reference/android/media/MediaPlayer#StateDiagram)上，可以看到 MediaPlayer 的狀態圖如下：

![](/images/2b95a342a8b3/1_dNkrLogDLASsmkOHdOl91A.png)

### 利用 Coroutine Channel 控制播放進度

基本的播放功能完成後，再來是這篇文章的重點：怎麼利用 Coroutine Channel 來控制播放的內容。

一般的網頁，少說會有幾十個句子，多的話，上百個句子也是很正常的。如果要一次把所有的文字內容餵給 tts API，上面的 API 說明中可以看到，它最多一次只能吃 4096 個字元而已；如果不特別檢查的話，可能常會遇到過長的情況。

再說，如果餵的文字太多，openAI tts 產生語音的時間也會隨之拉長(我猜的)。所以，我先將網頁中的文字依照句號(. 或是。)建立成 List ，打算一次只餵一句話或兩句話，讓朗讀功能能夠很快就開始運作，而且不會一次就把所有內容處理完，會邊播放，邊處理接下來的文字內容。畢竟，tts API 不便宜啊。

處理文字成 List 的方式：

```
val sentences: List<String> = text.split("(?<=\\.)|(?<=。)".toRegex())
```

再來是 Channel 的建立。我打算一次最多就處理三個句子，一旦句子的語音資料回來後，就可以依序讓 MediaPlayer 播放。而 Channel 能夠很有效地處理這種情形。

```
private var byteArrayChannel: Channel<ByteArray>? = null  
  
  
    fun readText(context: Context, text: String) {  
        // 在 Channel 中，最多能塞三個元素  
        byteArrayChannel = Channel(3)  
        viewModelScope.launch(Dispatchers.IO) {  
            val sentences: List<String> = text.split("(?<=\\.)|(?<=。)".toRegex())  
  
            for (sentence in sentences) {  
                val data = openaiRepository.tts(sentence)  
                if (data != null && byteArrayChannel != null) {  
                    // 拿到句子的語音檔，確定有資料後，便往 channel 中送。  
                    // 這邊代表著 producer  
                    byteArrayChannel?.send(data)  
                }  
            }  
        }
```

有了 Producer 後，再來是 Consumer 端的實作。Consumer 也是實作在 readText() 函式中。先將它包在 ViewModelScope 中，再利用 for loop 去取得 byteArrayChannel 中的元素。只要上面的實作不斷地有資料 send 到 channel 中，這裡的 for loop 就會不斷地播放語音內容。

```
fun readText(context: Context, text: String) {  
        ...  
        viewModelScope.launch(Dispatchers.IO) {  
            for (data in byteArrayChannel!!) {  
                playAudio(context, data)  
                delay(200)  
            }  
            byteArrayChannel = null  
        }  
    }
```

最後，要再處理一下，如果使用者聽一聽，不想要再聽的時候，必須把整個 Channel 停掉。我在 ViewModel 中實作了 stop()，將該停的該關的 resource 做處理。這麼一下來，下次使用者再點擊朗讀時，又可以再次正常運作。

```
    fun stop() {  
        byteArrayChannel?.cancel()  
        byteArrayChannel = null  
        mediaPlayer.stop()  
        mediaPlayer.reset()  
    }
```

### 完成的功能影片

### 後續

目前的實作是每一句話都會去打一次 API 和儲存成文件。理論上應該可以做些實驗，找出大約多少句子為一個單位去打 API，讓系統的反應速度會是最佳的，又不會過度讀寫檔案系統。但，除非是有很多使用者重度地在使用這功能，不然，現在的版本就很夠用了。

### 相關資料

1. [feat: roughly working stop tts.](https://github.com/plateaukao/einkbro/commit/f7525110818bd90b9c3ec3e2c23487c4c0b2fbca)
2. [feat: use single mediaplayer, add setting in chatgpt to use it for tts](https://github.com/plateaukao/einkbro/commit/bd67b21a971f8761f84b879be133cd15d2f6befa)
3. [feat: add openai tts api](https://github.com/plateaukao/einkbro/commit/bf11417d3c6357d84b413e7ef17135123f5283c8)
