#题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

#程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
#(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
#(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
#(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步

num_list = []
def fun(n):
    while True:
        for k in range(2,n+1):
            if n%k == 0:
                num_list.append(str(k))
                n = n//k
                break    
        if n == 1:
            break
def gongshi(n):
    if len(num_list) <= 1:
        print('%d是素数。'%n)
    else:
        print('%d = %s'%(n,'*'.join(num_list)))

n = int(input('请输入需要分解质因数的正整数：'))
fun(n)
#string = '*'.join(num_list)
#print(string)
gongshi(n)

#——————————————————————————————————分割线——————————————————————————————

b=int(input('输入任意正整数'))
mylist=[]
def func(a):
    for i in range(2,a):
        if a%i==0:
            mylist.append(i)
            a=a//i
            return func(a)
    mylist.append(a)
    if len(mylist)>1:
        print('{}能分解为{}'.format(b,mylist))
    else:
        print('{}是质数'.format(a))
 
func(b)




