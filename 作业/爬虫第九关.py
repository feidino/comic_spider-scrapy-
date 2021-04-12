# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
# import time

# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
# spider_driver = webdriver.Chrome(options = chrome_options)

# # spider_driver = webdriver.Chrome()

# spider_driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
# time.sleep(2)

# elem = spider_driver.find_element_by_name("teacher")
# elem.send_keys('吴枫')
# elem = spider_driver.find_element_by_name("assistant")
# elem.send_keys('酱酱')
# elem = spider_driver.find_element_by_class_name('sub')
# elem.click()
# time.sleep(2)


# articles = spider_driver.find_elements_by_class_name('content')
# print(articles)
# en_art,cn_art = articles
# en_art_txt = en_art.text
# cn_art_txt = cn_art.text
# en_art_list = en_art_txt.split('.')
# cn_art_list = cn_art_txt.split('\n')
# width_list_0 = []
# width_list_1 = []
# for n in en_art_list:
#     width_list_0.append(len(n))
# width_list_0.sort(reverse=True)
# for m in cn_art_list:
#     width_list_1.append(len(m))
# width_list_1.sort(reverse=True)
# for i in range(len(en_art_list)):
#     if i < len(cn_art_list):
#         print('%d、'%(i+1),'',en_art_list[i].ljust(width_list_0[0]),' '*10,cn_art_list[i].ljust(width_list_1[0]))
#     else:
#         print('%d、'%(i+1),'',en_art_list[i].ljust(width_list_0[0]))

# ------------------------华丽的分割线-----------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
from bs4 import BeautifulSoup
import time

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
spider_driver = webdriver.Chrome(options = chrome_options)

# spider_driver = webdriver.Chrome()

spider_driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

elem = spider_driver.find_element_by_name("teacher")
elem.send_keys('吴枫')
elem = spider_driver.find_element_by_name("assistant")
elem.send_keys('酱酱')
elem = spider_driver.find_element_by_class_name('sub')
elem.click()
time.sleep(2)

res = spider_driver.page_source
bs = BeautifulSoup(res,'html.parser')
articles = bs.find_all('div',class_="content")
en_art,cn_art = articles
en_art_txt = en_art.text
cn_art_txt = cn_art.text
en_art_list = en_art_txt.split('.')
cn_art_list = cn_art_txt.split('\n')
width_list_0 = []
width_list_1 = []
for n in en_art_list:
    width_list_0.append(len(n))
width_list_0.sort(reverse=True)
for m in cn_art_list:
    width_list_1.append(len(m))
width_list_1.sort(reverse=True)
for i in range(len(en_art_list)):
    if i < len(cn_art_list):
        print('%d、'%(i+1),'',en_art_list[i].ljust(width_list_0[0]),' '*10,cn_art_list[i].ljust(width_list_1[0]))
    else:
        print('%d、'%(i+1),'',en_art_list[i].ljust(width_list_0[0]))

