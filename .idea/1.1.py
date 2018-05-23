# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 15:57
# @Author  : Lxy
# @Site    : 
# @File    : 1.1.py
# @Software: PyCharm

#首先我们先导入requests这个包
import bs4

soup = bs4.BeautifulSoup(open('demo.html'), 'lxml')
#print(soup.prettify())
tag = soup.title
print(tag)
