'''
Created on 2016/8/2

@author: xianxun
'''

def multiply35(n):    
    a = 0
    b = 0
    while a < n - 1: 
        a = a + 1
               
        if(a % 5 == 0 or a % 3 == 0):
            #print(a, end=' ')
            b = b + a    
                
    print(b)

multiply35(1000)
    
