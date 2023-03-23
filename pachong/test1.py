from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
from urllib.parse import urlparse
# from lxml import etree
# import re

# import json
# import urllib.request
# from urllib.parse import urljoin
# from urllib import parse


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



# url = "https://tse1-mm.cn.bing.net/th/id/OIP-C.wc_dCG_KbIKZwMdtD3gL2QHaEt?w=247&h=180&c=7&r=0&o=5&dpr=1.25&pid=1.7"
# t1 = requests.get(url)
# t1 = t1.content
# with open(r"1.jpg","ab")as fp:
#     fp.write(t1)


url1 = "https://www.dushu.com/showbook/132098/"

t2 = requests.get(url1)
d.wait(url1)
t2.encoding="utf-8"
print(t2.text)
soup = BeautifulSoup(t2,"lxml")
# #
# #
t1 = soup.select(".container.margin-top .bookdetails-left .book-summary .border.margin-top.padding-large .text.txtsummary")
print(len(t1))
print(t1)
for i in t1:
    print(i)
    print(i["class"])
summ = 1
for i in t1:
    # print(i)
    # print(i["href"])
    url2 = url1 + i["href"]
    t3 = requests.get(url2).text
    # print(t3)
    d.wait(url2)
    soup = BeautifulSoup(t3, "lxml")
    t4 = soup.select("#readbox #content")
    print(len(t4))
    print("di{}".format(summ))
    summ += 1
    for i in t4:
        print(i.text)


# summ = 1
# for i in t1:
#     print(i)
#     print(i["src"])
#     print("******************************")
#     with open(r"{}.png".format(summ),"ab") as fp:
#         fp.write(requests.get(i["src"]).content)
#     summ += 1


# print(t1)
# sum = 1
# for i in t1:
#     print(i["src"])
#     with open(r"..\tupian\{}.png".format(sum),"ab")as fp:
#         fp.write(requests.get(i["src"]).content)
#         d.wait(i["src"])
#     sum += 1

# str1 ='''
# 123456{}
# '''.format(789)
# print(str1)


# https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=ubuntu%E5%AE%89%E8%A3%85MySQL&oq=Failed%2520to%2520start%2520mysqld.service%253A%2520Unit%2520mysqld.service%2520not%2520found.&rsv_pq=d0ef53af000ad1f5&rsv_t=8c1fDmpjQ%2BPCs1CCuaN05GVRbbTvzt1vvPo3CyEESEO5%2FhW0obM5%2Bm4%2BAXk&rqlang=cn&rsv_enter=0&rsv_dl=ts_5&rsv_btype=t&inputT=13057&rsv_sug3=156&rsv_sug1=144&rsv_sug7=101&rsv_sug2=1&prefixsug=Ubuntu%25E5%25AE%2589%25E8%25A3%2585&rsp=5&rsv_sug4=165119
# def f1(x):
#     print(x)
# f1(123432)

# with open(r"D:\text.txt","rb")  as fp:
#     print(fp.read())



# url = "https://tse1-mm.cn.bing.net/th/id/OIP-C.wc_dCG_KbIKZwMdtD3gL2QHaEt?w=247&h=180&c=7&r=0&o=5&dpr=1.25&pid=1.7"
# with open(r"test1.png","ab") as fp:
#     fp.write(requests.get(url).content)



# jh = {"lmy":12,"ldd":17,"wx":19}
# print(jh["wx"])


# url = "https://www.bbiquge.net/book/133312/"
#
# headers={
#     "cookie": "__gads=ID=2c5fdb4e814ccdf2-22000ff695d600e9:T=1662295482:RT=1662295482:S=ALNI_MZkmQNJVmykv68D5xoYNv7dyc9hBw; __gpi=UID=00000972ccc2b75e:T=1662295482:RT=1662382289:S=ALNI_MZQix2fbjmOhz4oemOiY7Co3FMgwg; Hm_lvt_007bc30c1abb0ffb7a93b4f3c8e10c5e=1662295474,1662382288,1662383682; jieqiVisitId=article_articleviews%3D133310; Hm_lpvt_007bc30c1abb0ffb7a93b4f3c8e10c5e=1662383870",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
#
# }
#
# print(requests.get(url=url,headers=headers))




























