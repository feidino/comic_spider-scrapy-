# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .settings import IMAGES_STORE
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import scrapy,os

# class ComicXiazaiPipeline:
#     def process_item(self, item, spider):
#         return item

class ComicImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item,info):
        for image_url in item['image_urls']:
            yield Request(image_url,meta={'item':item})      

    def file_path(self,request,response=None,info=None):
        # image_store = IMAGES_STORE
        item = request.meta['item']
        image_guid = item['image_name']
        # 接收meta传递过来的文件夹名称
        comic_name = item['comic_name']
        comic_chapter = item['comic_chapter']
        comic_path = os.path.join(comic_name,comic_chapter)
        # if not os.path.exists(comic_path): 
        #     os.makedirs(comic_path)
        filename = '%s/%s.jpg'%(comic_path,image_guid)
        return filename

