# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='goods')
        for i in range(len(item["name"])):
            name=item["name"][i]
            price = item["price"][i]
            comment = item["comment"][i]
            #print(name+':'+price+':'+comment)
            sql = "insert into shangping(name,price,comment) values('"+name+"','"+price+"','"+comment+"')"
            #print(sql)
            try:
                conn.query(sql)
            except Exception as err:
                print(err)
        conn.close()
        return item
