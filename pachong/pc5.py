import requests
from bs4 import BeautifulSoup

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
}

html = requests.get("https://www.itcast.cn/channel/teacher.shtml#ajavaee", headers=headers)
html.encoding= "utf-8"
print(html.text)
soup = BeautifulSoup(html.text,"lxml")
BT = soup.select(".tea_con .tea_txt img")
print(BT)
print(len(BT))
# for i in BT:
#     print(i.text)
#     print(i["href"])