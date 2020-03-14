# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FbmarketItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    location = scrapy.Field()
    search_term = scrapy.Field()
    img_url = scrapy.Field()
    item_url = scrapy.Field()
    # current_date = scrapy.Field()
    # slot_number = scrapy.Field()
    # pass
