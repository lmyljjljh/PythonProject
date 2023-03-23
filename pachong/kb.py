import urllib.request

import requests
from bs4 import BeautifulSoup

import pandas as pd

import csv
headers = {
    "Cookie": "JSESSIONID=8EFA9D34DCDF793B360523446A3DD87C; SERVERID=122",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
}

# ass = urllib.request.Request(headers=headers, url="http://218.199.113.111/jsxsd/framework/xsMain.jsp")
#
# response = urllib.request.urlopen(ass)
# response = requests.get("http://218.199.113.111/jsxsd/framework/xsMain.jsp",headers=headers)
# print(response)