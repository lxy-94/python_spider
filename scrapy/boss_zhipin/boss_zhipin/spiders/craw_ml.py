# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss_zhipin.items import BossZhipinItem


class CrawMlSpider(CrawlSpider):
    name = 'craw_ml'
    allowed_domains = ['zhipin.com']
    start_urls = [r'http://www.zhipin.com/c100010000/h_100010000/?query=机器学习&page=1', ]

    #   每一页的匹配规则
    pageLink = LinkExtractor(allow=(r"query=机器学习"))
    #   每个职位的匹配规则
    contentlink = LinkExtractor(allow=(r"/job_detail/^[a-zA-Z0-9]*$/ka=search_list_"))


    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
