import scrapy  
import bs4
from ..items import JobuiItem

class JobuiSpider(scrapy.Spider):
    name = 'job_spider'
    allowed_domains = ['jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    def parse(self, response):
        #parse是默认处理response的方法。
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        #用BeautifulSoup解析response。
        datas_0 = bs.find('div', class_="searchCont")
        datas = datas_0.find_all('li')
        for data in datas:
            #遍历data。
            id = data.find('a')['href']
            real_url = 'https://www.jobui.com'+id+'jobs/'
            yield scrapy.Request(real_url,callback=self.parse_job)
    def parse_job(self,response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        company = soup.find(id="companyH1").text
        job_data = soup.find_all('div',class_='c-job-list')
        for job in job_data:
            item = JobuiItem()
            #实例化DoubanItem这个类。
            item['company'] = company
            item['job_name'] = job.find('h3').text
            item['workplace'] = job.find_all('span')[0].text
            item['requirements'] = job.find_all('span')[1].text
            print(item['company'])
            #打印书名。
            yield item
            #yield item是把获得的item传递给引擎。