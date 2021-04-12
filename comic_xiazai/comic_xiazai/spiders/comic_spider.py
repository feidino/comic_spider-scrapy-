# -*- coding: utf-8 -*-
import scrapy,re
from scrapy_splash import SplashRequest 
from ..items import ComicXiazaiItem


class ComicSpiderSpider(scrapy.Spider):
    name = 'comic_spider'
    allowed_domains = ['manhuadb.com']
    start_urls = ['https://www.manhuadb.com/manhua/1888']

    def parse(self,response):
        url_list = response.css('li.sort_div a.fixed-a-es::attr(href)').extract()
        for chaptert_url  in url_list:
            chaptert_url = response.urljoin(chaptert_url)
            yield SplashRequest(chaptert_url,args={'wait':5,'images':0,'timeout':90,'resource_timeout':10},callback=self.parse_job)

    def parse_job(self,response):
        item = ComicXiazaiItem()
        comic_name = response.css('h1.text-center a::text').extract_first()
        chapter = response.css('h2.text-center::text').extract_first().strip('[').strip(']')
        page_sum = int(response.css('select.form-control option:last-child::text').extract_first().strip('第').strip('页'))
        page = response.css('select.form-control [selected]::text').extract_first()
        urls = response.css('div.text-center img.img-fluid::attr(src)').extract_first()
        # print(urls)
        item['image_urls'] = [urls]
        item['image_name'] = chapter+'-'+page
        item['comic_name'] = comic_name
        item['comic_chapter'] = chapter
        yield item
        for i in range(2,page_sum+1):
            next_url = re.split('_p\d+|.html',response.url)[0]+'_p%d.html'%(i)
            yield SplashRequest(next_url,args={'wait':5,'images':0,'timeout':10},callback=self.parse_job)
