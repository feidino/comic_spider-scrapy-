# import gevent
# from gevent.queue import Queue
# from gevent import monkey
# monkey.patch_all()
# 教学系统的浏览器设置方法
import time
# 本地Chrome浏览器的静默默模式设置：
from selenium import  webdriver #从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
import urllib.request,csv,os


chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行


url_file = open('url.csv','w',newline='',encoding='gbk',errors='ignore')
url_write = csv.writer(url_file)
url_write .writerow(['漫画名称','章节','页数','图片链接'])

start_url_list = []
driver.get('https://www.manhuabei.com/manhua/jinjidejuren/')
time.sleep(2)

for li_url in driver.find_elements_by_xpath("//ul[@id='chapter-list-1']/li/a"):
    start_url = li_url.get_attribute("href")
    start_url_list.append(start_url)
# work = Queue()
# for url in start_url_list:
#     work.put_nowait(url)


for url in start_url_list:
    # url = work.get_nowait()
    driver.get(url)
    time.sleep(2)

    comic_name = driver.find_element_by_xpath("//div[@class='head_title']/h1").text
    chapter = driver.find_element_by_xpath("//div[@class='head_title']/h2").text
    page_num = driver.find_element_by_xpath("//option[@selected='selected']").text
    link = driver.find_element_by_xpath("//div[@id='images']/img").get_attribute("src")
    url_write .writerow([comic_name,chapter,page_num,link])
    f = urllib.request.urlopen(link) 
    data = f.read() 
    name = comic_name+'-'+chapter+'-'+page_num 
    os.mkdir(r"D:\comic\进击的巨人\%s"%(chapter))
    with open(r"D:\comic\进击的巨人\%s\%s.jpg"%(chapter,name), "wb") as code:     
        code.write(data)
    num_str = driver.find_element_by_xpath("//div[@id='images']/p").text
    num = int(num_str[-3:-1])
    for i in range(1,num):
        next_url = url+'?p=%d'%(i+1)
        driver.get(next_url)
        time.sleep(2)

        page_num = '第%d页'%(i+1)
        link = driver.find_element_by_xpath("//div[@id='images']/img").get_attribute("src")
        url_write .writerow([comic_name,chapter,page_num,link])
        name = comic_name+'-'+chapter+'-'+page_num 
        f = urllib.request.urlopen(link) 
        data = f.read() 
        with open(r"D:\comic\进击的巨人\%s\%s.jpg"%(chapter,name), "wb") as code:     
            code.write(data)
url_file.close()      

# task_list = []
# for i in range(5):
#     task = gevent.spawn(comic_spider)
#     task_list.append(task)
# gevent.joinall(task_list)