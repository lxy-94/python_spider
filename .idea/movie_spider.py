# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 8:25
# @Author  : Lxy
# @Site    : 
# @File    : movie_spider.py
# @Software: PyCharm

'''
爬取最新电影排行榜单
url：http://dianying.2345.com/top/
使用 requests --- bs4 线路
Python版本： 3.5
OS： win os 10
'''
import requests
import bs4

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        #该网站采用gbk编码
        r.encoding='gbk'
        return r.text
    except:
        return ' ERROR '

def get_content(url):
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')

    #找到电影列表
    movie_list = soup.find('ul', class_='picList clearfix')
    movies = movie_list.find_all('li')

    for movie in movies:

        #图片链接
        img_url = movie.find('img')['src'].split('?')[0]
        #电影名字
        name = movie.find('span', class_='sTit').a.text
        #异常捕获
        try:
            time = movie.find('span',class_='sIntro').text
        except:
            time = "暂无上映时间"

        actors = movie.find('p', class_='pActor')
        actor = ''
        for act in actors.contents:
            actor = actor + act.string + ' '
        #电影简介
        intro = movie.find('p', class_='pTxt pIntroShow').text

        print("片名：{}\t{}\n{}\n{} \n \n ".format(name, time, actor, intro))

        with open('../../movie_img/'+name+'.png','wb+') as f:
            f.write(requests.get('http:'+img_url).content)


def get_pic_from_url(url):
    pic_content = requests.get(url, stream=True).content
    open('filename', 'wb').write(pic_content)

def main():
    url = 'http://dianying.2345.com/top/'
    get_content(url)

if __name__ == "__main__":
    main()