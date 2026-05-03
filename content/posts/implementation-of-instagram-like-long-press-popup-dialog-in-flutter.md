+++
title = "Implementation of Instagram-like Long Press popup Dialog in Flutter"
date = "2020-07-26T06:58:19.901Z"
description = "Scenario"
slug = "implementation-of-instagram-like-long-press-popup-dialog-in-flutter"
canonicalURL = "https://medium.com/@danielkao/implementation-of-instagram-like-long-press-popup-dialog-in-flutter-25fd955fd38a"
mediumID = "25fd955fd38a"
+++

### Scenario

Sometimes you want to give users a glimpse of more info about the item presented on current screen, but you don’t want to bring users to another screen. It’s too heavy and may distract user’s focus.

Instead of navigating to another detail screen, various UI components can be used to achieve this: to show a popup dialog or to slide in a bottom sheet panel. Either way is good; however, to dismiss the dialog or the bottom sheet panel, it involves user’s extra interaction. Users have to click on an OK button, or to slide the panel off explicitly.

A better way would be like Instagram’s long press behavior on its photo grid screen. In this case, Instagram uses this implementation to show a bigger photo, allowing users to see the bigger photo directly without leaving the current screen. Once user’s finger leaves the screen, the bigger photo will be disappeared.

![](/images/25fd955fd38a/1_b5v-yXolHum1xLXjHYKqIA.gif)
*Long Press on Photo Grid UI in Instagram App*

The behavior flow would be like the diagram below:

![](/images/25fd955fd38a/1_1rAdrm0LKs0As05Wd_sO9w.png)
*Flow of long press popup dialog*

### Problem

In Flutter, how could we achieve the same behavior? If you’re a bit familiar with Flutter coding, it’s not hard to know that `GestureDetector` can be used for the long press behavior handling with its `onLongPress` callback.

However, when trying to handle the `onLongPressEnd` callback in the same GestureDetector, you’ll find that this callback is never called. This is because when dialog is displayed, the GestureDetector is interrupted; you’ll no longer be able to get any gesture events.

In order to be able to handle both `onLongPress` and `onLongPressEnd` , we need to wrap the popup UI in another Flutter Widget — Overlay.

### Overlay & OverlayEntry

**Overlay** is a stack of entries that can be managed independent of the other Widgets that are already arranged on UI. Overlays let its child widgets “float” visual elements on top of other widgets by inserting them into the overlay’s Stack.

[Overlay class](https://api.flutter.dev/flutter/widgets/Overlay-class.html)

In order to use **Overlay**, we must wrap the widget we want to use into an **OverlayEntry**. Overlay entries are inserted into an Overlay using the **OverlayState.insert** or **OverlayState.insertAll** functions. To find the closest enclosing overlay for a given **BuildContext**, use the **Overlay.of** function, e.g.,

```
Overlay.of(context).insert(some_created_overlay_entry);
```

[OverlayEntry class](https://api.flutter.dev/flutter/widgets/OverlayEntry-class.html)

### Implementation

First, we write a flutter sample app with an image grid view in it. Function `_createGridTileWidget(String url)` is used to turn an image url into a Widget that will be shown as a grid tile. At line 82–89, you can see that `GestureDetector` is created. In `onLongPress()` , a popup dialog is created, and insert into `Overlay` , so that you can see the dialog is displayed.

In order to hide the dialog when user’s finger leaves the screen, at line 89, the dialog is removed from `Overlay` so that it can be hidden to user.

![](/images/25fd955fd38a/1_YxV94UGSWYvJ41eu3XHP-A.png)

To behave like Instagram, some animations are added into the popup dialog. an `AnimatedDialog` is written to handle the animation part; and it’s wrapped inside `OverlayEntry` . The real content is contained inside `_createPopupContent(String url)` .

![](/images/25fd955fd38a/1_Iw1fiIidr9IIXDHjBhMVNA.png)

About the dialog content, it’s nothing special. You can check the code below to know how it’s constructed.

![](/images/25fd955fd38a/1_lUjxvi2AeWr5tu1wCBg0-A.png)

### Demo

Now, here's the result gif of the demo application:

![](/images/25fd955fd38a/1_a-G2wuuKJJMii2SP-cvDWQ.gif)
*Demo of the sample app*

### Reference

If you want to see the whole demo application codes, you can refer to the Github project below:

[plateaukao/flutter\_long\_press\_dialog](https://github.com/plateaukao/flutter_long_press_dialog)
