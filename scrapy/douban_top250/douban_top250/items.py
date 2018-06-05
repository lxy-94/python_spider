# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanTop250Item(scrapy.Item):
    # define the fields for your item here like:
    #   标题、信息、评分、简介
    title = scrapy.Field()
    info = scrapy.Field()
    star = scrapy.Field()
    intro = scrapy.Field()