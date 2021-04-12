import requests
from bs4 import BeautifulSoup

page = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
soup = BeautifulSoup(page.text,'html.parser')
travel_info = soup.find_all('article',class_="product_pod")
num = 0
# print(travel_info)
for book_info in travel_info:
    # print(classi)
    num += 1
    book_name = book_info.find(class_="thumbnail")
    # print(book_name['alt'])
    book_comment = book_info.find('p',class_="star-rating")
    # print(book_comment)
    book_price = book_info.find('p',class_="price_color")
    # print(book_price)
    print('%d、书名:%s,评价：%s star,价格：%s'%(num,book_name['alt'],book_comment['class'][1],book_price.text)) 
