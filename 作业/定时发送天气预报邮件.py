import requests,schedule
from bs4 import BeautifulSoup
def weather_spider():
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101280601.shtml'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    res_soup = BeautifulSoup(res.text,'html.parser')
    info_list = res_soup.find('li',class_ = 'skyid')
    # print(info_list)
    weather = info_list.find('p',class_ = 'wea').text
    temper = info_list.find('p',class_ = 'tem').text
    winter = info_list.find('p',class_ = 'win').find('i').text
    info = ('今天天气：%s，温度：%s ，风力：%s'%(weather,temper.strip('\n'),winter.strip('\n')))
    # print(info)
    return info
    

import smtplib 
from email.mime.text import MIMEText
from email.header import Header
def send_email(info):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)

    account = input('请输入你的邮箱：')
    password = input('请输入你的密码：')
    qqmail.login(account,password)

    receiver=input('请输入收件人的邮箱：')
    content= '亲爱的今天天气情况：'+info 
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今天天气情况'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    info = weather_spider()
    send_email(info)
    print('任务完成')

schedule.every().day.at("07:30").do(job) 
while True:
    schedule.run_pending()
    time.sleep(1)