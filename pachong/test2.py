from bs4 import BeautifulSoup
import requests
from lxml import etree
import re
from urllib.parse import urlparse
from datetime import datetime
import time
import json
import urllib.request
from urllib.parse import urljoin
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

url = "https://new.qqaku.com/20220731/5TKw4kYs/1100kb/hls/index.m3u8"
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0",
"Referer": "https://jx.aidouer.net/"
}
t1 = requests.get(url,headers=headers).text
d.wait(url)
with open("..\wbwj\m3u83.text","w",encoding="utf-8") as fp:
    fp.write(t1)

with open("..\wbwj\m3u83.text","r",encoding="utf-8") as fp:
    t2 = fp.readlines()
    for j in t2:
        if j.startswith("#"):
            continue
        else:
            j.replace("\n", "")
            print(j)
            with open(r"..\wbwj\2.mp4", "ab") as f:
                f.write(requests.get(j,headers=headers).content)
                d.wait(j)

