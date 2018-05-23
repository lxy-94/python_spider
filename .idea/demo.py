# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 21:31
# @Author  : Lxy
# @Site    : 
# @File    : demo.py
# @Software: PyCharm

import requests
import shutil
import re
import urllib
import ast
import bs4

'''
question = 27797286        # 问题ID
url = "https://www.zhihu.com/question/%s" % (question)
hd = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
r = requests.get(url,headers=hd)
print(r.text)
'''
url = 'https://www.yuemei.com/c/1794211.html'

header = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
}

def get_html_text(url, timeout=5):
    '模拟get请求，获取页面'
    try:
        r = requests.get(url, headers=header)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'

html = get_html_text(url)

soup = bs4.BeautifulSoup(html,'lxml')
name = soup.find('div', class_='diary-data').a.get("href").split('/')[4]
basediv = soup.find_all('div', class_='list-imgs ')
print(basediv)