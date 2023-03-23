# import requests
# #
# # # print(requests.get("http://api.xfsub.com/index.php?url=https://www.iqiyi.com/v_19rr9xxnrk.html"))
# #
# # str = 12.341322
# #
# # print("{:.2f}".format(str))

from bs4 import BeautifulSoup
import requests
from lxml import etree
import re
from urllib.parse import urlparse
from datetime import datetime
import time
import json
import urllib.request


class lmy1:
    def __init__(self,delay=3):
        self.delay = delay
        self.urls = {}
    def wait(self,url):
        netloc = urlparse(url).netloc
        print(netloc)
        lastOne = self.urls.get(netloc,False)
        if lastOne and self.delay > 0:
            sleepTime = self.delay - (datetime.now()-lastOne).seconds
            if sleepTime > 0:
                time.sleep(sleepTime)
        self.urls[netloc] = datetime.now()


url1 = "http://www.cse.edu.cn/"

html1 = requests.get(url1).text
html1.encode("utf-8")
print(html1)
html1 = html1.splitlines()
with open(r"D:\桌面\新建文本文档 (2).html","a+") as fp:
    for i in html1:
        fp.write(i)