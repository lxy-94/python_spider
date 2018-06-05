# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ChuanzhiPipeline(object):
    #   可选，作为类的初始化
    def __init__(self):
        #   创建了一个文件
        self.filename = open("teacher.json", "wb+")
    #   必写，处理item数据
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False)+ '\n'
        self.filename.write(jsontext.encode("utf-8"))
        return item
    #   可选，类的结束方法
    def close_spider(self, spider):
        self.filename.close()
