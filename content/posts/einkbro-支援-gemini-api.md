+++
title = "EinkBro: 支援 Gemini API"
date = "2024-06-15T15:12:29.407Z"
description = "Google 在 Google IO 2024 公布了 Gemini 1.5 Flash model，並且幾乎免費地讓開發者可以來試用。為了能夠試試它的效果，我把它也整合進了 EinkBro。本篇文章會說明整合的方式。"
slug = "einkbro-支援-gemini-api"
canonicalURL = "https://medium.com/@danielkao/einkbro-gemini-10d5daf135e3"
mediumID = "10d5daf135e3"
tags = ["EinkBro"]
+++

![](/images/10d5daf135e3/1_mf0rksDlW76GwWX8qbwMtg.png)

Google 在 Google IO 2024 公布了 Gemini 1.5 Flash model，並且幾乎免費地讓開發者可以來試用。為了能夠試試它的效果，我把它也整合進了 EinkBro。本篇文章會說明整合的方式。

Gemini API 的呼叫大致上可以分為兩種方式：一種是透過 Google 在各平台或語言推出的 Gemini SDK，直接利用其中的 api client 呼叫其函式，代入參數，就可以收到結果，而且內容都已經幫忙解析好，為完整的 class 物件；另一種方式則是比較原始的方式，單純利用 http request 去跟 Gemini API server 溝通，等拿到 json 字串結果後，再自行解析成 response object。

各有各的好處，以 EinkBro 的情況來說，我並不想因為要整合 Gemini API，就把整套 SDK 都導入進來 (實測大約會多 150 KB)；所以，選擇的方式是直接打 API，等拿到 json 字串後，再從裡面取出所需要的值。雖然要寫的程式碼會多一點點，但省下來許多寶貴的 app size。

### 實作

#### HTTP REQUEST

最重要的是，Gemini API 的網址長得怎樣。下面可以看到，我已經把 model name 寫死，是 gemini-1.5-flash 。雖然 Gemini 也有開放免費試用的 1.5-pro，但因為一分鐘內只能呼叫兩次，個人覺得應該不大夠用，所以在 EinkBro 中就沒有開放彈性讓使用者指定 model name。

在網址的最後面必須代入 api key。相比於 OpenAI 的作法，Google Gemini 在申請 API Key 的流程上就很簡單，直接到 AI Studio 按個鈕就可以拿到一把 key。

```
https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=$apiKey
```

知道網址後，再來要看 request 的 body 中需要代入什麼內容。這邊主要塞了兩種資訊：

1. 詢問的內容
2. 安全性設定

關於 1. 詢問的內容，在 OpenAI 的場景下，是代入一個 message List，其中會包含使用者設定的 system prompt，以及一則 user prompt。而從網頁中的選取文字則是會被附加在 user prompt 的最後面。

但在 Gemini API 的情況下，目前我是先只塞了這個 message List 的最後一則資料，也就是 user prompt 的內容。

再來， 2. 安全性設定，則是要跟 Gemini 講，不要一遇有好像 sensitive 的內容，就拒絕回答。雖然它還是會做一些審查，但至少可以讓這情況不要太常發生。

```
        val data = RequestData(  
            contents = listOf(  
                Content(parts = listOf(ContentPart(text = contextMessage)))  
            ),  
            safety_settings = listOf(  
                SafetySetting(  
                    category = "HARM_CATEGORY_SEXUALLY_EXPLICIT",  
                    threshold = "BLOCK_ONLY_HIGH"  
                ),  
                SafetySetting(  
                    category = "HARM_CATEGORY_HATE_SPEECH",  
                    threshold = "BLOCK_ONLY_HIGH"  
                ),  
                SafetySetting(category = "HARM_CATEGORY_HARASSMENT", threshold = "BLOCK_ONLY_HIGH"),  
                SafetySetting(  
                    category = "HARM_CATEGORY_DANGEROUS_CONTENT",  
                    threshold = "BLOCK_ONLY_HIGH"  
                )  
            )  
        )  
  
        val requestBody =  
            json.encodeToString(data).toRequestBody("application/json".toMediaTypeOrNull())
```

#### HTTP RESPONSE

完成 request 後，利用 OkHttpClient 送到 Gemini API server 去，收到結果後，再包裝成 EinkBro 想要的格式。

```
        val request = Request.Builder()  
            .url(apiUrl)  
            .post(requestBody)  
            .apply {  
                headers.forEach { (key, value) -> addHeader(key, value) }  
            }  
            .build()  
  
        return withContext(Dispatchers.IO) {  
            try {  
                val response: Response = client.newCall(request).execute()  
                if (!response.isSuccessful) {  
                    return@withContext "Error querying Gemini API: ${response.code}"  
                }  
  
                val responseBody =  
                    response.body?.string() ?: return@withContext "Empty response from Gemini API"  
                val responseData = json.decodeFromString<ResponseData>(responseBody)  
                responseData.candidates.firstOrNull()?.content?.parts?.firstOrNull()?.text  
                    ?: "No content available"  
            } catch (exception: Exception) {  
                "something wrong"  
            }  
        }
```

從 ResponseData 中，一路拆解，最終可以拿到 Gemini model 產生回來的文字。ResponseData → List<Candidate> → Content → ContentPart → text

```
@Serializable  
data class ContentPart(val text: String)  
  
@Serializable  
data class Content(val parts: List<ContentPart>)  
  
@Serializable  
data class SafetySetting(val category: String, val threshold: String)  
  
@Serializable  
data class RequestData(  
    val contents: List<Content>,  
    val safety_settings: List<SafetySetting>  
)  
  
@Serializable  
data class ResponseData(val candidates: List<Candidate>)  
  
@Serializable  
data class Candidate(val content: Content)
```

主要的實作就這樣而已。不過，這樣子的作法還缺了點什麼：streaming。

#### 支援 Streaming

Gemini-1.5-Flash 有點話多。回答的內容常常會一大串。因此，應該要讓它也可以用 stream 的型式回傳結果，再隨時更新在畫面上。

但是，Gemini-1.5-Flash 的 streaming 實作使用的不是 OpenAI 在用的 SSE ，所以，只好再依照它的方式再實作一次。

首先，要將 request url 改掉。原先的最後一段 path segement 是 :generateContent , 要裝它改為 :streamGenerateContent。再來是 query 時，必須要從 api call 拿回 stream 的 buffer 來處理。

這裡的實作方式比較粗糙，先去從 stream 中拿到一行一行的內容，assign 給 chunk。如果 chunk 中的文字有發現到 text: 的字樣，我就認定這一行包含了產生的文字。利用 substringAfter() 和 substringBeforeLast() 夾擊，把文字抓出來。

透過這種陽春的解析法，一樣能達到 streaming 的結果，但不需要引入肥大的 Gemini SDK。

```
        val request = createGeminiRequest(messages, true)  
        client.newCall(request).execute().use { response ->  
            if (!response.isSuccessful) {  
                failureAction()  
                return  
            }  
            val inputStream = response.body?.byteStream() ?: return  
            inputStream.source().buffer().use { source ->  
                var outputString = ""  
                while (!source.exhausted()) {  
                    val chunk = source.readUtf8Line()  
                    if (chunk == null) {  
                        failureAction()  
                        return  
                    }  
                    try {  
                        //Log.d("OpenAiRepository", "chunk: $chunk")  
                        val textField = "\"text\": \""  
                        if (chunk.contains(textField)) {  
                            appendResponseAction(  
                                chunk.substringAfter(textField).substringBeforeLast("\"").unescape()  
                            )  
                        }  
                    } catch (e: Exception) {  
                        failureAction()  
                        return  
                    }  
                }  
            }
```

#### 支援簡易 Markdown 格式

Gemini API 還有另一個特色是：特別愛使用 markdown 的格式回傳內容，尤其是標題文字，粗體字，或是 bullet points。在畫面上看到 ###, \*\*文字\*\* ，或是 \* a, \* b 等，雖然不致於到看不懂，但總覺得不是那麼美觀。所以，EinkBro 還加入了基本的 Markdown 格式支援。

Jetpack Compose 的 Text Widget 有支援類似傳統 TextView 的 Spannable，叫做 AnnotatedString。實作方式便是解析文字內容，在遇到應該要呈現不同效果的標記時，把該個段落抽出來，包裝成一個 AnnotatedString。細節可以看[這個檔案](https://github.com/DAKSHSEMWAL/mdparserkit/blob/main/mdparserkitcore/src/main/java/com/daksh/mdparserkit/core/ParseMarkdown.kt)，這裡就不多做解釋了。

### 相關連結

- commit for 支援 Gemini: <https://github.com/plateaukao/einkbro/commit/4bc8bebe74fc36e6d33adca9cc89fe645c134828>
- commit for 支援 Gemini Streaming: <https://github.com/plateaukao/einkbro/commit/8fa995744d7495c9467ca28a95ecb1dbb602cee6>
