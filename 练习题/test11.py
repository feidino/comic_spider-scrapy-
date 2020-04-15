#题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
#      假如兔子都不死，问每个月的兔子总数为多少？ 
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >= 3:
        a = f(n-1)+f(n-2)
        return a
for i in range(1,13):
    print('第%d个月的兔子个数为：%d只'%(i,f(i)*2))
    