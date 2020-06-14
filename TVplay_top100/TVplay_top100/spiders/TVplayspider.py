import scrapy
from ..items import TvplayTop100Item

class TVplay_spider(scrapy.Spider):
    name = 'TVplay_spider'
    allowed_domains = ['http://www.mtime.com/']
    start_urls = []
    for i in range(1,11):
        if i == 1:
            url = 'http://www.mtime.com/top/tv/top100/'
            start_urls.append(url)
        else:
            url = 'http://www.mtime.com/top/tv/top100/'+'index-%d.html'%(i)
            start_urls.append(url)

    def parse(self,response):
        for info in response.css('#asyncRatingRegion>li'):
            item = TvplayTop100Item()
            item['rank'] = info.css('.number>em::text').extract_first()
            item['tvplay'] = ' '.join(info.css('.mov_con>h2>a::text').extract_first().split())
            if info.css('.mov_con>p::text').extract_first() == '导演： ':
                item['director'] = info.css('.mov_con>p>a::text').extract_first()
                item['actor'] = '/'.join(info.css('.mov_con>p>a::text').extract()[1:])
            elif info.css('.mov_con>p::text').extract_first() == '主演： ':
                item['actor'] = '/'.join(info.css('.mov_con>p>a::text').extract())
            item['synopsis'] = info.css('.mt3::text').extract_first()
            item['point'] = ''.join(info.css('.mov_point>b>span::text').extract())
            link = info.css('.mov_con>h2>a')
            item['link'] = link[0].xpath('@href').extract_first()
            yield item
