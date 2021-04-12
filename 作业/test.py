# from urllib.request import quote,unquote

# url_1 = 'http://suo.im/5wtls'
# url_2 = 'http://bulletin.cebpubservice.com/biddingBulletin/2019-12-24/2374991.html'

# res_1 = unquote(url_1,encoding='GB2312')
# res_2 = unquote(url_2,encoding='utf-8')
# print(res_1)
# print(res_2)

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
url = 'https://book.douban.com/subject/1007305/comments/hot?p=1'
page = True
url_li = []
while page == True:
    res = requests.get(url,headers = headers)
    bs = BeautifulSoup(res.text,'html.parser')
    data = bs.find('ul',class_="comment-paginator")
    url_0 = data.find_all('li', class_ = 'p')
    try:
        url_1 = url_0.pop().find('a')['href']
        url = 'https://book.douban.com/subject/1007305/comments/'+url_1
        url_li.append(url)
    except:
        page = False
real_url = url_li[0]
res_0 = requests.get(real_url,headers = headers)
soup = BeautifulSoup(res_0.text,'html.parser')
datas = soup.find('div', id = "content")
book_name = datas.find('h1').text
con_data = datas.find_all('li',class_ = 'comment-item')
# # print (con_data)
# for data in con_data:
#     user = data.find('span', class_='comment-info').find('a').text
#     # user_id = user.find('a')['title']
#     comment = data.find('p', class_='comment-content').text
#     # print(book_name)
#     print(user)
#     # print(comment)
# # print(url_li)

# response.urljoin(response.css('#chapter-list-1>li:first-child>a').xpath('./@href').extract_first()) 
# response.urljoin(response.css('#chapter-list-1>li:last-child>a').xpath('./@href').extract_first())

