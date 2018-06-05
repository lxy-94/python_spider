# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = 'tencentposition'
    allowed_domains = ['tencent.com']
    url = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        for each in response.xpath ("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            item['position_name'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['position_link'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['position_type'] = each.xpath("./td[2]/text()").extract()[0]
            item['people_num'] = each.xpath("./td[3]/text()").extract()[0]
            item['work_location'] = each.xpath("./td[4]/text()").extract()[0]
            item['publish_time'] = each.xpath("./td[5]/text()").extract()[0]

            yield item
        if self.offset < 3890:
            self.offset += 10
        #   每次处理完一页的数据后，重新发送下一页页面请求
        #   self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
