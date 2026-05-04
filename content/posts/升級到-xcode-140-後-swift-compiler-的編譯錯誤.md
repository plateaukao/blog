+++
title = "升級到 xcode 14.0 後 Swift Compiler 的編譯錯誤"
date = "2022-10-30T09:42:35.330Z"
description = "追新的版本，免不了常常會遇到原本能編譯的程式碼，突然又動不了。不論是 Android 環境或是 iOS，不論熟不熟悉，遇到問題時還是要上網找別人的經驗分享。"
slug = "升級到-xcode-140-後-swift-compiler-的編譯錯誤"
canonicalURL = "https://medium.com/@danielkao/%E5%8D%87%E7%B4%9A%E5%88%B0-xcode-14-0-%E5%BE%8C-swift-compiler-%E7%9A%84%E7%B7%A8%E8%AD%AF%E9%8C%AF%E8%AA%A4-c8a15d530d89"
mediumID = "c8a15d530d89"
[cover]
  image = "/images/c8a15d530d89/1_Ts-5Qv2VhlZT4CM34t9AEw.png"
+++


追新的版本，免不了常常會遇到原本能編譯的程式碼，突然又動不了。不論是 Android 環境或是 iOS，不論熟不熟悉，遇到問題時還是要上網找別人的經驗分享。

這次是 xcode 的問題，而且這問題我竟然遇到了兩次：一次是想要在 iPhone 上編譯一個 open source 的 browser app ；沒辦法，用其他的 browser 就是會覺得一直在被監視中。另一次是為了要把舊的手機中的一些檔案傳到新買的 iPhone 中，想要把之前魔改過的 Sharik (內網檔案互傳的跨平台 App) 裝進去，在編譯時卡住了。

#### Flutter Browser App

[GitHub - pichillilorenzo/flutter\_browser\_app: A Full-Featured Mobile Browser App (such as the…](https://github.com/pichillilorenzo/flutter_browser_app)

#### Sharik

[GitHub - plateaukao/sharik: Sharik is an open-source, cross-platform solution for sharing files via…](https://github.com/plateaukao/sharik)

錯誤訊息大致如下，關鍵字是它在抱怨看不懂 `@available`

![](/images/c8a15d530d89/1_Ts-5Qv2VhlZT4CM34t9AEw.png)

看來應該遇到的人還不少吧，比較容易的解決方式一下子就找到了。只要去修改一下 Podfile，指定平台是 iOS 14，跟把 Swift 版本設定為 5.0 就可以了。

```
platform :ios, '14.0'
```

```
...  
...
```

```
post_install do |installer|  
  installer.pods_project.targets.each do |target|  
    flutter_additional_ios_build_settings(target)  
  
    target.build_configurations.each do |config|  
      config.build_settings.delete 'IPHONEOS_DEPLOYMENT_TARGET'  
      config.build_settings['SWIFT_VERSION'] = '5.0'  
      config.build_settings['ENABLE_BITCODE'] = 'NO'  
      config.build_settings['GCC_PREPROCESSOR_DEFINITIONS'] ||= [  
        '$(inherited)',  
        'AUDIO_SESSION_MICROPHONE=0',  
        'DISABLE_PUSH_NOTIFICATIONS=1'  
      ]  
    end  
  end  
end
```

### 結語

能在 iPhone 上跑自己寫的程式，感覺真不錯。目前 Sharik 和 Flutter Browser 都可以正常執行了。接下來就要看要不要在 Flutter Browser 中，把一些 EinkBro 的功能移植過來，先頂一陣子。

![](/images/c8a15d530d89/1_dS44CJLKlocFZEuMoPt5Cw.jpeg)

### 相關連結

簡書上的文章：<https://www.jianshu.com/p/5d7af7b9eb71>
