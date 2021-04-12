# import os
#import random
#os.mkdir(r'e:\\海飞')
#print(os.listdir(r'e:\\'))
#with open(r'e:\vscode 文件\books.txt','r',encoding='utf-8') as f:
#lines = f.readlines()
#print(os.getcwd())

#i = 1%10
#a = 17%10
#b =27%10
#g = 71//10
#l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#g = lambda x:x*7 for x in range(1,15)
#print(i,a,b,g)
""" import csv
with open('assets.csv', 'a', newline='') as csvfile:
    #调用open()函数打开csv文件，传入参数：文件名“assets.csv”，、追加模式“a”、newline=''。
    writer = csv.writer(csvfile, dialect='excel')
    # 用csv.writer()函数创建一个writer对象。
    header = ['小区名称', '地址', '建筑时间', '楼栋', '单元', '门牌', '朝向', '面积']
    # 用writerow()函数将表头写进csv文件
    writer.writerow(header)
 """
""" import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count) """

""" spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
print(spam)
print(spam.strip('ampS')) """

""" import pyperclip
pyperclip.copy('SpamSpamBaconSpamEggsSpamSpam')
print(pyperclip.paste()) """

# import  re
# 我们一般采用编译的方式使用python的正则模块，如果在大量的数据量中，编译的方式使用正则性能会提高很多，具体读者们可以可以实际测试
# re_str = "hello this is python 2.7.13 and python 3.4.5"
# re_obj = re.compile(pattern = "python [0-9]\.[0-9]\.[0-9]",flags=re.IGNORECASE)
# res = re_obj.findall(re_str)
# print(res)

# pattern = re.compile("python [0-9]\.[0-9]\.[0-9]{1,}")
# res = pattern.findall(string=re_str)
# print(res)


# batRegex = re.compile('Bat(wo)*man')
# mo1 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo1)
# print(mo1.group())

# str = mo1.group().strip()
# print(str)


# # 引入requests库
# import requests

# # 发出请求，并把返回的结果放在变量res中
# res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# # 把Reponse对象的内容以二进制数据的形式返回
# pic = res.content
# # 新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# # 图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
# photo = open('ppt.jpg','wb')
# # 获取pic的二进制内容
# photo.write(pic) 
# # 关闭文件
# photo.close()

# import requests
# txt = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# res = txt.text
# sanguo = open ('sanguo.txt','w',encoding='utf-8')
# sanguo.write(res)
# sanguo.close()
# with open('sanguo.txt','r') as sanguo:
#     lines = sanguo.readlines()
# print(lines)

# import requests
# pic = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')
# data = pic.content
# picture = open ('Spider.jpg','wb')
# picture.write(data)
# picture.close()


# import requests
# mus = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
# data = mus.content
# music = open ('Rainbow.mp3','wb')
# music.write(data)
# music.close()

# import requests
# from bs4 import BeautifulSoup
# res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# html = res.text
# soup = BeautifulSoup( html,'html.parser')
# items = soup.find_all(class_='books')
# for item in items:
#     kind = item.find('h2')
#     # print(kind)
#     title = item.find(class_='title')
#     print(title)
#     brief = item.find(class_='info')
# print(kind.text,'\n',title.text,'\n',title['class'],'\n',brief.text) 

import requests
from bs4 import BeautifulSoup

# header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
# food_page = requests.get('https://movie.douban.com/top250?start=225&filter=',headers=header)
# soup = BeautifulSoup(food_page.text,'html.parser')
# # food_info = soup.find_all('div',class_="info pure-u")
# # num = 0
# print(soup)
# print(food_info)
# for massage in page_info:
#     # print(classi)
#     num += 1
#     art_title = massage.find('h2',class_="entry-title")
#     # print(art_title)
#     publ_time = massage.find('time',class_="entry-date published")
#     # print(publ_time)
#     art_link = massage.find('a')
#     # print(art_link['href'])

#     print('%d、title:%s, publish time：%s, artilcle link：%s'%(num,art_title.text,publ_time.text,art_link['href'])) 


# import requests
# from bs4 import BeautifulSoup

# header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
# num = 0
# # for i in range(0,250,25):
#     # print('https://movie.douban.com/top250?start=%d&filter='%(i))
# page = requests.get('https://movie.douban.com/top250?start=225&filter=',headers = header)
# soup = BeautifulSoup(page.text,'html.parser')
# movies_info = soup.find_all('ol',class_="grid_view")
# # print(soup)
# print(movies_info)
# for movie in movies_info:
#     # print(classi)
#     num += 1
#     movie_name = movie.find('span',class_="title")
#     # print(movie_name)
#     movie_grade= movie.find('span',class_="rating_num")
#     # print(movie_grade)
#     movie_comment = movie.find('span',class_="inq")
#     # print(movie_comment)
#     movie_link = movie.find('a',class_="")
#     try:
#         print('%d、电影名:%s, 豆瓣评分：%s分, 推荐语：%s, 电影链接：%s'%(num,movie_name.text,movie_grade.text,movie_comment.text,movie_link['href'])) 
#     except AttributeError:
#         print('')


string = 'abcdef'
string.strip('abc')
# s = string - 'abc'
print(string.strip('abc')+'ghi')


home_page = requests.get('https://www.ygdy8.com/index.html')
home_page.encoding = 'gbk'
soup = BeautifulSoup(home_page.text,'html.parser')
home_info = soup.find_all('div',id="menu")
# print(home_page.status_code)
# print(soup)
mov_cls = {}
mov_info = {}
mov_d_link = {}
def cal_info(home_info):
    for home in home_info:
        calssified = home.find_all('a')
        for link in calssified:
            mov_cls[link.text]='https://www.ygdy8.com/'+link['href']
# link_li = mov_cls.values()
# mov_cal_li = mov_cls.keys() 
# print(link_li)
# print(mov_cal_li)
def china_mov(china,name = None):
    for i in range(108):
        china_page = requests.get(mov_cls[china].strip('index.html')+'list_4_%d.html'%i)
        china_page.encoding = 'gbk'
        soup = BeautifulSoup(china_page.text,'html.parser')
        china_mov_info = soup.find_all('div',class_="co_content8")
        down_link = check_mov(china_mov_info,name)
        print(down_link)

def check_mov(info,name):
    for mov in info:
            mov_name = mov.find('b')
            mov_info[mov_name[1].text] = 'https://www.ygdy8.com/'+mov_name[1]['href']
            down_link = download_link(mov_info[name])
            return down_link

def download_link(mov_link):
    mov_page = requests.get(mov_link)
    mov_page.encoding = 'gbk'
    soup = BeautifulSoup(mov_page.text,'html.parser')
    download_info = soup.find_all('table',align="center")
    for links in download_info:
        D_link = links.find('a')['thunderrestitle']
    return D_link