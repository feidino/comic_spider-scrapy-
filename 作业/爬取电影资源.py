import requests,random
from bs4 import BeautifulSoup
from urllib.request import quote
def mov_downlink():
    mov_info_dict = {}
    mov_name = input('请输入想要下载的电影名称：')
    search_lin = quote(mov_name.encode('gbk'))
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
choice = 1
while choice:
    choice = input('输入0结束程序，任意键继续执行程序：')
    mov_info_dict = mov_downlink()
print (mov_info_dict)