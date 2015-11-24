#coding:utf8
import os 
import time
a=[1,4,6,3,5,7,8]

for i in range(len(a)):
    for j in range(i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
    
    os.system('clear') # shell 下清屏命令
    print a
    time.sleep(1)
