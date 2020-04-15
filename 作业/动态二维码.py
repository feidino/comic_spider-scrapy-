import os
from MyQR import myqr
pic_name = input('请输入需制作二维码的图片文件名（包含后缀）：')
save_name = input('请输入保存的图片文件名（包含后缀）：')
words = input('请输入内容(不能输入中文)')
myqr.run(words=words,level='H',picture=pic_name,colorized=True,contrast=1.0,brightness=1.0,save_name=save_name)

