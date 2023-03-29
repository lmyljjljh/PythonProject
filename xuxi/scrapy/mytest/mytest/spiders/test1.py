import scrapy
from bs4 import BeautifulSoup


class Test1Spider(scrapy.Spider):
    name = "test1"
    # 2、检查域名
    allowed_domains = ["itcast.cn"]
    # 1、修改起始url
    start_urls = ["https://www.itcast.cn/channel/teacher.shtml#ajavaee"]

    # 3、在parse方法中实现爬取逻辑
    def parse(self, response):
        # 定义对于响应的网站的相关操作
        # with open('1.html', 'wb')as f:
        #     f.write(response.body)
        # 获取教师节点
        # node_list = response.xpath('//*[@id="mCSB_1_container"]/ul/li/div')
        # print(len(node_list))
        # print(node_list)
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        BT = soup.select(".tea_con .tea_txt img")
        print(BT)
        for i in BT:
            print(i)
        print("******************************")
        # 遍历教师节点列表

        # 获取我们所需信息


        pass

