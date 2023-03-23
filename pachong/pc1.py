# import requests
# from urllib import request
# from lxml import etree
# from bs4 import BeautifulSoup
# url="https://www.acwing.com/file_system/gui/window/operate/open/994425"
#
# headers={
#             "Cookie" : "csrftoken=jCsYcD0JmkxwSm1Rqt2wwFs3RcE0pdGZ5Diu6v1SJjy5N1xF7vA1y80NVTt8E385; sessionid=6ly8wfdw4ftel3c6vaqky6fh14488o6j",
#             "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
#         }
# t2 = requests.get(url=url,headers=headers)
# print(t2)
# html = t2.text
# print(html)
# soup = BeautifulSoup(html,'lxml')
# print(soup)
# parse_html = etree.HTML(html)
# t1 = parse_html.xpath('//*[@id="form_upload_profileinfo"]/div[1]/label')
# print(t1)
# # response=request.urlopen('http://www.baidu.com/')
# # print(response.read().decode('utf-8'))


# import requests #导入requests包
# from bs4 import BeautifulSoup

# url="https://www.bilibili.com/bangumi/play/ss22088/?from=search&seid=503303968644820581"#把bilibil的网址复制过来
# req=requests.get(url)#用get方式拿到网页
# req.encoding='utf-8'#规定编码方式为utf-8
# soup=BeautifulSoup(req.text,'lxml')#使用BeautifulSoup的lxml解析网页
# description=soup.find('span',class_="absolute")#搜索每一个span元素拿到class为absolute的内容。
# print(description) #打印内容



from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
from urllib.parse import urlparse
from lxml import etree
import re

import json
import urllib.request
from urllib.parse import urljoin
from urllib import parse


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


url1 = "https://www.bbiquge.net/book/133312/"
t2 = requests.get(url1)
# d.wait(url1)
print(t2)
