# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayerLinkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()i
    name = scrapy.Field()
    url = scrapy.Field()
    status = scrapy.Field()
    uid = scrapy.Field()
