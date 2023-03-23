from bs4 import BeautifulSoup
import requests
from lxml import etree
import re
from urllib.parse import urlparse
from datetime import datetime
import time



class lmy1:
    def __init__(self,delay=3):
        self.delay = delay
        self.urls = {}
    def wait(self,url):
        netloc = urlparse(url).netloc
        # print(netloc)
        lastOne = self.urls.get(netloc,False)
        if lastOne and self.delay > 0:
            sleepTime = self.delay - (datetime.now()-lastOne).seconds
            if sleepTime > 0:
                time.sleep(sleepTime)
        self.urls[netloc] = datetime.now()

d = lmy1()

# 首先爬取该视频的保存地址
html1 = "https://new.qqaku.com/20220825/xVf2DfJd/1100kb/hls/playlist_up.m3u8"

reponse1 = requests.get(url=html1).text
d.wait(html1)
#
# # 将其保存下来
with open("test.txt","w") as fp:
    fp.write(reponse1)
#
# 遍历保存下来的文件
summ = 1
with open("test.txt",'r') as fp:
    t1 = fp.readlines()
    for i in t1:
        if i.startswith("#"):
            continue
        else:
            with open("sp1.mp4","ab") as fp:
                fp.write(requests.get(i).content)
                print(summ)
                summ += 1
                d.wait(i)



