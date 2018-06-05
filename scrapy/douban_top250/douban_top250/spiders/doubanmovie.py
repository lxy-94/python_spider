# -*- coding: utf-8 -*-
import scrapy
from douban_top250.items import DoubanTop250Item

class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = "https://movie.douban.com/top250?start="
    start_urls = [url+str(offset)]

    def parse(self, response):
        item = DoubanTop250Item()
        movies = response.xpath("//div[@class='info']")

        for each in movies:
            # 标题
            item['title'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            # 评分
            item['star'] = each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            # 信息
            item['info'] = each.xpath(".//div[@class='bd']/p/text()").extract()[0].replace('\n', '').strip(' ')
            #   部分电影没有简介，例如《小萝莉的猴神大叔》，需要做一个判断
            # 简介
            try:
                item['intro'] = each.xpath(".//div[@class='bd']/p[@class='quote']/span/text()").extract()[0]
            except:
                continue

            yield item
        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
