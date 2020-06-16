# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicXiazaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = scrapy.Field()
    iamges = scrapy.Field()
    image_name = scrapy.Field()
    comic_name = scrapy.Field()
    comic_chapter = scrapy.Field()
    
