# -*- coding: utf-8 -*-
import scrapy
from chuanzhi.items import ChuanzhiItem

class ChuanzhiSpider(scrapy.Spider):
    name = 'chuanzhi'

    allowed_domains = ["http://www.itcast.cn/"]

    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#apython"]

    def parse(self, response):
        #   通过xpath自动匹配出老师的节点

        teacher_list = response.xpath('//div[@class="li_txt"]')
        #   遍历根节点
        for each in teacher_list:
            item = ChuanzhiItem()
            name = each.xpath('./h3/text()').extract()[0]
            title = each.xpath('./h4/text()').extract()[0]
            info = each.xpath('./p/text()').extract()[0]
            item['name'] = name
            item['title'] = title
            item['info'] = info

            yield item