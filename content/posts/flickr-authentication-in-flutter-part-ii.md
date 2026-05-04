+++
title = "Flickr Authentication in Flutter (Part II)"
date = "2019-07-25T16:20:25.956Z"
description = "Following the steps described in last article, you can have a working version of Flickr authentication module in Flutter. However, it’s…"
slug = "flickr-authentication-in-flutter-part-ii"
canonicalURL = "https://medium.com/@danielkao/flickr-authentication-in-flutter-part-ii-c06495127f60"
mediumID = "c06495127f60"
[cover]
  image = "/images/c06495127f60/1_pecNyXcm3szOvnyBJH3Xzw.png"
+++


### Flickr Authentication in Flutter (II)

![](/images/c06495127f60/1_pecNyXcm3szOvnyBJH3Xzw.png)

Following the steps described in [last article](https://medium.com/@danielkao/flickr-api-integration-in-flutter-with-dart-1c07d4b9e8d6), you can have a working version of Flickr authentication module in Flutter. However, it’s very tedious to remember the pin code, and input it in the dialog in step 2.

By reading closely the **“**[**Getting a request token**](https://www.flickr.com/services/api/auth.oauth.html#request_token)**”** part in Flickr website, you’ll find that, in fact, there’s another way to get the verifier we need without user intervention. A parameter called “oauth\_callback” is used to specify a url. If it’s defined in the request; after authorization is complete, Flickr will redirect the user back to your application using the `oauth_callback` specified with your [Request Token](https://www.flickr.com/services/api/auth.oauth.html#request_token). It looks like this:

```
http://www.example.com/  
?oauth_token=72157626737672178-022bbd2f4c2f3432  
&oauth_verifier=5d1b96a26b494074
```

Since the oauth\_verifier can be obtained directly in the url, you don’t have to ask user to input the pin code anymore!

So, let’s start modify the original implementation.

Originally, I use ***url\_launcher*** package to display the web authentication page, and get the pin code. We have to change to use ***flutter\_webview\_plugin*** *instead, since it allows us to intercept the redirect urls.*

[View gist](https://gist.github.com/plateaukao/e978ec4235bd13329743c9b6b70477fa)

I used “http://localhost/” as my callback url, and try to check url change on *FlutterWebviewPlugin* instance. When its host is “localhost”, and it does contain a query parameter “**oauth\_verifier**”, I just feed it into requestToken directly. No more memory tests and displaying dialogs!

That’s it! Hope you find this article as useful as I do. Here’s the demo from my app:

![](/images/c06495127f60/1_macNSy153Ihz-b5aj9RkWw.gif)

### Reference:

[Flickr API integration in Flutter with Dart](https://medium.com/@danielkao/flickr-api-integration-in-flutter-with-dart-1c07d4b9e8d6)
