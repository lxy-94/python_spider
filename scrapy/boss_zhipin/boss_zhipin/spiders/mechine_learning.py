# -*- coding: utf-8 -*-
import scrapy
from boss_zhipin.items import BossZhipinItem


# 北京:c101010100
# 上海:c101020100
# 广州:c101280100
# 深圳:c101280600
# 杭州:c101210100
# 天津:c101030100
# 苏州:c101190400
# 西安:c101110100
# 成都:c101270100

class MechineLearningSpider(scrapy.Spider):
    name = 'mechine_learning'
    allowed_domains = ['zhipin.com']
    offset = 1
    city = ['c101010100', 'c101020100', 'c101280100', 'c101280600', 'c101210100', 'c101030100', 'c101190400', 'c101110100', 'c101270100']

    url = 'https://www.zhipin.com/'+city[8]+'/h_100010000/?query=机器学习&page='
    start_urls=[url + str(offset)]

    def parse(self, response):
        item = BossZhipinItem()
        ml_jobs = response.xpath("//div[@class='job-primary']")

        for each in ml_jobs:
            item['pid'] = each.xpath(".//a/@data-jobid").extract()[0]
            item['positionName'] =each.xpath(".//h3[@class='name']/a/div[@class='job-title']/text()").extract()[0]
            item['city'] = each.xpath(".//div[@class='info-primary']/p/text()[1]").extract()[0]
            item['workYear'] = each.xpath(".//div[@class='info-primary']/p/text()[2]").extract()[0]
            item['education'] =each.xpath(".//div[@class='info-primary']/p/text()[3]").extract()[0]
            item['salary'] = each.xpath(".//div[@class='info-primary']/h3/a/span/text()").extract()[0]
            item['companyShortName'] = each.xpath(".//div[@class='info-company']/div/h3/a/text()").extract()[0]
            item['industryField'] = each.xpath(".//div[@class='info-company']/div/p/text()[1]").extract()[0]
            item['financeStage'] = each.xpath(".//div[@class='info-company']/div/p/text()[2]").extract()[0]
            try:
                item['companySize'] = each.xpath(".//div[@class='info-company']/div/p/text()[3]").extract()[0]
            except:
                item['companySize'] = each.xpath(".//div[@class='info-company']/div/p/text()[2]").extract()[0]

            yield item
            # for i in range(9):
            #     self.url = 'https://www.zhipin.com/' + self.city[i] + '/h_100010000/?query=机器学习&page='
            if self.offset < 10:
                self.offset += 1
                yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
