from urllib.parse import urljoin

url = "https://cn.bing.com/search?q=%e5%b7%a7%e6%8e%88%e8%bf%9e%e7%8e%af%e8%ae%a1%e6%98%af%e8%b0%81&qs=SC&pq=%e5%b7%a7shou%27lian%27huang%27ji&sk=SC1&sc=2-19&cvid=3A674B7403DE4C1C88C7A6D83CAA99E2&FORM=QBLH&sp=2"
ends = "robots.txt"
url = url.split("/")
url = "/".join(url[:3])
url = urljoin(url,ends)

print(url)
import requests
html = requests.get(url).text
print(html)
headers = {
    "User-agent" : "Twitterbot"
}
for i in html.splitlines():
    print(i,end="\n")