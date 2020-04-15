import os
#import random
#os.mkdir(r'e:\\海飞')
#print(os.listdir(r'e:\\'))
#with open(r'e:\vscode 文件\books.txt','r',encoding='utf-8') as f:
#lines = f.readlines()
#print(os.getcwd())

#i = 1%10
#a = 17%10
#b =27%10
#g = 71//10
#l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#g = lambda x:x*7 for x in range(1,15)
#print(i,a,b,g)
""" import csv
with open('assets.csv', 'a', newline='') as csvfile:
    #调用open()函数打开csv文件，传入参数：文件名“assets.csv”，、追加模式“a”、newline=''。
    writer = csv.writer(csvfile, dialect='excel')
    # 用csv.writer()函数创建一个writer对象。
    header = ['小区名称', '地址', '建筑时间', '楼栋', '单元', '门牌', '朝向', '面积']
    # 用writerow()函数将表头写进csv文件
    writer.writerow(header)
 """
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)