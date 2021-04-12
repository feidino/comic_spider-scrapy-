# from scrapy_splash import SplashRequest
# import scrapy
# # from scrapy.selector import Selector
# # from scrapy.http import HtmlResponse
# # body = '<html><body><span>good</span></body></html>'
# # text = Selector(text=body).xpath('//span/text()').extract_first()
# # print(text)
# # mystr = '黑镜\xa0Black Mirror (2011)'
# # mystr = ' '.join(mystr.split())
# # print(mystr.split())
# response = scrapy.splash.Request('https://www.manhuabei.com/manhua/jinjidejuren/7900.html')
# print(reponse.css('#images>img'))
# import urllib.request
# import os
# url = 'https://img01.eshanyao.com/images/comic/4/7900/1539167722LrZ_71jczKgMrULj.jpg'

# os.mkdir(r"D:\comic\进击的巨人\1-1")
# f = urllib.request.urlopen(url) 
# data = f.read() 
# with open(r"D:\comic\进击的巨人\1-1.jpg", "wb") as code:     
#     code.write(data) 

import time
# 本地Chrome浏览器的静默默模式设置：
from selenium import  webdriver #从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
# import urllib.request,csv,os


# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome() # 设置引擎为Chrome，在后台默默运行

driver.get('https://www.manhuabei.com/')
time.sleep(3)

comic_text = input('请输入需要下载的漫画关键字：')
comic_find = driver.find_element_by_id("keywords")
comic_find.send_keys(comic_text)
search_button = driver.find_element_by_id("btnSearch")
search_button.click()
time.sleep(3)

c_url = driver.current_url
print(c_url)

driver.get(c_url)
time.sleep(3)

num = 0
choice_dit = {}
for comic_search in driver.find_elements_by_xpath("//li[@class='list-comic']/p/a"):
    num = num+1
    choice = str(num) + '、'+ comic_search.text
    choice_dit[str(num)] = [comic_search.text,comic_search]
    print(choice)
print(choice_dit)
cont = 1
while cont:
    choice_num = input('以上为本站的搜索结果，请选择您需要下载的漫画的数字编号：')
    if choice_dit[choice_num][0]:
        print(choice_dit[choice_num][0])
        continue_link = choice_dit[choice_num][1].get_attribute("href")
        print(continue_link)
        cont = 0
    else:
        print('输入有误，请重新输入')

# driver.get(continue_link)
# time.sleep(3)
# print(driver.find_elements_by_xpath("//div[@class='comic_deCon']/h1").text)

driver.close()