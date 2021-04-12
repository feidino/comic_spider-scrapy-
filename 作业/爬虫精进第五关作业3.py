# import requests
# #调用requests模块

# url = 'https://www.kuaidi100.com/query'
# epress_num = input('请输入需要查询的快递单号：')
# for x in range(5):

#     params = {
#     'type': 'zhongtong',
#     'postid': epress_num,
#     temp: 0.901642139253805
   
#     }
#     # 将参数封装为字典
#     res_music = requests.get(url,params=params)
#     # 调用get方法，下载这个列表
#     json_music = res_music.json()
#     # 使用json()方法，将response对象，转为列表/字典
#     list_music = json_music['data']['song']['list']
#     # 一层一层地取字典，获取歌单列表
#     for music in list_music:
#     # list_music是一个列表，music是它里面的元素
#         print(music['name'])
#         # 以name为键，查找歌曲名
#         print('所属专辑：'+music['album']['name'])
#         # 查找专辑名
#         print('播放时长：'+str(music['interval'])+'秒')
#         # 查找播放时长
#         print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')
#         # 查找播放链接

import requests,random
import json
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
# 伪装请求头

def get_express_type(postid):
    '''根据快递单号来智能判断快递类型'''
    url = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=%s' % (postid,)  # 这里可以用元组这样保证的数据的安全性
    # 把构造后的url通过requests请求来得到相应的数据是一个json数据
    rs = requests.get(url)
    # 再用json库中的loads数据来进行分析得到一个可用字典的方式来访问
    kd_type_info = rs.json()
    print(rs.status_code)
    kd_type = kd_type_info['auto'][0]['comCode']
    return kd_type, postid


def execute_data_query(type, postid):
    '''执行数据查询程序'''

    # 通过构造一个真正的url地址
    temp  = random.random()
    url = 'https://www.kuaidi100.com/query?type=%s&postid=%s&temp=%s&phone=' % (type, postid,str(temp)) # 这里可以用元组这样保证的数据的安全性
    # 把构造后的url通过requests请求来得到相应的数据是一个json数据
    rs = requests.get(url,headers=headers)
    # 再用json库中的loads数据来进行分析得到一个可用字典的方式来访问
    kd_info =  json.loads(rs.text)
    msg = kd_info['message']
    # 判断是否成功获取到了json的数据，如果有数据则进行下一步的解析
    if msg == 'ok':
        print('您的快递%s物流信息如下：' % postid)
        data = kd_info['data']
        for data_dict in data:
            time = data_dict['time']
            context = data_dict['context']
            print('时间：%s %s' % (time, context))
    else:
        if msg == '参数错误':
            print('您输入信息有误，请重输：')
        else:
            print(msg)


def main():
    '''快递查询主程序'''
    while True:
        print('**欢迎您登录快递查询系统**')
        print('-' * 30)
        print('** 1. 请输入您的快递单号 **')
        print('** 0. 退出查询系统       **')
        print('-' * 30)
        order = input('查询请输入1退出请输入0：')
        if order == '1':
            # 进行快递查询操作
            postid = input('请输入您的快递单号：')
            type, postid = get_express_type(postid)
            execute_data_query(type, postid)
        elif order == '0':
            exit()
        else:
            print('!!!!!您的指令输入有误，请重新输入：<---------')
main()