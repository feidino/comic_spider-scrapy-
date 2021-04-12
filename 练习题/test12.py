#题目：判断101-200之间有多少个素数，并输出所有素数。
#程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　
sum = 0
for i in range(101,201):
    a = 0
    for n in range(2,i):
        if i%n == 0: 
            break   #如果被被2到sqrt(这个数)之间任意一个数整除则跳出循环
        else:
            a += 1  #统计这个数不能被2到sqrt(这个数)整除的数字个数
    if a == i-2:    #当满足n-2个不能被整除的数字个数时，判断是素数
        print(i)
        sum += 1
print('101-200之间有%d个素数'%sum)

#————————————————————————分割线——————————————————————————————————————————
h = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print ('%-4d' % m)
        h += 1
        if h % 10 == 0:
            print ('')
    leap = 1
print ('The total is %d' % h)
