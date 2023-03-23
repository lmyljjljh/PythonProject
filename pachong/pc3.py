import re
import requests

url = "https://qq.yh31.com/ql/ls/"

t1 = requests.get(url).text
print(t1)

t2 = r'<img src=".*?" data-src="(.*?)" alt=".*?" border="0"/>'

t3 = re.findall(t2,t1)
print(t3)
url1 = "https://qq.yh31.com"
for i in range(len(t3)):
    t4 = url1+t3[i]
    response = requests.get(t4)
    