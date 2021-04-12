import requests,random
from bs4 import BeautifulSoup
from urllib.request import quote
import smtplib,schedule
from email.mime.text import MIMEText
from email.header import Header
def mov_search():
    mov_dict = {}
    for i in range(0,250,25):
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
        page = requests.get('https://movie.douban.com/top250?start=%d&filter='%(i),headers = header)
        soup = BeautifulSoup(page.text,'html.parser')
        movies_info = soup.find_all('div',class_='info')
        for movie in movies_info:
            movie_name = movie.find('span',class_="title").text
            movie_grade= movie.find('span',class_="rating_num").text+'分'
            movie_comment_0 = movie.find('span',class_="inq")
            movie_link = movie.find('a',class_="")['href']
            if movie_comment_0 != None:
                movie_comment = movie_comment_0.text
                mov_dict[movie_name] = ['豆瓣评分：%s'%movie_grade,'推荐语：%s'%movie_comment,'豆瓣电影链接：%s'%movie_link]
                # print('%d、电影名:%s 豆瓣评分：%s分 推荐语：%s 电影链接：%s'%(num,movie_name,movie_grade,movie_comment,movie_link)) 
            else:
                mov_dict[movie_name] = ['豆瓣评分：%s'%movie_grade,'推荐语：无','豆瓣电影链接：%s'%movie_link]
                # print('%d、电影名:%s 豆瓣评分：%s分 推荐语：无 电影链接：%s'%(num,movie_name,movie_grade,movie_link))
    mov_name_li = mov_dict.keys()
    mov_choose = random.sample(mov_name_li,3)
    return mov_choose,mov_dict
    # print(mov_choose)

def mov_downlink(mov_choose):
    mov_info_dict = {}
    for movie in mov_choose:
        search_lin = quote(movie.encode('gbk'))
        search_url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword='+search_lin
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
        res = requests.get(search_url,headers = header)
        # print(search_url)
        res.encoding = 'gbk'
        mv_s = BeautifulSoup(res.text,'html.parser')
        mov_s = mv_s.find_all('td',width="55%")
        if mov_s == []:
            mov_info_dict[movie] = '无可提供的下载链接'
        else:
            for search in mov_s:
                link = search.find('a')['href']
                mov_url = 'http://s.ygdy8.com'+link 
                res_0 = requests.get(mov_url,headers = headers)
                res_0.encoding = 'gbk'
                mov_soup = BeautifulSoup(res_0.text,'html.parser')
                mov_l = mov_soup.find_all('div',id = "Zoom")
                for movie_dlink in mov_l:
                    mov_dl = movie_dlink.find('td',style="WORD-WRAP: break-word").text
                    mov_info_dict[movie] = mov_dl
    return mov_info_dict
    # print(mov_info_dict)
def mail_text(mov_info_dict,mov_dict):
    i = 0
    recommend_mv_li = []
    for name,link in  mov_info_dict.items():
        i += 1
        text = str(i)+'、 '+name+ '\n'+'\n'.join(mov_dict[name]) +'\n' + '电影下载链接：'+link
        recommend_mv_li.append(text)
    return recommend_mv_li

def send_email(recommend_mv_li):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    account = '619274249@qq.com'
    password = 'sbiqnrmgshambgad'
    qqmail.login(account,password)
    receiver='hxqxkb@163.com'
    content = '\n'.join(recommend_mv_li)
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '本周最推荐电影'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()
def job():
    mov_choose,mov_dict = mov_search()
    mov_info_dict = mov_downlink(mov_choose)
    recommend_mv_li = mail_text(mov_info_dict,mov_dict)
    print(recommend_mv_li)
    send_email(recommend_mv_li)

# schedule.every().friday.at('12:00').do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1) 

job()



