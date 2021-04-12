# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl

class Doubantop250Pipeline:
    def __init__(self):
    #初始化函数 当类实例化时这个方法会自启动
        self.wb = openpyxl.Workbook()
        #创建工作薄
        self.ws = self.wb.active
        #定位活动表
        self.ws.append(['书名', '用户ID', '评论'])
        #用append函数往表格添加表头
        
    def process_item(self, item, spider):
        line = [item['book_name'], item['user_id'], item['comment']]
        #把公司名称、职位名称、工作地点和招聘要求都写成列表的形式，赋值给line
        self.ws.append(line)
        #用append函数把公司名称、职位名称、工作地点和招聘要求的数据都添加进表格
        return item
        #将item丢回给引擎，如果后面还有这个item需要经过的itempipeline，引擎会自己调度
    def close_spider(self, spider):
    #close_spider是当爬虫结束运行时，这个方法就会执行
        self.wb.save('./豆瓣评论.xlsx')
        #保存文件
        self.wb.close()
