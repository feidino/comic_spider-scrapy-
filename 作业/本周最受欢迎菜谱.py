import requests,schedule
from bs4 import BeautifulSoup
import smtplib 
from email.mime.text import MIMEText
from email.header import Header
url = 'http://www.xiachufang.com/explore/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
res_foods = requests.get(url,headers = headers)
res_foods.encoding = 'utf-8'
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
def food_pic():
    list_pic = []
    list_food_pic = bs_foods.find_all('div',class_='cover pure-u')
    pic_num = 0
    for pic in list_food_pic:
        pic_num += 1
        food_pic_link = pic.find('img')['data-src']
        res_pic = requests.get(food_pic_link,headers = headers)
        data  = res_pic.content
        picture = open ('food_pic%d.png'%pic_num,'wb')
        picture.write(data)
        picture.close()
        list_pic.append('food_pic%d.png'%pic_num)
    return list_pic
def food():
    list_food = []
    list_foods = bs_foods.find_all('div',class_='info pure-u')
    for food in list_foods:
        tag_a = food.find('a')
        name = tag_a.text[17:-13]
        URL = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text[1:-1]
        list_food.append([name,URL,ingredients])
    return list_food
    # print(list_food)
def text(list_food):
    food_text = open ('food.txt','w',encoding='utf-8')
    for food_info in list_food:
        food = food_info[0]+'\n'+food_info[1]+'\n'+food_info[2]+'\n'
        food_text.writelines(food)
    
def send_email():
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)

    account = '619274249@qq.com'
    password = 'sbiqnrmgshambgad'
    qqmail.login(account,password)
    receiver='hxqxkb@163.com'
    food_text = open ('food.txt','r',encoding='utf-8')
    content_list = food_text.readlines()
    content1 = ''.join(content_list)
    message = MIMEText(content1, 'plain', 'utf-8')
    subject = '本周最受欢迎的食谱'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()
def job():
    list_food = food()
    text(list_food)
    send_email()
schedule.every().friday.at('12:00').do(job)

while True:
    schedule.run_pending()
    time.sleep(1) 

