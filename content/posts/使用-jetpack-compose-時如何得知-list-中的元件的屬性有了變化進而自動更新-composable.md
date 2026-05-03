+++
title = "使用 Jetpack Compose 時如何得知 List 中的元件的屬性有了變化，進而自動更新 Composable"
date = "2023-03-22T20:37:59.157Z"
description = "被發了一條網頁分頁 favicon 更新不同步的 issue。雖然我自己也常常遇到，但因為無傷大雅，而且一直沒找到對的時機點修正，所以一直沒有理它。"
slug = "使用-jetpack-compose-時如何得知-list-中的元件的屬性有了變化進而自動更新-composable"
canonicalURL = "https://medium.com/@danielkao/%E4%BD%BF%E7%94%A8-jetpack-compose-%E6%99%82%E5%A6%82%E4%BD%95%E5%BE%97%E7%9F%A5-list-%E4%B8%AD%E7%9A%84%E5%85%83%E4%BB%B6%E7%9A%84%E5%B1%AC%E6%80%A7%E6%9C%89%E4%BA%86%E8%AE%8A%E5%8C%96-%E9%80%B2%E8%80%8C%E8%87%AA%E5%8B%95%E6%9B%B4%E6%96%B0-composable-dec5f5be7c85"
mediumID = "dec5f5be7c85"
+++

被發了一條網頁分頁 favicon 更新不同步的 issue。雖然我自己也常常遇到，但因為無傷大雅，而且一直沒找到對的時機點修正，所以一直沒有理它。

[Tabs show the previous web page's favicon icon · Issue #224 · plateaukao/einkbro](https://github.com/plateaukao/einkbro/issues/224)

但是，既然被發了 issue，就來解決看看吧。對於 Jetpack Compose 的元件更新機制的了解程度還是一團漿糊，所以胡亂試了好久，最終放棄亂槍打鳥，請出 chatGPT 給一下意見。

![](/images/dec5f5be7c85/1_CG-RwOLLgC0eGrQVBqiIrQ.png)

原來如此啊！如果想用 `mutableStateOf()` 代入一個列表，而且又希望列表中的項目的內容有改變時，能自動更新對應的 `Composable`，只要在項目中對應的內容也變成 `mutableStateOf()` 就可以了！

早點知道這件事的話，現在的一堆廢 code 應該就可以再找時間清一清了。

### 相關程式碼

下面的程式碼就不特別再講解了，單純是照著上面的作法，將 `Album` 中的 `bitmap` 多出另一個參數 `stateOfBitmap` 來記錄 `mutableStateOf()`，然後再把手動去踢 `Composable` 的程式片段移除。

[fix: #224 update album cover when updated · plateaukao/einkbro@6b5f700](https://github.com/plateaukao/einkbro/commit/6b5f7008efdd2e77c001ae213fe68096d2232d4b)
