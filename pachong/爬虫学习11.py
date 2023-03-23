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
url1 = "http://www.913543.com/js/zhuqinghao.html"
html1 = requests.get(url1).text
d.wait(url1)
soup = BeautifulSoup(html1,"lxml")
t1 = soup.select(".stui-pannel_bd.col-pd.clearfix ul li a")

for i in t1:
    print(i["href"])
    url2 = "http://www.913543.com"
    url2 = urljoin(url2,i["href"])
    print(url2)
    html2 = requests.get(url2)
    d.wait(url2)
    re_m3u8 = re.compile('"url":"(.*?)",')
    t2 = re_m3u8.findall(html2.text)
    print(t2)
    t2 = t2[1]
    url3 = t2.replace("\\","")
    html3 = requests.get(url3).text
    d.wait(url3)
    with open(r"..\wbwj\1.txt","w",encoding="utf-8")as fp:
        fp.write(html3)
    with open(r"..\wbwj\1.txt","r",encoding="utf-8")as fp:
        lines = fp.readlines()
        for j in lines:
            if j.startswith("#"):
                continue
            else:
                url4 = urljoin(url3[:-10],j)
                print(url4)
                print("*******************")
                break
    with open(r"..\wbwj\2.txt","w",encoding="utf-8")as fp:
        fp.write(requests.get(url4).text)
        d.wait(url4)
    with open(r"..\wbwj\2.txt","r",encoding="utf-8")as fp:
        lines = fp.readlines()
        for j in lines:
            if j.startswith("#"):
                continue
            else:
                url5 = urljoin(url4[:-10], j.replace("\n",""))
                print(url5)
                with open(r"..\wbwj\1.mp4", "ab") as f:
                    f.write(requests.get(url5).content)



# vip视频爬取
# import requests
# from urllib.parse import urljoin
# url = "https://76168ae09549e31a13f7a455c524ca70.rdt.tfogc.com:49156/omts.tc.qq.com/AJ6w0zcptozDKxaRBLnXYL-bI__vx7Zx6k0yBwo23LC4/uwMROfz2r55goaQXGdGnCWde46IpbL7X4pIWPOLNIkyWr8r8/svp_50112/zo9tk9fjq8devORNuKpx9VGAUCYv7QKdM-kS2vjGYf-V79t2-G3cvcQ9WGHSZ8-T9Bb3H2yUrkiQk5O7a_5a9ojWIzjfWXk9k7Q_eR8qIbPREzsMA19bwKz4y-HbcyqAdX9ueAt-MDtfaU4fi3ApjLS47m9RAP-D/gzc_1000102_0b53b4aaqaaakuao6xpzmbrmad6dbaeqadca.f323014.ts.m3u8?ver=4"
# base = "https://76168ae09549e31a13f7a455c524ca70.rdt.tfogc.com:49156/omts.tc.qq.com/AJ6w0zcptozDKxaRBLnXYL-bI__vx7Zx6k0yBwo23LC4/uwMROfz2r55goaQXGdGnCWde46IpbL7X4pIWPOLNIkyWr8r8/svp_50112/zo9tk9fjq8devORNuKpx9VGAUCYv7QKdM-kS2vjGYf-V79t2-G3cvcQ9WGHSZ8-T9Bb3H2yUrkiQk5O7a_5a9ojWIzjfWXk9k7Q_eR8qIbPREzsMA19bwKz4y-HbcyqAdX9ueAt-MDtfaU4fi3ApjLS47m9RAP-D/"
# response = requests.get(url)
# lines = response.text.split("\n")
# for line in lines:
#     if line.startswith("#"):
#         continue
#     print(line)
#     url = urljoin(base, line)
#     with open("2.mp4", "ab")as f:
#         f.write(requests.get(url).content)



























