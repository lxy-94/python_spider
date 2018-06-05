# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TencentSpider.items import TencentspiderItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    #   Response里面链接的提取规则，返回符合匹配规则的链接匹配对象的列表，allow和正则语法相关，有的需要加转义字符
    pagelink = LinkExtractor(allow=("start=\d+"))

    rules = (
        #   获取这个列表里的链接，一次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(pagelink, callback='parse_item', follow=True),
    )

    #   指定的回调函数
    def parse_item(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentspiderItem()
            item['position_name'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['position_link'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['position_type'] = each.xpath("./td[2]/text()").extract()[0]
            item['people_num'] = each.xpath("./td[3]/text()").extract()[0]
            item['work_location'] = each.xpath("./td[4]/text()").extract()[0]
            item['publish_time'] = each.xpath("./td[5]/text()").extract()[0]

            yield item
