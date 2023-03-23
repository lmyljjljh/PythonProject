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

url1 = "https://www.douyin.com/user/MS4wLjABAAAADmrCxKXVq5a2kNoTEKCR3j3WrrzwR-gFMYxtom7RoaR89tYEzNmc67bbrsM7MIqV?vid=7134664485918313759"

header={
# "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# "accept-encoding": "gzip, deflate, br",
# "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
# "cache-control": "max-age=0",
"cookie": "douyin.com; ttwid=1%7CwJsX-4-ARyp9_8S3Aed0tx4aYDts81D-i5z7BJzGFk8%7C1661171201%7Ce4277fbf14ca8f51c9f7c553f82f0555a655416052d0381de43e45e384f3da25; douyin.com; strategyABtestKey=1661171218.352; s_v_web_id=verify_l74qgcqv_qVrdnDaE_CM7p_4cly_BlWV_cCXMtyrcrJuo; passport_csrf_token=db1ae0c2917ac2d1f1bb4dfd358ee4ec; passport_csrf_token_default=db1ae0c2917ac2d1f1bb4dfd358ee4ec; ttcid=2b52d9a1332d4b5093525e9d28e0595615; THEME_STAY_TIME=%22299516%22; IS_HIDE_THEME_CHANGE=%221%22; msToken=wzI4MSWkOGedNqO0wBGYtC6ejK0tNg3Y5_MZo_XhJYWGge3aRnGKmGZaww8om9YbxKB07nEGSvLFvugVDZhtiXhh764-5NNQdn6qLEyDBfpPnFD5JOoWJts=; __ac_nonce=063039902001ed29713a5; __ac_signature=_02B4Z6wo00f019tuu0gAAIDDW2xBClz2p6PbTr.AAJXhZsNpipMgdaC22FjOvY1bwA-KXBL379NEpbJyl4XbXWcl5IwOi5IbusFY5Ku8vAkygzq6PBp3KilafhQKkDSBFJrwB-nJs8wlV34.1a; download_guide=%223%2F20220822%22; home_can_add_dy_2_desktop=%221%22; tt_scid=5oSuYRpnICTZy0I9s15oAOPDGZSKL6dDIYrjNpG.4aFpeorfLEv6kjhnFb3wHwQX861d; msToken=zUrKKncUngoan6Bc40oifWjafv0hbSlAGFvONSj_bpxo9EphRDXtK5uo6hycOlNNqt0FyQgrfd3S4TQ3xW5f0fX5GOUz6GNed80oKbGiw_S171p0RyJJhe4f3YpEWk4Q",
# "referer": "https://www.douyin.com/user/MS4wLjABAAAADmrCxKXVq5a2kNoTEKCR3j3WrrzwR-gFMYxtom7RoaR89tYEzNmc67bbrsM7MIqV?enter_from=author_card&from_gid=7134664485918313759&tab_name=recommend&vid=7134664485918313759",
# "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
# "sec-ch-ua-mobile": "?0",
# "sec-ch-ua-platform": "Windows",
# "sec-fetch-dest": "document",
# "sec-fetch-mode": "navigate",
# "sec-fetch-site": "same-origin",
# "sec-fetch-user": "?1",
# "upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
}

requests1 = urllib.request.Request(url1,headers=header)
html1 = urllib.request.urlopen(requests1)
# print(html1.read())
t1 = parse.unquote(str(html1.read().decode("utf-8")))
# print(t1)
soup = BeautifulSoup(t1,"lxml")
t1 = soup.select(".mwo84cvf .UFuuTZ1P .EZC0YBrG .Eie04v01 a")
print(len(t1))
num1 = 1
for i in t1:
    print(i["href"])
    url2 = urljoin("https://www.douyin.com",i["href"])
    print(url2)
    requests2 = urllib.request.Request(url2, headers=header)
    html2 = urllib.request.urlopen(requests2)
    t2 = parse.unquote(str(html2.read().decode("utf-8")))
    # print(t2)
    re_video = re.findall(':"//v26(.*?)"},{',t2)
    print(re_video[0])
    url3 = "http://v26"+re_video[0]
    print(url3)
    with open(r"..\wbwj\douyin{}.mp4".format(num1),"ab")as fp:
        # requests3 = urllib.request.Request(url3)
        fp.write(requests.get(url3).content)
    num1 += 1








