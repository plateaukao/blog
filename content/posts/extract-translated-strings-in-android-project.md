+++
title = "Extract translated strings in Android project"
date = "2019-04-03T06:50:11.309Z"
description = "It’s common that an android developer is working on several projects. Sometimes, you just need some existing string translations from…"
slug = "extract-translated-strings-in-android-project"
canonicalURL = "https://medium.com/@danielkao/extract-translated-strings-in-android-project-adef05165e23"
mediumID = "adef05165e23"
[cover]
  image = "/images/adef05165e23/1_bXZwCYedjvXKLs0P9qPQwg.png"
+++


![](/images/adef05165e23/1_bXZwCYedjvXKLs0P9qPQwg.png)
*Hakone.Japan*

It’s common that an android developer is working on several projects. Sometimes, you just need some existing string translations from another Android project. Usually, the translated strings are scattered in ***strings.xml*** file in tens of folders named ***values-xx***. There’s no easy way to copy these string definitions from multiple folders into new project.

Therefore, I wrote a simple python script to do the job. All you have to do is:

1. Configure input and output folder (usually it would be looked like ***…/project\_name/app/src/main/res/*** )
2. run commands for each string key you wanna copy.

[View gist](https://gist.github.com/plateaukao/61168e88548da8d44e8a786ab54cf429)

**new\_string\_key** is optional if you expect using the same string key in new project.

Here’s the link to Github repository. Happy Coding~

[plateaukao/AndroidExtractTranslatedString](https://github.com/plateaukao/AndroidExtractTranslatedString)
