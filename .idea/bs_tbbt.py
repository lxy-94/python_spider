# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 13:30
# @Author  : Lxy
# @Site    : 
# @File    : bs_tbbt.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        #检测是否请求成功
        r.raise_for_status()
        #r.encoding = r.apparent_encoding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "

def get_content(url):
    '''
    分析贴吧网页文件，整理信息
    '''
    comments = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    #因为百度贴吧贴子内容都在 <li class=" j_thread_list clearfix"> 中(有空格，注意)
    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})

    #找到每个帖子里我们需要的信息：
    for li in liTags:
        # 初始化字典存储文章信息
        comment = {}
        try:
            comment['title'] = li.find('a', attrs={'class':'j_th_tit '}).text.strip()
            comment['link'] = 'http://tieba.baidu.com' + li.find('a', attrs={'class':'j_th_tit '})['href']
            comment['name'] = li.find('span', attrs={'class':'tb_icon_author '}).text.strip()
            comment['time'] = li.find('span', attrs={'class':'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find('span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()

            comments.append(comment)
        except:
            print('出错了，爬取失败')

    return comments

def out2file(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 txt文件中
    '''
    with open('JUV.txt', 'a+',encoding='utf-8',  errors='ignore') as f:
        for comment in dict:
            f.write('标题：{}\t链接：{}\t发帖人：{}\t发帖时间：{}\t回复数量：{}\n'.format(
                comment['title'], comment['link'],comment['name'], comment['time'], comment['replyNum']))

        print('爬取结束')

def main(base_url, pages):
    url_list = []

    for i in range(0, pages):
        url_list.append(base_url + '&pn=' + str(50*i))
    print('所有的网页已经下载到本地！ 开始筛选信息')

    #循环写入所有数据

    for url in url_list:
        content = get_content(url)
        out2file(content)
    print('所有信息保存完毕！！！')

#&ie=utf-8 表示该连接采用的是utf-8编码
encode = '&ie=utf-8'

base_url = 'https://tieba.baidu.com/f?kw=%E5%B0%A4%E6%96%87%E5%9B%BE%E6%96%AF'+encode

pages = 3

if __name__=='__main__':
    main(base_url, pages)