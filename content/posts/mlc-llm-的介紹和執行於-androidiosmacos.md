+++
title = "MLC-LLM 的介紹和執行於 Android/iOS/MacOS"
date = "2023-09-09T06:43:09.204Z"
description = "MLC-LLM是今年五月出現的專案，用來提供一個通用的系統，試圖讓 LLM 可以執行於各種平台上，並能利用各平台的 GPU 性能，使其表現更佳。這篇文章將說明我在 Android, iOS, MacOS 平台上編譯和執行時的一些理解和心得。"
slug = "mlc-llm-的介紹和執行於-androidiosmacos"
canonicalURL = "https://medium.com/@danielkao/mlc-llm-%E7%9A%84%E4%BB%8B%E7%B4%B9%E5%92%8C%E5%9F%B7%E8%A1%8C%E6%96%BC-android-ios-macos-347fd8638eed"
mediumID = "347fd8638eed"
[cover]
  image = "/images/347fd8638eed/1_W71wKpAmPMEdGbhAETKepA.png"
+++


MLC-LLM是今年五月出現的專案，用來提供一個通用的系統，試圖讓 LLM 可以執行於各種平台上，並能利用各平台的 GPU 性能，使其表現更佳。這篇文章將說明我在 Android, iOS, MacOS 平台上編譯和執行時的一些理解和心得。

---

從 ChatGPT 橫空出世到現在也才快要一年，各式各樣的 LLM 如雨後春荀不斷冒出來。有的強調精確度，有的注重在瘦身 model size，有的專注於處理 coding 相關的問題。雖然大部分的 LLM 還是以執行在性能強大的電腦上，或是架設於雲端為主，但是也漸漸有人想要把它移植到移動式設備上，做所謂的 on-device computing。MLC-LLM 是其中之一，不過它的目標更遠大，它想要讓 LLM 只需要透過同一套流程，就能執行在各種平台上。而移動式設備只是它其中想支援的一環而已。

但這對我來說，就很足夠了。光是能讓 LLM 跑在手機上，我就願意來嘗試看看。反正目前手邊也有 Mac 電腦，能同時讓它支援手邊的設備，算是個附加好處吧。

### MLC-LLM 介紹

MLC-LLM 是一套來自於 CMU 大學的通用型方案，能讓各種 LLM 模型以 native 的型式發布到許多不同的平台上。並提供工具，能夠針對不同平台或需求，進一步優化模型的輸出和效能。

它的目標是讓每個人都能夠開發、優化、和以原生的型式發布 AI 模型到每個人的設備中。

下圖是目前它已經支援的平台，和各個平台上面的 GPU API framework。

![](/images/347fd8638eed/1_W71wKpAmPMEdGbhAETKepA.png)
*來自官網*

### 什麼是 MLC (Machine Learning Compilation)

在解釋 MLC 前，先來看一下整個 MLC-LLM 方案的流程。下圖可以分成三部分。

1. 是來自網路上各式各樣的 LLM 模型，或是自己訓練出來的模式；
2. 是這一小節要介紹的 MLC；
3. 是產生出來適用於不同平台的 runtime libraries，以及最終編譯出來的各平台執行程式。

![](/images/347fd8638eed/1_h2tUUl-RgFfH6GatfXhBlA.png)
*來自官網*

大概知道 MLC 在整套流程中的位置後，來聊聊何謂 MLC。雖然有個 Compilation 字樣，但它和一般寫程式的 compilation 只是概念上類似，但真正的產出物卻不大一樣。其實比較好的說法應該是 converter。

它會透過 TVM Unity compiler 將 1 中的語言模型做 quantization，然後將結果連同 quantized model weights 全放到一個目錄中。這過程都是用 python 開發出來的。

下圖是更詳細的流程圖。對於 compilation 步驟有興趣的話，讀者可以再去找 tvm 的文章來看。這篇文章重點會是在解釋和說明當 compilation 完成後的步驟。

![](/images/347fd8638eed/1_yq9AI330TII1H-k1PQvB3A.png)
*來自官網*

### 執行 Compilation 的方式

大概了解 compilation 的概念和它在流程中扮演的角色後，再來看看實際上要怎麼操作。

首先，必須要[安裝許多 python dependency](https://mlc.ai/mlc-llm/docs/compilation/compile_models.html)，再來是執行下面的指令。

```
python3 -m mlc_llm.build \  
    --model MODEL_NAME_OR_PATH \  
    [--hf-path HUGGINGFACE_NAME] \  
    --target TARGET_NAME \  
    --quantization QUANTIZATION_MODE \  
    [--max-seq-len MAX_ALLOWED_SEQUENCE_LENGTH] \  
    [--reuse-lib LIB_NAME] \  
    [--use-cache=0] \  
    [--debug-dump] \  
    [--use-safetensors]
```

以 Android 當例子，如果想要編譯 Llama2 的模型，使用 quantization 參數為 q4f16\_1 的話，可以執行下面的指令。

```
mkdir -p dist/models  
cd dist/models  
git clone https://huggingface.co/meta-llama/Llama-2-7b-chat-hf  
cd ../..  
python3 -m mlc_llm.build --model Llama-2-7b-chat-hf --target android --max-seq-len 768 --quantization q4f16_1
```

一切順利的話，它會將原先的 Llama2 模式轉換成之後 MLC Chat runtime 能夠讀取的格式。

### Compilation後的步驟

在 compilation完成後，產生的 model weights，model libs 還有 chat config，需要再編譯成每個平台上執行時所需的 MLC Chat Runtime。

如下圖，當有了 MLC Chat Runtime library 之後，就能利用它提供的 API 在真正的應用程式裡跟 LLM 互動。

![](/images/347fd8638eed/1_swiAozCsPqLu9wJ_H6cWig.png)
*來自官網*

關於 chat config 能設定些什麼，其實跟一般在執行 LLM 時的參數差不多，能夠調整 temperature ，repetition\_penalty 等等參數。詳細內容可以參考這篇[官方介紹](https://mlc.ai/mlc-llm/docs/get_started/mlc_chat_config.html)。

有了 runtime library 後，再來就是看看程式中怎麼去使用它。這邊先來看一下 library 中提供的函式有哪些(其實很陽春，就夠用而已)。這邊拿 C++ 當例子，會有以下的函式可以呼叫：不外乎 prefill, decode, reset\_chat, 等。

```
  PackedFunc prefill = mlc_llm->GetFunction("prefill");  
  PackedFunc decode = mlc_llm->GetFunction("decode");  
  PackedFunc stopped = mlc_llm->GetFunction("stopped");  
  PackedFunc get_message = mlc_llm->GetFunction("get_message");  
  PackedFunc reload = mlc_llm->GetFunction("reload");  
  PackedFunc get_role0 = mlc_llm->GetFunction("get_role0");  
  PackedFunc get_role1 = mlc_llm->GetFunction("get_role1");  
  PackedFunc runtime_stats_text = mlc_llm->GetFunction("runtime_stats_text");  
  PackedFunc reset_chat = mlc_llm->GetFunction("reset_chat");  
  PackedFunc process_system_prompts = mlc_llm->GetFunction("process_system_prompts");
```

官方有提供 Android 的 sample app，是以對話型式的 UI 呈現，並用上了比較新的 Jetpack Compose framework。

先來看一下[UI的實作](https://github.com/mlc-ai/mlc-llm/blob/main/android/MLCChat/app/src/main/java/ai/mlc/mlcchat/ChatView.kt#L112)，很單純地用了 LazyColumn，根據帶入的 chatState.messages 產生對應的每個訊息 MessageView；並依照 chatState.messages.size 調整現在訊息列表要捲動到在最下方。

```
LazyColumn(  
    modifier = Modifier.weight(9f),  
    verticalArrangement = Arrangement.spacedBy(5.dp, alignment = Alignment.Bottom),  
    state = lazyColumnListState  
) {  
    coroutineScope.launch {  
        lazyColumnListState.animateScrollToItem(chatState.messages.size)  
    }  
    items(  
        items = chatState.messages,  
        key = { message -> message.id },  
    ) { message ->  
        MessageView(messageData = message)  
    }  
    item {  
        // place holder item for scrolling to the bottom  
    }  
}
```

在 ViewModel 內，則是負責與 MLC Chat runtime 互動。當使用者輸入訊息後，會呼叫 requestGenerate()。這邊又是用 executorService，又是用 coroutine，感覺有點多餘。後來雖然我有把 executor service 拔掉，試著只透過 coroutine 執行，但不論是哪種作法，在執行時都還是會整台手機幾乎當住。目前的手機性能還是無法輕鬆地負荷這麼大的運算量吧。

```
fun requestGenerate(prompt: String) {  
     require(chatable())  
     switchToGenerating()  
     executorService.submit {  
         appendMessage(MessageRole.User, prompt)  
         appendMessage(MessageRole.Bot, "")  
         if (!callBackend { backend.prefill(prompt) }) return@submit  
         while (!backend.stopped()) {  
             if (!callBackend {  
                     backend.decode()  
                     val newText = backend.message  
                     viewModelScope.launch { updateMessage(MessageRole.Bot, newText) }  
                 }) return@submit  
             if (modelChatState.value != ModelChatState.Generating) return@submit  
         }        
         val runtimeStats = backend.runtimeStatsText()  
         viewModelScope.launch {  
             report.value = runtimeStats  
             if (modelChatState.value == ModelChatState.Generating) switchToReady()  
         }        
     }  
 }
```

### 執行後的感想

幾經波折後，替官方抓了不少文件上的不足，也發了 PR 去修正。

目前能夠成功地在 Android，iOS 還有 MacOS 上執行 MLC 的程式。以結果來看：在 M2 或 M1 CPU 加持下的 MacOS 上，是能很順暢地執行這些 LLM 的；只是產出的結果跟 chatgpt 或是 gpt4 比起來還差得很遠。

而 Android 上，執行速度很慢，連要拿來平常測試用的程度都還不到。不過，至少它是能夠跑[我 compile 出來的 Taiwan-Llama2 模型](https://huggingface.co/danielkao0421/mlc-chat-Taiwan-LLaMa)的。

iPhone 的話，我的 iPhone 14 Pro 雖然一執行 Taiwan-Llama2 模型就會因為記憶體不足而 crash，但是其他的模型運作在 iPhone 上卻有不錯的反應速度，已經可以拿來偶爾玩玩，跟它亂聊一通的程度。

相信再過不久，可能幾個月內，長則半年一年，手機上執行 LLM 的環境就會更加的成熟。在那之前，也希望能想到一些應用，好好地來利用這些能拿來當成手機上大腦的 LLM。

### 相關連結

- <https://github.com/mlc-ai/mlc-llm/tree/main>
- <https://mlc.ai/mlc-llm/>
- <https://mlc.ai/mlc-llm/docs/>
- <https://huggingface.co/danielkao0421/mlc-chat-Taiwan-LLaMa>
