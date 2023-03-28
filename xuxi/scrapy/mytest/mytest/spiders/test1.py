import scrapy


class Test1Spider(scrapy.Spider):
    name = "test1"
    allowed_domains = ["itcast.cn"]
    start_urls = ["http://itcast.cn/"]

    def parse(self, response):
        # 定义对于响应的网站的相关操作
        with open('1.html', 'wb')as f:
            f.write(response.body)

