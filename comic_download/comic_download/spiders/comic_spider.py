# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest 
from ..items import ComicDownloadItem

class ComicSpiderSpider(scrapy.Spider):
    name = 'comic_spider'
    allowed_domains = ['www.wuqimh.com']
    start_urls = ['http://www.wuqimh.com/17603/']

    def parse(self,response):
        url_list = response.css('div#chpater-list-1 ul>li>a').xpath('./@href').extract()
        for chaptert_url  in url_list:
            chaptert_url = response.urljoin(chaptert_url)
            yield SplashRequest(chaptert_url,args={'wait':5,'images':0,'timeout':90,'resource_timeout':10},callback=self.parse_job)

    def parse_job(self,response):
        item = ComicDownloadItem()
        comic_name = response.css("[class='w996 title pr'] h1 a::text").extract_first()
        chapter = response.css("[class='w996 title pr'] h2::text").extract_first()
        page_sum = response.css('select#pageSelect option:last-child::text').extract_first()
        page = response.css('div.pager span.current::text').extract_first()
        urls = response.css('img#manga::attr(src)').extract_first()
        # print(urls)
        item['image_urls'] = [urls]
        item['image_name'] = chapter+'-'+'第%s页'%(page)
        item['comic_name'] = comic_name
        item['comic_chapter'] = chapter
        yield item
        num = int(page_sum.strip('第').strip('页'))
        for i in range(2,num+1):
            next_url = response.url.split('?')[0]+'?p=%d'%(i)
            yield SplashRequest(next_url,args={'wait':5,'images':0,'timeout':10},callback=self.parse_job)
