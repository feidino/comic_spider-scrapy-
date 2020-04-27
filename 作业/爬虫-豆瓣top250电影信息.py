import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
num = 0
for i in range(0,250,25):
    # print('https://movie.douban.com/top250?start=%d&filter='%(i))
    page = requests.get('https://movie.douban.com/top250?start=%d&filter='%(i),headers = header)
    soup = BeautifulSoup(page.text,'html.parser')
    movies_info = soup.find_all('div',class_='info')
    # print(soup)
    # print(movies_info)
    for movie in movies_info:
        # print(classi)
        num += 1
        movie_name = movie.find('span',class_="title")
        # print(movie_name.text)
        movie_grade= movie.find('span',class_="rating_num")
        # print(movie_grade.text)
        movie_comment = movie.find('span',class_="inq")
        # print(movie_comment.text)
        movie_link = movie.find('a',class_="")
        # print(movie_link['href'])
        if movie_comment != None:
            print('%d、电影名:%s 豆瓣评分：%s分 推荐语：%s 电影链接：%s'%(num,movie_name.text,movie_grade.text,movie_comment.text,movie_link['href'])) 
        else:
            print('%d、电影名:%s 豆瓣评分：%s分 推荐语：无 电影链接：%s'%(num,movie_name.text,movie_grade.text,movie_link['href']))
        # except AttributeError:
        #     print('%d、该电影信息爬取不到'%num)