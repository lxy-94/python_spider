# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 9:54
# @Author  : Lxy
# @Site    : 
# @File    : scrapy_de.py
# @Software: PyCharm

from scrapy.selector import Selector

body = open('demo_scrapy.html').read()
print(Selector(text=body).xpath('/html/body/class[last()]/name/text()').extract())
