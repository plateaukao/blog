+++
title = "Android 裡從另一個 Activity 中取得資訊的方式"
date = "2022-07-16T16:57:23.887Z"
description = "從 startActivityForResult 和 onActivityResult 到 registerForActivityResult 的距離。"
slug = "android-裡從另一個-activity-中取得資訊的方式"
canonicalURL = "https://medium.com/@danielkao/android-%E8%A3%A1%E5%BE%9E%E5%8F%A6%E4%B8%80%E5%80%8B-activity-%E4%B8%AD%E5%8F%96%E5%BE%97%E8%B3%87%E8%A8%8A%E7%9A%84%E6%96%B9%E5%BC%8F-906f91e1bbbc"
mediumID = "906f91e1bbbc"
[cover]
  image = "/images/906f91e1bbbc/1_uExXxRTROEC2It1WLmDQGA.png"
+++


早期的寫法都是

1. 建立一個 Intent，指定想要的 Activity 或是塞一些 filter 讓系統或使用者幫忙找出能提供服務的 Activity。
2. 呼叫 Activity.StartActivityForResult()，放入上個步驟中建立好的 Intent 和一個自己定義好，不會重覆的 request code，這時，系統就會去啟動另一個 Activity 起來做事。
3. 覆寫 Activity 中的 onActivityResult 函式，判斷收到的 requestCode 是不是自己在步驟 2 中指定的那個數字，如果是的話，就可以拿 data 來做自己想要的後續步驟。

乍看之下，這方式似乎沒有什麼太大的問題。如果是個小 App，同個 Activity 中只有一兩個需要這麼處理的邏輯，而且不會常常改來改去的話，那在管理上還不會有太大的問題。但如果常常需要新增這類的應用的話，往往在 onActivityResult 中就會有大量的 request code 判斷和處理，也會產生許多 request code 需要細心地管理，避免重覆。

---

### 新的作法

後來在 AndroidX 中，Android 推出了 registerForActivityResult() 的方式，在 ComponentActivity 和 Fragment class 中都有包含這個函式。對於需要呼叫其他 Activity 起來作事再回傳資訊的，可以改成事前註冊的方式。註冊完後會取得一個 ActivityResultLauncher 的 instance。這個 instance 就可以在真正需要呼叫其他 Activity 時使用它的 launch() 函式來達到一樣的效果。

除了能讓不同的場景處理能夠很自然而然地分開到不同的 Launcher 中以外，在 Android 文件中還提到另一個好處是：常常在呼叫其他 Activity 起來後，由於系統資源不足，可能原本在等資訊的那個 Acitivity 會被系統砍掉。利用這方式能確保當它被系統 restore 時，同樣的 Launcher 還是會被生成，讓原先的 flow 能繼續進行下去。

---

### EinkBro 中的其中一個實作

由於 EinkBro 的前身是好幾年前就開始開發的，所以舊有的相關實作都還是利用 onActivityResult 完成。這次，為了要支援儲存 data url 的圖片，需要呼叫系統的檔案管理器畫面，讓使用者指定圖片想要儲存的位置和名稱。所以我在這流程中實用了這新的方式。

#### 建立 Launcher

首先，我在 BrowserActivity 中建立 saveImageFilePickerLauncher，它的真正實作放在 BrowserUnit 中，另外，我還塞入了一個當儲存完畢後的 postAction，讓我可以詢問使用者是不是要立即顯示圖片 (4 ~11行)。

![](/images/906f91e1bbbc/1_uExXxRTROEC2It1WLmDQGA.png)

在 BrowserUnit 中的實作則是填入當收到 ActivityResult 時，用來處理的函式：

![](/images/906f91e1bbbc/1_hYF5UvK83Up8vOJgs7PoaQ.png)

這邊使用了 ActivityResultContracts.StartActivityForResult()，這是內建的幾種 Contract 之一，如果沒有特殊需求的話，使用這個就行了，它的操作方式和原本的作法差不多，也是準備一個 intent 就能操作。

另外，要注意的是在 Callback 裡，呼叫了 handleSaveImageFilePickerResult()，這個函式會在下面一點的地方解釋。

#### 使用 Launcher

Launcher 準備就緒後，再來便是在需要使用它時，呼叫 Launcher 的 launch()。下面的程式碼是 BrowserActivity 中判斷 url 是不是 data url 的片段；在得知 url 是 “data:image” 開頭時，會呼叫 BrowserUnit.saveImageFromUrl()，並帶入之前建立好的 Launcher

![](/images/906f91e1bbbc/1_LlyNKEPSswwT26RJyOo9TQ.png)

BrowserUnit.saveImageFromUrl()，準備了些資訊，初始化好一個 intent，再來，就可以呼叫 Launcher.launch() 囉。當 16 行的 resultLauncher.launch(intent) 執行後，再來就是等 Callback 回來。

![](/images/906f91e1bbbc/1_9l-WgEK8ltvUKfAMpKO92A.png)

#### 在 Callback 中處理回傳的 ActivityResult

當使用者在 Activity 中完成操作後，相關的資訊會被代入 Launcher 中的 Callback。剛有提到的 handleSaveImageFilePickerResult 會被執行。

![](/images/906f91e1bbbc/1_z2Mqpd_znUfaBxOwxREdhw.png)

這邊有點類似是在 onActivityResult() 裡要做的邏輯：首先，檢查回傳的 activityResult.resultCode 是不是正常，以及 activityResult.data 有沒有資料。經過初步判斷後，就可以做正事，把收到的 content uri 塞進 saveImage() 函式去寫入檔案。在第 9 行可以看到：postAction 也被當成參數代入。這樣子才能確保當檔案非同步寫入完成後，可以跳出對話框問使用者是不是要立即檢視。

#### 注意事項

在官方文件中有提到，對於呼叫 registerActivityForResult() 和 ActivityResultLauncher.launch() 的呼叫時機有一些限制：

- registerActivityForResult() 必須要在 Activity 或 Fragment created 之前就呼叫。
- ActivityResultLauncher.launch() 則是要在 Activity 或 Fragment created 之後才可以使用。

![](/images/906f91e1bbbc/1_NX-JU28ddX5KVvaJffBgsQ.png)

這兩項限制使得動態地 register / unregister Launcher 變得不可能，有點可惜。

---

### 結語

新的 ActivityForResult 的機制，去除了自定 request code 的煩惱，程式碼能更加獨立。如果有更複雜的需求，也可以自訂 Launcher 或是 Contract；比起早期大鍋炒的 onActivityResult() 好多了。

### 參考資料

其實官方資料的說明就很清楚了

<https://developer.android.com/training/basics/intents/result>
