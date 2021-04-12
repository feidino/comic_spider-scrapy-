import requests
from bs4 import BeautifulSoup

page = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
soup = BeautifulSoup(page.text,'html.parser')
page_info = soup.find_all('article')
num = 0
# print(page_info)
for massage in page_info:
    # print(classi)
    num += 1
    art_title = massage.find('h2',class_="entry-title")
    # print(art_title)
    publ_time = massage.find('time',class_="entry-date published")
    # print(publ_time)
    art_link = massage.find('a')
    # print(art_link['href'])
    print('%d、title:%s, publish time：%s, artilcle link：%s'%(num,art_title.text,publ_time.text,art_link['href'])) 