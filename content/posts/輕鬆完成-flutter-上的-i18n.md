+++
title = "輕鬆完成 Flutter 上的 i18n"
date = "2020-08-16T03:46:06.205Z"
description = "對於 Flutter app 中，字串多國語系化這件事，官網中提供了步驟繁複的文件，深怕大家不知道它有多難搞。所以網路上出現了各種奇奇怪怪 plugin，有的是利用 json 來處理；有的是要你寫 dart class…"
slug = "輕鬆完成-flutter-上的-i18n"
canonicalURL = "https://medium.com/@danielkao/%E8%BC%95%E9%AC%86%E5%AE%8C%E6%88%90-flutter-%E4%B8%8A%E7%9A%84-i18n-19655dbe7546"
mediumID = "19655dbe7546"
[cover]
  image = "/images/19655dbe7546/1_JYUJ7d6mHBbcqZPYaDvIsw.jpeg"
+++


![](/images/19655dbe7546/1_JYUJ7d6mHBbcqZPYaDvIsw.jpeg)
*Flags in Annecy*

對於 Flutter app 中，字串多國語系化這件事，官網中提供了步驟繁複的文件，深怕大家不知道它有多難搞。所以網路上出現了各種奇奇怪怪 plugin，有的是利用 json 來處理；有的是要你寫 dart class 來放翻譯的內容。這幾天找到了一個還算單純的方式，而且是不用額外裝非官方的 plugin 就可以完成的。想說來跟大家分享一下。

#### 難用的官網教學

首先，為了做為參考，可以先看一下官網上的文件有多複雜：

[Internationalizing Flutter apps](https://flutter.dev/docs/development/accessibility-and-localization/internationalization)

---

### Flutter 後來做的改良

Flutter 應該也聽到了使用者的心聲，知道這整個流程有多麻煩，所以在 2020 年有了改良的版本，文件可以參考這個連結：

[Flutter Internationalization User Guide](https://docs.google.com/document/d/10e0saTfAv32OZLRmONy866vnaw0I2jwL8zukykpgWBc/edit)

步驟如下：

1. 在 pubspec.yml 中加入必要的 plugin

[View gist](https://gist.github.com/plateaukao/afc2ddbe521652a2ec699df22dc3fb99)

2. 在 Flutter app 的根目錄建立一個文字檔 `l10n.yaml`，加入下面的資訊。

[View gist](https://gist.github.com/plateaukao/66c9590e111535f902ab79d481752e75)

- `arb-dir` 是設定你將會把字串相關的檔案放置的目錄，裡頭包含 .arb 格式的檔案。
- `template-arb-file` 設定預設字串檔的檔名，其中需包含這些字串的 meta data。這檔案必須放在 arb-dir 下面。
- `output-localization-file` 設定當 Flutter 試著幫你產生所有需要的資訊並塞進一個 Dart 檔案時，該 Dart 檔案的名稱(app\_localizations.dart)。同樣的，這個檔案也是會生成在 `arb-dir` 下面。

3. 再來就是建立 arb-dir 下面的 app\_en.arb 檔案。裡面的寫法很直覺，在第二行寫上這個檔案所代表的 locale，4~7行則是一個字串的定義。目前測試的結果，在 app\_en.arb這個 template arb file中，5~7行的 description是不可以少的。(但你可以塞空字串進去，如果你不想為 description 傷神的話)。

[View gist](https://gist.github.com/plateaukao/5ad8d3bd8fa14239e637f5b7ee5c0a50)

4. 有了主要的 app\_en.arb 之後，你可以開始建立其他語系的 app\_xx.arb，然後仿造 app\_en.arb 的寫法，加入翻譯後的字串，比方說如下：

[View gist](https://gist.github.com/plateaukao/066ee39ad8704d85a68332baec65ede6)

5. 再來就是在主要的 Flutter 程式中，加入剛剛說的，Flutter 會幫你產生的 app\_localizations.dart。在第2行把它 import 進來，以及13，14行。

[View gist](https://gist.github.com/plateaukao/ad59f2862b72b7948ded63fa9e10d141)

6. 再來就可以開始使用我們之前建立好的字串了，請看第7行。

[View gist](https://gist.github.com/plateaukao/c2a0062213035e5ca4738a3553d12a67)

如果嫌 AppLocaziations.of(context).hello\_world 太長的話，可以考慮在一開始 `output-localization-file` 取個短一點的 class name，或是建立一個簡易的 class 如下：

```
class S {  
  static AppLocalizations of(BuildContext context) => AppLocalizations.of(context);  
}
```

然後在Flutter Widget 被生成後，建立 local variable

```
AppLocalizations _str;
```

```
@override  
void didChangeDependencies() {  
  super.didChangeDependencies();  
...
```

```
  _str = S.of(context);  
}
```

使用字串時，就可以變得很簡潔如 `_str.hello_world`。

如果要在 iOS app 中支援多國語系，必須在 iOS 設定檔中設定，可以參考

[Internationalizing Flutter apps](https://flutter.dev/docs/development/accessibility-and-localization/internationalization#appendix-updating-the-ios-app-bundle)

或是下面這篇文章中的 **iOS 的額外設定** 這一段。

[讓 Flutter App 支援多國語系的開發流程](https://medium.com/@zonble/%E8%AE%93-flutter-app-%E6%94%AF%E6%8F%B4%E5%A4%9A%E5%9C%8B%E8%AA%9E%E7%B3%BB%E7%9A%84%E9%96%8B%E7%99%BC%E6%B5%81%E7%A8%8B-ceb31532e2e1)

---

是不是比官網的教學容易多了呢？而且哪天要加入新的語系，只要再加入新的 app\_xx.arb 就可以了。
