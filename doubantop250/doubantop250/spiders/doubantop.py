import requests, scrapy
import bs4
from ..items import Doubantop250Item


class Douban_topSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['book.douban.com']
    start_urls = []
    for x in range(1):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)

    def parse(self, response):
        #parse是默认处理response的方法。
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        #用BeautifulSoup解析response。
        datas = bs.find_all('div', class_="pl2")
        #用find_all提取<tr class="item">元素，这个元素里含有书籍信息。
        cn = datas[0]
        com_url = cn.find('a')['href'] + 'comments/hot?p=1'
        yield scrapy.Request(com_url,callback=self.parse_job,dont_filter=True)
        
    # def url_find(self,response):
    #     page = True
    #     yield scrapy.Request(com_url,callback=self.parse_job,dont_filter=True)
    #     while page == True:
    #         res = bs4.BeautifulSoup(response.text,'html.parser')
    #         data = res.find('ul',class_="comment-paginator")
    #         url_0 = data.find_all('li', class_ = 'p')
    #         try:
    #             url_1 = url_0.pop().find('a')['href']
    #             real_url = 'https://book.douban.com/subject/1007305/comments/'+url_1
    #             yield scrapy.Request(real_url,callback=self.parse_job)
    #         except:
    #             page = False

    def parse_job(self,response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        datas = soup.find('div', id = "content")
        book_name = datas.find('h1').text
        con_data = datas.find_all('li',class_ = 'comment-item')
        for data in con_data:
            #遍历data。
            item = Doubantop250Item()
            #实例化DoubanItem这个类。
            item['book_name'] = book_name
            #提取出书名，并把这个数据放回DoubanItem类的title属性里。
            item['user_id'] = data.find('span', class_='comment-info').find('a').text
            #提取出出版信息，并把这个数据放回DoubanItem类的publish里。
            item['comment'] = data.find('p', class_='comment-content').text
            #提取出评分，并把这个数据放回DoubanItem类的score属性里。
            print(item['book_name'])
            #打印书名。
            yield item
            #yield item是把获得的item传递给引擎。
        next_url = response.xpath('//html/body/div/div//div/div/div/div/ul//li/a/@href')[2].extract_first()
        if next_url:
            next_url = 'https://book.douban.com/subject/1007305/comments/' + next_url
            yield scrapy.Request(next_url,callback=self.parse_job)
