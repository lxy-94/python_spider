# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
# import settings

#   保存成json
class DoubanTop250Pipeline(object):
    def __init__(self):
        self.filename = open("douban_top250.json", 'wb+')
    def process_item(self, item, spider):
        jsontxt = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.filename.write(jsontxt.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.filename.close()

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'douban'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'



        #   保存到mysql
#   mysql的密码方式和python有一些不同，需要修改，语句：
#   ALTER USER 'root'@'localhost' IDENTIFIED WITH (修改后的密码)
class DBPipeline(object):
    def __init__(self):
        # 保存带mysql数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        print("mysql connect succes")

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.cursor.execute('''insert into doubanmovie (title, star, info, intro) values(%s,%s,%s,%s)''',
                (item['title'],
                 item['star'],
                 item['info'],
                 item['intro']))
            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            log(error)
        return item
