import gevent
from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue
import requests,csv,time,unicodedata
from bs4 import BeautifulSoup

start = time.time()

header = {
    'Cookie': '_userCode_=202058191946339; _userIdentity_=2020581919462599; _tt_=BA4DF2F0EE951137C26B479FB60314EC; __utma=196937584.396819459.1588936787.1588936787.1588936787.1; __utmc=196937584; __utmz=196937584.1588936787.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_6dd1e3b818c756974fb222f0eae5512e=1588936787; Hm_lpvt_6dd1e3b818c756974fb222f0eae5512e=1588936787',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }
url_list = []
for i in range(10):
    i += 1
    if i == 1:
        url = 'http://www.mtime.com/top/tv/top100'
        url_list.append(url)
    else:
        url = 'http://www.mtime.com/top/tv/top100/index-%d.html'%i
        url_list.append(url)
work = Queue()
for url_e in url_list:
    work.put_nowait(url_e)

tv_file = open('时光电视剧TOP100.csv','a',newline='',encoding='gbk',errors='ignore')
tv_top100 = csv.writer(tv_file)
tv_top100.writerow(['排名','电视剧名称','导演','演员','简介'])

def crawler():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url,headers = header)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        tv_info_0 = soup.find('div',class_='top_list')
        tv_info = tv_info_0.find_all('li')
        # print(tv_info)
        for tv in tv_info:
            tv_info_list = []
            tv_rank = tv.find('div',class_="number").text
            tv_info_list = [tv_rank]
            tv_info = tv.find('div',class_="mov_con").text
            tv_info_0 = tv_info.replace('导演： ',' ')
            tv_info_1 = tv_info_0.replace('主演： ',' ')
            tv_info_2 = tv_info_1.split('  ')
            for tv_0 in tv_info_2:
                tv_tag = unicodedata.normalize('NFKC',tv_0)
                # tv_tag = ' '.join(tv_0.split())
                tv_info_list.append(tv_tag)
            print(tv_info_list)
            if len(tv_info_list) < 5:
                tv_info_list = tv_info_list[:2]+['无']+tv_info_list[2:]
                tv_top100.writerow(tv_info_list)
            else:
                tv_top100.writerow(tv_info_list)
        print(url,work.qsize(),res.status_code)

task_list = []
for i in range(3):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
end = time.time()
print(end-start)
tv_file.close()


