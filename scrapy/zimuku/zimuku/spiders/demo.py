# -*- coding: utf-8 -*-
import scrapy
from zimuku.items import ZimukuItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['zimuku.net']
    start_urls = ['http://zimuku.net/']

    def parse(self, response):
        '''
        parse()函数接收Response参数，用于处理响应，它负责解析爬取的内容
        :param response:
        :return:
        '''

        name = response.xpath('//b/text()').extract()[1]
        items = {}
        items['第一个'] = name
        return items
