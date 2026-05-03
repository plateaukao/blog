+++
title = "How to Publish an Android Library to jcenter"
date = "2019-12-03T07:49:52.893Z"
description = "I used to using this plugin for creating android library release zip file, and manually upload it to bintray website."
slug = "how-to-publish-an-android-library-to-jcenter"
canonicalURL = "https://medium.com/@danielkao/how-to-publish-an-android-library-to-jcenter-a31231b47241"
mediumID = "a31231b47241"
+++

![](/images/a31231b47241/1_jYFBXKXr_vrW7Vrb4bF8bQ.jpeg)

I used to using this plugin for creating android library release zip file, and manually upload it to **bintray** website.

[blundell/release-android-library](https://github.com/blundell/release-android-library)

Recently, it says it’s no longer being maintained; and another gradle plugin is recommended.

[novoda/bintray-release](https://github.com/novoda/bintray-release)

Novoda’s bintray-release allows you to upload locally built javadoc/source jars, and library aar files to **bintray** directly, without manual work. What a relief if it really works.

By following the instructions on GitHub, within minutes, the configuration is ready for trial.

However, during building local files, some javadoc error might happen with following error logs:

[View gist](https://gist.github.com/plateaukao/7263cf6fee8c7d2f59ce44e209a7c0af)

It happens when javadoc task encounters some errors. This error can be bypassed by adding following code snippet to the gradle file.

[View gist](https://gist.github.com/plateaukao/b477a0ddc22a25e34ead28bcfaf0e811)

After configuring all parameters for `bintray-release` plugin, remember to add `dryRun = false` in the script, or execute the command as below, to allows it really uploading the files to bintray:

```
./gradlew clean build bintrayUpload -PbintrayUser=me -PbintrayKey=key -PdryRun=false
```
