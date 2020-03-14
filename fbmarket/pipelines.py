# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class FbmarketPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='', database='fbmarketdb')
        self.cursor = self.conn.cursor()
        # self.conn.autocommit(True)

    def process_item(self, item, spider):
        self.insert_item(item)
        return item

    def insert_item(self, item):
        sql = "INSERT INTO fb_item (item_name, item_price, " \
              "item_category, item_location, item_search_term, item_img, item_url) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (
            item['name'],
            item['price'],
            item['category'],
            item['location'],
            item['search_term'],
            item['img_url'],
            item['item_url'],
        ))
        self.conn.commit()
