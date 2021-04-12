from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
import time

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
spider_driver = webdriver.Chrome(options = chrome_options)

spider_driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(2)

elem = spider_driver.find_element_by_name("log")
elem.send_keys('feidino')
elem = spider_driver.find_element_by_name("pwd")
elem.send_keys('31102341archer')
elem = spider_driver.find_element_by_id('wp-submit')
print(elem)
elem.click()

spider_driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
time.sleep(2)

articles = spider_driver.find_elements_by_class_name('entry-title')
art = input('请输入你想要评论的文章:')
link_text = spider_driver.find_element_by_link_text(art)
link_text.click()
# print(spider_driver.current_url)
time.sleep(2)

spider_driver.get(spider_driver.current_url)
time.sleep(2)

con = spider_driver.find_element_by_id("comment")
conmment = input('请输入你的评论：')
con.send_keys(conmment)
post = spider_driver.find_element_by_name("submit")
post.click()



