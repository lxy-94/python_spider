# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 21:25
# @Author  : Lxy
# @Site    : 
# @File    : zhihu_requests.py
# @Software: PyCharm



# ! /usr/bin/env python
from os.path import basename
from urllib.parse import urlparse
import re
import requests
import os
import json
import urllib

if not os.path.exists('images'):
    os.mkdir("images")

page_size = 50
offset = 0
x = 0

id = 37787176
url = 'https://www.zhihu.com/question/37787176'
url_content = urllib.request.urlopen(url).read()

while offset < 100:

    get_url = 'https://www.zhihu.com/api/v4/questions/37787176/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=' + str(
        offset)

    header = {
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
    }

    req = urllib.request.Request(get_url, headers=header)
    response = urllib.request.urlopen(req).read()
    txt = json.loads(response)
    print
    txt
    offset += 20
    img_urls = re.findall('img .*?src="(.*?_b.*?)"', str(txt))
    for img_url in img_urls:
        try:
            x += 1
            img_data = urllib.request.urlopen(img_url).read()
            # file_name = basename(urlsplit(img_url)[2])
            output = open('images/' + str(x), 'wb')
            output.write(img_data)
            output.close()
        except:
            pass
print (x)