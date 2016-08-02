'''
Created on 2016年8月2日

@author: xianxun
'''

def fib(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        a = b
        b = a + b
    print()

fib(1000)
    
