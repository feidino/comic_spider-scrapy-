import requests
from bs4 import BeautifulSoup

page = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(page.text,'html.parser')
b_classified = soup.find_all('div',class_="side_categories")
# b_classified_2 = b_classified_1.find_all('ul')
# b_classified_3 = b_classified_2('li')
# print(b_classified_3)
# print(type(soup))
# print(type(b_classified))
book_list = []
for classi in b_classified:
    # print(classi)
#     print(type(classi))
#     print(type(b_classified))
    book1 = classi.find('ul')
    # print(book1)
    book2 = book1.find('li')
    # book3 = book2.find('a')
    # print(book3)
    book_list.append(book2.text)
    # print('books classified:\n%s\n'%(book3.text.strip()))
b_l = book_list[0].splitlines(keepends=True)
print('books classified:')
for string in b_l:
    s = string.strip()
    a = s.strip('\n')
    if a != '':
        print(a)


