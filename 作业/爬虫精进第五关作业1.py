# 直接运行代码就好
import requests,re
# 引用requests模块
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
# 伪装请求头
singger_name = input('请输入需要查询的歌手名字：')
for x in range(1):
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.song_next',
    'searchid':'64405487069162918',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(x+1),
    'n':'20',
    'w':singger_name,
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'    
    }
    # 将参数封装为字典
    res_music = requests.get(url,headers=headers,params=params)
    # 调用get方法，下载这个字典
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
    # list_music是一个列表，music是它里面的元素
        print(music['name'])
        # 以name为键，查找歌曲名
        print('所属专辑：'+music['album']['name'])
        # 查找专辑名
        print('播放时长：'+str(music['interval'])+'秒')
        # 查找播放时长
        print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')
        # 查找播放链接
        lirc_params = {
            "nobase64":'1',
            'musicid':str(music['id']),
            '-':'jsonp1',
            'g_tk_new_20200303': '5381',
            'g_tk':'5381',
            'loginUin':'0',
            'hostUin':'0',
            'format':'json',
            'inCharset':'utf8',
            'outCharset':'utf-8',
            'notice':'0',
            'platform':'yqq.json',
            'needNewCode':'0'
        }
        lirc_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
        res_lirc = requests.get(lirc_url,headers=headers,params=lirc_params)
        json_lirc = res_lirc.json()
        list_lrc = json_lirc['lyric']
        music_lrc = list_lrc.split('&#10')
        lrc_list = []
        for i in music_lrc:
            jay_lrc = re.sub(r'[A-Za-z0-9\#\'\'\%\。\，\；\;\[\]\&]','',i)
            lrc_list.append(jay_lrc.strip())
        # print('%s歌词：'%music['name'])
        for s in lrc_list:
            print(s)
        print('\n\n')