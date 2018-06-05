# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DoubanTop250Pipeline(object):
    def __init__(self):
        self.filename = open("douban_top250.json", 'wb+')

    def process_item(self, item, spider):
        jsontxt = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.filename.write(jsontxt.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.filename.close()