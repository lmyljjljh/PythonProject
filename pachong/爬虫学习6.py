from bs4 import BeautifulSoup
import requests
from lxml import etree

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
}
html = requests.get("https://book.douban.com/subject/35776311/?icn=index-topchart-subject",headers=headers)
soup = etree.HTML(html.text)
print(soup)

result = soup.xpath("//div/h1/span/text()")
print(result)