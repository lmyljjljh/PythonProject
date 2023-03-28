import scrapy


class Test1Spider(scrapy.Spider):
    name = "test1"
    allowed_domains = ["itcase.cn"]
    start_urls = ["http://itcase.cn/"]

    def parse(self, response):
        pass
