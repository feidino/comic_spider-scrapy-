# 写一个函数，它接受一个字符串，做的事情和strip()字符串方法一样。如果只
# 传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。否
# 则，函数第二个参数指定的字符将从该字符串中去除。
import re

def strips(string,char=None):
    if char != None:
        pattern = '[^'+char+']'
        res = re.compile(pattern)
        str_list = res.findall(string)
        out_str = ''.join(str_list)
        #print(out_str)
        return out_str
    else:
        res = re.compile(r'\S+')
        str_list = res.findall(string)
        out_str = ''.join(str_list)
        #print(out_str)
        return out_str

in_str = input('请输入字符串：')

str = strips(in_str,'fe')
print(str)

print(in_str.strip())
print(in_str.strip('fe'))


