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
        print(netloc)
        lastOne = self.urls.get(netloc,False)
        if lastOne and self.delay > 0:
            sleepTime = self.delay - (datetime.now()-lastOne).seconds
            if sleepTime > 0:
                time.sleep(sleepTime)
        self.urls[netloc] = datetime.now()


headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
}

# 千图网
# for j in range(1,100):
#     html = requests.get("https://pro.58pic.com/psearch/lvyou-%E6%97%85%E6%B8%B8-0-0-0-p{}.html".format(j),headers=headers)
#     # print("https://pro.58pic.com/psearch/lvyou-%E6%97%85%E6%B8%B8-0-0-0-p{}.html".format(j))
#     html.encoding= "gbk"
#     # print(html.text)
#     soup = BeautifulSoup(html.text,"lxml")
#
#     imgurl = soup.select(".model-box img")
#     for i in imgurl:
#         # print(i)
#         print(i["title"],"https:"+i["data-original"])
#         a3 = requests.get(url="https:"+i["data-original"], headers=headers).content
#         path1 = "D://abc//" + i["title"] + ".jpg"
#         with open(path1, "wb") as fp:
#             fp.write(a3)

#王者荣耀
d = lmy1()
for j in range(1,21):
    if j == 1:
        html1="http://www.netbian.com/s/wangzherongyaoyingxiong/"
    else:
        html1 = "http://www.netbian.com/s/wangzherongyaoyingxiong/index_{}.htm".format(j)
    html = requests.get(html1,headers=headers)
    d.wait(html1)
    html.encoding= "gbk"
    # print(html.text)
    soup = BeautifulSoup(html.text,"lxml")

    imgurl = soup.select(".list img")
    for i in imgurl:
        print(i)
        print(i["alt"],i["src"])
        a3 = requests.get(url=i["src"], headers=headers).content
        d.wait(i["src"])
        path1 = "D://abc//" + i["alt"] + ".jpg"
        with open(path1, "wb") as fp:
            fp.write(a3)


