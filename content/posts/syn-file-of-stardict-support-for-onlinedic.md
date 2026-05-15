+++
title = "syn file (of stardict) support for OnlineDic"
date = "2008-05-08T09:45:00Z"
slug = "syn-file-of-stardict-support-for-onlinedic"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2008/05/syn-file-of-stardict-support-for.html"
bloggerID = "3016652411229004012"
tags = ["Computer", "Annecy Life", "Ricoh GRD"]
+++

[![R8071110 (by plateaukao)](/images/blogger/3016652411229004012/2474924895_19ca878e23.jpg "R8071110 (by plateaukao)")](http://www.flickr.com/photos/plateau/2474924895/ "R8071110 (by plateaukao)")  
(Ricoh GRD Nice, France)  
  
[![R8071019 (by plateaukao)](/images/blogger/3016652411229004012/2474856819_d09d631241_m.jpg "R8071019 (by plateaukao)")](http://www.flickr.com/photos/plateau/2474856819/ "R8071019 (by plateaukao)")  
  
在尼斯待了兩天，第二天一早買了Pass 1 jour (4歐)，可以坐Tram，巴士。想說就坐坐公車走遠一點兒吧。反正沒要去摩洛哥的話，時間就多了很多。看了一下公車站的地圖，有兩條線會沿著海岸往東去，一條線是81，圖上為綠色的線；另一條是100，圖上是灰色的線。綠色看起來比較順眼，所以我就選了81線坐。  
  
[![R8071031 (by plateaukao)](/images/blogger/3016652411229004012/2475683242_eb2bc861f1_m.jpg "R8071031 (by plateaukao)")](http://www.flickr.com/photos/plateau/2475683242/ "R8071031 (by plateaukao)")  
  
81線的起點是Gare Routiere(公車/客運總站)，我在它的下一站上車。公車班次還算密集，一小時有一班或是兩班。上車後發現車上都是老人。尼斯也是老人城嗎？還是我要走的這條線是適合養老的地方呢？我想應該都不是吧。因為我上車的時間是上班時間吧，年輕人都在上班或上課。  
  
無心插柳柳成蔭，我來到了一個叫Saint-Jean-Cap-Ferrat的地方。這是在尼斯東方凸出的一個小小半島，車程大約是三十分鐘到四十分鐘。遠離尼斯市區，這兒的海灘應該會有比較多上空美女吧(事實證明…我想太多了)。  
  
一路上風光明睸，到處都是港口和小船。岸上則是有山景可瞧，車子隨著海岸彎來彎去，倒也不嫌無聊。只可惜不行隨時停下來好好欣賞一下港口的景色。  
  
到了半島上，經過一間Office du Tourisme，我就臨時興起下車去瞧瞧，拿了一堆簡介、地圖，並問了小姐這附近有什麼景點，然後開始了我的漫步之旅。  
  
[![P5055850 (by plateaukao)](/images/blogger/3016652411229004012/2474885132_1537cc7c10.jpg "P5055850 (by plateaukao)")](http://www.flickr.com/photos/plateau/2474885132/ "P5055850 (by plateaukao)")  
  
這兒比較有名的景點是：Villa Grecque Kerylos(希臘別墅)、Villa & Jardins Ephrussi de Rothschild(某個花園)、動物園(動物園…老實說國外比台北市立動物園好的、大的沒幾個…所以直接跳過)，和沿著半島海岸的散步道，中間穿插著幾個收費或免費的海灘。前兩者要收費，合起來買套票會比較便宜，不過我都沒去，因為我還是對風景比較有興趣。散步道總共分成三段，所需時間各是1小時(Baie des Fourmis到Plage Cros des Pin)、半小時(Paloma Plage經過Pointe Saint Hospice, Pointe du Colombier，再回到原點)，和一個半小時(Les Fosses到Plage Passable)。這時間是小姐估的，我個人走起來，實際上都比這些時間還要長很多。  
  
散步嘛，不用急。前兩段散步道比較精緻，景色變化也比較大。最後一段，真的走起來大概要兩個半小時以上吧，而且前一個小時都是同樣的岩岸地形，有點枯燥。散步道的旅遊資訊做得還不錯，配合著我從旅遊中心拿的地圖，再加上不時出現的旅遊路標，儘管半島上的路很不規則，也不至於會迷路。  
  
[![R8071030 (by plateaukao)](/images/blogger/3016652411229004012/2475682562_37eed4d0e2.jpg "R8071030 (by plateaukao)")](http://www.flickr.com/photos/plateau/2475682562/ "R8071030 (by plateaukao)")  
  
逛到下午逛累了，再次走回office du tourisme，跟小姐要了份81路公車的時刻表(還蠻漂亮的)。這時刻表其實就是公車站牌上附的。搭著車回到市區。4歐的交通一日券，可以逛到這麼棒的景色，比花上15歐到伊芙島看島不生蛋的監獄要好多了。  
  
\*\*\*\*  
轉入正題。  
  
Let's talk about the new improvement of onlinedic. Long time ago, I found there's an extra file in stardict's dictionary zip file. For example, in the zip of Larousse Chambre Francai Anglais, I found a file with the extension of syn. At that time, I did not pay much attention about it; I was just busy with the main functions (make stardict fileformat work on my onlinedic).  
  
Today, I spent some time figuring out what it really is, and what it's for. In the source tree of stardict, under /doc/, a file called StardictFileFormat explained its usage:  
> {4}. The ",syn" file's format.  
> This file is optional, and you should notice tree dictionary needn't this file.  
> Only StarDict-2.4.8 and newer support this file.  
>   
> The .syn file contains information for synonyms, that means, when you input a synonym, StarDict will search another word that related to it.  
>   
> The format is simple. Each item contain one string and a number.  
> synonym\_word; // a utf-8 string terminated by '\0'.  
> original\_word\_index; // original word's index in .idx file.  
> Then other items without separation.  
> When you input synonym\_word, StarDict will search original\_word;  
>   
> The length of "synonym\_word" should be less than 256. original\_word\_index is a 2-bits unsigned number in network byte order. Two or more items may have the same synonym\_word" with different original\_word\_index. The items must be sorted by stardict\_strcmp() with synonym\_word.

  
  
Because the .syn file format is similar to that of the idx file, it's not difficult for me to make use of it. NOW, onlinedic supports syn!
