#冰墩墩宣传片，弹幕爬取 
#视频地址：https://www.bilibili.com/video/BV1hq4y1b7Pv/?spm_id_from=trigger_reload
import requests
cid=502631349   #冰墩墩短片cid  
url='https://comment.bilibili.com/{}.xml'.format(cid)
#弹幕文件所在位置：https://comment.bilibili.com/502631349.xml
rq=requests.get(url)    #此时rq为一个回应
rq.encoding='utf-8'
#rq.text                     #弹幕原始数据获取成功
#解析获取弹幕数据
from bs4 import BeautifulSoup
import pandas as pd
columns = ['出现时间点', '模式', '字体', '颜色', '发送时间', '弹幕池', '用户ID', 'rowID','其他']   # 各列数据名称
soup = BeautifulSoup(rq.text, 'lxml')    # 解析网页内容
BT = soup.select("d")
# print(BT)
zda = {}
for i in columns:
    zda[i] = []
for i in BT:
    print(i['p'])
    lista = i['p'].split(',')
    for j in range(len(lista)):
        zda[columns[j]].append(lista[j])
print(zda)


#to_csv()方法mode默认为w，我们加上mode='a'，便可以追加写入数据。
# data.to_csv('d:/aa/冰墩墩23.04.25.csv',index=None, encoding='utf-8-sig')    # 注意弹幕数据必须用'utf-8-sig'编码，追加可加属性 mode='a'
#data
