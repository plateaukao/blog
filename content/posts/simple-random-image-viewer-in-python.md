+++
title = "Simple Random Image Viewer in Python"
date = "2010-11-09T16:10:00Z"
slug = "simple-random-image-viewer-in-python"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2010/11/simple-random-image-viewer-in-python.html"
bloggerID = "7602878898480019565"
tags = ["Python"]
[cover]
  image = "/images/blogger/7602878898480019565/2474989614_a6fbaba822_z.jpg"
+++

[![P5055943](/images/blogger/7602878898480019565/2474989614_a6fbaba822_z.jpg)](http://www.flickr.com/photos/plateau/2474989614/ "P5055943 by plateaukao, on Flickr")  
Nice.France  
  
畫畫，是個人的事。  
只要有心，人人都是個畫家。  
  
\*\*\*\*\*  
  

Usually, I use my flickrRandomImage python script to fetch some random images from my flickr account to amuse myself. However, it heavily depends on the internet access speed. When the network traffic is jammed, it takes a long time to generate 10 thumbnails for each run. Therefore, I decided to go for another way: create a simple image viewer which can randomly pick photos from a designated folder on local hard disk.

  

Once the decision is made, it won't take too much time to find a starting solution. By choosing python as the development programming language, I can easily find the samples I need on the internet. The first step is to find a workable image viewer written in python. This is not a difficult task because python's library set is very rich; image viewer is something people tend to write as a sample app.

  

Well, this's what I found:[creating-a-simple-photo-viewer-with-wxpython/](http://www.blog.pythonlibrary.org/2010/03/26/creating-a-simple-photo-viewer-with-wxpython/).  
This sample basically provides most of the features I need:

1) pop up a directory dialog to choose a folder  
2) to view images in forward/backward direction  
3) to toggle Slide View  
  
**What's left is:**  
1) load image files recursively in a folder  
2) show image randomly instead of in predefined sequence  
3) rotate the image according to the exif orientation information  
4) launch image file format associated application to do other actions  
5) track the viewed sequence in order to view backward  
  
**solution:**  
1) this is easy part. Check out os.path.walk and search on the internet.  
2) use "from random import choice"  
3) import [exif.py](http://sourceforge.net/projects/exif-py/) and check the value of "Image Orientation".  
    use wxImage.Rotation90 to rotate image accordingly  
4) use os.startfile()  
5) use a list to keep track of viewed photos  
  
**SOURCE:**  
<http://dl.dropbox.com/u/10576598/image_viewer3.py>
