import gevent
from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue
import requests,csv,time
from bs4 import BeautifulSoup

start = time.time()

header = {
    'Cookie': 'Hm_lvt_7263598dfd4db0dc29539a51f116b23a=1589008173; Hm_lpvt_7263598dfd4db0dc29539a51f116b23a=1589010154',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }
url_list = []
for i in range(11):
    i += 1
    if i == 11:
        url_0 = 'http://www.boohee.com/food/view_menu'
        for page_num in range(10):
            page_num += 1
            url = url_0+'?page=%d'%page_num
            url_list.append(url)
    else:
        url_0 = 'http://www.boohee.com/food/group/%d'%i
        for page_num in range(10):
            page_num += 1
            url = url_0+'?page=%d'%page_num
            url_list.append(url)
work = Queue()
for url_e in url_list:
    work.put_nowait(url_e)

food_file = open('薄荷网11个常见食物分类里的食物信息.csv','w',newline='',encoding='gbk',errors='ignore')
food_info = csv.writer(food_file )
food_info.writerow(['食物种类','食物名','热量','食物详情页面链接'])

def crawler():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url,headers = header)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        food_all = soup.find('div',class_='widget-food-list pull-right')
        food_li = food_all.find_all('li',class_='item clearfix')
        for food in food_li:
            food_variety = food_all.find('h3').text
            food_link = 'http://www.boohee.com'+food.find('a')['href']
            food_name = food.find('img')['alt']
            food_heat = food.find('p').text
            print([food_variety,food_name,food_heat,food_link])
            food_info.writerow([food_variety,food_name,food_heat,food_link])
        # print(url,work.qsize(),res.status_code)

task_list = []
for i in range(5):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
end = time.time()
# crawler()
print(end-start)
food_file.close()
