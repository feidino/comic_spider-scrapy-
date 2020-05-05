import requests
from bs4 import BeautifulSoup
from urllib.request import quote

home_page = requests.get('https://www.ygdy8.com/index.html')
home_page.encoding = 'gbk'
soup = BeautifulSoup(home_page.text,'html.parser')
home_info = soup.find_all('div',id="menu")
# print(home_page.status_code)
# print(soup)
mov_cls = {}
# mov_info = {}
mov_d_link = {}
for home in home_info:
    calssified = home.find_all('a')
    for link in calssified:
        mov_cls[link.text]='https://www.ygdy8.com/'+link['href']
del mov_cls['最新影片']
del mov_cls['经典影片']
del mov_cls['收藏本站']
mov_cls.popitem()
mov_cls.popitem()
mov_cls.popitem()
mov_cls.popitem()
mov_cls.popitem()
link_li = list(mov_cls.values())
mov_cal_li = list(mov_cls.keys())
# print(link_li)
# print(mov_cal_li)
for link in link_li:
    i = 0
    print(link.rstrip('index.html'))
#     for i in range(200):
#         i += 1
#         china_page = requests.get(link.rstrip('index.html')+'list_4_%d.html'%i)
#         china_page.encoding = 'gbk'
#         soup = BeautifulSoup(china_page.text,'html.parser')
#         china_mov_info = soup.find_all('div',class_="co_content8")
#         for mov in info:
#             mov_name = mov.find('b')
#             mov_page = requests.get('https://www.ygdy8.com/'+mov_name[1]['href'])
#             mov_page.encoding = 'gbk'
#             soup = BeautifulSoup(mov_page.text,'html.parser')
#             download_info = soup.find_all('table',align="center")
#             for links in download_info:
#                 D_link = links.find('a')['thunderrestitle']
#             mov_d_link[mov_name.text] = D_link
# print(mov_d_link)
                
                






