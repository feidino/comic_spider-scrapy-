import requests, scrapy
import bs4
from ..items import DangdangItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['bang.dangdang.com']
    start_urls = []
    for x in range(3):
        x += 1
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(x)
        start_urls.append(url)

    def parse(self, response):
        #parse是默认处理response的方法。
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        #用BeautifulSoup解析response。
        datas_0 = bs.find('ul', class_="bang_list clearfix bang_list_mode")
        datas = datas_0.find_all('li')
        for data in datas:
            #遍历data。
            item = DangdangItem()
            #实例化DoubanItem这个类。
            item['book_name'] = data.find('div',class_='name').text
            item['book_author'] = data.find('div', class_='publisher_info').text
            item['book_price'] = data.find('span', class_='price_n').text
            print(item['book_name'])
            #打印书名。
            yield item
            #yield item是把获得的item传递给引擎。