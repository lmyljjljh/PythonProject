from bs4 import BeautifulSoup
import requests
from lxml import etree
import re
from urllib.parse import urlparse
from datetime import datetime
import time
import json


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
"Accept": "application/json, text/plain, */*",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Cookie": "_ga=GA1.2.1561192419.1660567582; _gid=GA1.2.1832675803.1660567582; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1660567582,1660568733; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1660570566; kw_token=Q8E559F8HXN",
"csrf": "Q8E559F8HXN",
"Host":"www.kuwo.cn",
"Referer": "http://www.kuwo.cn/playlist_detail/1082685104",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}

d = lmy1()
url1 = "https://www.kuwo.cn/api/www/playlist/playListInfo?pid=1082685104&pn=1&rn=30&httpsStatus=1&reqId=df85e050-1cb3-11ed-93f5-25a49c4948b4"
html1 = requests.get(url1,headers=headers).text

d.wait(url1)
print(html1)

html2 = json.loads(html1)
print(html2)

for i in html2["data"]["musicList"]:
    # print(i)
    print(i["name"],i["rid"])
    html3 = requests.get("https://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=df97e1b1-1cb3-11ed-93f5-25a49c4948b4".format(i["rid"]),headers=headers).text
    html3 = json.loads(html3)["data"]["url"]
    print(html3)
    d.wait("https://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=df97e1b1-1cb3-11ed-93f5-25a49c4948b4".format(i["rid"]))
    with open(r"..\music\{}.mp3".format(i["name"]),"wb") as fp:
        fp.write(requests.get(html3).content)
        d.wait(html3)
        print(i["name"],"下载完毕")



