+++
title = "在 Android 中利用 Room + Flow + ViewModel + RecyclerView 讓畫面上的列表自動反應資料庫的資料更新"
date = "2021-10-27T16:17:46.941Z"
description = "EinkBro App 中的實作大都是用很舊很舊的技術。雖然隨著功能不斷增加，我有逐漸把一些檔案翻新成 Kotlin，和盡量把相關的邏輯抽出到獨立的 class 或檔案中，不過整體來說，架構還是很老派(其實就是沒有什麼架構，全部的邏輯幾乎都塞在同一個 Activity 中)。"
slug = "在-android-中利用-room-flow-viewmodel-recyclerview-讓畫面上的列表自動反應資料庫的資料更新"
canonicalURL = "https://medium.com/@danielkao/%E5%9C%A8-android-%E4%B8%AD%E5%88%A9%E7%94%A8-room-flow-viewmodel-recyclerview-%E8%AE%93%E7%95%AB%E9%9D%A2%E4%B8%8A%E7%9A%84%E5%88%97%E8%A1%A8%E8%87%AA%E5%8B%95%E5%8F%8D%E6%87%89%E8%B3%87%E6%96%99%E5%BA%AB%E7%9A%84%E8%B3%87%E6%96%99%E6%9B%B4%E6%96%B0-53cb8d1aa8a0"
mediumID = "53cb8d1aa8a0"
tags = ["EinkBro"]
+++

EinkBro App 中的實作大都是用很舊很舊的技術。雖然隨著功能不斷增加，我有逐漸把一些檔案翻新成 Kotlin，和盡量把相關的邏輯抽出到獨立的 class 或檔案中，不過整體來說，架構還是很老派(其實就是沒有什麼架構，全部的邏輯幾乎都塞在同一個 `Activity` 中)。

前不久才導入了 DI library `Koin`，讓部分元件可以用注入的方式在程式中的各個地方能夠存取得到。今天要介紹的是如何利用 Room + Flow 的組合，讓畫面上的書籤列表可以自動更新，不用在每個有 CRUD 的場景手動呼叫。

### 步驟

1. 首先要在 `build.gradle` 中加入 `ViewModel` 的支援

```
implementation ‘androidx.lifecycle:lifecycle-viewmodel-ktx:2.3.1’
```

2. 在 Dao 類別中，加入會回傳 Flow 的函式。原本雖然已經有回傳 List<Bookmark> 的函式，但型式是 suspend，所以可以透過 coroutine 拿到非同步的結果，但拿完之後，並不會收到事後的任何更新。如果想要再次拿到資料庫中最新的資料，得要再呼叫一次才行。但改成回傳 Flow 的話，當資料庫有修改時，利用 Flow 的人都還是會收到通知。

```
@Query("SELECT * FROM bookmarks WHERE parent = :parentId ORDER BY title COLLATE NOCASE ASC")  
fun getBookmarksByParentFlow(parentId: Int): Flow<List<Bookmark>>
```

3. 建立 `ViewModel`，以便資料傳遞給 UI 層

```
class BookmarkViewModel(  
  private val bookmarkDao: BookmarkDao  
): ViewModel() {                               
  fun bookmarksByParent(parentId: Int): Flow<List<Bookmark>> = bookmarkDao.getBookmarksByParentFlow(parentId)                         }
```

```
class BookmarkViewModelFactory(  
  private val bookmarkDao: BookmarkDao  
) : ViewModelProvider.Factory {                               
   override fun <T : ViewModel?> create(modelClass: Class<T>): T {
```

```
     if (modelClass.isAssignableFrom(BookmarkViewModel::class.java)) {                                              
      @Suppress("UNCHECKED_CAST")                                        
      return BookmarkViewModel(bookmarkDao) as T                                   
      }   
      throw IllegalAccessException("Unknown ViewModel class")                               
  }                           
}
```

4. 在 `BrowserActivity.kt` 中建立 `bookmarkViewModel`，以利後面使用

```
private val bookmarkViewModel: BookmarkViewModel by viewModels {                                   
   BookmarkViewModelFactory(bookmarkManager.bookmarkDao)                             }
```

5. 當要開啟書籤列表時，把 `bookmarkViewModel` 傳進去，讓它可以跟 adapter 串在一起。

![](/images/53cb8d1aa8a0/1_l-Gd8svDQu8E5TjTr7uNdA.png)

6. 再來就是 adapter 的初始化部分。193 行到 197 行是這個重構最主要的關鍵。`bookmarkViewModel.bookmarksByParent()` 會回傳 Flow 物件；在這邊利用 collect 來取得結果，並將它代入 `adapter` 中。當資料庫有改變時，`collect` 會再次傳呼叫 195 行，讓 adapter 會再次代入新的資料，從而達到更新畫面的效果。當 `submitList` 送來新的資料時，`BookmarkAdapter` 因為有實作 `DiffUtil.ItemCallback<Bookmark>()`，它會只針對有更新的部分做變化。

![](/images/53cb8d1aa8a0/1_forb7WSBmpHHYn7MfLJ6JA.png)

經過上述的修改，書籤列表的呈現就會在資料庫有改變時，自動更新畫面。之前在加新書籤，刪除書籤，或是修改書籤時實作的手動改變 `adapter` 內容的實作，就可以全部拿掉啦。

目前 EinkBro App 中還有其他地方有使用到資料庫，像是瀏覽記錄，擋廣告白名單等，但大都還沒有改成用 Room 儲存到資料庫中，希望以後有空時，可以把所有資料庫相關的處理和呈現也都利用這種方式重構，減少不必要的手動更新畫面的邏輯，程式也可以看起來更加地簡潔。

### 參考資料

#### Android 官方的教學

比我的說明清楚許多。一步一步照著作就可以完成我上面的那些內容。

<https://developer.android.com/codelabs/basic-android-kotlin-training-intro-room-flow#1>

#### EinkBro App 的修正 commit

<https://github.com/plateaukao/browser/commit/771925da495b5e2995f060591d803498ee3da0b1>
