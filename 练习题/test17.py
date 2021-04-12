#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
import string

s = input('请输入字符串：')

count_c = 0
count_e = 0
count_em = 0
count_n = 0
count_o = 0

for i in s:
    if i.isalpha():
        count_e += 1
    elif i.isdigit():
        count_n += 1
    elif i.isspace():
        count_em += 1
    else:
        count_o += 1
print('''中英文字母:%d个
空格：%d个
数字：%d个
其他字符：%d个'''%(count_e ,count_em,count_n,count_o))