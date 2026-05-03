+++
title = "整合 ChatGPT 到 EinkBro 中"
date = "2023-05-05T16:24:00.545Z"
description = "找到合適的 OpenAI 函式庫"
slug = "整合-chatgpt-到-einkbro-中"
canonicalURL = "https://medium.com/@danielkao/%E6%95%B4%E5%90%88-chatgpt-%E5%88%B0-einkbro-%E4%B8%AD-941a77f8715c"
mediumID = "941a77f8715c"
+++

- 找到合適的 OpenAI 函式庫
- 包裝成 Repository 和 ViewModel
- 可以拖拉的對話框
- 新增設定介面

光是請 ChatpGPT 來幫忙寫 code 已經無法滿足我了，下一步是將 ChatGPT 整合進 EinkBro 中，讓使用者自己決定怎麼跟它互動。

目前的構想是：使用者可以先針對網頁選一段文字，然後再跟 ChatGPT 說你想要對這段文字做什麼事，看是要請它解釋給你聽，翻譯成其他語言，或是抓出其中的重點等等。

### 找到合適的 OpenAI 函式庫

這點倒是沒有花太多時間在上頭，反正 ChatGPT 的 API 沒有很複雜，它沒有提供認證的流程，使用者必須事前取得一把 key 才行。有了 key 之後，就只是單純的一支 API call。

後來我串接的是 com.aallam.open:openai-client:3.2.0 。

### 包裝成 Repository 和 ViewModel

因為 OpenAI 函式庫已經把 repository 要做的工作做完了，所以實際上我並沒有實作 repository layer，而是直接在 ViewModel 中生成 OpenAI instance。

```
class GptViewModel : ViewModel(), KoinComponent {  
    private val config: ConfigManager by inject()  
    private val openai: OpenAI by lazy { OpenAI(config.gptApiKey) }  
    ...  
}
```

ViewModel 中最重要的，也是唯一真正有呼叫 API 的函式是 query()。這邊寫死是使用 gpt-3.5-turbo 模型，雖然我最近終於排到了 gpt-4 model 的 API 使用權，但…太貴了，所以還是先用用 3.5 版本的就好。

```
    fun query(userMessage: String? = null) {  
        if (userMessage != null) {  
            _inputMessage.value = userMessage  
        }  
  
        val messages = mutableListOf<ChatMessage>()  
        if (config.gptSystemPrompt.isNotBlank()) {  
            messages.add(config.gptSystemPrompt.toSystemMessage())  
        }  
        messages.add("${config.gptUserPromptPrefix}${_inputMessage.value}".toUserMessage())  
  
        val chatCompletionRequest = ChatCompletionRequest(  
            model = ModelId("gpt-3.5-turbo"),  
            messages = messages  
        )  
  
        viewModelScope.launch(Dispatchers.IO) {  
            val response = openai.chatCompletion(chatCompletionRequest)  
            _responseMessage.value = response.choices.first().message?.content ?: ""  
        }  
    }
```

### 可拖拉移動的對話框

在網頁上選取文字後，Android 系統會跳出 ActionMode menu；這個選單是系統在控制何時出現，以及會呈現哪些選項供使用者使用。在此，我打算完全捨棄系統的 menu，並改成我實作的 Context Menu。關於實作細節，今天不在這裡展開，我們先來講講，當 Context Menu 上的 GPT 按鈕被點擊後的處理方式。

我建立了一個 GPTDialogFragment 來顯示 ChatGPT 的處理結果。在建構子 (constructor) 中塞了一個 anchorPoint 的參數。這參數是從 BrowserActivity 點擊時取得的，可以用來決定 DialogFragment 出現時能夠顯示在手指點擊的附近。

而 setupDialogPosition() 就是依照 anchorPoint 的指示，把對話框移到合適的位子。

```
class GPTDialogFragment(  
    private val gptViewModel: GptViewModel,  
    private val anchorPoint: Point,  
) : ComposeDialogFragment() {  
    ...  
    private fun setupDialogPosition(position: Point) {  
        val window = dialog?.window ?: return  
        window.setGravity(Gravity.TOP or Gravity.LEFT)  
  
        if (position.isValid()) {  
            val params = window.attributes.apply {  
                x = position.x  
                y = position.y  
            }  
            window.attributes = params  
        }  
    }  
}
```

一開始，顯示的位置對是對了，但如果想要在對話框還沒關閉前，可以把它移到別的位置的話，要怎麼做呢？這個需求不光是 GPT 的對話框有需求，剛剛提到的 custom ActionMode context menu 也需要這功能。所以，我把這功能抽到了一個 base 的 [DraggableComposeDialogFragment.kt](https://github.com/plateaukao/einkbro/commit/111de1cda0d15435c162d2515dd299f0db1e7aa6#diff-2c0624a93d5d40b836b5d49609e96dfe63fe018344e606bab9606695712a594e "app/src/main/java/info/plateaukao/einkbro/view/dialog/compose/DraggableComposeDialogFragment.kt")

首先，如同 GPT 對話框，它要能被指定一個起始的位置，所以這裡實作了 setupDialogPosition() 。

```
abstract class DraggableComposeDialogFragment: ComposeDialogFragment() {  
    private var initialTouchX: Float = 0f  
    private var initialTouchY: Float = 0f  
    private var initialX: Int = 0  
    private var initialY: Int = 0  
  
    @SuppressLint("ClickableViewAccessibility")  
    protected fun setupDialogPosition(position: Point) {  
        val window = dialog?.window ?: return  
        window.setGravity(Gravity.TOP or Gravity.LEFT)  
  
        if (position.isValid()) {  
            val params = window.attributes.apply {  
                x = position.x  
                y = position.y  
            }  
            window.attributes = params  
        }  
  
        supportDragToMove(window)  
    }  
    private fun Point.isValid() = x != 0 && y != 0  
    ...  
}
```

再來是處理使用者手指點在對話框上移動時的邏輯。老實說，這整個 Class 都是 ChatGPT 提供給我的。

```
private fun supportDragToMove(window: Window) {  
        val windowManager =  
            requireContext().getSystemService(Context.WINDOW_SERVICE) as WindowManager  
        window.decorView.setOnTouchListener { _, event ->  
            when (event.action) {  
                MotionEvent.ACTION_DOWN -> {  
                    // Get the initial touch position and dialog window position  
                    initialTouchX = event.rawX  
                    initialTouchY = event.rawY  
                    initialX = window.attributes.x  
                    initialY = window.attributes.y  
                    true  
                }  
  
                MotionEvent.ACTION_MOVE -> {  
                    // Calculate the new position of the dialog window  
                    val newX = initialX + (event.rawX - initialTouchX).toInt()  
                    val newY = initialY + (event.rawY - initialTouchY).toInt()  
  
                    // Update the position of the dialog window  
                    window.attributes.x = newX  
                    window.attributes.y = newY  
                    windowManager.updateViewLayout(window.decorView, window.attributes)  
                    true  
                }  
  
                else -> false  
            }  
        }  
    }
```

### 新增設定選項

這部分就不細講了。自從設定介面改用 Jetpack Compose 實作後，要新增設定的內容就單純多了。

目前的作法是，如果使用者有在設定中輸入 ChatGPT API key 的話，當選取文字後，就會看到 ChatGPT 的按鈕；反之則無。

### 圖片

![](/images/941a77f8715c/0_Vo5emrhnax9l6WW1.png)

![](/images/941a77f8715c/0_7N0UNNW78Kj72j7Y.png)

### 相關連結

- [整合 OpenAI 函式庫](https://github.com/plateaukao/einkbro/commit/6613a8ed556a81254b6ea9d95f04715f77b674da)
- [可拖拉的對話框](https://github.com/plateaukao/einkbro/commit/111de1cda0d15435c162d2515dd299f0db1e7aa6)
