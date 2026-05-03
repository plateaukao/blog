+++
title = "在 EinkBro 瀏覽器中整合 Pocket 的 API"
date = "2023-05-05T15:33:24.193Z"
description = "利用 ChatGPT 給出基本的認證流程"
slug = "在-einkbro-瀏覽器中整合-pocket-的-api"
canonicalURL = "https://medium.com/@danielkao/%E5%9C%A8-einkbro-%E7%80%8F%E8%A6%BD%E5%99%A8%E4%B8%AD%E6%95%B4%E5%90%88-pocket-%E7%9A%84-api-836ccdd395df"
mediumID = "836ccdd395df"
tags = ["EinkBro"]
+++

![](/images/836ccdd395df/1_nuyvULFtogktKnCtU-frJg.png)

- 利用 ChatGPT 給出基本的認證流程
- 請它再實作出 add Url to Pocket 的函式
- 最後，請它將其中一個 request 從 callback 的型式改成 coroutine

Pocket 服務能讓使用者將網路上想要保存的網頁儲存到 Pocket 的空間去，利用有優化過的 Reader Mode 來閱讀和整理分類。雖然我使用它的頻率不高，但如果能把它整合到 EinkBro 中，對於在電子書閱讀器上有安裝 Pocket App 的人來說，能夠更方便地將文章加入到 Pocket 清單中。

沒有安裝 Pocket App 的人也可以開新的分頁連結到 Pocket 網站，閱讀之前從各個設備加入的網頁文章。

之前都還沒有研究過 Pocket 的 API 支援，想說 Pocket 也已經推出好幾年了，應該 ChatGPT 當初也有 train 到它相關的 API 文件或整合的程式碼吧，趁著這次機會，來問問 ChatGPT。

### 利用 ChatGPT 給出基本的實作

一轉眼 ChatGPT 也推出快要半年多了，對於軟體工程師來說，ChatGPT 加上 Github 的 Copilot，寫起 code 來真的會有種加速衝刺的感覺；可以讓人的心思都放在核心想要解決的步驟上，其他需要查找的實作細節，這兩個工具可以幫忙完成至少六七成以上的程式碼，剩下的部分才需要自己再稍做修改，或是這時再搬出 Google 和 StackOverflow 來驗證和微調。

以下是我跟 ChatGPT 的對話：

我：act as a senior android programmer, teach me how to integrate pocket api into an android browser app (created with webview), let’s start from the authentication part. please give me sample codes.

ChatGPT:

As a senior Android developer, I’d be happy to help you integrate the Pocket API into your Android browser app built with WebView. First, we’ll cover the authentication part. To use the Pocket API, you’ll need to register your application and obtain a consumer key. You can do that here: <https://getpocket.com/developer/apps/new>

Once you have the consumer key, follow these steps:

1. Obtain a request token
2. Redirect the user to Pocket for authorization
3. Convert the request token into an access token

Here’s a step-by-step guide with sample code for each step:

Step 1: Obtain a request token

First, you need to make a POST request to `https://getpocket.com/v3/oauth/request` to obtain a request token. Use the following sample code:

```
import okhttp3.*  
import java.io.IOException  
  
val client = OkHttpClient()  
val consumerKey = "YOUR_CONSUMER_KEY"  
  
fun getRequestToken(callback: (String) -> Unit) {  
    val requestBody = FormBody.Builder()  
        .add("consumer_key", consumerKey)  
        .add("redirect_uri", "yourappname://pocket-auth")  
        .build()  
  
    val request = Request.Builder()  
        .url("https://getpocket.com/v3/oauth/request")  
        .post(requestBody)  
        .build()  
  
    client.newCall(request).enqueue(object : Callback {  
        override fun onFailure(call: Call, e: IOException) {  
            // Handle error  
        }  
  
        override fun onResponse(call: Call, response: Response) {  
            if (response.isSuccessful) {  
                val body = response.body?.string()  
                val requestToken = body?.replace("code=", "")  
                if (requestToken != null) {  
                    callback(requestToken)  
                }  
            }  
        }  
    })  
}
```

Step 2: Redirect the user to Pocket for authorization

Once you have the request token, you need to open the authorization URL in your WebView. Here’s how you can do that:

```
fun openAuthUrl(requestToken: String) {  
    val authUrl = "https://getpocket.com/auth/authorize?request_token=$requestToken&redirect_uri=yourappname://pocket-auth"  
    webView.loadUrl(authUrl)  
}
```

Step 3: Convert the request token into an access token

After the user has authorized your app, you’ll receive a callback to the `redirect_uri` you specified earlier. You'll need to intercept this callback in your WebView and obtain the access token. To do that, you can override the `shouldOverrideUrlLoading` method:

```
class MyWebViewClient(private val onPocketAuth: (String) -> Unit) : WebViewClient() {  
    override fun shouldOverrideUrlLoading(view: WebView, url: String): Boolean {  
        if (url.startsWith("yourappname://pocket-auth")) {  
            val requestToken = url.substringAfter("code=", "")  
            getAccessToken(requestToken, onPocketAuth)  
            return true  
        }  
  
        return super.shouldOverrideUrlLoading(view, url)  
    }  
}  
  
fun getAccessToken(requestToken: String, callback: (String) -> Unit) {  
    val requestBody = FormBody.Builder()  
        .add("consumer_key", consumerKey)  
        .add("code", requestToken)  
        .build()  
  
    val request = Request.Builder()  
        .url("https://getpocket.com/v3/oauth/authorize")  
        .post(requestBody)  
        .build()  
  
    client.newCall(request).enqueue(object : Callback {  
        override fun onFailure(call: Call, e: IOException) {  
            // Handle error  
        }  
  
        override fun onResponse(call: Call, response: Response) {  
            if (
```

我: continue

ChatGPT:

```
response.isSuccessful) {  
val body = response.body?.string()  
val accessToken = body?.substringAfter("access_token=")?.substringBefore("&")  
val username = body?.substringAfter("username=")  
if (accessToken != null) {  
callback(accessToken)  
}  
}  
}  
})  
}
```

> 註：上面這段程式碼沒在 markdown code snippet 中，所以格式都跑掉了，但貼到 Android Studio 中倒還好，IDE 也聰明地幫忙重新縮排

Now, put everything together in your Activity:

```
class MainActivity : AppCompatActivity() {  
    private lateinit var webView: WebView  
    private lateinit var webViewClient: MyWebViewClient  
  
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
        setContentView(R.layout.activity_main)  
  
        webView = findViewById(R.id.webView)  
        webView.settings.javaScriptEnabled = true  
  
        webViewClient = MyWebViewClient { accessToken ->  
            // Save the access token for future use, and load your desired URL  
            webView.loadUrl("https://example.com")  
        }  
  
        webView.webViewClient = webViewClient  
  
        getRequestToken { requestToken ->  
            openAuthUrl(requestToken)  
        }  
    }  
}
```

In this example, replace `YOUR_CONSUMER_KEY` with your actual consumer key, and change `yourappname` to the name of your app. After completing these steps, you should have a working authentication flow for the Pocket API integrated into your Android browser app.

Now that you have the access token, you can start making API calls to the Pocket API to retrieve, add, or modify items. More details can be found in the Pocket API documentation: <https://getpocket.com/developer/docs/overview>

Please note that the sample code provided uses the OkHttp library for network requests. If you haven’t added it to your project already, include the following dependency in your build.gradle file:

```
implementation 'com.squareup.okhttp3:okhttp:4.9.3'
```

### 新增連結到 Pocket 服務中

我：and, teach me how to add a url to pocket with the accesstoken just received

ChatGPT: Once you have the access token, you can use it to add a URL to Pocket using the `/v3/add` endpoint. Here's a function to add a URL to Pocket:

```
fun addUrlToPocket(accessToken: String, url: String, title: String? = null, tags: String? = null, callback: (Boolean) -> Unit) {  
    val requestBodyBuilder = FormBody.Builder()  
        .add("url", url)  
        .add("consumer_key", consumerKey)  
        .add("access_token", accessToken)  
  
    title?.let {  
        requestBodyBuilder.add("title", it)  
    }  
  
    tags?.let {  
        requestBodyBuilder.add("tags", it)  
    }  
  
    val requestBody = requestBodyBuilder.build()  
  
    val request = Request.Builder()  
        .url("https://getpocket.com/v3/add")  
        .post(requestBody)  
        .build()  
  
    client.newCall(request).enqueue(object : Callback {  
        override fun onFailure(call: Call, e: IOException) {  
            // Handle error  
            callback(false)  
        }  
  
        override fun onResponse(call: Call, response: Response) {  
            callback(response.isSuccessful)  
        }  
    })  
}
```

Here’s how to use the `addUrlToPocket` function:

```
val urlToAdd = "https://www.example.com"  
val title = "Example Title"  
val tags = "tag1,tag2,tag3"  
  
addUrlToPocket(accessToken, urlToAdd, title, tags) { success ->  
    if (success) {  
        // URL added successfully  
    } else {  
        // Failed to add URL  
    }  
}
```

In this example, replace `accessToken` with the access token you received earlier. The `urlToAdd` variable should contain the URL you want to add to Pocket. You can optionally provide a `title` and `tags` (comma-separated) for the URL. The `addUrlToPocket` function will send a POST request to the Pocket API to add the URL, and it will call the `callback` function with a boolean value indicating whether the operation was successful.

Please note that this example assumes you are using the OkHttp library for network requests, as demonstrated in the previous code samples.

---

### 請 ChatGPT 提供 coroutine 的實作

上面 ChatGPT 提供的程式碼幾乎是貼上就能使用，讓我省下許多時間。不過，它的實作是透過 enqueue 和 callback 完成的；在習慣使用 coroutine 後，對於 callback 有點感冒，所以又請它利用 coroutine 提供了其中一個 API 的實作方式。

我：change addUrlToPocket function with coroutine implementation

ChatGPT: To change the `addUrlToPocket` function to use coroutines, you can use the `suspendCoroutine` function and the `suspend` keyword. First, add the necessary dependencies for coroutines to your project by adding these lines to your `build.gradle` file:

```
implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-core:1.6.0'  
implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.0'
```

Then, update the `addUrlToPocket` function as follows:

```
import kotlinx.coroutines.suspendCancellableCoroutine  
import kotlin.coroutines.resume  
  
suspend fun addUrlToPocket(accessToken: String, url: String, title: String? = null, tags: String? = null): Boolean {  
    return suspendCancellableCoroutine { continuation ->  
        val requestBodyBuilder = FormBody.Builder()  
            .add("url", url)  
            .add("consumer_key", consumerKey)  
            .add("access_token", accessToken)  
  
        title?.let {  
            requestBodyBuilder.add("title", it)  
        }  
  
        tags?.let {  
            requestBodyBuilder.add("tags", it)  
        }  
  
        val requestBody = requestBodyBuilder.build()  
  
        val request = Request.Builder()  
            .url("https://getpocket.com/v3/add")  
            .post(requestBody)  
            .build()  
  
        client.newCall(request).enqueue(object : Callback {  
            override fun onFailure(call: Call, e: IOException) {  
                if (continuation.isActive) {  
                    continuation.resume(false)  
                }  
            }  
  
            override fun onResponse(call: Call, response: Response) {  
                if (continuation.isActive) {  
                    continuation.resume(response.isSuccessful)  
                }  
            }  
        })  
  
        continuation.invokeOnCancellation {  
            client.dispatcher.executorService.shutdownNow()  
        }  
    }  
}
```

The `addUrlToPocket` function is now a suspending function. It returns a `Boolean` value indicating the success of the operation. You can call this function within a coroutine scope, like this:

```
import kotlinx.coroutines.Dispatchers  
import kotlinx.coroutines.launch  
import kotlinx.coroutines.runBlocking  
  
fun main() {  
    val accessToken = "YOUR_ACCESS_TOKEN"  
    val urlToAdd = "https://www.example.com"  
    val title = "Example Title"  
    val tags = "tag1,tag2,tag3"  
  
    runBlocking {  
        launch(Dispatchers.IO) {  
            val success = addUrlToPocket(accessToken, urlToAdd, title, tags)  
            if (success) {  
                // URL added successfully  
            } else {  
                // Failed to add URL  
            }  
        }  
    }  
}
```

In this example, replace `YOUR_ACCESS_TOKEN` with your actual access token. The `urlToAdd` variable should contain the URL you want to add to Pocket. You can optionally provide a `title` and `tags` (comma-separated) for the URL. The `runBlocking` function creates a coroutine scope, and the `launch` function creates a new coroutine on the `Dispatchers.IO` dispatcher. The `addUrlToPocket` function is called within the coroutine, and the result is used to determine whether the operation was successful.

---

它利用 suspendCancellableCoroutine 把原先的 networking API 包了起來，雖然有達到我的要求，但總覺得 OkHttp 會有更 elegant 的解法，不過，這就有待以後再做 refactoring 了，目前修改過後的 addUrlToPocket 的實作已經是 suspend function 了。

後面還追問了怎麼新增一個 snackbar，因為我希望在加成功後，能回傳 Pocket article 的連結，如果使用者想要直接開始閱讀的話，點個連結就會進到 Pocket 的文章內文。

另外，還請它幫忙解析 addUrlToPocket() 回傳回來的資料，因為我想從中拿出 Pocket article url，它也都很快速地給我實作方式。

最終，我大部分的時間是花在將他的建議實作整合到我程式的架構中，在需要按鈕的地方加上按鈕，在需要加入攔捷 url request 的地方，放上 ChatGPT 來的實作。

這種合作開發方式，真的讓我能更專心在我想要完成的功能上，而不是去查這些技術的細節。

### 相關連結

- [整合 Pocket 的 commit](https://github.com/plateaukao/einkbro/commit/e0513a2d8a1da72efe4dadd3eb04389aa09e96ab)
- [將 addToPocket 換成 suspend function 並且加入 snackbar](https://github.com/plateaukao/einkbro/commit/88c73135628f6d933f14411a278840140035bfbb)
