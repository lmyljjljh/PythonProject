from bs4 import BeautifulSoup
import requests
from lxml import etree
import re

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
}
html = requests.get("https://finance.sina.com.cn/", headers=headers)
html.encoding= "utf-8"
# print(html.text)
soup = BeautifulSoup(html.text,"lxml")
BT = soup.select("#blk_hdline_01 h3 a")
for i in BT:
    print(i.text)
    print(i["href"])
print("***************************************************************************************")
ST = soup.select("#blk_hdline_01 p a")
for i in ST:
    print(i.text)
    print(i["href"])
print("***************************************************************************************")
WB = soup.select(".m-p1-mb2-list.m-list-container ul li a")
for i in WB:
    print(i.text)
    print(i["href"])
print("***************************************************************************************")
WB = soup.select(".m-p1-mb2-list.m-list-container ul li a")
for i in WB:
    print(i.text)
    print(i["href"])
    inHtml = requests.get(i["href"])
    inHtml.encoding = "utf-8"
    soup2 = BeautifulSoup(inHtml.text,"lxml")
    t3 = soup2.select(".article p")
    for i in t3:
        print(i.text)






# 正则
# print(re.findall(r".*?","aabaa"))
# print(re.findall(r"[a|A]jiu","ajiu--Ajiu"))
# str1 = "a     bald"
# print(re.split(" ",str1))
# print(str1.split(" "))
# str2 = "ajiu a is man! ajiu a is man! ajiu a is man!"
# t1 = re.finditer(r"(ajiu)",str2)
# print(t1)
# for i in t1:
#     print(i)
# for i in t1:
#     t2 = next(t1)
#     print(t2)






