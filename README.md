树莓派摄像头拍照+上传  
其实是想拍延时摄影的，想了想手头上有个树莓派，把摄像头往上面一插（  
事后再把图片下载来丢ffmpeg就好了  

安装：  
```
pip install pillow oss2 picamera
```
然后就可以python3 picam.py走起了！  
别忘了把里面的参数改成你自己的  
在网不好的场合下，上传OSS会出现报错退出的情况，建议上Supervisor  

have fun~