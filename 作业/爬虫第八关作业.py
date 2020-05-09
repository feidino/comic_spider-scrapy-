import requests,json
from bs4 import BeautifulSoup 

session = requests.session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
fiction_dict = {}
for i in range(5):
    url_html = ('https://www.xslou.com/top/allvisit_%s/'%str(i))
    results = requests.get(url_html,headers = headers)
    results.encoding = 'gbk'
    bs = BeautifulSoup(results.text,'html.parser')
    ols = bs.find_all('span',class_="up2")
    for ls in ols:
        url_link = ls.find('a')['href']
        fiction_name = ls.find('a').text
        id_list = list(filter(str.isdigit,url_link))
        fiction_id = ''.join(id_list)
        fiction_dict[fiction_name] = fiction_id
# print(fiction_dict)        
try:
    f = open('cookies.txt','r',encoding='utf-8')
    cookies_dict = json.loads(f.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    session.cookies = cookies
except FileNotFoundError:
    url = 'https://www.xslou.com/login.php'
    data = {
        'username': input('请输入账户:'),
        'password': input('请输入密码:'),
        'action': 'login'
            }
    session.post(url, headers = headers, data = data)
    cookes_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookes_str = json.dumps(cookes_dict)
    f_w = open ('cookies.txt','w',encoding='utf-8')
    f_w.write(cookes_str)
    f_w.close()
url_1 = 'https://www.xslou.com/modules/article/uservote.php'
fiction_name = input('请输入你需要推荐的小说名称：')
data_1 = {
    'id': fiction_dict[fiction_name]
}
comment = session.post(url_1, headers = headers, data = data_1,cookies = session.cookies)
print(comment.status_code)


# 参考答案----------------------------------------------
# import requests 
# from bs4 import BeautifulSoup 

# login_url = 'https://www.xslou.com/login.php'
# hot_url = 'https://www.xslou.com/top/allvisit_1/'
# urge_url = 'https://www.xslou.com/modules/article/uservote.php?id='
# session = requests.session()  
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
# }

# def login_cookies():
#     data = {'username':input('请输入你的账号:'),
#             'password':input('请输入你的密码:'),
#             'action':'login'}
#     session.post(login_url, headers=headers, data=data)

# def get_bookids():
#     result = requests.get(hot_url, headers=headers)
#     result.encoding = 'gbk'
#     bs = BeautifulSoup(result.text,'html.parser')
#     uls = bs.find_all('span',class_='up2')
#     books = {}
#     for li in uls:
#         book_name = li.find('a').text
#         link = li.find('a')['href']
#         id_list = list(filter(str.isdigit,link))
#         book_id = ''.join(id_list)
#         books[book_id] = book_name
#     return books

# def urge(book_id):
#     url = urge_url+book_id
#     result = session.get(url, headers=headers, cookies=session.cookies)
#     result.encoding = 'gbk'
#     if result.status_code == 200:
#         bs = BeautifulSoup(result.text,'html.parser')
#         urge_info = bs.find('div',class_='blocktitle').get_text()
#         urge_info2 = bs.find('div',class_='blockcontent').get_text()
#         print(urge_info)
#         print(urge_info2)

# def main ():
#     login_cookies()
#     books = get_bookids()
#     print('--------热门书籍--------')
#     for k,v in books.items():
#         print(k,':',v)
#     book_id = input('请输入想要推荐的书籍id：')
#     urge(book_id)
# main()