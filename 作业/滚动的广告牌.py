import time
import os
import csv

string = input('请输入滚动的广告语：')

for i in range(30):
    print(string)
    string = string[1:]  + string[0]
    time.sleep(0.2)
    os.system('cls')  
    
