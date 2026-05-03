+++
title = "Web Browser for Android E-Ink Devices"
date = "2021-02-21T16:17:15.667Z"
description = "As the CPU power getting stronger and stronger, and screen refresh speed keeps improving for E-Ink devices, more and more people start to…"
slug = "web-browser-for-android-e-ink-devices"
canonicalURL = "https://medium.com/@danielkao/web-browser-for-android-e-ink-devices-c78b680edf98"
mediumID = "c78b680edf98"
tags = ["EinkBro"]
+++

### Web Browser for Android E Ink Devices (EinkBro)

As the CPU power is getting stronger, and screen refresh speed keeps improving for E-Ink devices, more and more people start to use E-Ink devices to browse the internet. It’s doable; however the experience is still not good enough. Existing browsers are not designed for E-Ink devices. So many UI elements are designed for normal Android devices: fancy animations, dimming background when dialogs pop up, etc.

To make a browser suitable for E-Ink devices, two principles should be followed while designing UI interactions:

- Fewer repaint counts
- Make repaint area as small as possible

---

### Fewer Repaint Counts

To meet this criteria, the first step is to remove animations. Animation means showing the gradual transition status from one state to another state. It’s very nice to see transitions for normal devices; however, on E Ink devices, due to its low refresh rate, the transition is usually not smooth enough, and also it causes unnecessary residual image that make screen hard to read. Removing animations not only reduces CPU processing, but also reduces screen refresh counts.

In addition, while browsing web pages, it’s very common to scroll down the screen to read more content. This behavior also produces image residuals on Eink devices. It’s better to browse the web just like reading a book: page by page. To fulfill this, specific buttons can be added to handle page up and page down. If the E Ink devices has physical volume keys, we can also use them for the same purpose.

### Make Repaint Area as Small as Possible

If the repaint area is large, it’s more likely to create more image residual on E Ink device. So, reducing the area means fewer ghost images. An obvious example is showing a dialog. On mobile devices, Apps display dialogs for asking user whether they want to do something or not; or showing option dialogs to allow user choose from multiple items. When dialog pops up, to make user more concentrated on the dialog, system usually dims the rest of the screen. The intention is good, but this causes E-Ink device to flash the whole screen. If the dialog is well designed to achieve the same goal, the dimming effect could be removed.

---

### Create an E Ink Specific Browser App

So far, I haven’t seen a dedicated browser for E-Ink devices yet. I decided to make one, based on a Github project written by [Gaukler Faun](https://github.com/scoute-dich). FOSS Browser is a lightweight browser that supports many features, including ad blocking, tab control, gesture control, etc. I took some time to refactor the codes and make necessary modifications to make it more appealing for E-Ink devices. Now it has a lot of useful features for E Ink devices. I draw a mindmap image to layout the main features:

![](/images/c78b680edf98/1_y5X5xs3rZ_fJEacMoNN0dw.png)

#### **Now it has following E-ink related features:**

- Reader mode (remove headers, ads, sidebars, footers, for easier reading)
- Full text translation mode
- Vertical reading mode (suitable for Chinese and Japanese)
- Content display customization (bold font, font size change, font style change)
- Export web content as epub file
- PageUp/pageDown by (touch area / volume keys / onscreen buttons)

![](/images/c78b680edf98/1_qC1H_rrOMlEsBtxPNqrPqw.png)

- tool bar configuration (show/hide actions, or re-arrange order)

![](/images/c78b680edf98/1_NWlDs4JjkLeBGMZiVvxEsA.png)

![](/images/c78b680edf98/1_nXw0r3ehv6dPFBjRGnn0lg.png)
*All available actions on toolbar*

- **Desktop mode feature**
- All icons in high contrast colors
- Refactor most popup dialogs, so that there’s no longer animations.
- Remove gray mask when dialog pops up.

#### And more generic features

- Re-organize menu items so that they can be accessed without switching between tabs.

![](/images/c78b680edf98/1_UMwc2AvqL5Ejdz-AO5g81g.png)
*Action Menu*

### Feature Introduction Video

### EInkBro Browser

[EinkBro - Apps on Google Play](https://play.google.com/store/apps/details?id=info.plateaukao.einkbro)

#### F-Droid Download

[EinkBro | F-Droid - Free and Open Source Android App Repository](https://f-droid.org/packages/info.plateaukao.einkbro/)

#### Github Binary Release

[Releases · plateaukao/browser](https://github.com/plateaukao/browser/releases)

#### Github source codes:

[plateaukao/browser](https://github.com/plateaukao/browser)
