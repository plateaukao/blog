+++
title = "My 2 cents on Image Processing in Flutter"
date = "2019-07-29T14:05:31.022Z"
description = "In Flutter, it’s easy to load an Image widget. Flutter provides several different ways:  You can use Image.network, Image.asset or…"
slug = "my-2-cents-on-image-processing-in-flutter"
canonicalURL = "https://medium.com/@danielkao/my-2-cents-on-image-processing-in-flutter-a6ab5166f590"
mediumID = "a6ab5166f590"
+++

![](/images/a6ab5166f590/1_qKJvABWGL9EyztFfvLlJbQ.png)

In Flutter, it’s easy to load an Image widget. Flutter provides several different ways: You can use ***Image.network(), Image.asset() or Image.memory()***depending on the source you want to load the image.

However, Flutter is known to be slow at processing image, including decoding image when the source file is relatively large.

[View gist](https://gist.github.com/plateaukao/ffc76091e5d6901e220d6ea9bed60840)

The above code snippet is an example of loading an Image from the internet.

**At line 8**: download the data from the internet;

**At line 12**: an Image Widget is created;

**At line 14**: then ask system to build the Widget again by using ***setState().***

This code works, but UI often blinks when the image is replacing the placeholder on screen.

![](/images/a6ab5166f590/1_OEoTqSR2WAm_qBeEniQv7g.gif)

### precacheImage() Come to Rescue!

After searching for a long time on the internet, I finally found the way to fix this problem.

***Image.memory()*** is just setting up the Image Widget; it does not mean the Widget is ready to be drawn on screen yet. That’s why you would see the short period of blank screen on the animation above.

To solve this, all you have to do is wait until the Image Widget is ready, and then call setState() afterward. That’s where [***precacheImage()***](https://api.flutter.dev/flutter/widgets/precacheImage.html) comes to rescue. It can help you to cache (or load) the Image in advance. When you really need to draw it, you don’t have to spend time decoding the binary again.

[View gist](https://gist.github.com/plateaukao/3f0f587082f77d26c5729ab14c04cb40)

**At line 14**: we added the code, and that’s it!

Look at the no-blink-anymore UI! Hope this tip is useful for you too.

![](/images/a6ab5166f590/1_jRKOJ2SvoWOaII08Hmvb4w.gif)
