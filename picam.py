import picamera
from time import sleep
from PIL import Image
import datetime
import time
import oss2
import requests
import os

ossKeyId = ''
ossKeySecret = ''
ossBucket = ''
webhookUrl = ''

while True:

    ## 初始化摄像头
    camera = picamera.PiCamera()
    camera.rotation = 180
    camera.start_preview()
    t = datetime.datetime.now().strftime("%Y%m%d%H%M")
    fname = t+".jpg"
    print(fname)
    sleep(2)
    camera.capture(t+".jpg")
    camera.stop_preview()
    camera.close()

    ## 压缩图片
    with Image.open(fname) as img:
        img.save(fname, optimize=True, quality=85)
        img.close()

    ## 上传图片
    d = datetime.datetime.now().strftime("%Y%m%d")
    auth = oss2.Auth(ossKeyId, ossKeySecret)
    bucket = oss2.Bucket(auth, 'https://oss-cn-shenzhen.aliyuncs.com', ossBucket)
    ossPath = "raspiImg/"+d+"/"+fname
    bucket.put_object_from_file(ossPath, fname)
    print(ossPath)

    ## POST 图片文件名
    url = webhookUrl
    payload = ossPath
    headers = {
        'Content-Type': "text/plain",
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

    ## 删除图片
    os.remove(fname)

    ## 休眠
    time.sleep(60)