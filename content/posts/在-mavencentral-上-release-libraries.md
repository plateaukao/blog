+++
title = "在 MavenCentral 上 Release Libraries"
date = "2021-03-02T10:56:39.504Z"
description = "對於 Android  SDK 或 Library 的開發者來說，最近有件大新聞，JFrog 要 sunset 他們家的 JCenter, GoCenter, ChartCenter 服務了。JCenter 是目前大部分 Android…"
slug = "在-mavencentral-上-release-libraries"
canonicalURL = "https://medium.com/@danielkao/%E5%9C%A8-mavencentral-%E4%B8%8A-release-libraries-3928fcede74e"
mediumID = "3928fcede74e"
+++

對於 Android SDK 或 Library 的開發者來說，最近有件大新聞，JFrog 要 sunset 他們家的 JCenter, GoCenter, ChartCenter 服務了。JCenter 是目前大部分 Android 開發者在發佈函式庫時的主要去處。這項服務即將在明年(2022) 2 月中止，而新的版本發布則是可以到這個月底 (2021/03/31)。

[Into the Sunset: Bintray, JCenter, GoCenter, and ChartCenter](https://jfrog.com/blog/into-the-sunset-bintray-jcenter-gocenter-and-chartcenter/)

為了因應這項改變，原先發布的 library，都要趁著這段過度時間趕快搬到 mavenCentral 去才行。下面會介紹怎麼改成由 mavenCentral 來發布 library。步驟不多，但要注意的細節蠻多的，一不小心就會踩坑。

---

### 主要步驟

1. 建立 sonatype.org 的帳號
2. 在 Jira 上開張票建立一個新的專案
3. 證明你有 groupId domain name 的權限
4. 加入 gradle plugin，並填寫所有必需的設定
5. 產生 artifacts ，用 GPG 加密，並上傳
6. 發布
7. 設定 Github Actions (非必要)

---

#### 建立 sonatype.org 帳號

到下面這個網址建立一個 sonatype.org 的帳號

[Sign up for Jira - Sonatype JIRA](https://issues.sonatype.org/secure/Signup!default.jspa)

帳號建立好後，如果這個 groupId (domain) 是你自己的，那請直接進行下一個步驟；如果你要發布的 library/sdk 是要針對一個已經存在 mavenCentral 上的 groupId，你必須在 JIRA 中先開一條 ticket，請已經有權限的人 comment 一下，這樣子 sonatype 的人才會幫你加發布的權限。範例如下：

[Add "Deployer Role" to new user for "com.linecorp.\*" project](https://issues.sonatype.org/browse/OSSRH-64770)

#### 在 Jira 中開票建立新專案

前往[這個連結](https://issues.sonatype.org/secure/CreateIssue.jspa?issuetype=21&pid=10134)，開啟一個新的 project 的票。

![](/images/3928fcede74e/1_kpocjnmzsvnaua5FgP1U4w.png)
*issues.sonatype.org*

#### 證明你是 groupId domain 的持有者

你必須證明你擁有 groupId 倒過來的 domain。舉例來說，如果你的 groupId 定為 `info.plateaukao` ，你就必須在 `plateaukao.info` 的 DNS provider 中加入下面的 TXT 記錄：

```
@    TXT    3600    OSSRH-xxxxx
```

OSSRH-xxxx 要填入你建立 project 的那張票的 id，讓 Sonatype 可以去驗證你的 domain。

#### 加入 gradle plugin，並填寫所有必需的設定

1. 在案子的最上層 `build.gradle` 加入下面設定

[View gist](https://gist.github.com/plateaukao/9824e985de17f3058ce528805cacade8)

2. 在 library 的 `build.gradle` 加上所需的 plugin 和相關設定。這邊以 `com.linecorp.linesdk` 為例子

[View gist](https://gist.github.com/plateaukao/3c4cf4ca18d2e5a81dd7642ac602d0a7)

第4，5行的 `maven-publish` 和 `signing` 是 gradle 內建的 plugin，所以不需要額外的 implementation，只要引用就行。

第 25 行開始的 `afterEvaluate` 則是當 artifact 都建立後要進行 deploy 的相關設定。第 33 ~ 35 行將 binary aar，和 javadoc，sources codes 都列為 artifacts。這三者都要存在才可以正常的發布到 mavenCentral。

72 行設定的 `credentials` 是 sonatype 上的帳號和密碼，可以在 `gradle.properties` 中設定 `repositoryUsername` 和 `repositoryPassword` 。如果專案是 Open Source 的，不想把相關的資訊寫在 `gradle.properties` ，可以參考一會兒提到的 Github Actions 設定方式，讓 gradle 在建置時，可以從 Github 設定中取得相關資訊。

80 行設定的 `signing` 區塊是針對 GPG signing 的設定。GPG signing 要先建立 GPG key。 在 Mac 上的話，可以先透過 Brew 安裝 gpg。

```
brew install gpg
```

然後 GPG key 可以在電腦上利用下面的指令建立：

```
gpg --full-generate-key
```

建立好 GPG key 後，要把 public key 上傳到某個 server 上。我是選擇上傳到 ubuntu.com

```
gpg --keyserver hkp://keyserver.ubuntu.com --send-keys ur_pgp_key_id
```

在電腦上要驗證上傳 artifacts 的話，可以先產生 secret key 的檔案 (利用下面的指令產生 secring.gpg 檔案。

```
gpg --export-secret-keys -o secring.gpg
```

然後把 build.gradle 中的 `signing` 區塊改成

```
signing {  
  sign publishing.publications  
}
```

如果不是指定 `useInMemoryPgpKeys` 的話，`signing` 會試著去找 sign 的下面相關參數

```
signing.keyId=xxx  
signing.password=xxxxx  
signing.secretKeyRingFile=secring.gpg
```

> 因為最後我們會希望可以透過 Github 的 Actions 來直接發布 library，所以無法將 secring.gpg 直接放在 git 中，我們要用另一個型式把它存在 Github 的 project secrets 設定裡。這會在下個步驟才講到。

如果一切都設定得當，這時可以執行下面的指令把 library 的 artifact 上傳到 sonatype 上。

```
./gradlew publish
```

順利的話，你可以在[這個連結](https://oss.sonatype.org/#stagingRepositories)中，點選左邊的 staging repositories 看到你上傳的 library artifacts。

![](/images/3928fcede74e/1_aDdSrQXryd-oBqSBahi6DA.png)
*oss.sonatype.org/#stagingRepositories*

這時，你可以手動點選該 repository，先把它 Close，再選 Release，就完成了發布。

#### 發布

不過，如果希望同樣是透過 gradle task 發布的話，可以加上 89 ~ 95 行的 `nexusStaging` 設定。基本上就是填入跟 73, 74 行一樣的帳號密碼，然後執行下面的指令，完成 release。

```
./gradlew closeAndReleaseRepository
```

#### 設定 Github Actions

設定 Github Actions 包含兩個步驟：第一個步驟是先去 Github project settings 的 secrets 設定好所需的參數。透過 mavenCentra 發布的 task，會需要用到下面幾個參數

![](/images/3928fcede74e/1_8lPFzUuJYpGEJ8npYn2Dpw.png)

第二個步驟則是在 repository 的 `.github/workflows/` 下產生 actions 的 yml 設定檔。舉例來說，可以建立一個 `ossrh.yml` 。內容可以參考下方

[View gist](https://gist.github.com/plateaukao/d84eecb39d2f9dae46b5cb48e55532b6)

關於 Github Actions 的設定，可以另行尋找其他的文件，在此不多做說明。

第 27 行就是上面提到的 task，將 artifacts 上傳到 sonatype staging repositories；第 33 行則是真的 release 到 mavenCentral 去。

這邊有一點要注意的是：signing 的參數跟一開始提到的不太一樣。如果是在電腦上手動進行 sign 的動作時，需要的參數是 keyId, password 和 secret ring file。但如果想要透過 Github Actions 來做的話，就要把 keyId 和 secret ring file，換成 signing key。 signing key 的值在 MacOS 中可以透過下面的指令取得：

```
gpg --armor --export-secret-key your_email@address | pbcopy
```

一切設定好之後，在 Github project 的 Actions tab 下，會出現`Deploy to OSSRH` 的選項，讓你可以透過它直接發布版本到 mavenCentral。

![](/images/3928fcede74e/1_KcSdFWwVS2tt8xMGRS19RQ.png)

為了避免誤觸這個 Action，在 7 ~ 9 行，還有 29 行加了條件，要先輸入 release 字樣才會真的開始動作。

#### 後話

目前還沒有找到比較容易的檢驗方式，所以都需要不斷地把設定 merge 到 github repository 後，然後試著執行 Github Actions 看成不成功。如果之後有找到好的方法，會再更新於本篇心得中。

---

### 參考資料

**英文的教學文件**

[How to upload jars to maven central](https://blog.10pines.com/2018/06/25/publish-artifacts-on-maven-central/)

**Sonatype 官方文件**

[OSSRH Guide](https://central.sonatype.org/pages/ossrh-guide.html)
