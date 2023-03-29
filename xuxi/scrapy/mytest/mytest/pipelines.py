# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MytestPipeline:
    def process_item(self, item, spider):
        print('itcast:', item)
        # 默认使用完管道之后将数据返回给引擎
        return item


