# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossZhipinItem(scrapy.Item):
    # define the fields for your item here like:
    #   职位id
    pid = scrapy.Field()
    #   职位名称
    positionName = scrapy.Field()
    #   工作年限
    workYear = scrapy.Field()
    #   薪资
    salary = scrapy.Field()
    #   工作地点
    city = scrapy.Field()
    #   学历要求
    education = scrapy.Field()
    #   公司名称
    companyShortName = scrapy.Field()
    #   融资阶段
    financeStage = scrapy.Field()
    #   公司领域
    industryField = scrapy.Field()
    #   公司人数
    companySize = scrapy.Field()


