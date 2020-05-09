# # 引用requests库   
# import requests
# # 调用get方法，下载这个字典
# res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# # 使用json()方法，将response对象，转为列表/字典
# json_music = res_music.json()
# # 一层一层地取字典，获取歌单列表
# list_music = json_music['data']['song']['list']
# # list_music是一个列表，music是它里面的元素
# for music in list_music:
#     # 以name为键，查找歌曲名
#     print(music['name'])
#     # 查找专辑名
#     print('所属专辑：'+music['album']['name'])
#     # 查找播放时长
#     print('播放时长：'+str(music['interval'])+'秒')
#     # 查找播放链接
#     print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')


# import requests
# # 引用requests模块
# for i in range(5):
#     res_comments = requests.get('''https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0
#     &format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid
#     =102065756&cmd=6&needmusiccrit=0&pagenum=%d&pagesize=15&lasthotcommentid=song_102065756_3202544866_44059185&domain=qq.com&ct=24&
#     cv=10101010'''%i)
#     # 调用get方法，下载评论列表
#     json_comments = res_comments.json()
#     # 使用json()方法，将response对象，转为列表/字典
#     list_comments = json_comments['comment']['commentlist']
#     # 一层一层地取字典，获取评论列表
#     for comment in list_comments:
#     # list_comments是一个列表，comment是它里面的元素
#         print(comment['rootcommentcontent'])
#         # 输出评论
#         print('-----------------------------------')
#         # 将不同的评论分隔开来


# for i in range(5):
#     res_comments = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=6&needmusiccrit=0&pagenum='+str(i)+'&pagesize=15&lasthotcommentid=song_102065756_3202544866_44059185&domain=qq.com&ct=24&cv=10101010')
#     # 调用get方法，下载评论列表
#     json_comments = res_comments.json()
#     # 使用json()方法，将response对象，转为列表/字典
#     list_comments = json_comments['comment']['commentlist']
#     # 一层一层地取字典，获取评论列表
#     for comment in list_comments:
#     # list_comments是一个列表，comment是它里面的元素
#         print(comment['rootcommentcontent'])
#         # 输出评论
#         print('-----------------------------------')
#         # 将不同的评论分隔开来
# import openpyxl 
# wb=openpyxl.Workbook('Marvel.xlsx') 
# sheet=wb.active
# # sheet.title='new title'
# sheet['A1'] = 'footballclub'
# rows= [['利物浦','曼娘','阿森纳'],['红军','红魔','兵工厂']]
# for i in rows:
#     sheet.append(i)
# print(rows)
# import openpyxl 
# wb = openpyxl.load_workbook('Marvel.xlsx')
# sheet = wb.create_sheet('german')
# sheet['A1'] = '多特蒙德'
# sheet['A2'] = '拜仁慕尼黑'
# rows= [['利物浦','曼娘','阿森纳'],['红军','红魔','兵工厂']]
# for i in rows:
#     sheet.append(i)
# print(rows)
# wb.save('Marvel.xlsx')

# print(sheetname)
# A1_cell = sheet['A1']
# A1_value = A1_cell.value
# print(A1_value)

# import csv
# csv_file = open('demo.csv','w',newline='',encoding='gbk')
# csv_write = csv.writer(csv_file)
# csv_write.writerow(['利物浦','曼联','阿森纳','车尔西','曼城','热刺'])
# csv_file.close()

# import requests,openpyxl 
# wb=openpyxl.Workbook() 
# sheet=wb.active
# sheet.title='jay_song'
# rows= ['歌曲名称','所属专辑','播放时长','播放链接']
# sheet.append(rows)
# url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# for x in range(5):

#     params = {
#         'ct': '24',
#         'qqmusic_ver': '1298',
#         'new_json': '1',
#         'remoteplace': 'sizer.yqq.song_next',
#         'searchid': '64405487069162918',
#         't': '0',
#         'aggr': '1',
#         'cr': '1',
#         'catZhida': '1',
#         'lossless': '0',
#         'flag_qc': '0',
#         'p': str(x + 1),
#         'n': '20',
#         'w': '周杰伦',
#         'g_tk': '5381',
#         'loginUin': '0',
#         'hostUin': '0',
#         'format': 'json',
#         'inCharset': 'utf8',
#         'outCharset': 'utf-8',
#         'notice': '0',
#         'platform': 'yqq.json',
#         'needNewCode': '0'
#     }

#     res_music = requests.get(url, params=params)
#     json_music = res_music.json()
#     list_music = json_music['data']['song']['list']
#     song_info = []
#     for music in list_music:
#         musi_tim = str(music['interval']) + '秒'
#         musi_link = 'https://y.qq.com/n/yqq/song/' + music['file']['media_mid'] + '.html'
#         song_info = [music['name'],music['album']['name'],musi_tim,musi_link]
#         sheet.append(song_info)
#         print(music['name'])
#         print('所属专辑：' + music['album']['name'])
#         print('播放时长：' + str(music['interval']) + '秒')
#         print('播放链接：https://y.qq.com/n/yqq/song/' + music['file']['media_mid'] + '.html\n\n')


# 引入requests和bs
# import requests,json,csv
# # from bs4 import BeautifulSoup

# article_file = open('张佳玮知乎文章.csv','a',newline='',encoding='gbk',errors='ignore')
# article_info = csv.writer(article_file)
# print(type(article_info))
# article_info.writerow(['文章名称','文章摘要','文章链接'])
# # 使用headers是一种默认的习惯，默认你已经掌握啦~
# headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# # 发起请求，将响应的结果赋值给变量res。
# url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
# for i in range(10,130,20):
#     params = {
#         'include':' data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
#         'offset': str(i),
#         'limit': '10',
#         'sort_by': 'created'
#     }
#     res=requests.get(url,headers=headers,params=params)
#     # 检查状态码 
#     # print(res.status_code)
#     json_article = res.json()
#     # 使用json()方法，将response对象，转为列表/字典
#     article_list = json_article['data']
#     for article_info in article_list:
#         article_title = article_info['title']
#         article_digest = article_info['excerpt']
#         article_link = article_info['url']
#         # print(type(article_title),type(article_digest),type(article_link))
#         article_info.writer([article_title,article_digest,article_link])
#         # print('文章名称：%s\n文章摘要：%s\n文章链接：%s\n '%(article_title,article_digest,article_link))




# # 引入requests和bs
# import requests,json,openpyxl
# # from bs4 import BeautifulSoup

# wb=openpyxl.Workbook() 
# sheet=wb.active
# sheet.title='张佳玮知乎文章'
# rows= ['文章名称','文章摘要','文章链接']
# sheet.append(rows)

# # 使用headers是一种默认的习惯，默认你已经掌握啦~
# headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# # 发起请求，将响应的结果赋值给变量res。
# url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
# for i in range(10,1130,20):
#     params = {
#         'include':' data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
#         'offset': str(i),
#         'limit': '10',
#         'sort_by': 'created'
#     }
#     res=requests.get(url,headers=headers,params=params)
#     # 检查状态码 
#     # print(res.status_code)
#     json_article = res.json()
#     # 使用json()方法，将response对象，转为列表/字典
#     article_list = json_article['data']
#     for article_info in article_list:
#         article_title = article_info['title']
#         article_digest = article_info['excerpt']
#         article_link = article_info['url']
#         # print(type(article_title),type(article_digest),type(article_link))
#         sheet.append([article_title,article_digest,article_link])
#         # print('文章名称：%s\n文章摘要：%s\n文章链接：%s\n '%(article_title,article_digest,article_link))
# wb.save('张佳玮知乎文章.xlsx')

# import requests
# # 引用csv
# import csv
# # 调用open()函数打开csv文件，传入参数：文件名“articles.csv”、写入模式“w”、newline=''。
# csv_file=open('articles.csv','w',newline='',encoding='gbk')
# # 用csv.writer()函数创建一个writer对象。
# writer = csv.writer(csv_file)
# # 创建一个列表
# list2=['标题','链接','摘要']
# # 调用writer对象的writerow()方法，可以在csv文件里写入一行文字 “标题”和“链接”和"摘要"。
# writer.writerow(list2)
# # 使用headers是一种习惯
# headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# # 设置offset的起始值为10
# offset=10

# while True:
#     # 封装参数
#     params={
#         'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
#         'offset':str(offset),
#         'limit':'10',
#         'sort_by':'voteups',
#         }
#     # 发送请求，并把响应内容赋值到变量res里面
#     res=requests.get(url,headers=headers,params=params)
#     # 确认这个response对象状态正确 
#     print(res.status_code)
#     # 如果响应成功，继续
#     if int(res.status_code) == 200:
#         articles=res.json()
#         # print(articles)
#         # 定位数据
#         data=articles['data']
    
#         for i in data:
#             # 把目标数据封装成一个列表
#             list1=[i['title'],i['url'],i['excerpt']]
#             # 调用writerow()方法，把列表list1的内容写入
#             writer.writerow(list1)  
#         # 在while循环内部，offset的值每次增加20
#         offset=offset+20
#         if offset > 30:
#             break

# # 写入完成后，关闭文件就大功告成
# csv_file.close()
# print('okay')  

# import requests

# url_0 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
# }
# data = {
#     'log': 'spiderman',
#     'pwd': 'crawler334566',
#     'wp-submit': '登录',
#     'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#     'testcookie': '1'
# }
# login_in = requests.post(url_0,headers = headers,data = data)
# cookies = login_in.cookies
# url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# data_1 = {
#     'comment': input('请输入你的评论：'),
#     'submit': '发表评论',
#     'comment_post_ID': '23',
#     'comment_parent': '0'
# }
# comment  = requests.post(url_1,headers = headers,data = data_1,cookies = cookies)
# print(comment.status_code)

# import requests,json
# session = requests.session()
# #创建会话。
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
# }
# #添加请求头，避免被反爬虫。
# try:
# #如果能读取到cookies文件，执行以下代码，跳过except的代码，不用登录就能发表评论。
#     cookies_txt = open('cookies.txt', 'r')
#     #以reader读取模式，打开名为cookies.txt的文件。
#     cookies_dict = json.loads(cookies_txt.read())
#     #调用json模块的loads函数，把字符串转成字典。
#     cookies = requests.utils.cookiejar_from_dict(cookies_dict)
#     #把转成字典的cookies再转成cookies本来的格式。
#     session.cookies = cookies
#     #获取会话下的cookies

# except FileNotFoundError:
# #如果读取不到cookies文件，程序报“FileNotFoundError”（找不到文件）的错，则执行以下代码，重新登录获取cookies，再评论。

#     url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
#     #登录的网址。
#     data = {'log': input('请输入你的账号:'),
#             'pwd': input('请输入你的密码:'),
#             'wp-submit': '登录',
#             'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#             'testcookie': '1'}
#     #登录的参数。
#     session.post(url, headers=headers, data=data)
#     #在会话下，用post发起登录请求。

#     cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
#     #把cookies转化成字典。
#     cookies_str = json.dumps(cookies_dict)
#     #调用json模块的dump函数，把cookies从字典再转成字符串。
#     f = open('cookies.txt', 'w')
#     #创建名为cookies.txt的文件，以写入模式写入内容
#     f.write(cookies_str)
#     #把已经转成字符串的cookies写入文件
#     f.close()
#     #关闭文件

# url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# #文章的网址。
# data_1 = {
# 'comment': input('请输入你想评论的内容：'),
# 'submit': '发表评论',
# 'comment_post_ID': '13',
# 'comment_parent': '0'
# }
# #评论的参数。
# session.post(url_1, headers=headers, data=data_1)
# #在会话下，用post发起评论请求

# import tkinter
# top = tkinter.Tk()
# # 进入消息循环
# top.mainloop()

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://www.kuaidi100.com/')

# # 教学系统的浏览器设置方法
# import time
# # 本地Chrome浏览器的静默默模式设置：
# from selenium import  webdriver #从selenium库中调用webdriver模块
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类

# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
# driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行

# driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') # 访问页面
# time.sleep(2) # 暂停两秒，等待浏览器缓冲

# for i in range(20):
#     button = driver.find_element_by_class_name('js_get_more_hot') # 找到【提交】按钮
#     button.click() # 点击【提交】按钮
# time.sleep(1)
# comments = driver.find_elements_by_class_name('js_hot_text')
# print(len(comments))
# for comment in comments:
#     print(comment.text,'\n')
# # print(comment)
# time.sleep(1)
# driver.close() # 关闭浏览器

import gevent
from gevent.queue import Queue
from gevent import monkey
monkey.patch_all()
import time,requests

start = time.time()

url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']
work = Queue()
for url in url_list:
    work.put_nowait(url)
def crawler():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url)
        print(url,work.qsize(),res.status_code)
task_list = []
for i in range(3):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
end = time.time()
print(end-start)
