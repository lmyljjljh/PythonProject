import scrapy


class Test1Spider(scrapy.Spider):
    name = "test1"
    allowed_domains = ["itcast.cn"]
    start_urls = ["http://itcast.cn/"]

    def parse(self, response):
        pass
