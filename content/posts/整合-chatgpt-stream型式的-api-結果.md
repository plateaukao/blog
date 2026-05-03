+++
title = "整合 ChatGPT stream型式的 API 結果"
date = "2023-06-30T15:20:32.578Z"
description = "這篇文章將說明在已經整合好 ChatGPT 後，怎麼將 API 改成支援 stream 型式連續回傳部分結果，讓使用者可以更快地得到回應。"
slug = "整合-chatgpt-stream型式的-api-結果"
canonicalURL = "https://medium.com/@danielkao/%E6%95%B4%E5%90%88-chatgpt-stream%E5%9E%8B%E5%BC%8F%E7%9A%84-api-%E7%B5%90%E6%9E%9C-e7edaa388e16"
mediumID = "e7edaa388e16"
+++

這篇文章將說明在已經整合好 ChatGPT 後，怎麼將 API 改成支援 stream 型式連續回傳部分結果，讓使用者可以更快地得到回應。

前一陣子將 EinkBro 整合完 ChatGPT 後，常常會使用它來翻譯日文或韓文的網頁內文，並試著改善在 system role和 user prompt 中要代入的字串。不過，不論我怎麼怎麼修改，ChatGPT的回覆速度總是不盡人意，慢吞吞的，等個五到十秒是家常便飯，還常常會 timeout，連結果都不給了。

因此，我又再研究了一下，將它改成能夠接收部分的結果回來。一來，API 的第一反應速度快了超多，通常一秒內最多兩秒就會開始回傳資料；二來使用者可以馬上開始閱讀結果，只要閱讀速度夠快，就能在它回傳結束時，也同時閱讀完畢。如此一來，等於是幾乎沒有什麼等待的時間。

以下就是我做一些修改。

### 加入 sse 函式庫

目前整合 ChatGPT 的實作，是自己利用 okhttp3 函式庫硬刻出來的；所以，想要有 stream 型式回傳方式的話，要再加入 okhttp3 的 sse 函式庫。SSE 是 server sent event 的縮寫。

[Wiki](https://en.wikipedia.org/wiki/Server-sent_events) 上的原文解釋如下，這裡也附上 ChatGPT 翻譯的結果：**Server-Sent Events（SSE）是一種伺服器推送技術，使客戶端能夠透過HTTP連接自動接收伺服器的更新。**它描述了伺服器在建立初始客戶端連線後如何啟動資料傳輸給客戶端。SSE通常用於向瀏覽器客戶端發送訊息更新或連續的資料流，並透過一個名為EventSource的JavaScript API來增強本地、跨瀏覽器的串流功能。透過EventSource API，客戶端可以請求特定的URL以接收事件串流。EventSource API是作為HTML5的一部分，由WHATWG標準化。SSE的媒體類型是text/event-stream。

> **Server-Sent Events** (**SSE**) is a [server push](https://en.wikipedia.org/wiki/Server_push "Server push") technology enabling a client to receive automatic updates from a server via an HTTP connection, and describes how servers can initiate data transmission towards clients once an initial client connection has been established. They are commonly used to send message updates or continuous data streams to a browser client and designed to enhance native, cross-browser streaming through a JavaScript API called EventSource, through which a client requests a particular URL in order to receive an event stream. The EventSource API is standardized as part of [HTML5](https://en.wikipedia.org/wiki/HTML5 "HTML5")[[1]](https://en.wikipedia.org/wiki/Server-sent_events#cite_note-1) by the [WHATWG](https://en.wikipedia.org/wiki/World_Wide_Web_Consortium "World Wide Web Consortium"). The [media type](https://en.wikipedia.org/wiki/Media_type "Media type") for SSE is `text/event-stream`.

可以在 `build.gradle` 中加入以下的內容

```
    implementation 'com.squareup.okhttp3:okhttp:4.10.0'  
    implementation 'com.squareup.okhttp3:okhttp-sse:4.11.0' // for http sst
```

### 修改 HTTP Request，加入 stream 參數

OpenAI 的 [ChatGPT API](https://platform.openai.com/docs/api-reference/completions/create#completions/create-stream) 本身就有支援 stream，可以在 request 中將其設為 `true`。修改 request 就是這麼簡單。需要更動比較大的部分是在回傳值處理上。請見下一段的說明。

```
    private fun createRequest(  
        messages: List<ChatMessage>,  
        stream: Boolean = false, // 在函式中新增這個參數，想使用時，將其設為 true  
    ): Request = Request.Builder()  
        .url(endpoint)  
        .post(  
            json.encodeToString(ChatRequest("gpt-3.5-turbo", messages, stream))  
                .toRequestBody(mediaType)  
        )  
        .header("Authorization", "Bearer $apiKey")  
        .build()  
    }  
  
// ChatRequest  
@Serializable  
data class ChatRequest(  
    val model: String,  
    val messages: List<ChatMessage>,  
    val stream: Boolean = false, // 新增加的代入參數  
    val temperature: Double = 0.5,  
)
```

### 處理 stream 型式的回傳資料

當建立好 HTTP Request 後，由於我們已經預期要收到 stream 型式的結果，這個 request 在呼叫上的方式會有些許不同。這邊會使用到一開始引入的 okhttp3-sse 函式庫中的 `EventSources.createFactory()` ，藉此建立 `factory`。然後再利用 `factory.newEventSource` 建立 `EventSource`。這時，會有個 `onEvent` 函式能讓你收到一直傳來的 `data` string，你可以在這邊做結果的處理。

```
fun chatStream(  
        messages: List<ChatMessage>,  
        appendResponseAction: (String) -> Unit,  
        failureAction: () -> Unit,  
    ) {  
        val request = createRequest(messages, true)  
  
        factory.newEventSource(request, object : okhttp3.sse.EventSourceListener() {  
            override fun onEvent(  
                eventSource: EventSource, id: String?, type: String?, data: String  
            ) {  
                if (data == null || data.isEmpty() || data == "[DONE]") return  
                try {  
                    val chatCompletion = json.decodeFromString<ChatCompletionDelta>(data)  
                    appendResponseAction(chatCompletion.choices.first().delta.content ?: "")  
                } catch (e: Exception) {  
                    failureAction()  
                }  
            }  
        })  
    }
```

因為 stream 型式回來的資料型態有些不同，所以我又另外實作了幾個 data class 來做轉換，包含 `ChatCompletionDelta` 和 `ChatChoiceDelta` 和 `ChatDelta`。這裡主要就是對照著官網的回傳結果實作出來的。

```
@Serializable  
data class ChatCompletionDelta(  
    val id: String,  
    val created: Int,  
    val model: String,  
    val choices: List<ChatChoiceDelta>,  
)  
  
@Serializable  
data class ChatChoiceDelta(  
    val index: Int,  
    val delta: ChatDelta,  
    @kotlinx.serialization.Transient  
    @SerialName("finish_reason")  
    val finishReason: String? = null,  
)  
  
@Serializable  
data class ChatDelta(  
    val content: String? = null,  
)
```

### 在畫面上即時更新

資料部分都處理好了，再來是把相關的結果即時更新在畫面上。在 `chatStream` 中可以看到，在收到 `onEvent` 呼叫時，除了將結果轉成 data class 外，還會再呼叫 `appendResponseAction()` 。這個函式會是在原先的 `GptViewModel` 中實作。下面可以看到，因為已經在 `GptViewModel` 中有實作一個 `_responseMessage` 的 `MutableStateFlow`，所以這裡只要很單純地去把新拿到的結果 append 到它的 `value` 上就行。

Compose UI 本來就會`collect` `_responseMessage` 的狀態改變而跟著重繪內容。UI 和 ViewModel 間的實作完全不用動到！這就是用了 ViewModel 的好處呀~

```
fun query(userMessage: String? = null) {  
    ...  
    if (config.enableOpenAiStream) {  
        openaiRepository.chatStream(  
            messages,  
            appendResponseAction = { _responseMessage.value += it },  
            failureAction = { _responseMessage.value = "Something went wrong." }  
        )  
        return  
    }  
    ...  
}
```

### 示範畫面

### 相關程式碼

- **整合 stream** <https://github.com/plateaukao/einkbro/commit/5010d5c0d883dad7613a86ac42ebebe5859e4394>
- **新增開關 stream 的設定** <https://github.com/plateaukao/einkbro/commit/dc0f844c7cdc34487b2c0d82e3695108dd8c1fb6>
