+++
title = "Flickr API integration in Flutter with Dart"
date = "2019-07-23T15:14:57.050Z"
description = "Flickr used to be a cool photo service that gathered many talented photographers. I started uploading all my photos to it since 2005, and…"
slug = "flickr-api-integration-in-flutter-with-dart"
canonicalURL = "https://medium.com/@danielkao/flickr-api-integration-in-flutter-with-dart-1c07d4b9e8d6"
mediumID = "1c07d4b9e8d6"
+++

![](/images/1c07d4b9e8d6/1_BR4aqmuc6kDpZ8CbJ9_z0A.png)

> Flickr used to be a cool photo service that gathered many talented photographers. I started uploading all my photos to it since 2005, and now I’ve uploaded more than 160k photos. With so many memories in Flickr, I would like to have an app to randomly show me my own photos in order to refresh good old memories.

There are many Flickr API Kits in different programming languages in Flickr official website; however, Dart is not one of them. I either need to implement the API wrapper by referencing its Web API document or find another solution on the internet.

[Flickr Services](https://www.flickr.com/services/api/)

Without luck, I couldn’t find useful Flickr related implementations for dart. I decided to wrap the Web APIs in dart by myself. But first of all, I need to deal with the authentication process. You can see the authentication process explained below.

### Authentication difficulties

Flickr still uses OAuth version 1.0. It needs 3 API calls to complete the authentication process. Among the flow, a web page interaction is required for users to grant the access, and get the pin code to input into second API call.

[Flickr Services](https://www.flickr.com/services/api/auth.oauth.html)

![](/images/1c07d4b9e8d6/1_bQb5jOTAmN32hHp2ZY6PPQ.png)

It would take some effort to implement the OAuth1 signature generation, and appending related http query string parameters along with the APIs that needs authentication. Fortunately, someone already implemented the hard work for OAuth1 authentication. We only have to pass in necessary information related to Flickr in order to make it work.

By the way, remember to get your own developer API key and API secrete from Flickr.

### oauth1 for OAuth authentication

[oauth1 | Dart Package](https://pub.dev/packages/oauth1)

By following the oauth1 package’s documentation you can initiate the flow like this and call the *requestTemporaryCredentials().* It will return the Web url that you need to display to users.

[View gist](https://gist.github.com/plateaukao/4eb465b48e4f996dd97d566aa25b8383)

### url\_launcher : for WebView

For displaying webview, I used url\_launcher package. It’s very straightforward too.

[View gist](https://gist.github.com/plateaukao/024f8473cd7de238cfa713a77205bd9b)

![](/images/1c07d4b9e8d6/1_WWP6KGc8pZ9jeJwNHKa_jw.png)
*The WebView to ask for user permission.*

![](/images/1c07d4b9e8d6/1_1nqi0wbLwDHTJgT3ymM0Gw.png)
*After getting user permission, it will show the pin code*

[url\_launcher | Flutter Package](https://pub.dev/packages/url_launcher)

After getting the pin-code from webview, A dialog will be displayed to ask user input the pin-code, and feed it into requestToken().

![](/images/1c07d4b9e8d6/1_Bdw5KDMJ6Y0Y2vnYuHDWaA.png)
*Create a dialog to get the pin code from user.*

In the end, requestToken will successfully return an oauth1.Client object, that can be used to call other Flickr API.

[View gist](https://gist.github.com/plateaukao/0e66fb2ec5a4520b2bf769cd215588d3)

Voila! The authentication is done! The rest part is pure dart and flutter implementation which can be easily built up based on sample codes on flutter web site.

That’s it! With one night effort, my app is running well in my android phone, and also in the iOS simulator too. :)

![](/images/1c07d4b9e8d6/1_uFAf5_RBUwPwehK5Gi3ChA.png)
*A simple grid view layout to show random page of photos from my own Flickr account*

### PS.

Now there’s a better way to get pin code! Please check my another article:

[Flickr Authentication in Flutter (Part II)](https://medium.com/@danielkao/flickr-authentication-in-flutter-part-ii-c06495127f60)
