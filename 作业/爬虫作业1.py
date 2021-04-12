import requests
from bs4 import BeautifulSoup
i = 0
num = 0
for i in range(5):
    i += 1
    text = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/comment-page-%d/#comments'%(i))
    soup = BeautifulSoup(text.text,'html.parser')
    comments = soup.find_all('div',class_='comment-content')
    for e_com in comments:
        num += 1
        print('%d、%s\n'%(num,e_com.find('p').text))



