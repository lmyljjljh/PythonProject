from bs4 import BeautifulSoup
import requests

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
}
html = requests.get("https://book.douban.com/",headers=headers)
soup = BeautifulSoup(html.text,"lxml")

top = soup.select("li .info .title a")
print(top)
for i in top:
    print("**************")
    print(i.text)