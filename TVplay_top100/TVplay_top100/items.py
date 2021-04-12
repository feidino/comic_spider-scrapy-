# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TvplayTop100Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    tvplay = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    synopsis = scrapy.Field()
    point = scrapy.Field()
    link = scrapy.Field()
    pass
